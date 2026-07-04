# FreeMusic Ruby SDK Reference

Complete API reference for the FreeMusic Ruby SDK.


## FreeMusicSDK

### Constructor

```ruby
require_relative 'free-music_sdk'

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
v1_list = client.v1_list
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

#### `list(reqmatch, ctrl = nil) -> Array`

List entities matching the given criteria. Returns an array. Raises on error.

```ruby
results = client.v1_list.list(nil)
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v1_list.load({ "id" => "v1_list_id" })
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
v1_lookup = client.v1_lookup
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

#### `list(reqmatch, ctrl = nil) -> Array`

List entities matching the given criteria. Returns an array. Raises on error.

```ruby
results = client.v1_lookup.list(nil)
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v1_lookup.load({ "id" => "v1_lookup_id" })
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
v1_search = client.v1_search
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

#### `list(reqmatch, ctrl = nil) -> Array`

List entities matching the given criteria. Returns an array. Raises on error.

```ruby
results = client.v1_search.list(nil)
```

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v1_search.load({ "id" => "v1_search_id" })
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
v2_list = client.v2_list
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v2_list.load({ "id" => "v2_list_id" })
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
v2_lookup = client.v2_lookup
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |
| `artist` | ``$ARRAY`` | No |  |
| `track` | ``$ARRAY`` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v2_lookup.load({ "id" => "v2_lookup_id" })
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
v2_search = client.v2_search
```

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `album` | ``$ARRAY`` | No |  |
| `artist` | ``$ARRAY`` | No |  |
| `track` | ``$ARRAY`` | No |  |

### Operations

#### `load(reqmatch, ctrl = nil) -> result`

Load a single entity matching the given criteria. Raises on error.

```ruby
result = client.v2_search.load({ "id" => "v2_search_id" })
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

