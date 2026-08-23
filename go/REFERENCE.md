# FreeMusic Golang SDK Reference

Complete API reference for the FreeMusic Golang SDK.


## FreeMusicSDK

### Constructor

```go
func NewFreeMusicSDK(options map[string]any) *FreeMusicSDK
```

Create a new SDK client instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `options` | `map[string]any` | SDK configuration options. |
| `options["apikey"]` | `string` | API key for authentication. |
| `options["base"]` | `string` | Base URL for API requests. |
| `options["prefix"]` | `string` | URL prefix appended after base. |
| `options["suffix"]` | `string` | URL suffix appended after path. |
| `options["headers"]` | `map[string]any` | Custom headers for all requests. |
| `options["feature"]` | `map[string]any` | Feature configuration. |
| `options["system"]` | `map[string]any` | System overrides (e.g. custom fetch). |


### Static Methods

#### `Test() *FreeMusicSDK`

No-arg convenience constructor for the common no-options test case.

```go
client := sdk.Test()
```

#### `TestSDK(testopts, sdkopts map[string]any) *FreeMusicSDK`

Test client with options. Both arguments may be `nil`.

```go
client := sdk.TestSDK(testopts, sdkopts)
```


### Instance Methods

#### `V1List(data map[string]any) FreeMusicEntity`

Create a new `V1List` entity instance. Pass `nil` for no initial data.

#### `V1Lookup(data map[string]any) FreeMusicEntity`

Create a new `V1Lookup` entity instance. Pass `nil` for no initial data.

#### `V1Search(data map[string]any) FreeMusicEntity`

Create a new `V1Search` entity instance. Pass `nil` for no initial data.

#### `V2List(data map[string]any) FreeMusicEntity`

Create a new `V2List` entity instance. Pass `nil` for no initial data.

#### `V2Lookup(data map[string]any) FreeMusicEntity`

Create a new `V2Lookup` entity instance. Pass `nil` for no initial data.

#### `V2Search(data map[string]any) FreeMusicEntity`

Create a new `V2Search` entity instance. Pass `nil` for no initial data.

#### `OptionsMap() map[string]any`

Return a deep copy of the current SDK options.

#### `GetUtility() *Utility`

Return a copy of the SDK utility object.

#### `Direct(fetchargs map[string]any) (map[string]any, error)`

Make a direct HTTP request to any API endpoint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `fetchargs["path"]` | `string` | URL path with optional `{param}` placeholders. |
| `fetchargs["method"]` | `string` | HTTP method (default: `"GET"`). |
| `fetchargs["params"]` | `map[string]any` | Path parameter values for `{param}` substitution. |
| `fetchargs["query"]` | `map[string]any` | Query string parameters. |
| `fetchargs["headers"]` | `map[string]any` | Request headers (merged with defaults). |
| `fetchargs["body"]` | `any` | Request body (maps are JSON-serialized). |
| `fetchargs["ctrl"]` | `map[string]any` | Control options (e.g. `map[string]any{"explain": true}`). |

**Returns:** `(map[string]any, error)`

#### `Prepare(fetchargs map[string]any) (map[string]any, error)`

Prepare a fetch definition without sending the request. Accepts the
same parameters as `Direct()`.

**Returns:** `(map[string]any, error)`


---

## V1ListEntity

```go
v1List := client.V1List(nil)
fmt.Println(v1List.GetName()) // "v1_list"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `string` | No | Album ID |
| `idArtist` | `string` | No | Artist ID |
| `idIMVDB` | `string` | No | IMVDB ID |
| `idLyric` | `string` | No | Lyrics ID |
| `idTrack` | `string` | No | Unique track ID |
| `intCD` | `string` | No | CD number |
| `intDuration` | `string` | No | Track duration in milliseconds |
| `intLoved` | `string` | No | Number of loves/likes |
| `intMusicVidComments` | `string` | No | Music video comment count |
| `intMusicVidDislikes` | `string` | No | Music video dislike count |
| `intMusicVidFavorites` | `string` | No | Music video favorite count |
| `intMusicVidLikes` | `string` | No | Music video like count |
| `intMusicVidViews` | `string` | No | Music video view count |
| `intScore` | `string` | No | Track score/rating |
| `intScoreVotes` | `string` | No | Number of score votes |
| `intTotalListeners` | `string` | No | Total listener count |
| `intTotalPlays` | `string` | No | Total play count |
| `intTrackNumber` | `string` | No | Track number on album |
| `strAlbum` | `string` | No | Album name |
| `strArtist` | `string` | No | Artist name |
| `strArtistAlternate` | `string` | No | Alternative artist name |
| `strDescriptionEN` | `string` | No | Track description in English |
| `strGenre` | `string` | No | Musical genre |
| `strLocked` | `string` | No | Lock status |
| `strMood` | `string` | No | Track mood |
| `strMusicBrainzAlbumID` | `string` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | No | MusicBrainz Recording ID |
| `strMusicVid` | `string` | No | Music video URL |
| `strMusicVidCompany` | `string` | No | Music video production company |
| `strMusicVidDirector` | `string` | No | Music video director |
| `strMusicVidScreen1` | `string` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | No | Music video screenshot 3 |
| `strStyle` | `string` | No | Musical style |
| `strTheme` | `string` | No | Track theme |
| `strTrack` | `string` | No | Track name |
| `strTrack3x3` | `string` | No | 3x3 track image URL |
| `strTrackLyrics` | `string` | No | Track lyrics |
| `strTrackThumb` | `string` | No | Track thumbnail URL |
| `trending` | `[]any` | No |  |

### Operations

#### `List(reqmatch, ctrl map[string]any) (any, error)`

List entities matching the given criteria. Returns an array.

```go
results, err := client.V1List(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(results)
```

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V1List(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V1ListEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## V1LookupEntity

```go
v1Lookup := client.V1Lookup(nil)
fmt.Println(v1Lookup.GetName()) // "v1_lookup"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `idAlbum` | `string` | No | Album ID |
| `idArtist` | `string` | No | Artist ID |
| `idIMVDB` | `string` | No | IMVDB ID |
| `idLabel` | `string` | No | Label ID |
| `idLyric` | `string` | No | Lyrics ID |
| `idTrack` | `string` | No | Unique track ID |
| `intBornYear` | `string` | No | Birth year (for solo artists) |
| `intCD` | `string` | No | CD number |
| `intCharted` | `string` | No | Chart position |
| `intDiedYear` | `string` | No | Death year (if applicable) |
| `intDuration` | `string` | No | Track duration in milliseconds |
| `intFormedYear` | `string` | No | Year the artist was formed |
| `intLoved` | `string` | No | Number of loves/likes |
| `intMembers` | `string` | No | Number of band members |
| `intMusicVidComments` | `string` | No | Music video comment count |
| `intMusicVidDislikes` | `string` | No | Music video dislike count |
| `intMusicVidFavorites` | `string` | No | Music video favorite count |
| `intMusicVidLikes` | `string` | No | Music video like count |
| `intMusicVidViews` | `string` | No | Music video view count |
| `intSales` | `string` | No | Sales figures |
| `intScore` | `string` | No | Track score/rating |
| `intScoreVotes` | `string` | No | Number of score votes |
| `intTotalListeners` | `string` | No | Total listener count |
| `intTotalPlays` | `string` | No | Total play count |
| `intTrackNumber` | `string` | No | Track number on album |
| `intYearReleased` | `string` | No | Release year |
| `strAlbum` | `string` | No | Album name |
| `strAlbum3DCase` | `string` | No | 3D case image URL |
| `strAlbum3DFace` | `string` | No | 3D face image URL |
| `strAlbum3DFlat` | `string` | No | 3D flat image URL |
| `strAlbum3DThumb` | `string` | No | 3D thumbnail URL |
| `strAlbumCDart` | `string` | No | CD art URL |
| `strAlbumSpine` | `string` | No | Album spine image URL |
| `strAlbumStripped` | `string` | No | Album name stripped of special characters |
| `strAlbumThumb` | `string` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | No | Album back cover URL |
| `strAlbumThumbHQ` | `string` | No | High quality album thumbnail URL |
| `strAllMusicID` | `string` | No | AllMusic ID |
| `strAmazonID` | `string` | No | Amazon ID |
| `strArtist` | `string` | No | Artist name |
| `strArtistAlternate` | `string` | No | Alternative artist name |
| `strArtistBanner` | `string` | No | Banner image URL |
| `strArtistClearart` | `string` | No | Clear art image URL |
| `strArtistCutout` | `string` | No | Cutout image URL |
| `strArtistFanart` | `string` | No | Fan art image URL |
| `strArtistFanart2` | `string` | No | Additional fan art image URL |
| `strArtistFanart3` | `string` | No | Additional fan art image URL |
| `strArtistFanart4` | `string` | No | Additional fan art image URL |
| `strArtistLogo` | `string` | No | Logo image URL |
| `strArtistStripped` | `string` | No | Artist name stripped |
| `strArtistThumb` | `string` | No | Thumbnail image URL |
| `strArtistWideThumb` | `string` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | No | BBC Review ID |
| `strBiographyEN` | `string` | No | Biography in English |
| `strCountry` | `string` | No | Country of origin |
| `strCountryCode` | `string` | No | Country code |
| `strDescriptionEN` | `string` | No | Track description in English |
| `strDisbanded` | `string` | No | Disbandment status |
| `strDiscogsID` | `string` | No | Discogs ID |
| `strFacebook` | `string` | No | Facebook URL |
| `strGender` | `string` | No | Gender |
| `strGeniusID` | `string` | No | Genius ID |
| `strGenre` | `string` | No | Musical genre |
| `strISNIcode` | `string` | No | ISNI code |
| `strItunesID` | `string` | No | iTunes ID |
| `strLabel` | `string` | No | Record label |
| `strLastFMChart` | `string` | No | Last.fm chart URL |
| `strLocation` | `string` | No | Recording location |
| `strLocked` | `string` | No | Lock status |
| `strLyricWikiID` | `string` | No | LyricWiki ID |
| `strMood` | `string` | No | Track mood |
| `strMusicBrainzAlbumID` | `string` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | No | MusicBrainz Recording ID |
| `strMusicMozID` | `string` | No | MusicMoz ID |
| `strMusicVid` | `string` | No | Music video URL |
| `strMusicVidCompany` | `string` | No | Music video production company |
| `strMusicVidDirector` | `string` | No | Music video director |
| `strMusicVidScreen1` | `string` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | No | Rate Your Music ID |
| `strReleaseFormat` | `string` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | No | Album review |
| `strSpeed` | `string` | No | Album speed/tempo |
| `strStyle` | `string` | No | Musical style |
| `strTheme` | `string` | No | Track theme |
| `strTrack` | `string` | No | Track name |
| `strTrack3x3` | `string` | No | 3x3 track image URL |
| `strTrackLyrics` | `string` | No | Track lyrics |
| `strTrackThumb` | `string` | No | Track thumbnail URL |
| `strTwitter` | `string` | No | Twitter handle |
| `strWebsite` | `string` | No | Official website URL |
| `strWikidataID` | `string` | No | Wikidata ID |
| `strWikipediaID` | `string` | No | Wikipedia ID |

### Operations

#### `List(reqmatch, ctrl map[string]any) (any, error)`

List entities matching the given criteria. Returns an array.

```go
results, err := client.V1Lookup(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(results)
```

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V1Lookup(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V1LookupEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## V1SearchEntity

```go
v1Search := client.V1Search(nil)
fmt.Println(v1Search.GetName()) // "v1_search"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `[]any` | No |  |
| `idAlbum` | `string` | No | Unique album ID |
| `idArtist` | `string` | No | Artist ID |
| `idIMVDB` | `string` | No | IMVDB ID |
| `idLabel` | `string` | No | Label ID |
| `idLyric` | `string` | No | Lyrics ID |
| `idTrack` | `string` | No | Unique track ID |
| `intBornYear` | `string` | No | Birth year (for solo artists) |
| `intCD` | `string` | No | CD number |
| `intCharted` | `string` | No | Chart position |
| `intDiedYear` | `string` | No | Death year (if applicable) |
| `intDuration` | `string` | No | Track duration in milliseconds |
| `intFormedYear` | `string` | No | Year the artist was formed |
| `intLoved` | `string` | No | Number of loves/likes |
| `intMembers` | `string` | No | Number of band members |
| `intMusicVidComments` | `string` | No | Music video comment count |
| `intMusicVidDislikes` | `string` | No | Music video dislike count |
| `intMusicVidFavorites` | `string` | No | Music video favorite count |
| `intMusicVidLikes` | `string` | No | Music video like count |
| `intMusicVidViews` | `string` | No | Music video view count |
| `intSales` | `string` | No | Sales figures |
| `intScore` | `string` | No | Album score/rating |
| `intScoreVotes` | `string` | No | Number of score votes |
| `intTotalListeners` | `string` | No | Total listener count |
| `intTotalPlays` | `string` | No | Total play count |
| `intTrackNumber` | `string` | No | Track number on album |
| `intYearReleased` | `string` | No | Release year |
| `strAlbum` | `string` | No | Album name |
| `strAlbum3DCase` | `string` | No | 3D case image URL |
| `strAlbum3DFace` | `string` | No | 3D face image URL |
| `strAlbum3DFlat` | `string` | No | 3D flat image URL |
| `strAlbum3DThumb` | `string` | No | 3D thumbnail URL |
| `strAlbumCDart` | `string` | No | CD art URL |
| `strAlbumSpine` | `string` | No | Album spine image URL |
| `strAlbumStripped` | `string` | No | Album name stripped of special characters |
| `strAlbumThumb` | `string` | No | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | No | Album back cover URL |
| `strAlbumThumbHQ` | `string` | No | High quality album thumbnail URL |
| `strAllMusicID` | `string` | No | AllMusic ID |
| `strAmazonID` | `string` | No | Amazon ID |
| `strArtist` | `string` | No | Artist name |
| `strArtistAlternate` | `string` | No | Alternative artist name |
| `strArtistBanner` | `string` | No | Banner image URL |
| `strArtistClearart` | `string` | No | Clear art image URL |
| `strArtistCutout` | `string` | No | Cutout image URL |
| `strArtistFanart` | `string` | No | Fan art image URL |
| `strArtistFanart2` | `string` | No | Additional fan art image URL |
| `strArtistFanart3` | `string` | No | Additional fan art image URL |
| `strArtistFanart4` | `string` | No | Additional fan art image URL |
| `strArtistLogo` | `string` | No | Logo image URL |
| `strArtistStripped` | `string` | No | Artist name stripped |
| `strArtistThumb` | `string` | No | Thumbnail image URL |
| `strArtistWideThumb` | `string` | No | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | No | BBC Review ID |
| `strBiographyEN` | `string` | No | Biography in English |
| `strCountry` | `string` | No | Country of origin |
| `strCountryCode` | `string` | No | Country code |
| `strDescriptionEN` | `string` | No | Album description in English |
| `strDisbanded` | `string` | No | Disbandment status |
| `strDiscogsID` | `string` | No | Discogs ID |
| `strFacebook` | `string` | No | Facebook URL |
| `strGender` | `string` | No | Gender |
| `strGeniusID` | `string` | No | Genius ID |
| `strGenre` | `string` | No | Musical genre |
| `strISNIcode` | `string` | No | ISNI code |
| `strItunesID` | `string` | No | iTunes ID |
| `strLabel` | `string` | No | Record label |
| `strLastFMChart` | `string` | No | Last.fm chart URL |
| `strLocation` | `string` | No | Recording location |
| `strLocked` | `string` | No | Lock status |
| `strLyricWikiID` | `string` | No | LyricWiki ID |
| `strMood` | `string` | No | Album mood |
| `strMusicBrainzAlbumID` | `string` | No | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | No | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | No | MusicBrainz Release Group ID |
| `strMusicMozID` | `string` | No | MusicMoz ID |
| `strMusicVid` | `string` | No | Music video URL |
| `strMusicVidCompany` | `string` | No | Music video production company |
| `strMusicVidDirector` | `string` | No | Music video director |
| `strMusicVidScreen1` | `string` | No | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | No | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | No | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | No | Rate Your Music ID |
| `strReleaseFormat` | `string` | No | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | No | Album review |
| `strSpeed` | `string` | No | Album speed/tempo |
| `strStyle` | `string` | No | Musical style |
| `strTheme` | `string` | No | Album theme |
| `strTrack` | `string` | No | Track name |
| `strTrack3x3` | `string` | No | 3x3 track image URL |
| `strTrackLyrics` | `string` | No | Track lyrics |
| `strTrackThumb` | `string` | No | Track thumbnail URL |
| `strTwitter` | `string` | No | Twitter handle |
| `strWebsite` | `string` | No | Official website URL |
| `strWikidataID` | `string` | No | Wikidata ID |
| `strWikipediaID` | `string` | No | Wikipedia ID |

### Operations

#### `List(reqmatch, ctrl map[string]any) (any, error)`

List entities matching the given criteria. Returns an array.

```go
results, err := client.V1Search(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(results)
```

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V1Search(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V1SearchEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## V2ListEntity

```go
v2List := client.V2List(nil)
fmt.Println(v2List.GetName()) // "v2_list"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `[]any` | No |  |

### Operations

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V2List(nil).Load(map[string]any{"id_artist": 1}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V2ListEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## V2LookupEntity

```go
v2Lookup := client.V2Lookup(nil)
fmt.Println(v2Lookup.GetName()) // "v2_lookup"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `[]any` | No |  |
| `artists` | `[]any` | No |  |
| `track` | `[]any` | No |  |

### Operations

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V2Lookup(nil).Load(map[string]any{"id_album": 1}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V2LookupEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## V2SearchEntity

```go
v2Search := client.V2Search(nil)
fmt.Println(v2Search.GetName()) // "v2_search"
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `[]any` | No |  |
| `artists` | `[]any` | No |  |
| `track` | `[]any` | No |  |

### Operations

#### `Load(reqmatch, ctrl map[string]any) (any, error)`

Load a single entity matching the given criteria.

```go
result, err := client.V2Search(nil).Load(map[string]any{"album_name": "album_name"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(result)
```

### Common Methods

#### `Data(args ...any) any`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `Match(args ...any) any`

Get or set the entity match criteria. Works the same as `Data()`.

#### `Make() Entity`

Create a new `V2SearchEntity` instance with the same client and
options.

#### `GetName() string`

Return the entity name.


---

## Features

| Feature | Version | Description |
| --- | --- | --- |
| `test` | 0.0.1 | In-memory mock transport for testing without a live server |


Features are activated via the `feature` option:

```go
client := sdk.NewFreeMusicSDK(map[string]any{
    "feature": map[string]any{
        "test": map[string]any{"active": true},
    },
})
```

