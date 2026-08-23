# FreeMusic TypeScript SDK Reference

Complete API reference for the FreeMusic TypeScript SDK.


## FreeMusicSDK

### Constructor

```ts
new FreeMusicSDK(options?: object)
```

Create a new SDK client instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `options` | `object` | SDK configuration options. |
| `options.apikey` | `string` | API key for authentication. |
| `options.base` | `string` | Base URL for API requests. |
| `options.prefix` | `string` | URL prefix appended after base. |
| `options.suffix` | `string` | URL suffix appended after path. |
| `options.headers` | `object` | Custom headers for all requests. |
| `options.feature` | `object` | Feature configuration. |
| `options.system` | `object` | System overrides (e.g. custom fetch). |


### Static Methods

#### `FreeMusicSDK.test(testopts?, sdkopts?)`

Create a test client with mock features active.

```ts
const client = FreeMusicSDK.test()
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `testopts` | `object` | Test feature options. |
| `sdkopts` | `object` | Additional SDK options merged with test defaults. |

**Returns:** `FreeMusicSDK` instance in test mode.


### Instance Methods

#### `V1List(data?: object)`

Create a new `V1List` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V1ListEntity` instance.

#### `V1Lookup(data?: object)`

Create a new `V1Lookup` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V1LookupEntity` instance.

#### `V1Search(data?: object)`

Create a new `V1Search` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V1SearchEntity` instance.

#### `V2List(data?: object)`

Create a new `V2List` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V2ListEntity` instance.

#### `V2Lookup(data?: object)`

Create a new `V2Lookup` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V2LookupEntity` instance.

#### `V2Search(data?: object)`

Create a new `V2Search` entity instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `object` | Initial entity data. |

**Returns:** `V2SearchEntity` instance.

#### `options()`

Return a deep copy of the current SDK options.

**Returns:** `object`

#### `utility()`

Return a copy of the SDK utility object.

**Returns:** `object`

#### `direct(fetchargs?: object)`

Make a direct HTTP request to any API endpoint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `fetchargs.path` | `string` | URL path with optional `{param}` placeholders. |
| `fetchargs.method` | `string` | HTTP method (default: `GET`). |
| `fetchargs.params` | `object` | Path parameter values for `{param}` substitution. |
| `fetchargs.query` | `object` | Query string parameters. |
| `fetchargs.headers` | `object` | Request headers (merged with defaults). |
| `fetchargs.body` | `any` | Request body (objects are JSON-serialized). |
| `fetchargs.ctrl` | `object` | Control options (e.g. `{ explain: true }`). |

**Returns:** `Promise<{ ok, status, headers, data } | Error>`

#### `prepare(fetchargs?: object)`

Prepare a fetch definition without sending the request. Accepts the
same parameters as `direct()`.

**Returns:** `Promise<{ url, method, headers, body } | Error>`

#### `tester(testopts?, sdkopts?)`

Alias for `FreeMusicSDK.test()`.

**Returns:** `FreeMusicSDK` instance in test mode.


---

## V1ListEntity

```ts
const v1_list = client.V1List()
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
| `trending` | `any[]` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1List().list({ api_key: "example" })
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1List().load({ api_key: 'api_key' })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V1ListEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## V1LookupEntity

```ts
const v1_lookup = client.V1Lookup()
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

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1Lookup().list({ api_key: "example" })
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1Lookup().load({ api_key: 'api_key' })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V1LookupEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## V1SearchEntity

```ts
const v1_search = client.V1Search()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `any[]` | No |  |
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

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1Search().list({ api_key: "example" })
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1Search().load({ api_key: 'api_key' })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V1SearchEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## V2ListEntity

```ts
const v2_list = client.V2List()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `any[]` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V2List().load({ id_artist: 1 })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V2ListEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## V2LookupEntity

```ts
const v2_lookup = client.V2Lookup()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `any[]` | No |  |
| `artists` | `any[]` | No |  |
| `track` | `any[]` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V2Lookup().load({ id_album: 1 })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V2LookupEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## V2SearchEntity

```ts
const v2_search = client.V2Search()
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `any[]` | No |  |
| `artists` | `any[]` | No |  |
| `track` | `any[]` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V2Search().load({ album_name: 'album_name' })
```

### Common Methods

#### `data(data?: object)`

Get or set the entity data. When called with data, sets the entity's
internal data and returns the current data. When called without
arguments, returns a copy of the current data.

#### `match(match?: object)`

Get or set the entity match criteria. Works the same as `data()`.

#### `make()`

Create a new `V2SearchEntity` instance with the same client and
options.

#### `client()`

Return the parent `FreeMusicSDK` instance.

#### `entopts()`

Return a copy of the entity options.


---

## Features

| Feature | Version | Description |
| --- | --- | --- |
| `test` | 0.0.1 | In-memory mock transport for testing without a live server |


Features are activated via the `feature` option:

```ts
const client = new FreeMusicSDK({
  feature: {
    test: { active: true },
  }
})
```

