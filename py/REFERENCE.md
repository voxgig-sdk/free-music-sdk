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
| `idAlbum` | `str` | No |  |
| `idArtist` | `str` | No |  |
| `idIMVDB` | `str` | No |  |
| `idLyric` | `str` | No |  |
| `idTrack` | `str` | No |  |
| `intCD` | `str` | No |  |
| `intDuration` | `str` | No |  |
| `intLoved` | `str` | No |  |
| `intMusicVidComments` | `str` | No |  |
| `intMusicVidDislikes` | `str` | No |  |
| `intMusicVidFavorites` | `str` | No |  |
| `intMusicVidLikes` | `str` | No |  |
| `intMusicVidViews` | `str` | No |  |
| `intScore` | `str` | No |  |
| `intScoreVotes` | `str` | No |  |
| `intTotalListeners` | `str` | No |  |
| `intTotalPlays` | `str` | No |  |
| `intTrackNumber` | `str` | No |  |
| `strAlbum` | `str` | No |  |
| `strArtist` | `str` | No |  |
| `strArtistAlternate` | `str` | No |  |
| `strDescriptionEN` | `str` | No |  |
| `strGenre` | `str` | No |  |
| `strLocked` | `str` | No |  |
| `strMood` | `str` | No |  |
| `strMusicBrainzAlbumID` | `str` | No |  |
| `strMusicBrainzArtistID` | `str` | No |  |
| `strMusicBrainzID` | `str` | No |  |
| `strMusicVid` | `str` | No |  |
| `strMusicVidCompany` | `str` | No |  |
| `strMusicVidDirector` | `str` | No |  |
| `strMusicVidScreen1` | `str` | No |  |
| `strMusicVidScreen2` | `str` | No |  |
| `strMusicVidScreen3` | `str` | No |  |
| `strStyle` | `str` | No |  |
| `strTheme` | `str` | No |  |
| `strTrack` | `str` | No |  |
| `strTrack3x3` | `str` | No |  |
| `strTrackLyrics` | `str` | No |  |
| `strTrackThumb` | `str` | No |  |
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
| `idAlbum` | `str` | No |  |
| `idArtist` | `str` | No |  |
| `idIMVDB` | `str` | No |  |
| `idLabel` | `str` | No |  |
| `idLyric` | `str` | No |  |
| `idTrack` | `str` | No |  |
| `intBornYear` | `str` | No |  |
| `intCD` | `str` | No |  |
| `intCharted` | `str` | No |  |
| `intDiedYear` | `str` | No |  |
| `intDuration` | `str` | No |  |
| `intFormedYear` | `str` | No |  |
| `intLoved` | `str` | No |  |
| `intMembers` | `str` | No |  |
| `intMusicVidComments` | `str` | No |  |
| `intMusicVidDislikes` | `str` | No |  |
| `intMusicVidFavorites` | `str` | No |  |
| `intMusicVidLikes` | `str` | No |  |
| `intMusicVidViews` | `str` | No |  |
| `intSales` | `str` | No |  |
| `intScore` | `str` | No |  |
| `intScoreVotes` | `str` | No |  |
| `intTotalListeners` | `str` | No |  |
| `intTotalPlays` | `str` | No |  |
| `intTrackNumber` | `str` | No |  |
| `intYearReleased` | `str` | No |  |
| `strAlbum` | `str` | No |  |
| `strAlbum3DCase` | `str` | No |  |
| `strAlbum3DFace` | `str` | No |  |
| `strAlbum3DFlat` | `str` | No |  |
| `strAlbum3DThumb` | `str` | No |  |
| `strAlbumCDart` | `str` | No |  |
| `strAlbumSpine` | `str` | No |  |
| `strAlbumStripped` | `str` | No |  |
| `strAlbumThumb` | `str` | No |  |
| `strAlbumThumbBack` | `str` | No |  |
| `strAlbumThumbHQ` | `str` | No |  |
| `strAllMusicID` | `str` | No |  |
| `strAmazonID` | `str` | No |  |
| `strArtist` | `str` | No |  |
| `strArtistAlternate` | `str` | No |  |
| `strArtistBanner` | `str` | No |  |
| `strArtistClearart` | `str` | No |  |
| `strArtistCutout` | `str` | No |  |
| `strArtistFanart` | `str` | No |  |
| `strArtistFanart2` | `str` | No |  |
| `strArtistFanart3` | `str` | No |  |
| `strArtistFanart4` | `str` | No |  |
| `strArtistLogo` | `str` | No |  |
| `strArtistStripped` | `str` | No |  |
| `strArtistThumb` | `str` | No |  |
| `strArtistWideThumb` | `str` | No |  |
| `strBBCReviewID` | `str` | No |  |
| `strBiographyEN` | `str` | No |  |
| `strCountry` | `str` | No |  |
| `strCountryCode` | `str` | No |  |
| `strDescriptionEN` | `str` | No |  |
| `strDisbanded` | `str` | No |  |
| `strDiscogsID` | `str` | No |  |
| `strFacebook` | `str` | No |  |
| `strGender` | `str` | No |  |
| `strGeniusID` | `str` | No |  |
| `strGenre` | `str` | No |  |
| `strISNIcode` | `str` | No |  |
| `strItunesID` | `str` | No |  |
| `strLabel` | `str` | No |  |
| `strLastFMChart` | `str` | No |  |
| `strLocation` | `str` | No |  |
| `strLocked` | `str` | No |  |
| `strLyricWikiID` | `str` | No |  |
| `strMood` | `str` | No |  |
| `strMusicBrainzAlbumID` | `str` | No |  |
| `strMusicBrainzArtistID` | `str` | No |  |
| `strMusicBrainzID` | `str` | No |  |
| `strMusicMozID` | `str` | No |  |
| `strMusicVid` | `str` | No |  |
| `strMusicVidCompany` | `str` | No |  |
| `strMusicVidDirector` | `str` | No |  |
| `strMusicVidScreen1` | `str` | No |  |
| `strMusicVidScreen2` | `str` | No |  |
| `strMusicVidScreen3` | `str` | No |  |
| `strRateYourMusicID` | `str` | No |  |
| `strReleaseFormat` | `str` | No |  |
| `strReview` | `str` | No |  |
| `strSpeed` | `str` | No |  |
| `strStyle` | `str` | No |  |
| `strTheme` | `str` | No |  |
| `strTrack` | `str` | No |  |
| `strTrack3x3` | `str` | No |  |
| `strTrackLyrics` | `str` | No |  |
| `strTrackThumb` | `str` | No |  |
| `strTwitter` | `str` | No |  |
| `strWebsite` | `str` | No |  |
| `strWikidataID` | `str` | No |  |
| `strWikipediaID` | `str` | No |  |

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
| `idAlbum` | `str` | No |  |
| `idArtist` | `str` | No |  |
| `idIMVDB` | `str` | No |  |
| `idLabel` | `str` | No |  |
| `idLyric` | `str` | No |  |
| `idTrack` | `str` | No |  |
| `intBornYear` | `str` | No |  |
| `intCD` | `str` | No |  |
| `intCharted` | `str` | No |  |
| `intDiedYear` | `str` | No |  |
| `intDuration` | `str` | No |  |
| `intFormedYear` | `str` | No |  |
| `intLoved` | `str` | No |  |
| `intMembers` | `str` | No |  |
| `intMusicVidComments` | `str` | No |  |
| `intMusicVidDislikes` | `str` | No |  |
| `intMusicVidFavorites` | `str` | No |  |
| `intMusicVidLikes` | `str` | No |  |
| `intMusicVidViews` | `str` | No |  |
| `intSales` | `str` | No |  |
| `intScore` | `str` | No |  |
| `intScoreVotes` | `str` | No |  |
| `intTotalListeners` | `str` | No |  |
| `intTotalPlays` | `str` | No |  |
| `intTrackNumber` | `str` | No |  |
| `intYearReleased` | `str` | No |  |
| `strAlbum` | `str` | No |  |
| `strAlbum3DCase` | `str` | No |  |
| `strAlbum3DFace` | `str` | No |  |
| `strAlbum3DFlat` | `str` | No |  |
| `strAlbum3DThumb` | `str` | No |  |
| `strAlbumCDart` | `str` | No |  |
| `strAlbumSpine` | `str` | No |  |
| `strAlbumStripped` | `str` | No |  |
| `strAlbumThumb` | `str` | No |  |
| `strAlbumThumbBack` | `str` | No |  |
| `strAlbumThumbHQ` | `str` | No |  |
| `strAllMusicID` | `str` | No |  |
| `strAmazonID` | `str` | No |  |
| `strArtist` | `str` | No |  |
| `strArtistAlternate` | `str` | No |  |
| `strArtistBanner` | `str` | No |  |
| `strArtistClearart` | `str` | No |  |
| `strArtistCutout` | `str` | No |  |
| `strArtistFanart` | `str` | No |  |
| `strArtistFanart2` | `str` | No |  |
| `strArtistFanart3` | `str` | No |  |
| `strArtistFanart4` | `str` | No |  |
| `strArtistLogo` | `str` | No |  |
| `strArtistStripped` | `str` | No |  |
| `strArtistThumb` | `str` | No |  |
| `strArtistWideThumb` | `str` | No |  |
| `strBBCReviewID` | `str` | No |  |
| `strBiographyEN` | `str` | No |  |
| `strCountry` | `str` | No |  |
| `strCountryCode` | `str` | No |  |
| `strDescriptionEN` | `str` | No |  |
| `strDisbanded` | `str` | No |  |
| `strDiscogsID` | `str` | No |  |
| `strFacebook` | `str` | No |  |
| `strGender` | `str` | No |  |
| `strGeniusID` | `str` | No |  |
| `strGenre` | `str` | No |  |
| `strISNIcode` | `str` | No |  |
| `strItunesID` | `str` | No |  |
| `strLabel` | `str` | No |  |
| `strLastFMChart` | `str` | No |  |
| `strLocation` | `str` | No |  |
| `strLocked` | `str` | No |  |
| `strLyricWikiID` | `str` | No |  |
| `strMood` | `str` | No |  |
| `strMusicBrainzAlbumID` | `str` | No |  |
| `strMusicBrainzArtistID` | `str` | No |  |
| `strMusicBrainzID` | `str` | No |  |
| `strMusicMozID` | `str` | No |  |
| `strMusicVid` | `str` | No |  |
| `strMusicVidCompany` | `str` | No |  |
| `strMusicVidDirector` | `str` | No |  |
| `strMusicVidScreen1` | `str` | No |  |
| `strMusicVidScreen2` | `str` | No |  |
| `strMusicVidScreen3` | `str` | No |  |
| `strRateYourMusicID` | `str` | No |  |
| `strReleaseFormat` | `str` | No |  |
| `strReview` | `str` | No |  |
| `strSpeed` | `str` | No |  |
| `strStyle` | `str` | No |  |
| `strTheme` | `str` | No |  |
| `strTrack` | `str` | No |  |
| `strTrack3x3` | `str` | No |  |
| `strTrackLyrics` | `str` | No |  |
| `strTrackThumb` | `str` | No |  |
| `strTwitter` | `str` | No |  |
| `strWebsite` | `str` | No |  |
| `strWikidataID` | `str` | No |  |
| `strWikipediaID` | `str` | No |  |

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

