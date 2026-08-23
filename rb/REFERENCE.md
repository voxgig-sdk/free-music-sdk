# FreeMusic Ruby SDK Reference

Complete API reference for the FreeMusic Ruby SDK.


## FreeMusicSDK

### Constructor

```ruby
require_relative 'FreeMusic_sdk'

client = FreeMusicSDK.new(options)
```

Create a new SDK client instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `options` | `Hash` | SDK configuration options. |
| `options["apikey"]` | `String` | API key for authentication. |
| `options["base"]` | `String` | Base URL for API requests. |
| `options["prefix"]` | `String` | URL prefix appended after base. |
| `options["suffix"]` | `String` | URL suffix appended after path. |
| `options["headers"]` | `Hash` | Custom headers for all requests. |
| `options["feature"]` | `Hash` | Feature configuration. |
| `options["system"]` | `Hash` | System overrides (e.g. custom fetch). |


### Static Methods

#### `FreeMusicSDK.test(testopts = nil, sdkopts = nil)`

Create a test client with mock features active. Both arguments may be `nil`.

```ruby
client = FreeMusicSDK.test
```


### Instance Methods

#### `V1List(data = nil)`

Create a new `V1List` entity instance. Pass `nil` for no initial data.

#### `V1Lookup(data = nil)`

Create a new `V1Lookup` entity instance. Pass `nil` for no initial data.

#### `V1Search(data = nil)`

Create a new `V1Search` entity instance. Pass `nil` for no initial data.

#### `V2List(data = nil)`

Create a new `V2List` entity instance. Pass `nil` for no initial data.

#### `V2Lookup(data = nil)`

Create a new `V2Lookup` entity instance. Pass `nil` for no initial data.

#### `V2Search(data = nil)`

Create a new `V2Search` entity instance. Pass `nil` for no initial data.

#### `options_map -> Hash`

Return a deep copy of the current SDK options.

#### `get_utility -> Utility`

Return a copy of the SDK utility object.

#### `direct(fetchargs = {}) -> Hash`

Make a direct HTTP request to any API endpoint. Returns a result hash
(`{ "ok" => ..., "status" => ..., "data" => ..., "err" => ... }`); it
does not raise — inspect `result["ok"]`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `fetchargs["path"]` | `String` | URL path with optional `{param}` placeholders. |
| `fetchargs["method"]` | `String` | HTTP method (default: `"GET"`). |
| `fetchargs["params"]` | `Hash` | Path parameter values for `{param}` substitution. |
| `fetchargs["query"]` | `Hash` | Query string parameters. |
| `fetchargs["headers"]` | `Hash` | Request headers (merged with defaults). |
| `fetchargs["body"]` | `any` | Request body (hashes are JSON-serialized). |
| `fetchargs["ctrl"]` | `Hash` | Control options (e.g. `{ "explain" => true }`). |

**Returns:** `Hash`

#### `prepare(fetchargs = {}) -> Hash`

Prepare a fetch definition without sending the request. Accepts the
same parameters as `direct()`. Raises on error.

**Returns:** `Hash` (the fetch definition; raises on error)


---

## V1ListEntity

```ruby
v1_list = client.V1List
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `String` | No | Album ID |
| `idArtist` | `String` | No | Artist ID |
| `idIMVDB` | `String` | No | IMVDB ID |
| `idLyric` | `String` | No | Lyrics ID |
| `idTrack` | `String` | No | Unique track ID |
| `intCD` | `String` | No | CD number |
| `intDuration` | `String` | No | Track duration in milliseconds |
| `intLoved` | `String` | No | Number of loves/likes |
| `intMusicVidComments` | `String` | No | Music video comment count |
| `intMusicVidDislikes` | `String` | No | Music video dislike count |
| `intMusicVidFavorites` | `String` | No | Music video favorite count |
| `intMusicVidLikes` | `String` | No | Music video like count |
| `intMusicVidViews` | `String` | No | Music video view count |
| `intScore` | `String` | No | Track score/rating |
| `intScoreVotes` | `String` | No | Number of score votes |
| `intTotalListeners` | `String` | No | Total listener count |
| `intTotalPlays` | `String` | No | Total play count |
| `intTrackNumber` | `String` | No | Track number on album |
| `strAlbum` | `String` | No | Album name |
| `strArtist` | `String` | No | Artist name |
| `strArtistAlternate` | `String` | No | Alternative artist name |
| `strDescriptionEN` | `String` | No | Track description in English |
| `strGenre` | `String` | No | Musical genre |
| `strLocked` | `String` | No | Lock status |
| `strMood` | `String` | No | Track mood |
| `strMusicBrainzAlbumID` | `String` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | No | MusicBrainz Recording ID |
| `strMusicVid` | `String` | No | Music video URL |
| `strMusicVidCompany` | `String` | No | Music video production company |
| `strMusicVidDirector` | `String` | No | Music video director |
| `strMusicVidScreen1` | `String` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | No | Music video screenshot 3 |
| `strStyle` | `String` | No | Musical style |
| `strTheme` | `String` | No | Track theme |
| `strTrack` | `String` | No | Track name |
| `strTrack3x3` | `String` | No | 3x3 track image URL |
| `strTrackLyrics` | `String` | No | Track lyrics |
| `strTrackThumb` | `String` | No | Track thumbnail URL |
| `trending` | `Array` | No |  |

### Operations

#### `list(reqmatch = nil, ctrl = nil) -> Array`

List entities matching the given criteria (call with no argument to list all). Returns an array. Raises on error.

```ruby
results = client.V1List.list
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V1List.load({ "api_key" => "api_key" })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V1ListEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## V1LookupEntity

```ruby
v1_lookup = client.V1Lookup
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `String` | No | Album ID |
| `idArtist` | `String` | No | Artist ID |
| `idIMVDB` | `String` | No | IMVDB ID |
| `idLabel` | `String` | No | Label ID |
| `idLyric` | `String` | No | Lyrics ID |
| `idTrack` | `String` | No | Unique track ID |
| `intBornYear` | `String` | No | Birth year (for solo artists) |
| `intCD` | `String` | No | CD number |
| `intCharted` | `String` | No | Chart position |
| `intDiedYear` | `String` | No | Death year (if applicable) |
| `intDuration` | `String` | No | Track duration in milliseconds |
| `intFormedYear` | `String` | No | Year the artist was formed |
| `intLoved` | `String` | No | Number of loves/likes |
| `intMembers` | `String` | No | Number of band members |
| `intMusicVidComments` | `String` | No | Music video comment count |
| `intMusicVidDislikes` | `String` | No | Music video dislike count |
| `intMusicVidFavorites` | `String` | No | Music video favorite count |
| `intMusicVidLikes` | `String` | No | Music video like count |
| `intMusicVidViews` | `String` | No | Music video view count |
| `intSales` | `String` | No | Sales figures |
| `intScore` | `String` | No | Track score/rating |
| `intScoreVotes` | `String` | No | Number of score votes |
| `intTotalListeners` | `String` | No | Total listener count |
| `intTotalPlays` | `String` | No | Total play count |
| `intTrackNumber` | `String` | No | Track number on album |
| `intYearReleased` | `String` | No | Release year |
| `strAlbum` | `String` | No | Album name |
| `strAlbum3DCase` | `String` | No | 3D case image URL |
| `strAlbum3DFace` | `String` | No | 3D face image URL |
| `strAlbum3DFlat` | `String` | No | 3D flat image URL |
| `strAlbum3DThumb` | `String` | No | 3D thumbnail URL |
| `strAlbumCDart` | `String` | No | CD art URL |
| `strAlbumSpine` | `String` | No | Album spine image URL |
| `strAlbumStripped` | `String` | No | Album name stripped of special characters |
| `strAlbumThumb` | `String` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `String` | No | Album back cover URL |
| `strAlbumThumbHQ` | `String` | No | High quality album thumbnail URL |
| `strAllMusicID` | `String` | No | AllMusic ID |
| `strAmazonID` | `String` | No | Amazon ID |
| `strArtist` | `String` | No | Artist name |
| `strArtistAlternate` | `String` | No | Alternative artist name |
| `strArtistBanner` | `String` | No | Banner image URL |
| `strArtistClearart` | `String` | No | Clear art image URL |
| `strArtistCutout` | `String` | No | Cutout image URL |
| `strArtistFanart` | `String` | No | Fan art image URL |
| `strArtistFanart2` | `String` | No | Additional fan art image URL |
| `strArtistFanart3` | `String` | No | Additional fan art image URL |
| `strArtistFanart4` | `String` | No | Additional fan art image URL |
| `strArtistLogo` | `String` | No | Logo image URL |
| `strArtistStripped` | `String` | No | Artist name stripped |
| `strArtistThumb` | `String` | No | Thumbnail image URL |
| `strArtistWideThumb` | `String` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `String` | No | BBC Review ID |
| `strBiographyEN` | `String` | No | Biography in English |
| `strCountry` | `String` | No | Country of origin |
| `strCountryCode` | `String` | No | Country code |
| `strDescriptionEN` | `String` | No | Track description in English |
| `strDisbanded` | `String` | No | Disbandment status |
| `strDiscogsID` | `String` | No | Discogs ID |
| `strFacebook` | `String` | No | Facebook URL |
| `strGender` | `String` | No | Gender |
| `strGeniusID` | `String` | No | Genius ID |
| `strGenre` | `String` | No | Musical genre |
| `strISNIcode` | `String` | No | ISNI code |
| `strItunesID` | `String` | No | iTunes ID |
| `strLabel` | `String` | No | Record label |
| `strLastFMChart` | `String` | No | Last.fm chart URL |
| `strLocation` | `String` | No | Recording location |
| `strLocked` | `String` | No | Lock status |
| `strLyricWikiID` | `String` | No | LyricWiki ID |
| `strMood` | `String` | No | Track mood |
| `strMusicBrainzAlbumID` | `String` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | No | MusicBrainz Recording ID |
| `strMusicMozID` | `String` | No | MusicMoz ID |
| `strMusicVid` | `String` | No | Music video URL |
| `strMusicVidCompany` | `String` | No | Music video production company |
| `strMusicVidDirector` | `String` | No | Music video director |
| `strMusicVidScreen1` | `String` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `String` | No | Rate Your Music ID |
| `strReleaseFormat` | `String` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `String` | No | Album review |
| `strSpeed` | `String` | No | Album speed/tempo |
| `strStyle` | `String` | No | Musical style |
| `strTheme` | `String` | No | Track theme |
| `strTrack` | `String` | No | Track name |
| `strTrack3x3` | `String` | No | 3x3 track image URL |
| `strTrackLyrics` | `String` | No | Track lyrics |
| `strTrackThumb` | `String` | No | Track thumbnail URL |
| `strTwitter` | `String` | No | Twitter handle |
| `strWebsite` | `String` | No | Official website URL |
| `strWikidataID` | `String` | No | Wikidata ID |
| `strWikipediaID` | `String` | No | Wikipedia ID |

### Operations

#### `list(reqmatch = nil, ctrl = nil) -> Array`

List entities matching the given criteria (call with no argument to list all). Returns an array. Raises on error.

```ruby
results = client.V1Lookup.list
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V1Lookup.load({ "api_key" => "api_key" })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V1LookupEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## V1SearchEntity

```ruby
v1_search = client.V1Search
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `Array` | No |  |
| `idAlbum` | `String` | No | Unique album ID |
| `idArtist` | `String` | No | Artist ID |
| `idIMVDB` | `String` | No | IMVDB ID |
| `idLabel` | `String` | No | Label ID |
| `idLyric` | `String` | No | Lyrics ID |
| `idTrack` | `String` | No | Unique track ID |
| `intBornYear` | `String` | No | Birth year (for solo artists) |
| `intCD` | `String` | No | CD number |
| `intCharted` | `String` | No | Chart position |
| `intDiedYear` | `String` | No | Death year (if applicable) |
| `intDuration` | `String` | No | Track duration in milliseconds |
| `intFormedYear` | `String` | No | Year the artist was formed |
| `intLoved` | `String` | No | Number of loves/likes |
| `intMembers` | `String` | No | Number of band members |
| `intMusicVidComments` | `String` | No | Music video comment count |
| `intMusicVidDislikes` | `String` | No | Music video dislike count |
| `intMusicVidFavorites` | `String` | No | Music video favorite count |
| `intMusicVidLikes` | `String` | No | Music video like count |
| `intMusicVidViews` | `String` | No | Music video view count |
| `intSales` | `String` | No | Sales figures |
| `intScore` | `String` | No | Album score/rating |
| `intScoreVotes` | `String` | No | Number of score votes |
| `intTotalListeners` | `String` | No | Total listener count |
| `intTotalPlays` | `String` | No | Total play count |
| `intTrackNumber` | `String` | No | Track number on album |
| `intYearReleased` | `String` | No | Release year |
| `strAlbum` | `String` | No | Album name |
| `strAlbum3DCase` | `String` | No | 3D case image URL |
| `strAlbum3DFace` | `String` | No | 3D face image URL |
| `strAlbum3DFlat` | `String` | No | 3D flat image URL |
| `strAlbum3DThumb` | `String` | No | 3D thumbnail URL |
| `strAlbumCDart` | `String` | No | CD art URL |
| `strAlbumSpine` | `String` | No | Album spine image URL |
| `strAlbumStripped` | `String` | No | Album name stripped of special characters |
| `strAlbumThumb` | `String` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `String` | No | Album back cover URL |
| `strAlbumThumbHQ` | `String` | No | High quality album thumbnail URL |
| `strAllMusicID` | `String` | No | AllMusic ID |
| `strAmazonID` | `String` | No | Amazon ID |
| `strArtist` | `String` | No | Artist name |
| `strArtistAlternate` | `String` | No | Alternative artist name |
| `strArtistBanner` | `String` | No | Banner image URL |
| `strArtistClearart` | `String` | No | Clear art image URL |
| `strArtistCutout` | `String` | No | Cutout image URL |
| `strArtistFanart` | `String` | No | Fan art image URL |
| `strArtistFanart2` | `String` | No | Additional fan art image URL |
| `strArtistFanart3` | `String` | No | Additional fan art image URL |
| `strArtistFanart4` | `String` | No | Additional fan art image URL |
| `strArtistLogo` | `String` | No | Logo image URL |
| `strArtistStripped` | `String` | No | Artist name stripped |
| `strArtistThumb` | `String` | No | Thumbnail image URL |
| `strArtistWideThumb` | `String` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `String` | No | BBC Review ID |
| `strBiographyEN` | `String` | No | Biography in English |
| `strCountry` | `String` | No | Country of origin |
| `strCountryCode` | `String` | No | Country code |
| `strDescriptionEN` | `String` | No | Album description in English |
| `strDisbanded` | `String` | No | Disbandment status |
| `strDiscogsID` | `String` | No | Discogs ID |
| `strFacebook` | `String` | No | Facebook URL |
| `strGender` | `String` | No | Gender |
| `strGeniusID` | `String` | No | Genius ID |
| `strGenre` | `String` | No | Musical genre |
| `strISNIcode` | `String` | No | ISNI code |
| `strItunesID` | `String` | No | iTunes ID |
| `strLabel` | `String` | No | Record label |
| `strLastFMChart` | `String` | No | Last.fm chart URL |
| `strLocation` | `String` | No | Recording location |
| `strLocked` | `String` | No | Lock status |
| `strLyricWikiID` | `String` | No | LyricWiki ID |
| `strMood` | `String` | No | Album mood |
| `strMusicBrainzAlbumID` | `String` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | No | MusicBrainz Release Group ID |
| `strMusicMozID` | `String` | No | MusicMoz ID |
| `strMusicVid` | `String` | No | Music video URL |
| `strMusicVidCompany` | `String` | No | Music video production company |
| `strMusicVidDirector` | `String` | No | Music video director |
| `strMusicVidScreen1` | `String` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `String` | No | Rate Your Music ID |
| `strReleaseFormat` | `String` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `String` | No | Album review |
| `strSpeed` | `String` | No | Album speed/tempo |
| `strStyle` | `String` | No | Musical style |
| `strTheme` | `String` | No | Album theme |
| `strTrack` | `String` | No | Track name |
| `strTrack3x3` | `String` | No | 3x3 track image URL |
| `strTrackLyrics` | `String` | No | Track lyrics |
| `strTrackThumb` | `String` | No | Track thumbnail URL |
| `strTwitter` | `String` | No | Twitter handle |
| `strWebsite` | `String` | No | Official website URL |
| `strWikidataID` | `String` | No | Wikidata ID |
| `strWikipediaID` | `String` | No | Wikipedia ID |

### Operations

#### `list(reqmatch = nil, ctrl = nil) -> Array`

List entities matching the given criteria (call with no argument to list all). Returns an array. Raises on error.

```ruby
results = client.V1Search.list
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V1Search.load({ "api_key" => "api_key" })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V1SearchEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## V2ListEntity

```ruby
v2_list = client.V2List
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `Array` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V2List.load({ "id_artist" => 1 })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V2ListEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## V2LookupEntity

```ruby
v2_lookup = client.V2Lookup
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `Array` | No |  |
| `artists` | `Array` | No |  |
| `track` | `Array` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V2Lookup.load({ "id_album" => 1 })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V2LookupEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## V2SearchEntity

```ruby
v2_search = client.V2Search
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `Array` | No |  |
| `artists` | `Array` | No |  |
| `track` | `Array` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.V2Search.load({ "album_name" => "album_name" })
```

### Common Methods

#### `data_get -> Hash`

Get the entity data. Returns a copy of the current data.

#### `data_set(data)`

Set the entity data.

#### `match_get -> Hash`

Get the entity match criteria.

#### `match_set(match)`

Set the entity match criteria.

#### `make -> Entity`

Create a new `V2SearchEntity` instance with the same client and
options.

#### `get_name -> String`

Return the entity name.


---

## Features

| Feature | Version | Description |
| --- | --- | --- |
| `test` | 0.0.1 | In-memory mock transport for testing without a live server |


Features are activated via the `feature` option:

```ruby
client = FreeMusicSDK.new({
  "feature" => {
    "test" => { "active" => true },
  },
})
```

