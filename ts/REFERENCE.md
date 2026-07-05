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
| `id_album` | `string` | No |  |
| `id_artist` | `string` | No |  |
| `id_imvdb` | `string` | No |  |
| `id_lyric` | `string` | No |  |
| `id_track` | `string` | No |  |
| `int_cd` | `string` | No |  |
| `int_duration` | `string` | No |  |
| `int_loved` | `string` | No |  |
| `int_music_vid_comment` | `string` | No |  |
| `int_music_vid_dislike` | `string` | No |  |
| `int_music_vid_favorite` | `string` | No |  |
| `int_music_vid_like` | `string` | No |  |
| `int_music_vid_view` | `string` | No |  |
| `int_score` | `string` | No |  |
| `int_score_vote` | `string` | No |  |
| `int_total_listener` | `string` | No |  |
| `int_total_play` | `string` | No |  |
| `int_track_number` | `string` | No |  |
| `str_album` | `string` | No |  |
| `str_artist` | `string` | No |  |
| `str_artist_alternate` | `string` | No |  |
| `str_description_en` | `string` | No |  |
| `str_genre` | `string` | No |  |
| `str_locked` | `string` | No |  |
| `str_mood` | `string` | No |  |
| `str_music_brainz_album_id` | `string` | No |  |
| `str_music_brainz_artist_id` | `string` | No |  |
| `str_music_brainz_id` | `string` | No |  |
| `str_music_vid` | `string` | No |  |
| `str_music_vid_company` | `string` | No |  |
| `str_music_vid_director` | `string` | No |  |
| `str_music_vid_screen1` | `string` | No |  |
| `str_music_vid_screen2` | `string` | No |  |
| `str_music_vid_screen3` | `string` | No |  |
| `str_style` | `string` | No |  |
| `str_theme` | `string` | No |  |
| `str_track` | `string` | No |  |
| `str_track3x3` | `string` | No |  |
| `str_track_lyric` | `string` | No |  |
| `str_track_thumb` | `string` | No |  |
| `trending` | `any[]` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1List().list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1List().load()
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
| `id_album` | `string` | No |  |
| `id_artist` | `string` | No |  |
| `id_imvdb` | `string` | No |  |
| `id_label` | `string` | No |  |
| `id_lyric` | `string` | No |  |
| `id_track` | `string` | No |  |
| `int_born_year` | `string` | No |  |
| `int_cd` | `string` | No |  |
| `int_charted` | `string` | No |  |
| `int_died_year` | `string` | No |  |
| `int_duration` | `string` | No |  |
| `int_formed_year` | `string` | No |  |
| `int_loved` | `string` | No |  |
| `int_member` | `string` | No |  |
| `int_music_vid_comment` | `string` | No |  |
| `int_music_vid_dislike` | `string` | No |  |
| `int_music_vid_favorite` | `string` | No |  |
| `int_music_vid_like` | `string` | No |  |
| `int_music_vid_view` | `string` | No |  |
| `int_sale` | `string` | No |  |
| `int_score` | `string` | No |  |
| `int_score_vote` | `string` | No |  |
| `int_total_listener` | `string` | No |  |
| `int_total_play` | `string` | No |  |
| `int_track_number` | `string` | No |  |
| `int_year_released` | `string` | No |  |
| `str_album` | `string` | No |  |
| `str_album3_d_case` | `string` | No |  |
| `str_album3_d_face` | `string` | No |  |
| `str_album3_d_flat` | `string` | No |  |
| `str_album3_d_thumb` | `string` | No |  |
| `str_album_c_dart` | `string` | No |  |
| `str_album_spine` | `string` | No |  |
| `str_album_stripped` | `string` | No |  |
| `str_album_thumb` | `string` | No |  |
| `str_album_thumb_back` | `string` | No |  |
| `str_album_thumb_hq` | `string` | No |  |
| `str_all_music_id` | `string` | No |  |
| `str_amazon_id` | `string` | No |  |
| `str_artist` | `string` | No |  |
| `str_artist_alternate` | `string` | No |  |
| `str_artist_banner` | `string` | No |  |
| `str_artist_clearart` | `string` | No |  |
| `str_artist_cutout` | `string` | No |  |
| `str_artist_fanart` | `string` | No |  |
| `str_artist_fanart2` | `string` | No |  |
| `str_artist_fanart3` | `string` | No |  |
| `str_artist_fanart4` | `string` | No |  |
| `str_artist_logo` | `string` | No |  |
| `str_artist_stripped` | `string` | No |  |
| `str_artist_thumb` | `string` | No |  |
| `str_artist_wide_thumb` | `string` | No |  |
| `str_bbc_review_id` | `string` | No |  |
| `str_biography_en` | `string` | No |  |
| `str_country` | `string` | No |  |
| `str_country_code` | `string` | No |  |
| `str_description_en` | `string` | No |  |
| `str_disbanded` | `string` | No |  |
| `str_discogs_id` | `string` | No |  |
| `str_facebook` | `string` | No |  |
| `str_gender` | `string` | No |  |
| `str_genius_id` | `string` | No |  |
| `str_genre` | `string` | No |  |
| `str_isn_icode` | `string` | No |  |
| `str_itunes_id` | `string` | No |  |
| `str_label` | `string` | No |  |
| `str_last_fm_chart` | `string` | No |  |
| `str_location` | `string` | No |  |
| `str_locked` | `string` | No |  |
| `str_lyric_wiki_id` | `string` | No |  |
| `str_mood` | `string` | No |  |
| `str_music_brainz_album_id` | `string` | No |  |
| `str_music_brainz_artist_id` | `string` | No |  |
| `str_music_brainz_id` | `string` | No |  |
| `str_music_moz_id` | `string` | No |  |
| `str_music_vid` | `string` | No |  |
| `str_music_vid_company` | `string` | No |  |
| `str_music_vid_director` | `string` | No |  |
| `str_music_vid_screen1` | `string` | No |  |
| `str_music_vid_screen2` | `string` | No |  |
| `str_music_vid_screen3` | `string` | No |  |
| `str_rate_your_music_id` | `string` | No |  |
| `str_release_format` | `string` | No |  |
| `str_review` | `string` | No |  |
| `str_speed` | `string` | No |  |
| `str_style` | `string` | No |  |
| `str_theme` | `string` | No |  |
| `str_track` | `string` | No |  |
| `str_track3x3` | `string` | No |  |
| `str_track_lyric` | `string` | No |  |
| `str_track_thumb` | `string` | No |  |
| `str_twitter` | `string` | No |  |
| `str_website` | `string` | No |  |
| `str_wikidata_id` | `string` | No |  |
| `str_wikipedia_id` | `string` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1Lookup().list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1Lookup().load()
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
| `id_album` | `string` | No |  |
| `id_artist` | `string` | No |  |
| `id_imvdb` | `string` | No |  |
| `id_label` | `string` | No |  |
| `id_lyric` | `string` | No |  |
| `id_track` | `string` | No |  |
| `int_born_year` | `string` | No |  |
| `int_cd` | `string` | No |  |
| `int_charted` | `string` | No |  |
| `int_died_year` | `string` | No |  |
| `int_duration` | `string` | No |  |
| `int_formed_year` | `string` | No |  |
| `int_loved` | `string` | No |  |
| `int_member` | `string` | No |  |
| `int_music_vid_comment` | `string` | No |  |
| `int_music_vid_dislike` | `string` | No |  |
| `int_music_vid_favorite` | `string` | No |  |
| `int_music_vid_like` | `string` | No |  |
| `int_music_vid_view` | `string` | No |  |
| `int_sale` | `string` | No |  |
| `int_score` | `string` | No |  |
| `int_score_vote` | `string` | No |  |
| `int_total_listener` | `string` | No |  |
| `int_total_play` | `string` | No |  |
| `int_track_number` | `string` | No |  |
| `int_year_released` | `string` | No |  |
| `str_album` | `string` | No |  |
| `str_album3_d_case` | `string` | No |  |
| `str_album3_d_face` | `string` | No |  |
| `str_album3_d_flat` | `string` | No |  |
| `str_album3_d_thumb` | `string` | No |  |
| `str_album_c_dart` | `string` | No |  |
| `str_album_spine` | `string` | No |  |
| `str_album_stripped` | `string` | No |  |
| `str_album_thumb` | `string` | No |  |
| `str_album_thumb_back` | `string` | No |  |
| `str_album_thumb_hq` | `string` | No |  |
| `str_all_music_id` | `string` | No |  |
| `str_amazon_id` | `string` | No |  |
| `str_artist` | `string` | No |  |
| `str_artist_alternate` | `string` | No |  |
| `str_artist_banner` | `string` | No |  |
| `str_artist_clearart` | `string` | No |  |
| `str_artist_cutout` | `string` | No |  |
| `str_artist_fanart` | `string` | No |  |
| `str_artist_fanart2` | `string` | No |  |
| `str_artist_fanart3` | `string` | No |  |
| `str_artist_fanart4` | `string` | No |  |
| `str_artist_logo` | `string` | No |  |
| `str_artist_stripped` | `string` | No |  |
| `str_artist_thumb` | `string` | No |  |
| `str_artist_wide_thumb` | `string` | No |  |
| `str_bbc_review_id` | `string` | No |  |
| `str_biography_en` | `string` | No |  |
| `str_country` | `string` | No |  |
| `str_country_code` | `string` | No |  |
| `str_description_en` | `string` | No |  |
| `str_disbanded` | `string` | No |  |
| `str_discogs_id` | `string` | No |  |
| `str_facebook` | `string` | No |  |
| `str_gender` | `string` | No |  |
| `str_genius_id` | `string` | No |  |
| `str_genre` | `string` | No |  |
| `str_isn_icode` | `string` | No |  |
| `str_itunes_id` | `string` | No |  |
| `str_label` | `string` | No |  |
| `str_last_fm_chart` | `string` | No |  |
| `str_location` | `string` | No |  |
| `str_locked` | `string` | No |  |
| `str_lyric_wiki_id` | `string` | No |  |
| `str_mood` | `string` | No |  |
| `str_music_brainz_album_id` | `string` | No |  |
| `str_music_brainz_artist_id` | `string` | No |  |
| `str_music_brainz_id` | `string` | No |  |
| `str_music_moz_id` | `string` | No |  |
| `str_music_vid` | `string` | No |  |
| `str_music_vid_company` | `string` | No |  |
| `str_music_vid_director` | `string` | No |  |
| `str_music_vid_screen1` | `string` | No |  |
| `str_music_vid_screen2` | `string` | No |  |
| `str_music_vid_screen3` | `string` | No |  |
| `str_rate_your_music_id` | `string` | No |  |
| `str_release_format` | `string` | No |  |
| `str_review` | `string` | No |  |
| `str_speed` | `string` | No |  |
| `str_style` | `string` | No |  |
| `str_theme` | `string` | No |  |
| `str_track` | `string` | No |  |
| `str_track3x3` | `string` | No |  |
| `str_track_lyric` | `string` | No |  |
| `str_track_thumb` | `string` | No |  |
| `str_twitter` | `string` | No |  |
| `str_website` | `string` | No |  |
| `str_wikidata_id` | `string` | No |  |
| `str_wikipedia_id` | `string` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.V1Search().list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V1Search().load()
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
const result = await client.V2List().load()
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
| `artist` | `any[]` | No |  |
| `track` | `any[]` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V2Lookup().load()
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
| `artist` | `any[]` | No |  |
| `track` | `any[]` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.V2Search().load()
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

