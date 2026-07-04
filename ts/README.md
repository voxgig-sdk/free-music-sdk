# FreeMusic TypeScript SDK



The TypeScript SDK for the FreeMusic API — a type-safe, entity-oriented client with full async/await support.

> Other languages, the CLI, and MCP server live alongside this one — see
> the [top-level README](../README.md).


## Install
This package is not yet published to npm. Install it from the GitHub
release tag (`ts/vX.Y.Z`):

- Releases: [https://github.com/voxgig-sdk/free-music-sdk/releases](https://github.com/voxgig-sdk/free-music-sdk/releases)


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### 1. Create a client

```ts
import { FreeMusicSDK } from '@voxgig-sdk/free-music'

const client = new FreeMusicSDK({
  apikey: process.env.FREE_MUSIC_APIKEY,
})
```

### 2. List v1list records

`list()` resolves to an array of V1List objects — iterate it directly:

```ts
const v1lists = await client.V1List().list()

for (const v1list of v1lists) {
  console.log(v1list)
}
```

### 3. Load a v1list

`load()` returns the entity directly and throws on failure:

```ts
try {
  const v1list = await client.V1List().load({ id: 'example_id' })
  console.log(v1list)
} catch (err) {
  console.error('load failed:', err)
}
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```ts
const result = await client.direct({
  path: '/api/resource/{id}',
  method: 'GET',
  params: { id: 'example' },
})

if (result instanceof Error) {
  throw result
}
if (result.ok) {
  console.log(result.status)  // 200
  console.log(result.data)    // response body
}
```

### Prepare a request without sending it

```ts
const fetchdef = await client.prepare({
  path: '/api/resource/{id}',
  method: 'DELETE',
  params: { id: 'example' },
})

// Inspect before sending
console.log(fetchdef.url)
console.log(fetchdef.method)
console.log(fetchdef.headers)
```

### Use test mode

Create a mock client for unit testing — no server required:

```ts
const client = FreeMusicSDK.test()

const v1list = await client.V1List().load({ id: 'test01' })
// v1list is a bare entity populated with mock response data
console.log(v1list)
```

You can also use the instance method:

```ts
const client = new FreeMusicSDK({ apikey: '...' })
const testClient = client.tester()
```

### Retain entity state across calls

Entity instances remember their last match and data:

```ts
const entity = client.V1List()

// First call sets internal match
await entity.load({ id: 'example' })

// Subsequent calls reuse the stored match
const data = entity.data()
console.log(data.id) // 'example'
```

### Add custom middleware

Pass features via the `extend` option:

```ts
const logger = {
  hooks: {
    PreRequest: (ctx: any) => {
      console.log('Requesting:', ctx.spec.method, ctx.spec.path)
    },
    PreResponse: (ctx: any) => {
      console.log('Status:', ctx.out.request?.status)
    },
  },
}

const client = new FreeMusicSDK({
  apikey: '...',
  extend: [logger],
})
```

### Run live tests

Create a `.env.local` file at the project root:

```
FREE_MUSIC_TEST_LIVE=TRUE
FREE_MUSIC_APIKEY=<your-key>
```

Then run:

```bash
cd ts && npm test
```


## Reference

### FreeMusicSDK

#### Constructor

```ts
new FreeMusicSDK(options?: {
  apikey?: string
  base?: string
  prefix?: string
  suffix?: string
  feature?: Record<string, { active: boolean }>
  extend?: Feature[]
})
```

| Option | Type | Description |
| --- | --- | --- |
| `apikey` | `string` | API key for authentication. |
| `base` | `string` | Base URL of the API server. |
| `prefix` | `string` | URL path prefix prepended to all requests. |
| `suffix` | `string` | URL path suffix appended to all requests. |
| `feature` | `object` | Feature activation flags (e.g. `{ test: { active: true } }`). |
| `extend` | `Feature[]` | Additional feature instances to load. |

#### Methods

| Method | Returns | Description |
| --- | --- | --- |
| `options()` | `object` | Deep copy of current SDK options. |
| `utility()` | `Utility` | Deep copy of the SDK utility object. |
| `prepare(fetchargs?)` | `Promise<FetchDef>` | Build an HTTP request definition without sending it. |
| `direct(fetchargs?)` | `Promise<DirectResult>` | Build and send an HTTP request. |
| `V1List(data?)` | `V1ListEntity` | Create a V1List entity instance. |
| `V1Lookup(data?)` | `V1LookupEntity` | Create a V1Lookup entity instance. |
| `V1Search(data?)` | `V1SearchEntity` | Create a V1Search entity instance. |
| `V2List(data?)` | `V2ListEntity` | Create a V2List entity instance. |
| `V2Lookup(data?)` | `V2LookupEntity` | Create a V2Lookup entity instance. |
| `V2Search(data?)` | `V2SearchEntity` | Create a V2Search entity instance. |
| `tester(testopts?, sdkopts?)` | `FreeMusicSDK` | Create a test-mode client instance. |

#### Static methods

| Method | Returns | Description |
| --- | --- | --- |
| `FreeMusicSDK.test(testopts?, sdkopts?)` | `FreeMusicSDK` | Create a test-mode client. |

### Entity interface

All entities share the same interface.

#### Methods

| Method | Signature | Description |
| --- | --- | --- |
| `load` | `load(reqmatch?, ctrl?): Promise<Entity>` | Load a single entity by match criteria. |
| `list` | `list(reqmatch?, ctrl?): Promise<Entity[]>` | List entities matching the criteria. |
| `create` | `create(reqdata?, ctrl?): Promise<Entity>` | Create a new entity. |
| `update` | `update(reqdata?, ctrl?): Promise<Entity>` | Update an existing entity. |
| `remove` | `remove(reqmatch?, ctrl?): Promise<void>` | Remove an entity. |
| `data` | `data(data?): any` | Get or set entity data. |
| `match` | `match(match?): any` | Get or set entity match criteria. |
| `make` | `make(): Entity` | Create a new instance with the same options. |
| `client` | `client(): FreeMusicSDK` | Return the parent SDK client. |
| `entopts` | `entopts(): object` | Return a copy of the entity options. |

#### Return values

Entity operations resolve to the entity data directly — there is no
result envelope:

- `load`, `create` and `update` resolve to a single entity object.
- `list` resolves to an **array** of entity objects (iterate it directly;
  there is no `.data` and no `.ok`).
- `remove` resolves to `void`.

On a failed request these methods **throw**, so wrap calls in
`try`/`catch` to handle errors. Only `direct()` returns the result
envelope described below.

### DirectResult shape

The `direct()` method returns:

```ts
{
  ok: boolean
  status: number
  headers: object
  data: any
}
```

On error, `ok` is `false` and an `err` property contains the error.

### FetchDef shape

The `prepare()` method returns:

```ts
{
  url: string
  method: string
  headers: Record<string, string>
  body?: any
}
```

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

Operations: list, load.

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

Operations: list, load.

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

Operations: list, load.

API path: `/{apiKey}/searchalbum.php`

#### V2List

| Field | Description |
| --- | --- |
| `album` |  |

Operations: load.

API path: `/list/discography/{idArtist}`

#### V2Lookup

| Field | Description |
| --- | --- |
| `album` |  |
| `artist` |  |
| `track` |  |

Operations: load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `album` |  |
| `artist` |  |
| `track` |  |

Operations: load.

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
error is returned to the caller.

An unexpected exception triggers the `PreUnexpected` hook before
propagating.

### Features and hooks

Features are the extension mechanism. A feature is an object with a
`hooks` map. Each hook key is a pipeline stage name, and the value is
a function that receives the context.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Module structure

```
free-music/
├── src/
│   ├── FreeMusicSDK.ts        # Main SDK class
│   ├── entity/             # Entity implementations
│   ├── feature/            # Built-in features (Base, Test, Log)
│   └── utility/            # Utility functions
├── test/                   # Test suites
└── dist/                   # Compiled output
```

Import the SDK from the package root:

```ts
import { FreeMusicSDK } from '@voxgig-sdk/free-music'
```

### Entity state

Entity instances are stateful. After a successful `load`, the entity
stores the returned data and match criteria internally. Subsequent
calls on the same instance can rely on this state.

```ts
const v1list = client.V1List()
await v1list.load({ id: "example_id" })

// v1list.data() now returns the loaded v1list data
// v1list.match() returns { id: "example_id" }
```

Call `make()` to create a fresh instance with the same configuration
but no stored state.

### Direct vs entity access

The entity interface handles URL construction, parameter placement,
and response parsing automatically. Use it for standard CRUD operations.

The `direct` method gives full control over the HTTP request. Use it
for non-standard endpoints, bulk operations, or any path not modelled
as an entity. The `prepare` method is useful for debugging — it
shows exactly what `direct` would send.


## Full Reference

See [REFERENCE.md](REFERENCE.md) for complete API reference
documentation including all method signatures, entity field schemas,
and detailed usage examples.
