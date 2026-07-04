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
const v1_list = client.v1_list
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id_album` | ``$STRING`` | No |  |
| `id_artist` | ``$STRING`` | No |  |
| `id_imvdb` | ``$STRING`` | No |  |
| `id_lyric` | ``$STRING`` | No |  |
| `id_track` | ``$STRING`` | No |  |
| `int_cd` | ``$STRING`` | No |  |
| `int_duration` | ``$STRING`` | No |  |
| `int_loved` | ``$STRING`` | No |  |
| `int_music_vid_comment` | ``$STRING`` | No |  |
| `int_music_vid_dislike` | ``$STRING`` | No |  |
| `int_music_vid_favorite` | ``$STRING`` | No |  |
| `int_music_vid_like` | ``$STRING`` | No |  |
| `int_music_vid_view` | ``$STRING`` | No |  |
| `int_score` | ``$STRING`` | No |  |
| `int_score_vote` | ``$STRING`` | No |  |
| `int_total_listener` | ``$STRING`` | No |  |
| `int_total_play` | ``$STRING`` | No |  |
| `int_track_number` | ``$STRING`` | No |  |
| `str_album` | ``$STRING`` | No |  |
| `str_artist` | ``$STRING`` | No |  |
| `str_artist_alternate` | ``$STRING`` | No |  |
| `str_description_en` | ``$STRING`` | No |  |
| `str_genre` | ``$STRING`` | No |  |
| `str_locked` | ``$STRING`` | No |  |
| `str_mood` | ``$STRING`` | No |  |
| `str_music_brainz_album_id` | ``$STRING`` | No |  |
| `str_music_brainz_artist_id` | ``$STRING`` | No |  |
| `str_music_brainz_id` | ``$STRING`` | No |  |
| `str_music_vid` | ``$STRING`` | No |  |
| `str_music_vid_company` | ``$STRING`` | No |  |
| `str_music_vid_director` | ``$STRING`` | No |  |
| `str_music_vid_screen1` | ``$STRING`` | No |  |
| `str_music_vid_screen2` | ``$STRING`` | No |  |
| `str_music_vid_screen3` | ``$STRING`` | No |  |
| `str_style` | ``$STRING`` | No |  |
| `str_theme` | ``$STRING`` | No |  |
| `str_track` | ``$STRING`` | No |  |
| `str_track3x3` | ``$STRING`` | No |  |
| `str_track_lyric` | ``$STRING`` | No |  |
| `str_track_thumb` | ``$STRING`` | No |  |
| `trending` | ``$ARRAY`` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.v1_list.list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v1_list.load({ id: 'v1_list_id' })
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
const v1_lookup = client.v1_lookup
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id_album` | ``$STRING`` | No |  |
| `id_artist` | ``$STRING`` | No |  |
| `id_imvdb` | ``$STRING`` | No |  |
| `id_label` | ``$STRING`` | No |  |
| `id_lyric` | ``$STRING`` | No |  |
| `id_track` | ``$STRING`` | No |  |
| `int_born_year` | ``$STRING`` | No |  |
| `int_cd` | ``$STRING`` | No |  |
| `int_charted` | ``$STRING`` | No |  |
| `int_died_year` | ``$STRING`` | No |  |
| `int_duration` | ``$STRING`` | No |  |
| `int_formed_year` | ``$STRING`` | No |  |
| `int_loved` | ``$STRING`` | No |  |
| `int_member` | ``$STRING`` | No |  |
| `int_music_vid_comment` | ``$STRING`` | No |  |
| `int_music_vid_dislike` | ``$STRING`` | No |  |
| `int_music_vid_favorite` | ``$STRING`` | No |  |
| `int_music_vid_like` | ``$STRING`` | No |  |
| `int_music_vid_view` | ``$STRING`` | No |  |
| `int_sale` | ``$STRING`` | No |  |
| `int_score` | ``$STRING`` | No |  |
| `int_score_vote` | ``$STRING`` | No |  |
| `int_total_listener` | ``$STRING`` | No |  |
| `int_total_play` | ``$STRING`` | No |  |
| `int_track_number` | ``$STRING`` | No |  |
| `int_year_released` | ``$STRING`` | No |  |
| `str_album` | ``$STRING`` | No |  |
| `str_album3_d_case` | ``$STRING`` | No |  |
| `str_album3_d_face` | ``$STRING`` | No |  |
| `str_album3_d_flat` | ``$STRING`` | No |  |
| `str_album3_d_thumb` | ``$STRING`` | No |  |
| `str_album_c_dart` | ``$STRING`` | No |  |
| `str_album_spine` | ``$STRING`` | No |  |
| `str_album_stripped` | ``$STRING`` | No |  |
| `str_album_thumb` | ``$STRING`` | No |  |
| `str_album_thumb_back` | ``$STRING`` | No |  |
| `str_album_thumb_hq` | ``$STRING`` | No |  |
| `str_all_music_id` | ``$STRING`` | No |  |
| `str_amazon_id` | ``$STRING`` | No |  |
| `str_artist` | ``$STRING`` | No |  |
| `str_artist_alternate` | ``$STRING`` | No |  |
| `str_artist_banner` | ``$STRING`` | No |  |
| `str_artist_clearart` | ``$STRING`` | No |  |
| `str_artist_cutout` | ``$STRING`` | No |  |
| `str_artist_fanart` | ``$STRING`` | No |  |
| `str_artist_fanart2` | ``$STRING`` | No |  |
| `str_artist_fanart3` | ``$STRING`` | No |  |
| `str_artist_fanart4` | ``$STRING`` | No |  |
| `str_artist_logo` | ``$STRING`` | No |  |
| `str_artist_stripped` | ``$STRING`` | No |  |
| `str_artist_thumb` | ``$STRING`` | No |  |
| `str_artist_wide_thumb` | ``$STRING`` | No |  |
| `str_bbc_review_id` | ``$STRING`` | No |  |
| `str_biography_en` | ``$STRING`` | No |  |
| `str_country` | ``$STRING`` | No |  |
| `str_country_code` | ``$STRING`` | No |  |
| `str_description_en` | ``$STRING`` | No |  |
| `str_disbanded` | ``$STRING`` | No |  |
| `str_discogs_id` | ``$STRING`` | No |  |
| `str_facebook` | ``$STRING`` | No |  |
| `str_gender` | ``$STRING`` | No |  |
| `str_genius_id` | ``$STRING`` | No |  |
| `str_genre` | ``$STRING`` | No |  |
| `str_isn_icode` | ``$STRING`` | No |  |
| `str_itunes_id` | ``$STRING`` | No |  |
| `str_label` | ``$STRING`` | No |  |
| `str_last_fm_chart` | ``$STRING`` | No |  |
| `str_location` | ``$STRING`` | No |  |
| `str_locked` | ``$STRING`` | No |  |
| `str_lyric_wiki_id` | ``$STRING`` | No |  |
| `str_mood` | ``$STRING`` | No |  |
| `str_music_brainz_album_id` | ``$STRING`` | No |  |
| `str_music_brainz_artist_id` | ``$STRING`` | No |  |
| `str_music_brainz_id` | ``$STRING`` | No |  |
| `str_music_moz_id` | ``$STRING`` | No |  |
| `str_music_vid` | ``$STRING`` | No |  |
| `str_music_vid_company` | ``$STRING`` | No |  |
| `str_music_vid_director` | ``$STRING`` | No |  |
| `str_music_vid_screen1` | ``$STRING`` | No |  |
| `str_music_vid_screen2` | ``$STRING`` | No |  |
| `str_music_vid_screen3` | ``$STRING`` | No |  |
| `str_rate_your_music_id` | ``$STRING`` | No |  |
| `str_release_format` | ``$STRING`` | No |  |
| `str_review` | ``$STRING`` | No |  |
| `str_speed` | ``$STRING`` | No |  |
| `str_style` | ``$STRING`` | No |  |
| `str_theme` | ``$STRING`` | No |  |
| `str_track` | ``$STRING`` | No |  |
| `str_track3x3` | ``$STRING`` | No |  |
| `str_track_lyric` | ``$STRING`` | No |  |
| `str_track_thumb` | ``$STRING`` | No |  |
| `str_twitter` | ``$STRING`` | No |  |
| `str_website` | ``$STRING`` | No |  |
| `str_wikidata_id` | ``$STRING`` | No |  |
| `str_wikipedia_id` | ``$STRING`` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.v1_lookup.list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v1_lookup.load({ id: 'v1_lookup_id' })
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
const v1_search = client.v1_search
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |
| `id_album` | ``$STRING`` | No |  |
| `id_artist` | ``$STRING`` | No |  |
| `id_imvdb` | ``$STRING`` | No |  |
| `id_label` | ``$STRING`` | No |  |
| `id_lyric` | ``$STRING`` | No |  |
| `id_track` | ``$STRING`` | No |  |
| `int_born_year` | ``$STRING`` | No |  |
| `int_cd` | ``$STRING`` | No |  |
| `int_charted` | ``$STRING`` | No |  |
| `int_died_year` | ``$STRING`` | No |  |
| `int_duration` | ``$STRING`` | No |  |
| `int_formed_year` | ``$STRING`` | No |  |
| `int_loved` | ``$STRING`` | No |  |
| `int_member` | ``$STRING`` | No |  |
| `int_music_vid_comment` | ``$STRING`` | No |  |
| `int_music_vid_dislike` | ``$STRING`` | No |  |
| `int_music_vid_favorite` | ``$STRING`` | No |  |
| `int_music_vid_like` | ``$STRING`` | No |  |
| `int_music_vid_view` | ``$STRING`` | No |  |
| `int_sale` | ``$STRING`` | No |  |
| `int_score` | ``$STRING`` | No |  |
| `int_score_vote` | ``$STRING`` | No |  |
| `int_total_listener` | ``$STRING`` | No |  |
| `int_total_play` | ``$STRING`` | No |  |
| `int_track_number` | ``$STRING`` | No |  |
| `int_year_released` | ``$STRING`` | No |  |
| `str_album` | ``$STRING`` | No |  |
| `str_album3_d_case` | ``$STRING`` | No |  |
| `str_album3_d_face` | ``$STRING`` | No |  |
| `str_album3_d_flat` | ``$STRING`` | No |  |
| `str_album3_d_thumb` | ``$STRING`` | No |  |
| `str_album_c_dart` | ``$STRING`` | No |  |
| `str_album_spine` | ``$STRING`` | No |  |
| `str_album_stripped` | ``$STRING`` | No |  |
| `str_album_thumb` | ``$STRING`` | No |  |
| `str_album_thumb_back` | ``$STRING`` | No |  |
| `str_album_thumb_hq` | ``$STRING`` | No |  |
| `str_all_music_id` | ``$STRING`` | No |  |
| `str_amazon_id` | ``$STRING`` | No |  |
| `str_artist` | ``$STRING`` | No |  |
| `str_artist_alternate` | ``$STRING`` | No |  |
| `str_artist_banner` | ``$STRING`` | No |  |
| `str_artist_clearart` | ``$STRING`` | No |  |
| `str_artist_cutout` | ``$STRING`` | No |  |
| `str_artist_fanart` | ``$STRING`` | No |  |
| `str_artist_fanart2` | ``$STRING`` | No |  |
| `str_artist_fanart3` | ``$STRING`` | No |  |
| `str_artist_fanart4` | ``$STRING`` | No |  |
| `str_artist_logo` | ``$STRING`` | No |  |
| `str_artist_stripped` | ``$STRING`` | No |  |
| `str_artist_thumb` | ``$STRING`` | No |  |
| `str_artist_wide_thumb` | ``$STRING`` | No |  |
| `str_bbc_review_id` | ``$STRING`` | No |  |
| `str_biography_en` | ``$STRING`` | No |  |
| `str_country` | ``$STRING`` | No |  |
| `str_country_code` | ``$STRING`` | No |  |
| `str_description_en` | ``$STRING`` | No |  |
| `str_disbanded` | ``$STRING`` | No |  |
| `str_discogs_id` | ``$STRING`` | No |  |
| `str_facebook` | ``$STRING`` | No |  |
| `str_gender` | ``$STRING`` | No |  |
| `str_genius_id` | ``$STRING`` | No |  |
| `str_genre` | ``$STRING`` | No |  |
| `str_isn_icode` | ``$STRING`` | No |  |
| `str_itunes_id` | ``$STRING`` | No |  |
| `str_label` | ``$STRING`` | No |  |
| `str_last_fm_chart` | ``$STRING`` | No |  |
| `str_location` | ``$STRING`` | No |  |
| `str_locked` | ``$STRING`` | No |  |
| `str_lyric_wiki_id` | ``$STRING`` | No |  |
| `str_mood` | ``$STRING`` | No |  |
| `str_music_brainz_album_id` | ``$STRING`` | No |  |
| `str_music_brainz_artist_id` | ``$STRING`` | No |  |
| `str_music_brainz_id` | ``$STRING`` | No |  |
| `str_music_moz_id` | ``$STRING`` | No |  |
| `str_music_vid` | ``$STRING`` | No |  |
| `str_music_vid_company` | ``$STRING`` | No |  |
| `str_music_vid_director` | ``$STRING`` | No |  |
| `str_music_vid_screen1` | ``$STRING`` | No |  |
| `str_music_vid_screen2` | ``$STRING`` | No |  |
| `str_music_vid_screen3` | ``$STRING`` | No |  |
| `str_rate_your_music_id` | ``$STRING`` | No |  |
| `str_release_format` | ``$STRING`` | No |  |
| `str_review` | ``$STRING`` | No |  |
| `str_speed` | ``$STRING`` | No |  |
| `str_style` | ``$STRING`` | No |  |
| `str_theme` | ``$STRING`` | No |  |
| `str_track` | ``$STRING`` | No |  |
| `str_track3x3` | ``$STRING`` | No |  |
| `str_track_lyric` | ``$STRING`` | No |  |
| `str_track_thumb` | ``$STRING`` | No |  |
| `str_twitter` | ``$STRING`` | No |  |
| `str_website` | ``$STRING`` | No |  |
| `str_wikidata_id` | ``$STRING`` | No |  |
| `str_wikipedia_id` | ``$STRING`` | No |  |

### Operations

#### `list(match: object, ctrl?: object)`

List entities matching the given criteria. Returns an array.

```ts
const results = await client.v1_search.list()
```

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v1_search.load({ id: 'v1_search_id' })
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
const v2_list = client.v2_list
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v2_list.load({ id: 'v2_list_id' })
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
const v2_lookup = client.v2_lookup
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |
| `artist` | ``$ARRAY`` | No |  |
| `track` | ``$ARRAY`` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v2_lookup.load({ id: 'v2_lookup_id' })
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
const v2_search = client.v2_search
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |
| `artist` | ``$ARRAY`` | No |  |
| `track` | ``$ARRAY`` | No |  |

### Operations

#### `load(match: object, ctrl?: object)`

Load a single entity matching the given criteria.

```ts
const result = await client.v2_search.load({ id: 'v2_search_id' })
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

