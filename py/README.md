# FreeMusic Python SDK



The Python SDK for the FreeMusic API — an entity-oriented client following Pythonic conventions.

The SDK exposes the API as capitalised, semantic **Entities** — for example `client.V1List()` — each
carrying a small, uniform set of operations (`list`, `load`) instead of raw URL
paths and query strings. You work with named resources and verbs, which
keeps the cognitive load low.

> Other languages, the CLI, and MCP server live alongside this one — see
> the [top-level README](../README.md).


## Install
This package is not yet published to PyPI. Install it from the GitHub
release tag (`py/vX.Y.Z`, see [Releases](https://github.com/voxgig-sdk/free-music-sdk/releases)) or
from a source checkout:

```bash
pip install -e .
```


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### 1. Create a client

```python
import os
from freemusic_sdk import FreeMusicSDK

client = FreeMusicSDK({
    "apikey": os.environ.get("FREE_MUSIC_APIKEY"),
})
```

### 2. List v1list records

`list()` returns a `list` of records (each a `dict`) and raises on
error — iterate it directly.

```python
try:
    v1lists = client.V1List().list({"api_key": "example"})
    for v1list in v1lists:
        print(v1list)
except Exception as err:
    print(f"list failed: {err}")
```

### 3. Load a v2list

V2List is nested under id_artist, so provide the `id_artist`.
`load()` returns the ENTITY — call data_get() for the record — and raises on error.

```python
try:
    v2list = client.V2List().load({"id_artist": 1})
    print(v2list)
except Exception as err:
    print(f"load failed: {err}")
```


## Error handling

Entity operations raise on failure, so wrap them in `try` / `except`:

```python
try:
    v2lookup = client.V2Lookup().load({"id_album": 1})
    print(v2lookup)
except Exception as err:
    print(f"load failed: {err}")
```

`direct()` does **not** raise — it returns the result envelope. Branch
on `ok`; on failure `status` holds the HTTP status (for error responses)
and `err` holds a transport error, so read both defensively:

```python
result = client.direct({
    "path": "/api/resource/{id}",
    "method": "GET",
    "params": {"id": "example_id"},
})

if not result["ok"]:
    print("request failed:", result.get("status"), result.get("err"))
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```python
result = client.direct({
    "path": "/api/resource/{id}",
    "method": "GET",
    "params": {"id": "example"},
})

if result["ok"]:
    print(result["status"])  # 200
    print(result["data"])    # response body
else:
    # A non-2xx response carries status + data (the error body); a
    # transport-level failure carries err instead. Only one is present, so
    # read both with .get() rather than indexing a key that may be absent.
    print(result.get("status"), result.get("err"))
```

### Prepare a request without sending it

```python
# prepare() returns the fetch definition and raises on error.
fetchdef = client.prepare({
    "path": "/api/resource/{id}",
    "method": "DELETE",
    "params": {"id": "example"},
})

print(fetchdef["url"])
print(fetchdef["method"])
print(fetchdef["headers"])
```

### Use test mode

Create a mock client for unit testing — no server required:

```python
client = FreeMusicSDK.test()

# Entity ops return the ENTITY and raises on error;
# call data_get() for the record.
v2lookup = client.V2Lookup().load({"id_album": 1})
# v2lookup contains the mock response record
```

### Use a custom fetch function

Replace the HTTP transport with your own function:

```python
def mock_fetch(url, init):
    return {
        "status": 200,
        "statusText": "OK",
        "headers": {},
        "json": lambda: {"id": "mock01"},
    }, None

client = FreeMusicSDK({
    "base": "http://localhost:8080",
    "system": {
        "fetch": mock_fetch,
    },
})
```

### Run live tests

Create a `.env.local` file at the project root:

```
FREE_MUSIC_TEST_LIVE=TRUE
FREE_MUSIC_APIKEY=<your-key>
```

Then run:

```bash
cd py && pytest test/
```


## Reference

### FreeMusicSDK

```python
from freemusic_sdk import FreeMusicSDK

client = FreeMusicSDK(options)
```

Creates a new SDK client.

| Option | Type | Description |
| --- | --- | --- |
| `apikey` | `str` | API key for authentication. |
| `base` | `str` | Base URL of the API server. |
| `prefix` | `str` | URL path prefix prepended to all requests. |
| `suffix` | `str` | URL path suffix appended to all requests. |
| `feature` | `dict` | Feature activation flags. |
| `extend` | `list` | Additional Feature instances to load. |
| `system` | `dict` | System overrides (e.g. custom `fetch` function). |

### test

```python
client = FreeMusicSDK.test(testopts, sdkopts)
```

Creates a test-mode client with mock transport. Both arguments may be `None`.

### FreeMusicSDK methods

| Method | Signature | Description |
| --- | --- | --- |
| `options_map` | `() -> dict` | Deep copy of current SDK options. |
| `get_utility` | `() -> Utility` | Copy of the SDK utility object. |
| `prepare` | `(fetchargs) -> dict` | Build an HTTP request definition without sending. Raises on error. |
| `direct` | `(fetchargs) -> dict` | Build and send an HTTP request. Returns a result dict (branch on `ok`). |
| `V1List` | `(data) -> V1ListEntity` | Create a V1List entity instance. |
| `V1Lookup` | `(data) -> V1LookupEntity` | Create a V1Lookup entity instance. |
| `V1Search` | `(data) -> V1SearchEntity` | Create a V1Search entity instance. |
| `V2List` | `(data) -> V2ListEntity` | Create a V2List entity instance. |
| `V2Lookup` | `(data) -> V2LookupEntity` | Create a V2Lookup entity instance. |
| `V2Search` | `(data) -> V2SearchEntity` | Create a V2Search entity instance. |

### Entity interface

All entities share the same interface.

| Method | Signature | Description |
| --- | --- | --- |
| `load` | `(reqmatch, ctrl) -> any` | Load a single entity by match criteria. Raises on error. |
| `list` | `(reqmatch, ctrl) -> list` | List entities matching the criteria. Raises on error. |
| `data_get` | `() -> dict` | Get entity data. |
| `data_set` | `(data)` | Set entity data. |
| `match_get` | `() -> dict` | Get entity match criteria. |
| `match_set` | `(match)` | Set entity match criteria. |
| `make` | `() -> Entity` | Create a new instance with the same options. |
| `get_name` | `() -> str` | Return the entity name. |

### Result shape

Entity operations return the ENTITY (call data_get() for the record) (a `dict` for single-entity
ops, a `list` for `list`) and raise on error. Wrap calls in
`try`/`except` to handle failures.

The `direct()` escape hatch never raises — it returns a result `dict`
you branch on via `result["ok"]`:

| Key | Type | Description |
| --- | --- | --- |
| `ok` | `bool` | `True` if the HTTP status is 2xx. |
| `status` | `int` | HTTP status code. |
| `headers` | `dict` | Response headers. |
| `data` | `any` | Parsed JSON response body. |

On error, `ok` is `False` and `err` contains the error value.

### Entities

#### V1List

| Field | Description |
| --- | --- |
| `idAlbum` | Album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intCD` | CD number |
| `intDuration` | Track duration in milliseconds |
| `intLoved` | Number of loves/likes |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intScore` | Track score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `strAlbum` | Album name |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strDescriptionEN` | Track description in English |
| `strGenre` | Musical genre |
| `strLocked` | Lock status |
| `strMood` | Track mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Recording ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strStyle` | Musical style |
| `strTheme` | Track theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `trending` |  |

Operations: List, Load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `idAlbum` | Album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLabel` | Label ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intBornYear` | Birth year (for solo artists) |
| `intCD` | CD number |
| `intCharted` | Chart position |
| `intDiedYear` | Death year (if applicable) |
| `intDuration` | Track duration in milliseconds |
| `intFormedYear` | Year the artist was formed |
| `intLoved` | Number of loves/likes |
| `intMembers` | Number of band members |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intSales` | Sales figures |
| `intScore` | Track score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `intYearReleased` | Release year |
| `strAlbum` | Album name |
| `strAlbum3DCase` | 3D case image URL |
| `strAlbum3DFace` | 3D face image URL |
| `strAlbum3DFlat` | 3D flat image URL |
| `strAlbum3DThumb` | 3D thumbnail URL |
| `strAlbumCDart` | CD art URL |
| `strAlbumSpine` | Album spine image URL |
| `strAlbumStripped` | Album name stripped of special characters |
| `strAlbumThumb` | Album thumbnail URL |
| `strAlbumThumbBack` | Album back cover URL |
| `strAlbumThumbHQ` | High quality album thumbnail URL |
| `strAllMusicID` | AllMusic ID |
| `strAmazonID` | Amazon ID |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strArtistBanner` | Banner image URL |
| `strArtistClearart` | Clear art image URL |
| `strArtistCutout` | Cutout image URL |
| `strArtistFanart` | Fan art image URL |
| `strArtistFanart2` | Additional fan art image URL |
| `strArtistFanart3` | Additional fan art image URL |
| `strArtistFanart4` | Additional fan art image URL |
| `strArtistLogo` | Logo image URL |
| `strArtistStripped` | Artist name stripped |
| `strArtistThumb` | Thumbnail image URL |
| `strArtistWideThumb` | Wide thumbnail image URL |
| `strBBCReviewID` | BBC Review ID |
| `strBiographyEN` | Biography in English |
| `strCountry` | Country of origin |
| `strCountryCode` | Country code |
| `strDescriptionEN` | Track description in English |
| `strDisbanded` | Disbandment status |
| `strDiscogsID` | Discogs ID |
| `strFacebook` | Facebook URL |
| `strGender` | Gender |
| `strGeniusID` | Genius ID |
| `strGenre` | Musical genre |
| `strISNIcode` | ISNI code |
| `strItunesID` | iTunes ID |
| `strLabel` | Record label |
| `strLastFMChart` | Last.fm chart URL |
| `strLocation` | Recording location |
| `strLocked` | Lock status |
| `strLyricWikiID` | LyricWiki ID |
| `strMood` | Track mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Recording ID |
| `strMusicMozID` | MusicMoz ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strRateYourMusicID` | Rate Your Music ID |
| `strReleaseFormat` | Release format (CD, Vinyl, etc.) |
| `strReview` | Album review |
| `strSpeed` | Album speed/tempo |
| `strStyle` | Musical style |
| `strTheme` | Track theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `strTwitter` | Twitter handle |
| `strWebsite` | Official website URL |
| `strWikidataID` | Wikidata ID |
| `strWikipediaID` | Wikipedia ID |

Operations: List, Load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `album` |  |
| `idAlbum` | Unique album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLabel` | Label ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intBornYear` | Birth year (for solo artists) |
| `intCD` | CD number |
| `intCharted` | Chart position |
| `intDiedYear` | Death year (if applicable) |
| `intDuration` | Track duration in milliseconds |
| `intFormedYear` | Year the artist was formed |
| `intLoved` | Number of loves/likes |
| `intMembers` | Number of band members |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intSales` | Sales figures |
| `intScore` | Album score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `intYearReleased` | Release year |
| `strAlbum` | Album name |
| `strAlbum3DCase` | 3D case image URL |
| `strAlbum3DFace` | 3D face image URL |
| `strAlbum3DFlat` | 3D flat image URL |
| `strAlbum3DThumb` | 3D thumbnail URL |
| `strAlbumCDart` | CD art URL |
| `strAlbumSpine` | Album spine image URL |
| `strAlbumStripped` | Album name stripped of special characters |
| `strAlbumThumb` | Album thumbnail URL |
| `strAlbumThumbBack` | Album back cover URL |
| `strAlbumThumbHQ` | High quality album thumbnail URL |
| `strAllMusicID` | AllMusic ID |
| `strAmazonID` | Amazon ID |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strArtistBanner` | Banner image URL |
| `strArtistClearart` | Clear art image URL |
| `strArtistCutout` | Cutout image URL |
| `strArtistFanart` | Fan art image URL |
| `strArtistFanart2` | Additional fan art image URL |
| `strArtistFanart3` | Additional fan art image URL |
| `strArtistFanart4` | Additional fan art image URL |
| `strArtistLogo` | Logo image URL |
| `strArtistStripped` | Artist name stripped |
| `strArtistThumb` | Thumbnail image URL |
| `strArtistWideThumb` | Wide thumbnail image URL |
| `strBBCReviewID` | BBC Review ID |
| `strBiographyEN` | Biography in English |
| `strCountry` | Country of origin |
| `strCountryCode` | Country code |
| `strDescriptionEN` | Album description in English |
| `strDisbanded` | Disbandment status |
| `strDiscogsID` | Discogs ID |
| `strFacebook` | Facebook URL |
| `strGender` | Gender |
| `strGeniusID` | Genius ID |
| `strGenre` | Musical genre |
| `strISNIcode` | ISNI code |
| `strItunesID` | iTunes ID |
| `strLabel` | Record label |
| `strLastFMChart` | Last.fm chart URL |
| `strLocation` | Recording location |
| `strLocked` | Lock status |
| `strLyricWikiID` | LyricWiki ID |
| `strMood` | Album mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Release Group ID |
| `strMusicMozID` | MusicMoz ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strRateYourMusicID` | Rate Your Music ID |
| `strReleaseFormat` | Release format (CD, Vinyl, etc.) |
| `strReview` | Album review |
| `strSpeed` | Album speed/tempo |
| `strStyle` | Musical style |
| `strTheme` | Album theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `strTwitter` | Twitter handle |
| `strWebsite` | Official website URL |
| `strWikidataID` | Wikidata ID |
| `strWikipediaID` | Wikipedia ID |

Operations: List, Load.

API path: `/{apiKey}/searchalbum.php`

#### V2List

| Field | Description |
| --- | --- |
| `album` |  |

Operations: Load.

API path: `/list/discography/{idArtist}`

#### V2Lookup

| Field | Description |
| --- | --- |
| `album` |  |
| `artists` |  |
| `track` |  |

Operations: Load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `album` |  |
| `artists` |  |
| `track` |  |

Operations: Load.

API path: `/search/album/{albumName}`



## Entities


### V1List

Create an instance: `v1_list = client.V1List()`

#### Operations

| Method | Description |
| --- | --- |
| `list()` | List entities, optionally matching the given criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `str` | Album ID |
| `idArtist` | `str` | Artist ID |
| `idIMVDB` | `str` | IMVDB ID |
| `idLyric` | `str` | Lyrics ID |
| `idTrack` | `str` | Unique track ID |
| `intCD` | `str` | CD number |
| `intDuration` | `str` | Track duration in milliseconds |
| `intLoved` | `str` | Number of loves/likes |
| `intMusicVidComments` | `str` | Music video comment count |
| `intMusicVidDislikes` | `str` | Music video dislike count |
| `intMusicVidFavorites` | `str` | Music video favorite count |
| `intMusicVidLikes` | `str` | Music video like count |
| `intMusicVidViews` | `str` | Music video view count |
| `intScore` | `str` | Track score/rating |
| `intScoreVotes` | `str` | Number of score votes |
| `intTotalListeners` | `str` | Total listener count |
| `intTotalPlays` | `str` | Total play count |
| `intTrackNumber` | `str` | Track number on album |
| `strAlbum` | `str` | Album name |
| `strArtist` | `str` | Artist name |
| `strArtistAlternate` | `str` | Alternative artist name |
| `strDescriptionEN` | `str` | Track description in English |
| `strGenre` | `str` | Musical genre |
| `strLocked` | `str` | Lock status |
| `strMood` | `str` | Track mood |
| `strMusicBrainzAlbumID` | `str` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | MusicBrainz Recording ID |
| `strMusicVid` | `str` | Music video URL |
| `strMusicVidCompany` | `str` | Music video production company |
| `strMusicVidDirector` | `str` | Music video director |
| `strMusicVidScreen1` | `str` | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | Music video screenshot 3 |
| `strStyle` | `str` | Musical style |
| `strTheme` | `str` | Track theme |
| `strTrack` | `str` | Track name |
| `strTrack3x3` | `str` | 3x3 track image URL |
| `strTrackLyrics` | `str` | Track lyrics |
| `strTrackThumb` | `str` | Track thumbnail URL |
| `trending` | `list` |  |

#### Example: Load

```python
v1_list = client.V1List().load({"api_key": "api_key"})
```

#### Example: List

```python
v1_lists = client.V1List().list({"api_key": "example"})
```


### V1Lookup

Create an instance: `v1_lookup = client.V1Lookup()`

#### Operations

| Method | Description |
| --- | --- |
| `list()` | List entities, optionally matching the given criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `str` | Album ID |
| `idArtist` | `str` | Artist ID |
| `idIMVDB` | `str` | IMVDB ID |
| `idLabel` | `str` | Label ID |
| `idLyric` | `str` | Lyrics ID |
| `idTrack` | `str` | Unique track ID |
| `intBornYear` | `str` | Birth year (for solo artists) |
| `intCD` | `str` | CD number |
| `intCharted` | `str` | Chart position |
| `intDiedYear` | `str` | Death year (if applicable) |
| `intDuration` | `str` | Track duration in milliseconds |
| `intFormedYear` | `str` | Year the artist was formed |
| `intLoved` | `str` | Number of loves/likes |
| `intMembers` | `str` | Number of band members |
| `intMusicVidComments` | `str` | Music video comment count |
| `intMusicVidDislikes` | `str` | Music video dislike count |
| `intMusicVidFavorites` | `str` | Music video favorite count |
| `intMusicVidLikes` | `str` | Music video like count |
| `intMusicVidViews` | `str` | Music video view count |
| `intSales` | `str` | Sales figures |
| `intScore` | `str` | Track score/rating |
| `intScoreVotes` | `str` | Number of score votes |
| `intTotalListeners` | `str` | Total listener count |
| `intTotalPlays` | `str` | Total play count |
| `intTrackNumber` | `str` | Track number on album |
| `intYearReleased` | `str` | Release year |
| `strAlbum` | `str` | Album name |
| `strAlbum3DCase` | `str` | 3D case image URL |
| `strAlbum3DFace` | `str` | 3D face image URL |
| `strAlbum3DFlat` | `str` | 3D flat image URL |
| `strAlbum3DThumb` | `str` | 3D thumbnail URL |
| `strAlbumCDart` | `str` | CD art URL |
| `strAlbumSpine` | `str` | Album spine image URL |
| `strAlbumStripped` | `str` | Album name stripped of special characters |
| `strAlbumThumb` | `str` | Album thumbnail URL |
| `strAlbumThumbBack` | `str` | Album back cover URL |
| `strAlbumThumbHQ` | `str` | High quality album thumbnail URL |
| `strAllMusicID` | `str` | AllMusic ID |
| `strAmazonID` | `str` | Amazon ID |
| `strArtist` | `str` | Artist name |
| `strArtistAlternate` | `str` | Alternative artist name |
| `strArtistBanner` | `str` | Banner image URL |
| `strArtistClearart` | `str` | Clear art image URL |
| `strArtistCutout` | `str` | Cutout image URL |
| `strArtistFanart` | `str` | Fan art image URL |
| `strArtistFanart2` | `str` | Additional fan art image URL |
| `strArtistFanart3` | `str` | Additional fan art image URL |
| `strArtistFanart4` | `str` | Additional fan art image URL |
| `strArtistLogo` | `str` | Logo image URL |
| `strArtistStripped` | `str` | Artist name stripped |
| `strArtistThumb` | `str` | Thumbnail image URL |
| `strArtistWideThumb` | `str` | Wide thumbnail image URL |
| `strBBCReviewID` | `str` | BBC Review ID |
| `strBiographyEN` | `str` | Biography in English |
| `strCountry` | `str` | Country of origin |
| `strCountryCode` | `str` | Country code |
| `strDescriptionEN` | `str` | Track description in English |
| `strDisbanded` | `str` | Disbandment status |
| `strDiscogsID` | `str` | Discogs ID |
| `strFacebook` | `str` | Facebook URL |
| `strGender` | `str` | Gender |
| `strGeniusID` | `str` | Genius ID |
| `strGenre` | `str` | Musical genre |
| `strISNIcode` | `str` | ISNI code |
| `strItunesID` | `str` | iTunes ID |
| `strLabel` | `str` | Record label |
| `strLastFMChart` | `str` | Last.fm chart URL |
| `strLocation` | `str` | Recording location |
| `strLocked` | `str` | Lock status |
| `strLyricWikiID` | `str` | LyricWiki ID |
| `strMood` | `str` | Track mood |
| `strMusicBrainzAlbumID` | `str` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | MusicBrainz Recording ID |
| `strMusicMozID` | `str` | MusicMoz ID |
| `strMusicVid` | `str` | Music video URL |
| `strMusicVidCompany` | `str` | Music video production company |
| `strMusicVidDirector` | `str` | Music video director |
| `strMusicVidScreen1` | `str` | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | Music video screenshot 3 |
| `strRateYourMusicID` | `str` | Rate Your Music ID |
| `strReleaseFormat` | `str` | Release format (CD, Vinyl, etc.) |
| `strReview` | `str` | Album review |
| `strSpeed` | `str` | Album speed/tempo |
| `strStyle` | `str` | Musical style |
| `strTheme` | `str` | Track theme |
| `strTrack` | `str` | Track name |
| `strTrack3x3` | `str` | 3x3 track image URL |
| `strTrackLyrics` | `str` | Track lyrics |
| `strTrackThumb` | `str` | Track thumbnail URL |
| `strTwitter` | `str` | Twitter handle |
| `strWebsite` | `str` | Official website URL |
| `strWikidataID` | `str` | Wikidata ID |
| `strWikipediaID` | `str` | Wikipedia ID |

#### Example: Load

```python
v1_lookup = client.V1Lookup().load({"api_key": "api_key"})
```

#### Example: List

```python
v1_lookups = client.V1Lookup().list({"api_key": "example"})
```


### V1Search

Create an instance: `v1_search = client.V1Search()`

#### Operations

| Method | Description |
| --- | --- |
| `list()` | List entities, optionally matching the given criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `list` |  |
| `idAlbum` | `str` | Unique album ID |
| `idArtist` | `str` | Artist ID |
| `idIMVDB` | `str` | IMVDB ID |
| `idLabel` | `str` | Label ID |
| `idLyric` | `str` | Lyrics ID |
| `idTrack` | `str` | Unique track ID |
| `intBornYear` | `str` | Birth year (for solo artists) |
| `intCD` | `str` | CD number |
| `intCharted` | `str` | Chart position |
| `intDiedYear` | `str` | Death year (if applicable) |
| `intDuration` | `str` | Track duration in milliseconds |
| `intFormedYear` | `str` | Year the artist was formed |
| `intLoved` | `str` | Number of loves/likes |
| `intMembers` | `str` | Number of band members |
| `intMusicVidComments` | `str` | Music video comment count |
| `intMusicVidDislikes` | `str` | Music video dislike count |
| `intMusicVidFavorites` | `str` | Music video favorite count |
| `intMusicVidLikes` | `str` | Music video like count |
| `intMusicVidViews` | `str` | Music video view count |
| `intSales` | `str` | Sales figures |
| `intScore` | `str` | Album score/rating |
| `intScoreVotes` | `str` | Number of score votes |
| `intTotalListeners` | `str` | Total listener count |
| `intTotalPlays` | `str` | Total play count |
| `intTrackNumber` | `str` | Track number on album |
| `intYearReleased` | `str` | Release year |
| `strAlbum` | `str` | Album name |
| `strAlbum3DCase` | `str` | 3D case image URL |
| `strAlbum3DFace` | `str` | 3D face image URL |
| `strAlbum3DFlat` | `str` | 3D flat image URL |
| `strAlbum3DThumb` | `str` | 3D thumbnail URL |
| `strAlbumCDart` | `str` | CD art URL |
| `strAlbumSpine` | `str` | Album spine image URL |
| `strAlbumStripped` | `str` | Album name stripped of special characters |
| `strAlbumThumb` | `str` | Album thumbnail URL |
| `strAlbumThumbBack` | `str` | Album back cover URL |
| `strAlbumThumbHQ` | `str` | High quality album thumbnail URL |
| `strAllMusicID` | `str` | AllMusic ID |
| `strAmazonID` | `str` | Amazon ID |
| `strArtist` | `str` | Artist name |
| `strArtistAlternate` | `str` | Alternative artist name |
| `strArtistBanner` | `str` | Banner image URL |
| `strArtistClearart` | `str` | Clear art image URL |
| `strArtistCutout` | `str` | Cutout image URL |
| `strArtistFanart` | `str` | Fan art image URL |
| `strArtistFanart2` | `str` | Additional fan art image URL |
| `strArtistFanart3` | `str` | Additional fan art image URL |
| `strArtistFanart4` | `str` | Additional fan art image URL |
| `strArtistLogo` | `str` | Logo image URL |
| `strArtistStripped` | `str` | Artist name stripped |
| `strArtistThumb` | `str` | Thumbnail image URL |
| `strArtistWideThumb` | `str` | Wide thumbnail image URL |
| `strBBCReviewID` | `str` | BBC Review ID |
| `strBiographyEN` | `str` | Biography in English |
| `strCountry` | `str` | Country of origin |
| `strCountryCode` | `str` | Country code |
| `strDescriptionEN` | `str` | Album description in English |
| `strDisbanded` | `str` | Disbandment status |
| `strDiscogsID` | `str` | Discogs ID |
| `strFacebook` | `str` | Facebook URL |
| `strGender` | `str` | Gender |
| `strGeniusID` | `str` | Genius ID |
| `strGenre` | `str` | Musical genre |
| `strISNIcode` | `str` | ISNI code |
| `strItunesID` | `str` | iTunes ID |
| `strLabel` | `str` | Record label |
| `strLastFMChart` | `str` | Last.fm chart URL |
| `strLocation` | `str` | Recording location |
| `strLocked` | `str` | Lock status |
| `strLyricWikiID` | `str` | LyricWiki ID |
| `strMood` | `str` | Album mood |
| `strMusicBrainzAlbumID` | `str` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | MusicBrainz Release Group ID |
| `strMusicMozID` | `str` | MusicMoz ID |
| `strMusicVid` | `str` | Music video URL |
| `strMusicVidCompany` | `str` | Music video production company |
| `strMusicVidDirector` | `str` | Music video director |
| `strMusicVidScreen1` | `str` | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | Music video screenshot 3 |
| `strRateYourMusicID` | `str` | Rate Your Music ID |
| `strReleaseFormat` | `str` | Release format (CD, Vinyl, etc.) |
| `strReview` | `str` | Album review |
| `strSpeed` | `str` | Album speed/tempo |
| `strStyle` | `str` | Musical style |
| `strTheme` | `str` | Album theme |
| `strTrack` | `str` | Track name |
| `strTrack3x3` | `str` | 3x3 track image URL |
| `strTrackLyrics` | `str` | Track lyrics |
| `strTrackThumb` | `str` | Track thumbnail URL |
| `strTwitter` | `str` | Twitter handle |
| `strWebsite` | `str` | Official website URL |
| `strWikidataID` | `str` | Wikidata ID |
| `strWikipediaID` | `str` | Wikipedia ID |

#### Example: Load

```python
v1_search = client.V1Search().load({"api_key": "api_key"})
```

#### Example: List

```python
v1_searchs = client.V1Search().list({"api_key": "example"})
```


### V2List

Create an instance: `v2_list = client.V2List()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `list` |  |

#### Example: Load

```python
v2_list = client.V2List().load({"id_artist": 1})
```


### V2Lookup

Create an instance: `v2_lookup = client.V2Lookup()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `list` |  |
| `artists` | `list` |  |
| `track` | `list` |  |

#### Example: Load

```python
v2_lookup = client.V2Lookup().load({"id_album": 1})
```


### V2Search

Create an instance: `v2_search = client.V2Search()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `list` |  |
| `artists` | `list` |  |
| `track` | `list` |  |

#### Example: Load

```python
v2_search = client.V2Search().load({"album_name": "album_name"})
```


## Advanced

> The sections above cover everyday use. The material below explains the
> SDK's internals — useful when extending it with custom features, but not
> needed for normal use.

### The operation pipeline

Every entity operation follows a six-stage pipeline. Each stage fires a
feature hook before executing:

```
PrePoint → PreSpec → PreRequest → PreResponse → PreResult → PreDone
```

- **PrePoint**: Resolves which API endpoint to call based on the
  operation name and entity configuration.
- **PreSpec**: Builds the HTTP spec — URL, method, headers, body —
  from the resolved point and the caller's parameters.
- **PreRequest**: Sends the HTTP request. Features can intercept here
  to replace the transport (as TestFeature does with mocks).
- **PreResponse**: Parses the raw HTTP response.
- **PreResult**: Extracts the business data from the parsed response.
- **PreDone**: Final stage before returning to the caller. Entity
  state (match, data) is updated here.

If any stage errors, the pipeline short-circuits and the error surfaces
to the caller — see [Error handling](#error-handling) for how that looks
in this language.

### Features and hooks

Features are the extension mechanism. A feature is a Python class
with hook methods named after pipeline stages (e.g. `PrePoint`,
`PreSpec`). Each method receives the context.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Data as dicts

The Python SDK uses plain dicts throughout rather than typed
objects. This mirrors the dynamic nature of the API and keeps the
SDK flexible — no code generation is needed when the API schema
changes.

Use `helpers.to_map()` to safely validate that a value is a dict.

### Module structure

```
py/
├── freemusic_sdk.py         -- Main SDK module
├── config.py                    -- Configuration
├── features.py                  -- Feature factory
├── core/                        -- Core types and context
├── entity/                      -- Entity implementations
├── feature/                     -- Built-in features (Base, Test, Log)
├── utility/                     -- Utility functions and struct library
└── test/                        -- Test suites
```

The main module (`freemusic_sdk`) exports the SDK class.
Import entity or utility modules directly only when needed.

### Entity state

Entity instances are stateful. After a successful `load`, the entity
stores the returned data and match criteria internally.

```python
v2lookup = client.V2Lookup()
v2lookup.load({"id_album": 1})

# v2lookup.data_get() now returns the v2lookup data from the last load
# v2lookup.match_get() returns the last match criteria
```

Call `make()` to create a fresh instance with the same configuration
but no stored state.

### Direct vs entity access

The entity interface handles URL construction, parameter placement,
and response parsing automatically. Use it for standard CRUD operations.

`direct()` gives full control over the HTTP request. Use it for
non-standard endpoints, bulk operations, or any path not modelled as
an entity. `prepare()` builds the request without sending it — useful
for debugging or custom transport.


## Full Reference

See [REFERENCE.md](REFERENCE.md) for complete API reference
documentation including all method signatures, entity field schemas,
and detailed usage examples.
