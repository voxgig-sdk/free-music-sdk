# FreeMusic PHP SDK Reference

Complete API reference for the FreeMusic PHP SDK.


## FreeMusicSDK

### Constructor

```php
require_once __DIR__ . '/freemusic_sdk.php';

$client = new FreeMusicSDK($options);
```

Create a new SDK client instance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `$options` | `array` | SDK configuration options. |
| `$options["apikey"]` | `string` | API key for authentication. |
| `$options["base"]` | `string` | Base URL for API requests. |
| `$options["prefix"]` | `string` | URL prefix appended after base. |
| `$options["suffix"]` | `string` | URL suffix appended after path. |
| `$options["headers"]` | `array` | Custom headers for all requests. |
| `$options["feature"]` | `array` | Feature configuration. |
| `$options["system"]` | `array` | System overrides (e.g. custom fetch). |


### Static Methods

#### `FreeMusicSDK::test($testopts = null, $sdkopts = null)`

Create a test client with mock features active. Both arguments may be `null`.

```php
$client = FreeMusicSDK::test();
```


### Instance Methods

#### `V1List($data = null)`

Create a new `V1ListEntity` instance. Pass `null` for no initial data.

#### `V1Lookup($data = null)`

Create a new `V1LookupEntity` instance. Pass `null` for no initial data.

#### `V1Search($data = null)`

Create a new `V1SearchEntity` instance. Pass `null` for no initial data.

#### `V2List($data = null)`

Create a new `V2ListEntity` instance. Pass `null` for no initial data.

#### `V2Lookup($data = null)`

Create a new `V2LookupEntity` instance. Pass `null` for no initial data.

#### `V2Search($data = null)`

Create a new `V2SearchEntity` instance. Pass `null` for no initial data.

#### `options_map(): array`

Return a deep copy of the current SDK options.

#### `get_utility(): FreeMusicUtility`

Return a copy of the SDK utility object.

#### `direct(array $fetchargs = []): array`

Make a direct HTTP request to any API endpoint. This is the raw-HTTP escape
hatch: it does **not** throw. It returns a result array
`["ok" => bool, "status" => int, "headers" => array, "data" => mixed]`, or
`["ok" => false, "err" => \Exception]` on failure. Branch on `$result["ok"]`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `$fetchargs["path"]` | `string` | URL path with optional `{param}` placeholders. |
| `$fetchargs["method"]` | `string` | HTTP method (default: `"GET"`). |
| `$fetchargs["params"]` | `array` | Path parameter values for `{param}` substitution. |
| `$fetchargs["query"]` | `array` | Query string parameters. |
| `$fetchargs["headers"]` | `array` | Request headers (merged with defaults). |
| `$fetchargs["body"]` | `mixed` | Request body (arrays are JSON-serialized). |
| `$fetchargs["ctrl"]` | `array` | Control options. |

**Returns:** `array` — the result dict (see above); never throws.

#### `prepare(array $fetchargs = []): mixed`

Prepare a fetch definition without sending the request. Returns the
`$fetchdef` array. Throws on error.


---

## V1ListEntity

```php
$v1_list = $client->V1List();
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
| `trending` | `array` | No |  |

### Operations

#### `list(?array $reqmatch = null, ?array $ctrl = null): mixed`

List entities matching the given criteria (call with no argument to list all). Returns an array. Throws on error.

```php
$results = $client->V1List()->list();
```

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V1List()->load(["api_key" => "api_key"]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V1ListEntity`

Create a new `V1ListEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## V1LookupEntity

```php
$v1_lookup = $client->V1Lookup();
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

#### `list(?array $reqmatch = null, ?array $ctrl = null): mixed`

List entities matching the given criteria (call with no argument to list all). Returns an array. Throws on error.

```php
$results = $client->V1Lookup()->list();
```

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V1Lookup()->load(["api_key" => "api_key"]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V1LookupEntity`

Create a new `V1LookupEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## V1SearchEntity

```php
$v1_search = $client->V1Search();
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `array` | No |  |
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

#### `list(?array $reqmatch = null, ?array $ctrl = null): mixed`

List entities matching the given criteria (call with no argument to list all). Returns an array. Throws on error.

```php
$results = $client->V1Search()->list();
```

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V1Search()->load(["api_key" => "api_key"]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V1SearchEntity`

Create a new `V1SearchEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## V2ListEntity

```php
$v2_list = $client->V2List();
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `array` | No |  |

### Operations

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V2List()->load(["id_artist" => 1]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V2ListEntity`

Create a new `V2ListEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## V2LookupEntity

```php
$v2_lookup = $client->V2Lookup();
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `array` | No |  |
| `artists` | `array` | No |  |
| `track` | `array` | No |  |

### Operations

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V2Lookup()->load(["id_album" => 1]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V2LookupEntity`

Create a new `V2LookupEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## V2SearchEntity

```php
$v2_search = $client->V2Search();
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | `array` | No |  |
| `artists` | `array` | No |  |
| `track` | `array` | No |  |

### Operations

#### `load(array $reqmatch, ?array $ctrl = null): mixed`

Load a single entity matching the given criteria. Throws on error.

```php
$result = $client->V2Search()->load(["album_name" => "album_name"]);
```

### Common Methods

#### `data_get(): array`

Get the entity data. Returns a copy of the current data.

#### `data_set($data): void`

Set the entity data.

#### `match_get(): array`

Get the entity match criteria.

#### `match_set($match): void`

Set the entity match criteria.

#### `make(): V2SearchEntity`

Create a new `V2SearchEntity` instance with the same client and
options.

#### `get_name(): string`

Return the entity name.


---

## Features

| Feature | Version | Description |
| --- | --- | --- |
| `test` | 0.0.1 | In-memory mock transport for testing without a live server |


Features are activated via the `feature` option:

```php
$client = new FreeMusicSDK([
  "feature" => [
    "test" => ["active" => true],
  ],
]);
```

