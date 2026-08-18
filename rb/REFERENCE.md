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
| `idAlbum` | `String` | No |  |
| `idArtist` | `String` | No |  |
| `idIMVDB` | `String` | No |  |
| `idLyric` | `String` | No |  |
| `idTrack` | `String` | No |  |
| `intCD` | `String` | No |  |
| `intDuration` | `String` | No |  |
| `intLoved` | `String` | No |  |
| `intMusicVidComments` | `String` | No |  |
| `intMusicVidDislikes` | `String` | No |  |
| `intMusicVidFavorites` | `String` | No |  |
| `intMusicVidLikes` | `String` | No |  |
| `intMusicVidViews` | `String` | No |  |
| `intScore` | `String` | No |  |
| `intScoreVotes` | `String` | No |  |
| `intTotalListeners` | `String` | No |  |
| `intTotalPlays` | `String` | No |  |
| `intTrackNumber` | `String` | No |  |
| `strAlbum` | `String` | No |  |
| `strArtist` | `String` | No |  |
| `strArtistAlternate` | `String` | No |  |
| `strDescriptionEN` | `String` | No |  |
| `strGenre` | `String` | No |  |
| `strLocked` | `String` | No |  |
| `strMood` | `String` | No |  |
| `strMusicBrainzAlbumID` | `String` | No |  |
| `strMusicBrainzArtistID` | `String` | No |  |
| `strMusicBrainzID` | `String` | No |  |
| `strMusicVid` | `String` | No |  |
| `strMusicVidCompany` | `String` | No |  |
| `strMusicVidDirector` | `String` | No |  |
| `strMusicVidScreen1` | `String` | No |  |
| `strMusicVidScreen2` | `String` | No |  |
| `strMusicVidScreen3` | `String` | No |  |
| `strStyle` | `String` | No |  |
| `strTheme` | `String` | No |  |
| `strTrack` | `String` | No |  |
| `strTrack3x3` | `String` | No |  |
| `strTrackLyrics` | `String` | No |  |
| `strTrackThumb` | `String` | No |  |
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
| `idAlbum` | `String` | No |  |
| `idArtist` | `String` | No |  |
| `idIMVDB` | `String` | No |  |
| `idLabel` | `String` | No |  |
| `idLyric` | `String` | No |  |
| `idTrack` | `String` | No |  |
| `intBornYear` | `String` | No |  |
| `intCD` | `String` | No |  |
| `intCharted` | `String` | No |  |
| `intDiedYear` | `String` | No |  |
| `intDuration` | `String` | No |  |
| `intFormedYear` | `String` | No |  |
| `intLoved` | `String` | No |  |
| `intMembers` | `String` | No |  |
| `intMusicVidComments` | `String` | No |  |
| `intMusicVidDislikes` | `String` | No |  |
| `intMusicVidFavorites` | `String` | No |  |
| `intMusicVidLikes` | `String` | No |  |
| `intMusicVidViews` | `String` | No |  |
| `intSales` | `String` | No |  |
| `intScore` | `String` | No |  |
| `intScoreVotes` | `String` | No |  |
| `intTotalListeners` | `String` | No |  |
| `intTotalPlays` | `String` | No |  |
| `intTrackNumber` | `String` | No |  |
| `intYearReleased` | `String` | No |  |
| `strAlbum` | `String` | No |  |
| `strAlbum3DCase` | `String` | No |  |
| `strAlbum3DFace` | `String` | No |  |
| `strAlbum3DFlat` | `String` | No |  |
| `strAlbum3DThumb` | `String` | No |  |
| `strAlbumCDart` | `String` | No |  |
| `strAlbumSpine` | `String` | No |  |
| `strAlbumStripped` | `String` | No |  |
| `strAlbumThumb` | `String` | No |  |
| `strAlbumThumbBack` | `String` | No |  |
| `strAlbumThumbHQ` | `String` | No |  |
| `strAllMusicID` | `String` | No |  |
| `strAmazonID` | `String` | No |  |
| `strArtist` | `String` | No |  |
| `strArtistAlternate` | `String` | No |  |
| `strArtistBanner` | `String` | No |  |
| `strArtistClearart` | `String` | No |  |
| `strArtistCutout` | `String` | No |  |
| `strArtistFanart` | `String` | No |  |
| `strArtistFanart2` | `String` | No |  |
| `strArtistFanart3` | `String` | No |  |
| `strArtistFanart4` | `String` | No |  |
| `strArtistLogo` | `String` | No |  |
| `strArtistStripped` | `String` | No |  |
| `strArtistThumb` | `String` | No |  |
| `strArtistWideThumb` | `String` | No |  |
| `strBBCReviewID` | `String` | No |  |
| `strBiographyEN` | `String` | No |  |
| `strCountry` | `String` | No |  |
| `strCountryCode` | `String` | No |  |
| `strDescriptionEN` | `String` | No |  |
| `strDisbanded` | `String` | No |  |
| `strDiscogsID` | `String` | No |  |
| `strFacebook` | `String` | No |  |
| `strGender` | `String` | No |  |
| `strGeniusID` | `String` | No |  |
| `strGenre` | `String` | No |  |
| `strISNIcode` | `String` | No |  |
| `strItunesID` | `String` | No |  |
| `strLabel` | `String` | No |  |
| `strLastFMChart` | `String` | No |  |
| `strLocation` | `String` | No |  |
| `strLocked` | `String` | No |  |
| `strLyricWikiID` | `String` | No |  |
| `strMood` | `String` | No |  |
| `strMusicBrainzAlbumID` | `String` | No |  |
| `strMusicBrainzArtistID` | `String` | No |  |
| `strMusicBrainzID` | `String` | No |  |
| `strMusicMozID` | `String` | No |  |
| `strMusicVid` | `String` | No |  |
| `strMusicVidCompany` | `String` | No |  |
| `strMusicVidDirector` | `String` | No |  |
| `strMusicVidScreen1` | `String` | No |  |
| `strMusicVidScreen2` | `String` | No |  |
| `strMusicVidScreen3` | `String` | No |  |
| `strRateYourMusicID` | `String` | No |  |
| `strReleaseFormat` | `String` | No |  |
| `strReview` | `String` | No |  |
| `strSpeed` | `String` | No |  |
| `strStyle` | `String` | No |  |
| `strTheme` | `String` | No |  |
| `strTrack` | `String` | No |  |
| `strTrack3x3` | `String` | No |  |
| `strTrackLyrics` | `String` | No |  |
| `strTrackThumb` | `String` | No |  |
| `strTwitter` | `String` | No |  |
| `strWebsite` | `String` | No |  |
| `strWikidataID` | `String` | No |  |
| `strWikipediaID` | `String` | No |  |

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
| `idAlbum` | `String` | No |  |
| `idArtist` | `String` | No |  |
| `idIMVDB` | `String` | No |  |
| `idLabel` | `String` | No |  |
| `idLyric` | `String` | No |  |
| `idTrack` | `String` | No |  |
| `intBornYear` | `String` | No |  |
| `intCD` | `String` | No |  |
| `intCharted` | `String` | No |  |
| `intDiedYear` | `String` | No |  |
| `intDuration` | `String` | No |  |
| `intFormedYear` | `String` | No |  |
| `intLoved` | `String` | No |  |
| `intMembers` | `String` | No |  |
| `intMusicVidComments` | `String` | No |  |
| `intMusicVidDislikes` | `String` | No |  |
| `intMusicVidFavorites` | `String` | No |  |
| `intMusicVidLikes` | `String` | No |  |
| `intMusicVidViews` | `String` | No |  |
| `intSales` | `String` | No |  |
| `intScore` | `String` | No |  |
| `intScoreVotes` | `String` | No |  |
| `intTotalListeners` | `String` | No |  |
| `intTotalPlays` | `String` | No |  |
| `intTrackNumber` | `String` | No |  |
| `intYearReleased` | `String` | No |  |
| `strAlbum` | `String` | No |  |
| `strAlbum3DCase` | `String` | No |  |
| `strAlbum3DFace` | `String` | No |  |
| `strAlbum3DFlat` | `String` | No |  |
| `strAlbum3DThumb` | `String` | No |  |
| `strAlbumCDart` | `String` | No |  |
| `strAlbumSpine` | `String` | No |  |
| `strAlbumStripped` | `String` | No |  |
| `strAlbumThumb` | `String` | No |  |
| `strAlbumThumbBack` | `String` | No |  |
| `strAlbumThumbHQ` | `String` | No |  |
| `strAllMusicID` | `String` | No |  |
| `strAmazonID` | `String` | No |  |
| `strArtist` | `String` | No |  |
| `strArtistAlternate` | `String` | No |  |
| `strArtistBanner` | `String` | No |  |
| `strArtistClearart` | `String` | No |  |
| `strArtistCutout` | `String` | No |  |
| `strArtistFanart` | `String` | No |  |
| `strArtistFanart2` | `String` | No |  |
| `strArtistFanart3` | `String` | No |  |
| `strArtistFanart4` | `String` | No |  |
| `strArtistLogo` | `String` | No |  |
| `strArtistStripped` | `String` | No |  |
| `strArtistThumb` | `String` | No |  |
| `strArtistWideThumb` | `String` | No |  |
| `strBBCReviewID` | `String` | No |  |
| `strBiographyEN` | `String` | No |  |
| `strCountry` | `String` | No |  |
| `strCountryCode` | `String` | No |  |
| `strDescriptionEN` | `String` | No |  |
| `strDisbanded` | `String` | No |  |
| `strDiscogsID` | `String` | No |  |
| `strFacebook` | `String` | No |  |
| `strGender` | `String` | No |  |
| `strGeniusID` | `String` | No |  |
| `strGenre` | `String` | No |  |
| `strISNIcode` | `String` | No |  |
| `strItunesID` | `String` | No |  |
| `strLabel` | `String` | No |  |
| `strLastFMChart` | `String` | No |  |
| `strLocation` | `String` | No |  |
| `strLocked` | `String` | No |  |
| `strLyricWikiID` | `String` | No |  |
| `strMood` | `String` | No |  |
| `strMusicBrainzAlbumID` | `String` | No |  |
| `strMusicBrainzArtistID` | `String` | No |  |
| `strMusicBrainzID` | `String` | No |  |
| `strMusicMozID` | `String` | No |  |
| `strMusicVid` | `String` | No |  |
| `strMusicVidCompany` | `String` | No |  |
| `strMusicVidDirector` | `String` | No |  |
| `strMusicVidScreen1` | `String` | No |  |
| `strMusicVidScreen2` | `String` | No |  |
| `strMusicVidScreen3` | `String` | No |  |
| `strRateYourMusicID` | `String` | No |  |
| `strReleaseFormat` | `String` | No |  |
| `strReview` | `String` | No |  |
| `strSpeed` | `String` | No |  |
| `strStyle` | `String` | No |  |
| `strTheme` | `String` | No |  |
| `strTrack` | `String` | No |  |
| `strTrack3x3` | `String` | No |  |
| `strTrackLyrics` | `String` | No |  |
| `strTrackThumb` | `String` | No |  |
| `strTwitter` | `String` | No |  |
| `strWebsite` | `String` | No |  |
| `strWikidataID` | `String` | No |  |
| `strWikipediaID` | `String` | No |  |

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

