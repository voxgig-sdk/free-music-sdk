# FreeMusic Python SDK Reference

Complete API reference for the FreeMusic Python SDK.


## FreeMusicSDK

### Constructor

```python
from freemusic_sdk import FreeMusicSDK

client = FreeMusicSDK(options)
```

Create a new SDK client instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `options` | `dict` | SDK configuration options. |
| `options["apikey"]` | `str` | API key for authentication. |
| `options["base"]` | `str` | Base URL for API requests. |
| `options["prefix"]` | `str` | URL prefix appended after base. |
| `options["suffix"]` | `str` | URL suffix appended after path. |
| `options["headers"]` | `dict` | Custom headers for all requests. |
| `options["feature"]` | `dict` | Feature configuration. |
| `options["system"]` | `dict` | System overrides (e.g. custom fetch). |


### Static Methods

#### `FreeMusicSDK.test(testopts=None, sdkopts=None)`

Create a test client with mock features active. Both arguments may be `None`.

```python
client = FreeMusicSDK.test()
```


### Instance Methods

#### `V1List(data=None)`

Create a new `V1ListEntity` instance. Pass `None` for no initial data.

#### `V1Lookup(data=None)`

Create a new `V1LookupEntity` instance. Pass `None` for no initial data.

#### `V1Search(data=None)`

Create a new `V1SearchEntity` instance. Pass `None` for no initial data.

#### `V2List(data=None)`

Create a new `V2ListEntity` instance. Pass `None` for no initial data.

#### `V2Lookup(data=None)`

Create a new `V2LookupEntity` instance. Pass `None` for no initial data.

#### `V2Search(data=None)`

Create a new `V2SearchEntity` instance. Pass `None` for no initial data.

#### `options_map() -> dict`

Return a deep copy of the current SDK options.

#### `get_utility() -> Utility`

Return a copy of the SDK utility object.

#### `direct(fetchargs=None) -> dict`

Make a direct HTTP request to any API endpoint. Returns a result `dict` with `ok`, `status`, `headers`, and `data` (or `err` on failure). This escape hatch never raises — branch on `result["ok"]`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `fetchargs["path"]` | `str` | URL path with optional `{param}` placeholders. |
| `fetchargs["method"]` | `str` | HTTP method (default: `"GET"`). |
| `fetchargs["params"]` | `dict` | Path parameter values. |
| `fetchargs["query"]` | `dict` | Query string parameters. |
| `fetchargs["headers"]` | `dict` | Request headers (merged with defaults). |
| `fetchargs["body"]` | `any` | Request body (dicts are JSON-serialized). |

**Returns:** `result_dict`

#### `prepare(fetchargs=None) -> dict`

Prepare a fetch definition without sending. Returns the `fetchdef` and raises on error.


---

## V1ListEntity

```python
v1_list = client.V1List()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `str` | No | Album ID |
| `idArtist` | `str` | No | Artist ID |
| `idIMVDB` | `str` | No | IMVDB ID |
| `idLyric` | `str` | No | Lyrics ID |
| `idTrack` | `str` | No | Unique track ID |
| `intCD` | `str` | No | CD number |
| `intDuration` | `str` | No | Track duration in milliseconds |
| `intLoved` | `str` | No | Number of loves/likes |
| `intMusicVidComments` | `str` | No | Music video comment count |
| `intMusicVidDislikes` | `str` | No | Music video dislike count |
| `intMusicVidFavorites` | `str` | No | Music video favorite count |
| `intMusicVidLikes` | `str` | No | Music video like count |
| `intMusicVidViews` | `str` | No | Music video view count |
| `intScore` | `str` | No | Track score/rating |
| `intScoreVotes` | `str` | No | Number of score votes |
| `intTotalListeners` | `str` | No | Total listener count |
| `intTotalPlays` | `str` | No | Total play count |
| `intTrackNumber` | `str` | No | Track number on album |
| `strAlbum` | `str` | No | Album name |
| `strArtist` | `str` | No | Artist name |
| `strArtistAlternate` | `str` | No | Alternative artist name |
| `strDescriptionEN` | `str` | No | Track description in English |
| `strGenre` | `str` | No | Musical genre |
| `strLocked` | `str` | No | Lock status |
| `strMood` | `str` | No | Track mood |
| `strMusicBrainzAlbumID` | `str` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | No | MusicBrainz Recording ID |
| `strMusicVid` | `str` | No | Music video URL |
| `strMusicVidCompany` | `str` | No | Music video production company |
| `strMusicVidDirector` | `str` | No | Music video director |
| `strMusicVidScreen1` | `str` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | No | Music video screenshot 3 |
| `strStyle` | `str` | No | Musical style |
| `strTheme` | `str` | No | Track theme |
| `strTrack` | `str` | No | Track name |
| `strTrack3x3` | `str` | No | 3x3 track image URL |
| `strTrackLyrics` | `str` | No | Track lyrics |
| `strTrackThumb` | `str` | No | Track thumbnail URL |
| `trending` | `list` | No |  |

### Operations

#### `list(reqmatch=None, ctrl=None) -> list`

List entities matching the given criteria. The match is optional — call `list()` with no argument to list all records. Returns a list and raises on error.

```python
results = client.V1List().list({"api_key": "example"})
for v1_list in results:
    print(v1_list)
```

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V1List().load({"api_key": "api_key"})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V1ListEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## V1LookupEntity

```python
v1_lookup = client.V1Lookup()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `str` | No | Album ID |
| `idArtist` | `str` | No | Artist ID |
| `idIMVDB` | `str` | No | IMVDB ID |
| `idLabel` | `str` | No | Label ID |
| `idLyric` | `str` | No | Lyrics ID |
| `idTrack` | `str` | No | Unique track ID |
| `intBornYear` | `str` | No | Birth year (for solo artists) |
| `intCD` | `str` | No | CD number |
| `intCharted` | `str` | No | Chart position |
| `intDiedYear` | `str` | No | Death year (if applicable) |
| `intDuration` | `str` | No | Track duration in milliseconds |
| `intFormedYear` | `str` | No | Year the artist was formed |
| `intLoved` | `str` | No | Number of loves/likes |
| `intMembers` | `str` | No | Number of band members |
| `intMusicVidComments` | `str` | No | Music video comment count |
| `intMusicVidDislikes` | `str` | No | Music video dislike count |
| `intMusicVidFavorites` | `str` | No | Music video favorite count |
| `intMusicVidLikes` | `str` | No | Music video like count |
| `intMusicVidViews` | `str` | No | Music video view count |
| `intSales` | `str` | No | Sales figures |
| `intScore` | `str` | No | Track score/rating |
| `intScoreVotes` | `str` | No | Number of score votes |
| `intTotalListeners` | `str` | No | Total listener count |
| `intTotalPlays` | `str` | No | Total play count |
| `intTrackNumber` | `str` | No | Track number on album |
| `intYearReleased` | `str` | No | Release year |
| `strAlbum` | `str` | No | Album name |
| `strAlbum3DCase` | `str` | No | 3D case image URL |
| `strAlbum3DFace` | `str` | No | 3D face image URL |
| `strAlbum3DFlat` | `str` | No | 3D flat image URL |
| `strAlbum3DThumb` | `str` | No | 3D thumbnail URL |
| `strAlbumCDart` | `str` | No | CD art URL |
| `strAlbumSpine` | `str` | No | Album spine image URL |
| `strAlbumStripped` | `str` | No | Album name stripped of special characters |
| `strAlbumThumb` | `str` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `str` | No | Album back cover URL |
| `strAlbumThumbHQ` | `str` | No | High quality album thumbnail URL |
| `strAllMusicID` | `str` | No | AllMusic ID |
| `strAmazonID` | `str` | No | Amazon ID |
| `strArtist` | `str` | No | Artist name |
| `strArtistAlternate` | `str` | No | Alternative artist name |
| `strArtistBanner` | `str` | No | Banner image URL |
| `strArtistClearart` | `str` | No | Clear art image URL |
| `strArtistCutout` | `str` | No | Cutout image URL |
| `strArtistFanart` | `str` | No | Fan art image URL |
| `strArtistFanart2` | `str` | No | Additional fan art image URL |
| `strArtistFanart3` | `str` | No | Additional fan art image URL |
| `strArtistFanart4` | `str` | No | Additional fan art image URL |
| `strArtistLogo` | `str` | No | Logo image URL |
| `strArtistStripped` | `str` | No | Artist name stripped |
| `strArtistThumb` | `str` | No | Thumbnail image URL |
| `strArtistWideThumb` | `str` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `str` | No | BBC Review ID |
| `strBiographyEN` | `str` | No | Biography in English |
| `strCountry` | `str` | No | Country of origin |
| `strCountryCode` | `str` | No | Country code |
| `strDescriptionEN` | `str` | No | Track description in English |
| `strDisbanded` | `str` | No | Disbandment status |
| `strDiscogsID` | `str` | No | Discogs ID |
| `strFacebook` | `str` | No | Facebook URL |
| `strGender` | `str` | No | Gender |
| `strGeniusID` | `str` | No | Genius ID |
| `strGenre` | `str` | No | Musical genre |
| `strISNIcode` | `str` | No | ISNI code |
| `strItunesID` | `str` | No | iTunes ID |
| `strLabel` | `str` | No | Record label |
| `strLastFMChart` | `str` | No | Last.fm chart URL |
| `strLocation` | `str` | No | Recording location |
| `strLocked` | `str` | No | Lock status |
| `strLyricWikiID` | `str` | No | LyricWiki ID |
| `strMood` | `str` | No | Track mood |
| `strMusicBrainzAlbumID` | `str` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | No | MusicBrainz Recording ID |
| `strMusicMozID` | `str` | No | MusicMoz ID |
| `strMusicVid` | `str` | No | Music video URL |
| `strMusicVidCompany` | `str` | No | Music video production company |
| `strMusicVidDirector` | `str` | No | Music video director |
| `strMusicVidScreen1` | `str` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `str` | No | Rate Your Music ID |
| `strReleaseFormat` | `str` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `str` | No | Album review |
| `strSpeed` | `str` | No | Album speed/tempo |
| `strStyle` | `str` | No | Musical style |
| `strTheme` | `str` | No | Track theme |
| `strTrack` | `str` | No | Track name |
| `strTrack3x3` | `str` | No | 3x3 track image URL |
| `strTrackLyrics` | `str` | No | Track lyrics |
| `strTrackThumb` | `str` | No | Track thumbnail URL |
| `strTwitter` | `str` | No | Twitter handle |
| `strWebsite` | `str` | No | Official website URL |
| `strWikidataID` | `str` | No | Wikidata ID |
| `strWikipediaID` | `str` | No | Wikipedia ID |

### Operations

#### `list(reqmatch=None, ctrl=None) -> list`

List entities matching the given criteria. The match is optional — call `list()` with no argument to list all records. Returns a list and raises on error.

```python
results = client.V1Lookup().list({"api_key": "example"})
for v1_lookup in results:
    print(v1_lookup)
```

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V1Lookup().load({"api_key": "api_key"})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V1LookupEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## V1SearchEntity

```python
v1_search = client.V1Search()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `list` | No |  |
| `idAlbum` | `str` | No | Unique album ID |
| `idArtist` | `str` | No | Artist ID |
| `idIMVDB` | `str` | No | IMVDB ID |
| `idLabel` | `str` | No | Label ID |
| `idLyric` | `str` | No | Lyrics ID |
| `idTrack` | `str` | No | Unique track ID |
| `intBornYear` | `str` | No | Birth year (for solo artists) |
| `intCD` | `str` | No | CD number |
| `intCharted` | `str` | No | Chart position |
| `intDiedYear` | `str` | No | Death year (if applicable) |
| `intDuration` | `str` | No | Track duration in milliseconds |
| `intFormedYear` | `str` | No | Year the artist was formed |
| `intLoved` | `str` | No | Number of loves/likes |
| `intMembers` | `str` | No | Number of band members |
| `intMusicVidComments` | `str` | No | Music video comment count |
| `intMusicVidDislikes` | `str` | No | Music video dislike count |
| `intMusicVidFavorites` | `str` | No | Music video favorite count |
| `intMusicVidLikes` | `str` | No | Music video like count |
| `intMusicVidViews` | `str` | No | Music video view count |
| `intSales` | `str` | No | Sales figures |
| `intScore` | `str` | No | Album score/rating |
| `intScoreVotes` | `str` | No | Number of score votes |
| `intTotalListeners` | `str` | No | Total listener count |
| `intTotalPlays` | `str` | No | Total play count |
| `intTrackNumber` | `str` | No | Track number on album |
| `intYearReleased` | `str` | No | Release year |
| `strAlbum` | `str` | No | Album name |
| `strAlbum3DCase` | `str` | No | 3D case image URL |
| `strAlbum3DFace` | `str` | No | 3D face image URL |
| `strAlbum3DFlat` | `str` | No | 3D flat image URL |
| `strAlbum3DThumb` | `str` | No | 3D thumbnail URL |
| `strAlbumCDart` | `str` | No | CD art URL |
| `strAlbumSpine` | `str` | No | Album spine image URL |
| `strAlbumStripped` | `str` | No | Album name stripped of special characters |
| `strAlbumThumb` | `str` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `str` | No | Album back cover URL |
| `strAlbumThumbHQ` | `str` | No | High quality album thumbnail URL |
| `strAllMusicID` | `str` | No | AllMusic ID |
| `strAmazonID` | `str` | No | Amazon ID |
| `strArtist` | `str` | No | Artist name |
| `strArtistAlternate` | `str` | No | Alternative artist name |
| `strArtistBanner` | `str` | No | Banner image URL |
| `strArtistClearart` | `str` | No | Clear art image URL |
| `strArtistCutout` | `str` | No | Cutout image URL |
| `strArtistFanart` | `str` | No | Fan art image URL |
| `strArtistFanart2` | `str` | No | Additional fan art image URL |
| `strArtistFanart3` | `str` | No | Additional fan art image URL |
| `strArtistFanart4` | `str` | No | Additional fan art image URL |
| `strArtistLogo` | `str` | No | Logo image URL |
| `strArtistStripped` | `str` | No | Artist name stripped |
| `strArtistThumb` | `str` | No | Thumbnail image URL |
| `strArtistWideThumb` | `str` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `str` | No | BBC Review ID |
| `strBiographyEN` | `str` | No | Biography in English |
| `strCountry` | `str` | No | Country of origin |
| `strCountryCode` | `str` | No | Country code |
| `strDescriptionEN` | `str` | No | Album description in English |
| `strDisbanded` | `str` | No | Disbandment status |
| `strDiscogsID` | `str` | No | Discogs ID |
| `strFacebook` | `str` | No | Facebook URL |
| `strGender` | `str` | No | Gender |
| `strGeniusID` | `str` | No | Genius ID |
| `strGenre` | `str` | No | Musical genre |
| `strISNIcode` | `str` | No | ISNI code |
| `strItunesID` | `str` | No | iTunes ID |
| `strLabel` | `str` | No | Record label |
| `strLastFMChart` | `str` | No | Last.fm chart URL |
| `strLocation` | `str` | No | Recording location |
| `strLocked` | `str` | No | Lock status |
| `strLyricWikiID` | `str` | No | LyricWiki ID |
| `strMood` | `str` | No | Album mood |
| `strMusicBrainzAlbumID` | `str` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `str` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `str` | No | MusicBrainz Release Group ID |
| `strMusicMozID` | `str` | No | MusicMoz ID |
| `strMusicVid` | `str` | No | Music video URL |
| `strMusicVidCompany` | `str` | No | Music video production company |
| `strMusicVidDirector` | `str` | No | Music video director |
| `strMusicVidScreen1` | `str` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `str` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `str` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `str` | No | Rate Your Music ID |
| `strReleaseFormat` | `str` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `str` | No | Album review |
| `strSpeed` | `str` | No | Album speed/tempo |
| `strStyle` | `str` | No | Musical style |
| `strTheme` | `str` | No | Album theme |
| `strTrack` | `str` | No | Track name |
| `strTrack3x3` | `str` | No | 3x3 track image URL |
| `strTrackLyrics` | `str` | No | Track lyrics |
| `strTrackThumb` | `str` | No | Track thumbnail URL |
| `strTwitter` | `str` | No | Twitter handle |
| `strWebsite` | `str` | No | Official website URL |
| `strWikidataID` | `str` | No | Wikidata ID |
| `strWikipediaID` | `str` | No | Wikipedia ID |

### Operations

#### `list(reqmatch=None, ctrl=None) -> list`

List entities matching the given criteria. The match is optional — call `list()` with no argument to list all records. Returns a list and raises on error.

```python
results = client.V1Search().list({"api_key": "example"})
for v1_search in results:
    print(v1_search)
```

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V1Search().load({"api_key": "api_key"})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V1SearchEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## V2ListEntity

```python
v2_list = client.V2List()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `list` | No |  |

### Operations

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V2List().load({"id_artist": 1})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V2ListEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## V2LookupEntity

```python
v2_lookup = client.V2Lookup()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `list` | No |  |
| `artists` | `list` | No |  |
| `track` | `list` | No |  |

### Operations

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V2Lookup().load({"id_album": 1})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V2LookupEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## V2SearchEntity

```python
v2_search = client.V2Search()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `list` | No |  |
| `artists` | `list` | No |  |
| `track` | `list` | No |  |

### Operations

#### `load(reqmatch, ctrl=None) -> dict`

Load a single entity matching the given criteria. Returns the entity data and raises on error.

```python
result = client.V2Search().load({"album_name": "album_name"})
```

### Common Methods

#### `data_get() -> dict`

Get the entity data.

#### `data_set(data)`

Set the entity data.

#### `match_get() -> dict`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make() -> Entity`

Create a new `V2SearchEntity` instance with the same options.

#### `get_name() -> str`

Return the entity name.


---

## Features

| Feature | Version | Description |
| --- | --- | --- |
| `test` | 0.0.1 | In-memory mock transport for testing without a live server |


Features are activated via the `feature` option:

```python
client = FreeMusicSDK({
    "feature": {
        "test": {"active": True},
    },
})
```

