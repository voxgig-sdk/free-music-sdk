# FreeMusic Lua SDK



The Lua SDK for the FreeMusic API — an entity-oriented client using Lua conventions.

It exposes the API as capitalised, semantic **Entities** — e.g. `client:V1List()` — each with the same small set of operations (`list`, `load`) instead of raw URL paths and query strings. You call meaning, not endpoints, which keeps the cognitive load low.

> Other languages, the CLI, and MCP server live alongside this one — see
> the [top-level README](../README.md).


## Install
This package is not yet published to LuaRocks. Install it from the
GitHub release tag (`lua/vX.Y.Z`, see [Releases](https://github.com/voxgig-sdk/free-music-sdk/releases)),
or add the source directory to your `LUA_PATH`:

```bash
export LUA_PATH="path/to/lua/?.lua;path/to/lua/?/init.lua;;"
```


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### 1. Create a client

```lua
local sdk = require("free-music_sdk")

local client = sdk.new({
  apikey = os.getenv("FREE_MUSIC_APIKEY"),
})
```

### 2. List v1list records

Entity operations return `(value, err)`. For `list`, `value` is the
array of records itself — iterate it directly (there is no wrapper).

```lua
local v1lists, err = client:V1List():list()
if err then error(err) end

for _, item in ipairs(v1lists) do
  print(item["idAlbum"])
end
```

### 3. Load a v2list

V2List is nested under id_artist, so provide the `id_artist`.

```lua
local v2list, err = client:V2List():load({ id_artist = 1 })
if err then error(err) end
print(v2list)
```


## Error handling

Entity operations return `(value, err)`. Check `err` before using
the value:

```lua
local v2lookup, err = client:V2Lookup():load({ id_album = 1 })
if err then error(err) end
```

`direct` follows the same `(value, err)` convention:

```lua
local result, err = client:direct({
  path = "/api/resource/{id}",
  method = "GET",
  params = { id = "example_id" },
})
if err then error(err) end
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```lua
local result, err = client:direct({
  path = "/api/resource/{id}",
  method = "GET",
  params = { id = "example" },
})
if err then error(err) end

if result["ok"] then
  print(result["status"])  -- 200
  print(result["data"])    -- response body
end
```

### Prepare a request without sending it

```lua
local fetchdef, err = client:prepare({
  path = "/api/resource/{id}",
  method = "DELETE",
  params = { id = "example" },
})
if err then error(err) end

print(fetchdef["url"])
print(fetchdef["method"])
print(fetchdef["headers"])
```

### Use test mode

Create a mock client for unit testing — no server required:

```lua
local client = sdk.test()

local result, err = client:V2Lookup():load({ id_album = 1 })
-- result is the returned data; err is set on failure
```

### Use a custom fetch function

Replace the HTTP transport with your own function:

```lua
local function mock_fetch(url, init)
  return {
    status = 200,
    statusText = "OK",
    headers = {},
    json = function()
      return { id = "mock01" }
    end,
  }, nil
end

local client = sdk.new({
  base = "http://localhost:8080",
  system = {
    fetch = mock_fetch,
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
cd lua && busted test/
```


## Reference

### FreeMusicSDK

```lua
local sdk = require("free-music_sdk")
local client = sdk.new(options)
```

Creates a new SDK client.

| Option | Type | Description |
| --- | --- | --- |
| `apikey` | `string` | API key for authentication. |
| `base` | `string` | Base URL of the API server. |
| `prefix` | `string` | URL path prefix prepended to all requests. |
| `suffix` | `string` | URL path suffix appended to all requests. |
| `feature` | `table` | Feature activation flags. |
| `extend` | `table` | Additional Feature instances to load. |
| `system` | `table` | System overrides (e.g. custom `fetch` function). |

### test

```lua
local client = sdk.test(testopts, sdkopts)
```

Creates a test-mode client with mock transport. Both arguments may be `nil`.

### FreeMusicSDK methods

| Method | Signature | Description |
| --- | --- | --- |
| `options_map` | `() -> table` | Deep copy of current SDK options. |
| `get_utility` | `() -> Utility` | Copy of the SDK utility object. |
| `prepare` | `(fetchargs) -> table, err` | Build an HTTP request definition without sending. |
| `direct` | `(fetchargs) -> table, err` | Build and send an HTTP request. |
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
| `load` | `(reqmatch, ctrl) -> any, err` | Load a single entity by match criteria. |
| `list` | `(reqmatch, ctrl) -> any, err` | List entities matching the criteria. |
| `data_get` | `() -> table` | Get entity data. |
| `data_set` | `(data)` | Set entity data. |
| `match_get` | `() -> table` | Get entity match criteria. |
| `match_set` | `(match)` | Set entity match criteria. |
| `make` | `() -> Entity` | Create a new instance with the same options. |
| `get_name` | `() -> string` | Return the entity name. |

### Result shape

Entity operations return `(value, err)`. The `value` is the operation's
data **directly** — there is no wrapper:

| Operation | `value` |
| --- | --- |
| `load` | the entity record (a `table`) |
| `list` | an array (`table`) of entity records |

Check `err` first (it is non-`nil` on failure), then use `value`:

    local v1_list, err = client:V1List():load()
    if err then error(err) end
    -- v1_list is the loaded record

Only `direct()` returns a response envelope — a `table` with `ok`,
`status`, `headers`, and `data` keys.

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

Create an instance: `local v1_list = client:V1List(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `string` | Album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intCD` | `string` | CD number |
| `intDuration` | `string` | Track duration in milliseconds |
| `intLoved` | `string` | Number of loves/likes |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intScore` | `string` | Track score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `strAlbum` | `string` | Album name |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strDescriptionEN` | `string` | Track description in English |
| `strGenre` | `string` | Musical genre |
| `strLocked` | `string` | Lock status |
| `strMood` | `string` | Track mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Recording ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Track theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `trending` | `table` |  |

#### Example: Load

```lua
local v1_list, err = client:V1List():load({ api_key = "api_key" })
```

#### Example: List

```lua
local v1_lists, err = client:V1List():list()
```


### V1Lookup

Create an instance: `local v1_lookup = client:V1Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `string` | Album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLabel` | `string` | Label ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intBornYear` | `string` | Birth year (for solo artists) |
| `intCD` | `string` | CD number |
| `intCharted` | `string` | Chart position |
| `intDiedYear` | `string` | Death year (if applicable) |
| `intDuration` | `string` | Track duration in milliseconds |
| `intFormedYear` | `string` | Year the artist was formed |
| `intLoved` | `string` | Number of loves/likes |
| `intMembers` | `string` | Number of band members |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intSales` | `string` | Sales figures |
| `intScore` | `string` | Track score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `intYearReleased` | `string` | Release year |
| `strAlbum` | `string` | Album name |
| `strAlbum3DCase` | `string` | 3D case image URL |
| `strAlbum3DFace` | `string` | 3D face image URL |
| `strAlbum3DFlat` | `string` | 3D flat image URL |
| `strAlbum3DThumb` | `string` | 3D thumbnail URL |
| `strAlbumCDart` | `string` | CD art URL |
| `strAlbumSpine` | `string` | Album spine image URL |
| `strAlbumStripped` | `string` | Album name stripped of special characters |
| `strAlbumThumb` | `string` | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | Album back cover URL |
| `strAlbumThumbHQ` | `string` | High quality album thumbnail URL |
| `strAllMusicID` | `string` | AllMusic ID |
| `strAmazonID` | `string` | Amazon ID |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strArtistBanner` | `string` | Banner image URL |
| `strArtistClearart` | `string` | Clear art image URL |
| `strArtistCutout` | `string` | Cutout image URL |
| `strArtistFanart` | `string` | Fan art image URL |
| `strArtistFanart2` | `string` | Additional fan art image URL |
| `strArtistFanart3` | `string` | Additional fan art image URL |
| `strArtistFanart4` | `string` | Additional fan art image URL |
| `strArtistLogo` | `string` | Logo image URL |
| `strArtistStripped` | `string` | Artist name stripped |
| `strArtistThumb` | `string` | Thumbnail image URL |
| `strArtistWideThumb` | `string` | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | BBC Review ID |
| `strBiographyEN` | `string` | Biography in English |
| `strCountry` | `string` | Country of origin |
| `strCountryCode` | `string` | Country code |
| `strDescriptionEN` | `string` | Track description in English |
| `strDisbanded` | `string` | Disbandment status |
| `strDiscogsID` | `string` | Discogs ID |
| `strFacebook` | `string` | Facebook URL |
| `strGender` | `string` | Gender |
| `strGeniusID` | `string` | Genius ID |
| `strGenre` | `string` | Musical genre |
| `strISNIcode` | `string` | ISNI code |
| `strItunesID` | `string` | iTunes ID |
| `strLabel` | `string` | Record label |
| `strLastFMChart` | `string` | Last.fm chart URL |
| `strLocation` | `string` | Recording location |
| `strLocked` | `string` | Lock status |
| `strLyricWikiID` | `string` | LyricWiki ID |
| `strMood` | `string` | Track mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Recording ID |
| `strMusicMozID` | `string` | MusicMoz ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | Rate Your Music ID |
| `strReleaseFormat` | `string` | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | Album review |
| `strSpeed` | `string` | Album speed/tempo |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Track theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `strTwitter` | `string` | Twitter handle |
| `strWebsite` | `string` | Official website URL |
| `strWikidataID` | `string` | Wikidata ID |
| `strWikipediaID` | `string` | Wikipedia ID |

#### Example: Load

```lua
local v1_lookup, err = client:V1Lookup():load({ api_key = "api_key" })
```

#### Example: List

```lua
local v1_lookups, err = client:V1Lookup():list()
```


### V1Search

Create an instance: `local v1_search = client:V1Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `table` |  |
| `idAlbum` | `string` | Unique album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLabel` | `string` | Label ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intBornYear` | `string` | Birth year (for solo artists) |
| `intCD` | `string` | CD number |
| `intCharted` | `string` | Chart position |
| `intDiedYear` | `string` | Death year (if applicable) |
| `intDuration` | `string` | Track duration in milliseconds |
| `intFormedYear` | `string` | Year the artist was formed |
| `intLoved` | `string` | Number of loves/likes |
| `intMembers` | `string` | Number of band members |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intSales` | `string` | Sales figures |
| `intScore` | `string` | Album score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `intYearReleased` | `string` | Release year |
| `strAlbum` | `string` | Album name |
| `strAlbum3DCase` | `string` | 3D case image URL |
| `strAlbum3DFace` | `string` | 3D face image URL |
| `strAlbum3DFlat` | `string` | 3D flat image URL |
| `strAlbum3DThumb` | `string` | 3D thumbnail URL |
| `strAlbumCDart` | `string` | CD art URL |
| `strAlbumSpine` | `string` | Album spine image URL |
| `strAlbumStripped` | `string` | Album name stripped of special characters |
| `strAlbumThumb` | `string` | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | Album back cover URL |
| `strAlbumThumbHQ` | `string` | High quality album thumbnail URL |
| `strAllMusicID` | `string` | AllMusic ID |
| `strAmazonID` | `string` | Amazon ID |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strArtistBanner` | `string` | Banner image URL |
| `strArtistClearart` | `string` | Clear art image URL |
| `strArtistCutout` | `string` | Cutout image URL |
| `strArtistFanart` | `string` | Fan art image URL |
| `strArtistFanart2` | `string` | Additional fan art image URL |
| `strArtistFanart3` | `string` | Additional fan art image URL |
| `strArtistFanart4` | `string` | Additional fan art image URL |
| `strArtistLogo` | `string` | Logo image URL |
| `strArtistStripped` | `string` | Artist name stripped |
| `strArtistThumb` | `string` | Thumbnail image URL |
| `strArtistWideThumb` | `string` | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | BBC Review ID |
| `strBiographyEN` | `string` | Biography in English |
| `strCountry` | `string` | Country of origin |
| `strCountryCode` | `string` | Country code |
| `strDescriptionEN` | `string` | Album description in English |
| `strDisbanded` | `string` | Disbandment status |
| `strDiscogsID` | `string` | Discogs ID |
| `strFacebook` | `string` | Facebook URL |
| `strGender` | `string` | Gender |
| `strGeniusID` | `string` | Genius ID |
| `strGenre` | `string` | Musical genre |
| `strISNIcode` | `string` | ISNI code |
| `strItunesID` | `string` | iTunes ID |
| `strLabel` | `string` | Record label |
| `strLastFMChart` | `string` | Last.fm chart URL |
| `strLocation` | `string` | Recording location |
| `strLocked` | `string` | Lock status |
| `strLyricWikiID` | `string` | LyricWiki ID |
| `strMood` | `string` | Album mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Release Group ID |
| `strMusicMozID` | `string` | MusicMoz ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | Rate Your Music ID |
| `strReleaseFormat` | `string` | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | Album review |
| `strSpeed` | `string` | Album speed/tempo |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Album theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `strTwitter` | `string` | Twitter handle |
| `strWebsite` | `string` | Official website URL |
| `strWikidataID` | `string` | Wikidata ID |
| `strWikipediaID` | `string` | Wikipedia ID |

#### Example: Load

```lua
local v1_search, err = client:V1Search():load({ api_key = "api_key" })
```

#### Example: List

```lua
local v1_searchs, err = client:V1Search():list()
```


### V2List

Create an instance: `local v2_list = client:V2List(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `table` |  |

#### Example: Load

```lua
local v2_list, err = client:V2List():load({ id_artist = 1 })
```


### V2Lookup

Create an instance: `local v2_lookup = client:V2Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `table` |  |
| `artists` | `table` |  |
| `track` | `table` |  |

#### Example: Load

```lua
local v2_lookup, err = client:V2Lookup():load({ id_album = 1 })
```


### V2Search

Create an instance: `local v2_search = client:V2Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `table` |  |
| `artists` | `table` |  |
| `track` | `table` |  |

#### Example: Load

```lua
local v2_search, err = client:V2Search():load({ album_name = "album_name" })
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

Features are the extension mechanism. A feature is a Lua table
with hook methods named after pipeline stages (e.g. `PrePoint`,
`PreSpec`). Each method receives the context.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Data as tables

The Lua SDK uses plain Lua tables throughout rather than typed
objects. This mirrors the dynamic nature of the API and keeps the
SDK flexible — no code generation is needed when the API schema
changes.

Use `helpers.to_map()` to safely validate that a value is a table.

### Module structure

```
lua/
├── free-music_sdk.lua    -- Main SDK module
├── config.lua               -- Configuration
├── features.lua             -- Feature factory
├── core/                    -- Core types and context
├── entity/                  -- Entity implementations
├── feature/                 -- Built-in features (Base, Test, Log)
├── utility/                 -- Utility functions and struct library
└── test/                    -- Test suites
```

The main module (`free-music_sdk`) exports the SDK constructor
and test helper. Import entity or utility modules directly only
when needed.

### Entity state

Entity instances are stateful. After a successful `load`, the entity
stores the returned data and match criteria internally.

```lua
local v2lookup = client:V2Lookup()
v2lookup:load({ id_album = 1 })

-- v2lookup:data_get() now returns the v2lookup data from the last load
-- v2lookup:match_get() returns the last match criteria
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
