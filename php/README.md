# FreeMusic PHP SDK

The PHP SDK for the FreeMusic API. Provides an entity-oriented interface using PHP conventions.


## Install
```bash
composer require voxgig/free-music-sdk
```


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### 1. Create a client

```php
<?php
require_once 'freemusic_sdk.php';

$client = new FreeMusicSDK([
    "apikey" => getenv("FREE-MUSIC_APIKEY"),
]);
```

### 2. List v1lists

```php
[$result, $err] = $client->V1List(null)->list(null, null);
if ($err) { throw new \Exception($err); }

if (is_array($result)) {
    foreach ($result as $item) {
        $d = $item->data_get();
        echo $d["id"] . " " . $d["name"] . "\n";
    }
}
```

### 3. Load a v1list

```php
[$result, $err] = $client->V1List(null)->load(["id" => "example_id"], null);
if ($err) { throw new \Exception($err); }
print_r($result);
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```php
[$result, $err] = $client->direct([
    "path" => "/api/resource/{id}",
    "method" => "GET",
    "params" => ["id" => "example"],
]);
if ($err) { throw new \Exception($err); }

if ($result["ok"]) {
    echo $result["status"];  // 200
    print_r($result["data"]);  // response body
}
```

### Prepare a request without sending it

```php
[$fetchdef, $err] = $client->prepare([
    "path" => "/api/resource/{id}",
    "method" => "DELETE",
    "params" => ["id" => "example"],
]);
if ($err) { throw new \Exception($err); }

echo $fetchdef["url"];
echo $fetchdef["method"];
print_r($fetchdef["headers"]);
```

### Use test mode

Create a mock client for unit testing — no server required:

```php
$client = FreeMusicSDK::test(null, null);

[$result, $err] = $client->FreeMusic(null)->load(
    ["id" => "test01"], null
);
// $result contains mock response data
```

### Use a custom fetch function

Replace the HTTP transport with your own function:

```php
$mock_fetch = function ($url, $init) {
    return [
        [
            "status" => 200,
            "statusText" => "OK",
            "headers" => [],
            "json" => function () { return ["id" => "mock01"]; },
        ],
        null,
    ];
};

$client = new FreeMusicSDK([
    "base" => "http://localhost:8080",
    "system" => [
        "fetch" => $mock_fetch,
    ],
]);
```

### Run live tests

Create a `.env.local` file at the project root:

```
FREE-MUSIC_TEST_LIVE=TRUE
FREE-MUSIC_APIKEY=<your-key>
```

Then run:

```bash
cd php && ./vendor/bin/phpunit test/
```


## Reference

### FreeMusicSDK

```php
require_once 'freemusic_sdk.php';
$client = new FreeMusicSDK($options);
```

Creates a new SDK client.

| Option | Type | Description |
| --- | --- | --- |
| `apikey` | `string` | API key for authentication. |
| `base` | `string` | Base URL of the API server. |
| `prefix` | `string` | URL path prefix prepended to all requests. |
| `suffix` | `string` | URL path suffix appended to all requests. |
| `feature` | `array` | Feature activation flags. |
| `extend` | `array` | Additional Feature instances to load. |
| `system` | `array` | System overrides (e.g. custom `fetch` callable). |

### test

```php
$client = FreeMusicSDK::test($testopts, $sdkopts);
```

Creates a test-mode client with mock transport. Both arguments may be `null`.

### FreeMusicSDK methods

| Method | Signature | Description |
| --- | --- | --- |
| `options_map` | `(): array` | Deep copy of current SDK options. |
| `get_utility` | `(): Utility` | Copy of the SDK utility object. |
| `prepare` | `(array $fetchargs): array` | Build an HTTP request definition without sending. |
| `direct` | `(array $fetchargs): array` | Build and send an HTTP request. |
| `V1List` | `($data): V1ListEntity` | Create a V1List entity instance. |
| `V1Lookup` | `($data): V1LookupEntity` | Create a V1Lookup entity instance. |
| `V1Search` | `($data): V1SearchEntity` | Create a V1Search entity instance. |
| `V2List` | `($data): V2ListEntity` | Create a V2List entity instance. |
| `V2Lookup` | `($data): V2LookupEntity` | Create a V2Lookup entity instance. |
| `V2Search` | `($data): V2SearchEntity` | Create a V2Search entity instance. |

### Entity interface

All entities share the same interface.

| Method | Signature | Description |
| --- | --- | --- |
| `load` | `($reqmatch, $ctrl): array` | Load a single entity by match criteria. |
| `list` | `($reqmatch, $ctrl): array` | List entities matching the criteria. |
| `create` | `($reqdata, $ctrl): array` | Create a new entity. |
| `update` | `($reqdata, $ctrl): array` | Update an existing entity. |
| `remove` | `($reqmatch, $ctrl): array` | Remove an entity. |
| `data_get` | `(): array` | Get entity data. |
| `data_set` | `($data): void` | Set entity data. |
| `match_get` | `(): array` | Get entity match criteria. |
| `match_set` | `($match): void` | Set entity match criteria. |
| `make` | `(): Entity` | Create a new instance with the same options. |
| `get_name` | `(): string` | Return the entity name. |

### Result shape

Entity operations return `[$result, $err]`. The first value is an
`array` with these keys:

| Key | Type | Description |
| --- | --- | --- |
| `ok` | `bool` | `true` if the HTTP status is 2xx. |
| `status` | `int` | HTTP status code. |
| `headers` | `array` | Response headers. |
| `data` | `mixed` | Parsed JSON response body. |

On error, `ok` is `false` and `$err` contains the error value.

### Entities

#### V1List

| Field | Description |
| --- | --- |
| `id_album` |  |
| `id_artist` |  |
| `id_imvdb` |  |
| `id_lyric` |  |
| `id_track` |  |
| `int_cd` |  |
| `int_duration` |  |
| `int_loved` |  |
| `int_music_vid_comment` |  |
| `int_music_vid_dislike` |  |
| `int_music_vid_favorite` |  |
| `int_music_vid_like` |  |
| `int_music_vid_view` |  |
| `int_score` |  |
| `int_score_vote` |  |
| `int_total_listener` |  |
| `int_total_play` |  |
| `int_track_number` |  |
| `str_album` |  |
| `str_artist` |  |
| `str_artist_alternate` |  |
| `str_description_en` |  |
| `str_genre` |  |
| `str_locked` |  |
| `str_mood` |  |
| `str_music_brainz_album_id` |  |
| `str_music_brainz_artist_id` |  |
| `str_music_brainz_id` |  |
| `str_music_vid` |  |
| `str_music_vid_company` |  |
| `str_music_vid_director` |  |
| `str_music_vid_screen1` |  |
| `str_music_vid_screen2` |  |
| `str_music_vid_screen3` |  |
| `str_style` |  |
| `str_theme` |  |
| `str_track` |  |
| `str_track3x3` |  |
| `str_track_lyric` |  |
| `str_track_thumb` |  |
| `trending` |  |

Operations: List, Load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `id_album` |  |
| `id_artist` |  |
| `id_imvdb` |  |
| `id_label` |  |
| `id_lyric` |  |
| `id_track` |  |
| `int_born_year` |  |
| `int_cd` |  |
| `int_charted` |  |
| `int_died_year` |  |
| `int_duration` |  |
| `int_formed_year` |  |
| `int_loved` |  |
| `int_member` |  |
| `int_music_vid_comment` |  |
| `int_music_vid_dislike` |  |
| `int_music_vid_favorite` |  |
| `int_music_vid_like` |  |
| `int_music_vid_view` |  |
| `int_sale` |  |
| `int_score` |  |
| `int_score_vote` |  |
| `int_total_listener` |  |
| `int_total_play` |  |
| `int_track_number` |  |
| `int_year_released` |  |
| `str_album` |  |
| `str_album3_d_case` |  |
| `str_album3_d_face` |  |
| `str_album3_d_flat` |  |
| `str_album3_d_thumb` |  |
| `str_album_c_dart` |  |
| `str_album_spine` |  |
| `str_album_stripped` |  |
| `str_album_thumb` |  |
| `str_album_thumb_back` |  |
| `str_album_thumb_hq` |  |
| `str_all_music_id` |  |
| `str_amazon_id` |  |
| `str_artist` |  |
| `str_artist_alternate` |  |
| `str_artist_banner` |  |
| `str_artist_clearart` |  |
| `str_artist_cutout` |  |
| `str_artist_fanart` |  |
| `str_artist_fanart2` |  |
| `str_artist_fanart3` |  |
| `str_artist_fanart4` |  |
| `str_artist_logo` |  |
| `str_artist_stripped` |  |
| `str_artist_thumb` |  |
| `str_artist_wide_thumb` |  |
| `str_bbc_review_id` |  |
| `str_biography_en` |  |
| `str_country` |  |
| `str_country_code` |  |
| `str_description_en` |  |
| `str_disbanded` |  |
| `str_discogs_id` |  |
| `str_facebook` |  |
| `str_gender` |  |
| `str_genius_id` |  |
| `str_genre` |  |
| `str_isn_icode` |  |
| `str_itunes_id` |  |
| `str_label` |  |
| `str_last_fm_chart` |  |
| `str_location` |  |
| `str_locked` |  |
| `str_lyric_wiki_id` |  |
| `str_mood` |  |
| `str_music_brainz_album_id` |  |
| `str_music_brainz_artist_id` |  |
| `str_music_brainz_id` |  |
| `str_music_moz_id` |  |
| `str_music_vid` |  |
| `str_music_vid_company` |  |
| `str_music_vid_director` |  |
| `str_music_vid_screen1` |  |
| `str_music_vid_screen2` |  |
| `str_music_vid_screen3` |  |
| `str_rate_your_music_id` |  |
| `str_release_format` |  |
| `str_review` |  |
| `str_speed` |  |
| `str_style` |  |
| `str_theme` |  |
| `str_track` |  |
| `str_track3x3` |  |
| `str_track_lyric` |  |
| `str_track_thumb` |  |
| `str_twitter` |  |
| `str_website` |  |
| `str_wikidata_id` |  |
| `str_wikipedia_id` |  |

Operations: List, Load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `album` |  |
| `id_album` |  |
| `id_artist` |  |
| `id_imvdb` |  |
| `id_label` |  |
| `id_lyric` |  |
| `id_track` |  |
| `int_born_year` |  |
| `int_cd` |  |
| `int_charted` |  |
| `int_died_year` |  |
| `int_duration` |  |
| `int_formed_year` |  |
| `int_loved` |  |
| `int_member` |  |
| `int_music_vid_comment` |  |
| `int_music_vid_dislike` |  |
| `int_music_vid_favorite` |  |
| `int_music_vid_like` |  |
| `int_music_vid_view` |  |
| `int_sale` |  |
| `int_score` |  |
| `int_score_vote` |  |
| `int_total_listener` |  |
| `int_total_play` |  |
| `int_track_number` |  |
| `int_year_released` |  |
| `str_album` |  |
| `str_album3_d_case` |  |
| `str_album3_d_face` |  |
| `str_album3_d_flat` |  |
| `str_album3_d_thumb` |  |
| `str_album_c_dart` |  |
| `str_album_spine` |  |
| `str_album_stripped` |  |
| `str_album_thumb` |  |
| `str_album_thumb_back` |  |
| `str_album_thumb_hq` |  |
| `str_all_music_id` |  |
| `str_amazon_id` |  |
| `str_artist` |  |
| `str_artist_alternate` |  |
| `str_artist_banner` |  |
| `str_artist_clearart` |  |
| `str_artist_cutout` |  |
| `str_artist_fanart` |  |
| `str_artist_fanart2` |  |
| `str_artist_fanart3` |  |
| `str_artist_fanart4` |  |
| `str_artist_logo` |  |
| `str_artist_stripped` |  |
| `str_artist_thumb` |  |
| `str_artist_wide_thumb` |  |
| `str_bbc_review_id` |  |
| `str_biography_en` |  |
| `str_country` |  |
| `str_country_code` |  |
| `str_description_en` |  |
| `str_disbanded` |  |
| `str_discogs_id` |  |
| `str_facebook` |  |
| `str_gender` |  |
| `str_genius_id` |  |
| `str_genre` |  |
| `str_isn_icode` |  |
| `str_itunes_id` |  |
| `str_label` |  |
| `str_last_fm_chart` |  |
| `str_location` |  |
| `str_locked` |  |
| `str_lyric_wiki_id` |  |
| `str_mood` |  |
| `str_music_brainz_album_id` |  |
| `str_music_brainz_artist_id` |  |
| `str_music_brainz_id` |  |
| `str_music_moz_id` |  |
| `str_music_vid` |  |
| `str_music_vid_company` |  |
| `str_music_vid_director` |  |
| `str_music_vid_screen1` |  |
| `str_music_vid_screen2` |  |
| `str_music_vid_screen3` |  |
| `str_rate_your_music_id` |  |
| `str_release_format` |  |
| `str_review` |  |
| `str_speed` |  |
| `str_style` |  |
| `str_theme` |  |
| `str_track` |  |
| `str_track3x3` |  |
| `str_track_lyric` |  |
| `str_track_thumb` |  |
| `str_twitter` |  |
| `str_website` |  |
| `str_wikidata_id` |  |
| `str_wikipedia_id` |  |

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
| `artist` |  |
| `track` |  |

Operations: Load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `album` |  |
| `artist` |  |
| `track` |  |

Operations: Load.

API path: `/search/album/{albumName}`



## Entities


### V1List

Create an instance: `const v1_list = client.V1List()`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `id_album` | ``$STRING`` |  |
| `id_artist` | ``$STRING`` |  |
| `id_imvdb` | ``$STRING`` |  |
| `id_lyric` | ``$STRING`` |  |
| `id_track` | ``$STRING`` |  |
| `int_cd` | ``$STRING`` |  |
| `int_duration` | ``$STRING`` |  |
| `int_loved` | ``$STRING`` |  |
| `int_music_vid_comment` | ``$STRING`` |  |
| `int_music_vid_dislike` | ``$STRING`` |  |
| `int_music_vid_favorite` | ``$STRING`` |  |
| `int_music_vid_like` | ``$STRING`` |  |
| `int_music_vid_view` | ``$STRING`` |  |
| `int_score` | ``$STRING`` |  |
| `int_score_vote` | ``$STRING`` |  |
| `int_total_listener` | ``$STRING`` |  |
| `int_total_play` | ``$STRING`` |  |
| `int_track_number` | ``$STRING`` |  |
| `str_album` | ``$STRING`` |  |
| `str_artist` | ``$STRING`` |  |
| `str_artist_alternate` | ``$STRING`` |  |
| `str_description_en` | ``$STRING`` |  |
| `str_genre` | ``$STRING`` |  |
| `str_locked` | ``$STRING`` |  |
| `str_mood` | ``$STRING`` |  |
| `str_music_brainz_album_id` | ``$STRING`` |  |
| `str_music_brainz_artist_id` | ``$STRING`` |  |
| `str_music_brainz_id` | ``$STRING`` |  |
| `str_music_vid` | ``$STRING`` |  |
| `str_music_vid_company` | ``$STRING`` |  |
| `str_music_vid_director` | ``$STRING`` |  |
| `str_music_vid_screen1` | ``$STRING`` |  |
| `str_music_vid_screen2` | ``$STRING`` |  |
| `str_music_vid_screen3` | ``$STRING`` |  |
| `str_style` | ``$STRING`` |  |
| `str_theme` | ``$STRING`` |  |
| `str_track` | ``$STRING`` |  |
| `str_track3x3` | ``$STRING`` |  |
| `str_track_lyric` | ``$STRING`` |  |
| `str_track_thumb` | ``$STRING`` |  |
| `trending` | ``$ARRAY`` |  |

#### Example: Load

```ts
const v1_list = await client.V1List().load({ id: 'v1_list_id' })
```

#### Example: List

```ts
const v1_lists = await client.V1List().list()
```


### V1Lookup

Create an instance: `const v1_lookup = client.V1Lookup()`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `id_album` | ``$STRING`` |  |
| `id_artist` | ``$STRING`` |  |
| `id_imvdb` | ``$STRING`` |  |
| `id_label` | ``$STRING`` |  |
| `id_lyric` | ``$STRING`` |  |
| `id_track` | ``$STRING`` |  |
| `int_born_year` | ``$STRING`` |  |
| `int_cd` | ``$STRING`` |  |
| `int_charted` | ``$STRING`` |  |
| `int_died_year` | ``$STRING`` |  |
| `int_duration` | ``$STRING`` |  |
| `int_formed_year` | ``$STRING`` |  |
| `int_loved` | ``$STRING`` |  |
| `int_member` | ``$STRING`` |  |
| `int_music_vid_comment` | ``$STRING`` |  |
| `int_music_vid_dislike` | ``$STRING`` |  |
| `int_music_vid_favorite` | ``$STRING`` |  |
| `int_music_vid_like` | ``$STRING`` |  |
| `int_music_vid_view` | ``$STRING`` |  |
| `int_sale` | ``$STRING`` |  |
| `int_score` | ``$STRING`` |  |
| `int_score_vote` | ``$STRING`` |  |
| `int_total_listener` | ``$STRING`` |  |
| `int_total_play` | ``$STRING`` |  |
| `int_track_number` | ``$STRING`` |  |
| `int_year_released` | ``$STRING`` |  |
| `str_album` | ``$STRING`` |  |
| `str_album3_d_case` | ``$STRING`` |  |
| `str_album3_d_face` | ``$STRING`` |  |
| `str_album3_d_flat` | ``$STRING`` |  |
| `str_album3_d_thumb` | ``$STRING`` |  |
| `str_album_c_dart` | ``$STRING`` |  |
| `str_album_spine` | ``$STRING`` |  |
| `str_album_stripped` | ``$STRING`` |  |
| `str_album_thumb` | ``$STRING`` |  |
| `str_album_thumb_back` | ``$STRING`` |  |
| `str_album_thumb_hq` | ``$STRING`` |  |
| `str_all_music_id` | ``$STRING`` |  |
| `str_amazon_id` | ``$STRING`` |  |
| `str_artist` | ``$STRING`` |  |
| `str_artist_alternate` | ``$STRING`` |  |
| `str_artist_banner` | ``$STRING`` |  |
| `str_artist_clearart` | ``$STRING`` |  |
| `str_artist_cutout` | ``$STRING`` |  |
| `str_artist_fanart` | ``$STRING`` |  |
| `str_artist_fanart2` | ``$STRING`` |  |
| `str_artist_fanart3` | ``$STRING`` |  |
| `str_artist_fanart4` | ``$STRING`` |  |
| `str_artist_logo` | ``$STRING`` |  |
| `str_artist_stripped` | ``$STRING`` |  |
| `str_artist_thumb` | ``$STRING`` |  |
| `str_artist_wide_thumb` | ``$STRING`` |  |
| `str_bbc_review_id` | ``$STRING`` |  |
| `str_biography_en` | ``$STRING`` |  |
| `str_country` | ``$STRING`` |  |
| `str_country_code` | ``$STRING`` |  |
| `str_description_en` | ``$STRING`` |  |
| `str_disbanded` | ``$STRING`` |  |
| `str_discogs_id` | ``$STRING`` |  |
| `str_facebook` | ``$STRING`` |  |
| `str_gender` | ``$STRING`` |  |
| `str_genius_id` | ``$STRING`` |  |
| `str_genre` | ``$STRING`` |  |
| `str_isn_icode` | ``$STRING`` |  |
| `str_itunes_id` | ``$STRING`` |  |
| `str_label` | ``$STRING`` |  |
| `str_last_fm_chart` | ``$STRING`` |  |
| `str_location` | ``$STRING`` |  |
| `str_locked` | ``$STRING`` |  |
| `str_lyric_wiki_id` | ``$STRING`` |  |
| `str_mood` | ``$STRING`` |  |
| `str_music_brainz_album_id` | ``$STRING`` |  |
| `str_music_brainz_artist_id` | ``$STRING`` |  |
| `str_music_brainz_id` | ``$STRING`` |  |
| `str_music_moz_id` | ``$STRING`` |  |
| `str_music_vid` | ``$STRING`` |  |
| `str_music_vid_company` | ``$STRING`` |  |
| `str_music_vid_director` | ``$STRING`` |  |
| `str_music_vid_screen1` | ``$STRING`` |  |
| `str_music_vid_screen2` | ``$STRING`` |  |
| `str_music_vid_screen3` | ``$STRING`` |  |
| `str_rate_your_music_id` | ``$STRING`` |  |
| `str_release_format` | ``$STRING`` |  |
| `str_review` | ``$STRING`` |  |
| `str_speed` | ``$STRING`` |  |
| `str_style` | ``$STRING`` |  |
| `str_theme` | ``$STRING`` |  |
| `str_track` | ``$STRING`` |  |
| `str_track3x3` | ``$STRING`` |  |
| `str_track_lyric` | ``$STRING`` |  |
| `str_track_thumb` | ``$STRING`` |  |
| `str_twitter` | ``$STRING`` |  |
| `str_website` | ``$STRING`` |  |
| `str_wikidata_id` | ``$STRING`` |  |
| `str_wikipedia_id` | ``$STRING`` |  |

#### Example: Load

```ts
const v1_lookup = await client.V1Lookup().load({ id: 'v1_lookup_id' })
```

#### Example: List

```ts
const v1_lookups = await client.V1Lookup().list()
```


### V1Search

Create an instance: `const v1_search = client.V1Search()`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | ``$ARRAY`` |  |
| `id_album` | ``$STRING`` |  |
| `id_artist` | ``$STRING`` |  |
| `id_imvdb` | ``$STRING`` |  |
| `id_label` | ``$STRING`` |  |
| `id_lyric` | ``$STRING`` |  |
| `id_track` | ``$STRING`` |  |
| `int_born_year` | ``$STRING`` |  |
| `int_cd` | ``$STRING`` |  |
| `int_charted` | ``$STRING`` |  |
| `int_died_year` | ``$STRING`` |  |
| `int_duration` | ``$STRING`` |  |
| `int_formed_year` | ``$STRING`` |  |
| `int_loved` | ``$STRING`` |  |
| `int_member` | ``$STRING`` |  |
| `int_music_vid_comment` | ``$STRING`` |  |
| `int_music_vid_dislike` | ``$STRING`` |  |
| `int_music_vid_favorite` | ``$STRING`` |  |
| `int_music_vid_like` | ``$STRING`` |  |
| `int_music_vid_view` | ``$STRING`` |  |
| `int_sale` | ``$STRING`` |  |
| `int_score` | ``$STRING`` |  |
| `int_score_vote` | ``$STRING`` |  |
| `int_total_listener` | ``$STRING`` |  |
| `int_total_play` | ``$STRING`` |  |
| `int_track_number` | ``$STRING`` |  |
| `int_year_released` | ``$STRING`` |  |
| `str_album` | ``$STRING`` |  |
| `str_album3_d_case` | ``$STRING`` |  |
| `str_album3_d_face` | ``$STRING`` |  |
| `str_album3_d_flat` | ``$STRING`` |  |
| `str_album3_d_thumb` | ``$STRING`` |  |
| `str_album_c_dart` | ``$STRING`` |  |
| `str_album_spine` | ``$STRING`` |  |
| `str_album_stripped` | ``$STRING`` |  |
| `str_album_thumb` | ``$STRING`` |  |
| `str_album_thumb_back` | ``$STRING`` |  |
| `str_album_thumb_hq` | ``$STRING`` |  |
| `str_all_music_id` | ``$STRING`` |  |
| `str_amazon_id` | ``$STRING`` |  |
| `str_artist` | ``$STRING`` |  |
| `str_artist_alternate` | ``$STRING`` |  |
| `str_artist_banner` | ``$STRING`` |  |
| `str_artist_clearart` | ``$STRING`` |  |
| `str_artist_cutout` | ``$STRING`` |  |
| `str_artist_fanart` | ``$STRING`` |  |
| `str_artist_fanart2` | ``$STRING`` |  |
| `str_artist_fanart3` | ``$STRING`` |  |
| `str_artist_fanart4` | ``$STRING`` |  |
| `str_artist_logo` | ``$STRING`` |  |
| `str_artist_stripped` | ``$STRING`` |  |
| `str_artist_thumb` | ``$STRING`` |  |
| `str_artist_wide_thumb` | ``$STRING`` |  |
| `str_bbc_review_id` | ``$STRING`` |  |
| `str_biography_en` | ``$STRING`` |  |
| `str_country` | ``$STRING`` |  |
| `str_country_code` | ``$STRING`` |  |
| `str_description_en` | ``$STRING`` |  |
| `str_disbanded` | ``$STRING`` |  |
| `str_discogs_id` | ``$STRING`` |  |
| `str_facebook` | ``$STRING`` |  |
| `str_gender` | ``$STRING`` |  |
| `str_genius_id` | ``$STRING`` |  |
| `str_genre` | ``$STRING`` |  |
| `str_isn_icode` | ``$STRING`` |  |
| `str_itunes_id` | ``$STRING`` |  |
| `str_label` | ``$STRING`` |  |
| `str_last_fm_chart` | ``$STRING`` |  |
| `str_location` | ``$STRING`` |  |
| `str_locked` | ``$STRING`` |  |
| `str_lyric_wiki_id` | ``$STRING`` |  |
| `str_mood` | ``$STRING`` |  |
| `str_music_brainz_album_id` | ``$STRING`` |  |
| `str_music_brainz_artist_id` | ``$STRING`` |  |
| `str_music_brainz_id` | ``$STRING`` |  |
| `str_music_moz_id` | ``$STRING`` |  |
| `str_music_vid` | ``$STRING`` |  |
| `str_music_vid_company` | ``$STRING`` |  |
| `str_music_vid_director` | ``$STRING`` |  |
| `str_music_vid_screen1` | ``$STRING`` |  |
| `str_music_vid_screen2` | ``$STRING`` |  |
| `str_music_vid_screen3` | ``$STRING`` |  |
| `str_rate_your_music_id` | ``$STRING`` |  |
| `str_release_format` | ``$STRING`` |  |
| `str_review` | ``$STRING`` |  |
| `str_speed` | ``$STRING`` |  |
| `str_style` | ``$STRING`` |  |
| `str_theme` | ``$STRING`` |  |
| `str_track` | ``$STRING`` |  |
| `str_track3x3` | ``$STRING`` |  |
| `str_track_lyric` | ``$STRING`` |  |
| `str_track_thumb` | ``$STRING`` |  |
| `str_twitter` | ``$STRING`` |  |
| `str_website` | ``$STRING`` |  |
| `str_wikidata_id` | ``$STRING`` |  |
| `str_wikipedia_id` | ``$STRING`` |  |

#### Example: Load

```ts
const v1_search = await client.V1Search().load({ id: 'v1_search_id' })
```

#### Example: List

```ts
const v1_searchs = await client.V1Search().list()
```


### V2List

Create an instance: `const v2_list = client.V2List()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | ``$ARRAY`` |  |

#### Example: Load

```ts
const v2_list = await client.V2List().load({ id: 'v2_list_id' })
```


### V2Lookup

Create an instance: `const v2_lookup = client.V2Lookup()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | ``$ARRAY`` |  |
| `artist` | ``$ARRAY`` |  |
| `track` | ``$ARRAY`` |  |

#### Example: Load

```ts
const v2_lookup = await client.V2Lookup().load({ id: 'v2_lookup_id' })
```


### V2Search

Create an instance: `const v2_search = client.V2Search()`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | ``$ARRAY`` |  |
| `artist` | ``$ARRAY`` |  |
| `track` | ``$ARRAY`` |  |

#### Example: Load

```ts
const v2_search = await client.V2Search().load({ id: 'v2_search_id' })
```


## Explanation

### The operation pipeline

Every entity operation (load, list, create, update, remove) follows a
six-stage pipeline. Each stage fires a feature hook before executing:

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

If any stage returns an error, the pipeline short-circuits and the
error is returned to the caller as the second element in the return array.

### Features and hooks

Features are the extension mechanism. A feature is a PHP class
with hook methods named after pipeline stages (e.g. `PrePoint`,
`PreSpec`). Each method receives the context.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Data as arrays

The PHP SDK uses plain PHP associative arrays throughout rather than typed
objects. This mirrors the dynamic nature of the API and keeps the
SDK flexible — no code generation is needed when the API schema
changes.

Use `Helpers::to_map()` to safely validate that a value is an array.

### Directory structure

```
php/
├── freemusic_sdk.php          -- Main SDK class
├── config.php                     -- Configuration
├── features.php                   -- Feature factory
├── core/                          -- Core types and context
├── entity/                        -- Entity implementations
├── feature/                       -- Built-in features (Base, Test, Log)
├── utility/                       -- Utility functions and struct library
└── test/                          -- Test suites
```

The main class (`freemusic_sdk.php`) exports the SDK class
and test helper. Import entity or utility modules directly only
when needed.

### Entity state

Entity instances are stateful. After a successful `load`, the entity
stores the returned data and match criteria internally.

```php
$moon = $client->Moon();
[$result, $err] = $moon->load(["planet_id" => "earth", "id" => "luna"]);

// $moon->dataGet() now returns the loaded moon data
// $moon->matchGet() returns the last match criteria
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
