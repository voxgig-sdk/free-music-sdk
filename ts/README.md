# FreeMusic TypeScript SDK



The TypeScript SDK for the FreeMusic API — a type-safe, entity-oriented client with full async/await support.

The API is exposed as capitalised, semantic **Entities** — e.g.
`client.V1List()` — each with a small set of operations (`list`, `load`)
instead of raw URL paths and query parameters. This keeps the surface
predictable and low-friction for both humans and AI agents.

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

`list()` resolves to an array of V1List ENTITIES — every operation
resolves to entities, not raw records. Iterate them directly, and call
`.data()` on one for the record it holds:

```ts
const v1lists = await client.V1List().list({ api_key: "example" })

for (const v1list of v1lists) {
  console.log(v1list)
}
```

### 3. Load a v2list

V2List is nested under id_artist, so provide the `id_artist`.
`load()` returns the entity directly and throws on failure:

```ts
try {
  const v2list = await client.V2List().load({
    id_artist: 1,
  })
  console.log(v2list)
} catch (err) {
  console.error('load failed:', err)
}
```


## Error handling

Entity operations reject on failure, so wrap them in `try` / `catch`:

```ts
try {
  const v2lookup = await client.V2Lookup().load({ id_album: 1 })
  console.log(v2lookup)
} catch (err) {
  console.error('load failed:', err)
}
```

The low-level `direct()` method does **not** throw — it returns the
value or an `Error`, so check the result before using it:

```ts
const result = await client.direct({
  path: '/api/resource/{id}',
  method: 'GET',
  params: { id: 'example_id' },
})

if (result instanceof Error) {
  throw result
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

const v2lookup = await client.V2Lookup().load({ id_album: 1 })
// v2lookup is the entity, populated with mock response data
// — call v2lookup.data() for the record itself
console.log(v2lookup)
```

You can also use the instance method:

```ts
const client = new FreeMusicSDK({ apikey: '...' })
const testClient = client.tester()
```

### Retain entity state across calls

Entity instances remember their last match and data:

```ts
const entity = client.V2Lookup()

// First call runs the operation and stores its result
await entity.load({ id_album: 1 })

// Subsequent calls reuse the stored state
const data = entity.data()
console.log(data)
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
| `data` | `data(data?: Partial<Entity>): Entity` | Get or set entity data. |
| `match` | `match(match?: Partial<Entity>): Partial<Entity>` | Get or set entity match criteria. |
| `make` | `make(): Entity` | Create a new instance with the same options. |
| `client` | `client(): FreeMusicSDK` | Return the parent SDK client. |
| `entopts` | `entopts(): object` | Return a copy of the entity options. |

#### Return values

Entity operations resolve to the entity data directly — there is no
result envelope:

- `load` resolves to a single entity object.
- `list` resolves to an **array** of entity objects (iterate it directly;
  there is no `.data` and no `.ok`).

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
| `idAlbum` |  |
| `idArtist` |  |
| `idIMVDB` |  |
| `idLyric` |  |
| `idTrack` |  |
| `intCD` |  |
| `intDuration` |  |
| `intLoved` |  |
| `intMusicVidComments` |  |
| `intMusicVidDislikes` |  |
| `intMusicVidFavorites` |  |
| `intMusicVidLikes` |  |
| `intMusicVidViews` |  |
| `intScore` |  |
| `intScoreVotes` |  |
| `intTotalListeners` |  |
| `intTotalPlays` |  |
| `intTrackNumber` |  |
| `strAlbum` |  |
| `strArtist` |  |
| `strArtistAlternate` |  |
| `strDescriptionEN` |  |
| `strGenre` |  |
| `strLocked` |  |
| `strMood` |  |
| `strMusicBrainzAlbumID` |  |
| `strMusicBrainzArtistID` |  |
| `strMusicBrainzID` |  |
| `strMusicVid` |  |
| `strMusicVidCompany` |  |
| `strMusicVidDirector` |  |
| `strMusicVidScreen1` |  |
| `strMusicVidScreen2` |  |
| `strMusicVidScreen3` |  |
| `strStyle` |  |
| `strTheme` |  |
| `strTrack` |  |
| `strTrack3x3` |  |
| `strTrackLyrics` |  |
| `strTrackThumb` |  |
| `trending` |  |

Operations: list, load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `idAlbum` |  |
| `idArtist` |  |
| `idIMVDB` |  |
| `idLabel` |  |
| `idLyric` |  |
| `idTrack` |  |
| `intBornYear` |  |
| `intCD` |  |
| `intCharted` |  |
| `intDiedYear` |  |
| `intDuration` |  |
| `intFormedYear` |  |
| `intLoved` |  |
| `intMembers` |  |
| `intMusicVidComments` |  |
| `intMusicVidDislikes` |  |
| `intMusicVidFavorites` |  |
| `intMusicVidLikes` |  |
| `intMusicVidViews` |  |
| `intSales` |  |
| `intScore` |  |
| `intScoreVotes` |  |
| `intTotalListeners` |  |
| `intTotalPlays` |  |
| `intTrackNumber` |  |
| `intYearReleased` |  |
| `strAlbum` |  |
| `strAlbum3DCase` |  |
| `strAlbum3DFace` |  |
| `strAlbum3DFlat` |  |
| `strAlbum3DThumb` |  |
| `strAlbumCDart` |  |
| `strAlbumSpine` |  |
| `strAlbumStripped` |  |
| `strAlbumThumb` |  |
| `strAlbumThumbBack` |  |
| `strAlbumThumbHQ` |  |
| `strAllMusicID` |  |
| `strAmazonID` |  |
| `strArtist` |  |
| `strArtistAlternate` |  |
| `strArtistBanner` |  |
| `strArtistClearart` |  |
| `strArtistCutout` |  |
| `strArtistFanart` |  |
| `strArtistFanart2` |  |
| `strArtistFanart3` |  |
| `strArtistFanart4` |  |
| `strArtistLogo` |  |
| `strArtistStripped` |  |
| `strArtistThumb` |  |
| `strArtistWideThumb` |  |
| `strBBCReviewID` |  |
| `strBiographyEN` |  |
| `strCountry` |  |
| `strCountryCode` |  |
| `strDescriptionEN` |  |
| `strDisbanded` |  |
| `strDiscogsID` |  |
| `strFacebook` |  |
| `strGender` |  |
| `strGeniusID` |  |
| `strGenre` |  |
| `strISNIcode` |  |
| `strItunesID` |  |
| `strLabel` |  |
| `strLastFMChart` |  |
| `strLocation` |  |
| `strLocked` |  |
| `strLyricWikiID` |  |
| `strMood` |  |
| `strMusicBrainzAlbumID` |  |
| `strMusicBrainzArtistID` |  |
| `strMusicBrainzID` |  |
| `strMusicMozID` |  |
| `strMusicVid` |  |
| `strMusicVidCompany` |  |
| `strMusicVidDirector` |  |
| `strMusicVidScreen1` |  |
| `strMusicVidScreen2` |  |
| `strMusicVidScreen3` |  |
| `strRateYourMusicID` |  |
| `strReleaseFormat` |  |
| `strReview` |  |
| `strSpeed` |  |
| `strStyle` |  |
| `strTheme` |  |
| `strTrack` |  |
| `strTrack3x3` |  |
| `strTrackLyrics` |  |
| `strTrackThumb` |  |
| `strTwitter` |  |
| `strWebsite` |  |
| `strWikidataID` |  |
| `strWikipediaID` |  |

Operations: list, load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `album` |  |
| `idAlbum` |  |
| `idArtist` |  |
| `idIMVDB` |  |
| `idLabel` |  |
| `idLyric` |  |
| `idTrack` |  |
| `intBornYear` |  |
| `intCD` |  |
| `intCharted` |  |
| `intDiedYear` |  |
| `intDuration` |  |
| `intFormedYear` |  |
| `intLoved` |  |
| `intMembers` |  |
| `intMusicVidComments` |  |
| `intMusicVidDislikes` |  |
| `intMusicVidFavorites` |  |
| `intMusicVidLikes` |  |
| `intMusicVidViews` |  |
| `intSales` |  |
| `intScore` |  |
| `intScoreVotes` |  |
| `intTotalListeners` |  |
| `intTotalPlays` |  |
| `intTrackNumber` |  |
| `intYearReleased` |  |
| `strAlbum` |  |
| `strAlbum3DCase` |  |
| `strAlbum3DFace` |  |
| `strAlbum3DFlat` |  |
| `strAlbum3DThumb` |  |
| `strAlbumCDart` |  |
| `strAlbumSpine` |  |
| `strAlbumStripped` |  |
| `strAlbumThumb` |  |
| `strAlbumThumbBack` |  |
| `strAlbumThumbHQ` |  |
| `strAllMusicID` |  |
| `strAmazonID` |  |
| `strArtist` |  |
| `strArtistAlternate` |  |
| `strArtistBanner` |  |
| `strArtistClearart` |  |
| `strArtistCutout` |  |
| `strArtistFanart` |  |
| `strArtistFanart2` |  |
| `strArtistFanart3` |  |
| `strArtistFanart4` |  |
| `strArtistLogo` |  |
| `strArtistStripped` |  |
| `strArtistThumb` |  |
| `strArtistWideThumb` |  |
| `strBBCReviewID` |  |
| `strBiographyEN` |  |
| `strCountry` |  |
| `strCountryCode` |  |
| `strDescriptionEN` |  |
| `strDisbanded` |  |
| `strDiscogsID` |  |
| `strFacebook` |  |
| `strGender` |  |
| `strGeniusID` |  |
| `strGenre` |  |
| `strISNIcode` |  |
| `strItunesID` |  |
| `strLabel` |  |
| `strLastFMChart` |  |
| `strLocation` |  |
| `strLocked` |  |
| `strLyricWikiID` |  |
| `strMood` |  |
| `strMusicBrainzAlbumID` |  |
| `strMusicBrainzArtistID` |  |
| `strMusicBrainzID` |  |
| `strMusicMozID` |  |
| `strMusicVid` |  |
| `strMusicVidCompany` |  |
| `strMusicVidDirector` |  |
| `strMusicVidScreen1` |  |
| `strMusicVidScreen2` |  |
| `strMusicVidScreen3` |  |
| `strRateYourMusicID` |  |
| `strReleaseFormat` |  |
| `strReview` |  |
| `strSpeed` |  |
| `strStyle` |  |
| `strTheme` |  |
| `strTrack` |  |
| `strTrack3x3` |  |
| `strTrackLyrics` |  |
| `strTrackThumb` |  |
| `strTwitter` |  |
| `strWebsite` |  |
| `strWikidataID` |  |
| `strWikipediaID` |  |

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
| `artists` |  |
| `track` |  |

Operations: load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `album` |  |
| `artists` |  |
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
| `idAlbum` | `string` |  |
| `idArtist` | `string` |  |
| `idIMVDB` | `string` |  |
| `idLyric` | `string` |  |
| `idTrack` | `string` |  |
| `intCD` | `string` |  |
| `intDuration` | `string` |  |
| `intLoved` | `string` |  |
| `intMusicVidComments` | `string` |  |
| `intMusicVidDislikes` | `string` |  |
| `intMusicVidFavorites` | `string` |  |
| `intMusicVidLikes` | `string` |  |
| `intMusicVidViews` | `string` |  |
| `intScore` | `string` |  |
| `intScoreVotes` | `string` |  |
| `intTotalListeners` | `string` |  |
| `intTotalPlays` | `string` |  |
| `intTrackNumber` | `string` |  |
| `strAlbum` | `string` |  |
| `strArtist` | `string` |  |
| `strArtistAlternate` | `string` |  |
| `strDescriptionEN` | `string` |  |
| `strGenre` | `string` |  |
| `strLocked` | `string` |  |
| `strMood` | `string` |  |
| `strMusicBrainzAlbumID` | `string` |  |
| `strMusicBrainzArtistID` | `string` |  |
| `strMusicBrainzID` | `string` |  |
| `strMusicVid` | `string` |  |
| `strMusicVidCompany` | `string` |  |
| `strMusicVidDirector` | `string` |  |
| `strMusicVidScreen1` | `string` |  |
| `strMusicVidScreen2` | `string` |  |
| `strMusicVidScreen3` | `string` |  |
| `strStyle` | `string` |  |
| `strTheme` | `string` |  |
| `strTrack` | `string` |  |
| `strTrack3x3` | `string` |  |
| `strTrackLyrics` | `string` |  |
| `strTrackThumb` | `string` |  |
| `trending` | `any[]` |  |

#### Example: Load

```ts
const v1_list = await client.V1List().load({ api_key: 'api_key' })
```

#### Example: List

```ts
const v1_lists = await client.V1List().list({ api_key: "example" })
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
| `idAlbum` | `string` |  |
| `idArtist` | `string` |  |
| `idIMVDB` | `string` |  |
| `idLabel` | `string` |  |
| `idLyric` | `string` |  |
| `idTrack` | `string` |  |
| `intBornYear` | `string` |  |
| `intCD` | `string` |  |
| `intCharted` | `string` |  |
| `intDiedYear` | `string` |  |
| `intDuration` | `string` |  |
| `intFormedYear` | `string` |  |
| `intLoved` | `string` |  |
| `intMembers` | `string` |  |
| `intMusicVidComments` | `string` |  |
| `intMusicVidDislikes` | `string` |  |
| `intMusicVidFavorites` | `string` |  |
| `intMusicVidLikes` | `string` |  |
| `intMusicVidViews` | `string` |  |
| `intSales` | `string` |  |
| `intScore` | `string` |  |
| `intScoreVotes` | `string` |  |
| `intTotalListeners` | `string` |  |
| `intTotalPlays` | `string` |  |
| `intTrackNumber` | `string` |  |
| `intYearReleased` | `string` |  |
| `strAlbum` | `string` |  |
| `strAlbum3DCase` | `string` |  |
| `strAlbum3DFace` | `string` |  |
| `strAlbum3DFlat` | `string` |  |
| `strAlbum3DThumb` | `string` |  |
| `strAlbumCDart` | `string` |  |
| `strAlbumSpine` | `string` |  |
| `strAlbumStripped` | `string` |  |
| `strAlbumThumb` | `string` |  |
| `strAlbumThumbBack` | `string` |  |
| `strAlbumThumbHQ` | `string` |  |
| `strAllMusicID` | `string` |  |
| `strAmazonID` | `string` |  |
| `strArtist` | `string` |  |
| `strArtistAlternate` | `string` |  |
| `strArtistBanner` | `string` |  |
| `strArtistClearart` | `string` |  |
| `strArtistCutout` | `string` |  |
| `strArtistFanart` | `string` |  |
| `strArtistFanart2` | `string` |  |
| `strArtistFanart3` | `string` |  |
| `strArtistFanart4` | `string` |  |
| `strArtistLogo` | `string` |  |
| `strArtistStripped` | `string` |  |
| `strArtistThumb` | `string` |  |
| `strArtistWideThumb` | `string` |  |
| `strBBCReviewID` | `string` |  |
| `strBiographyEN` | `string` |  |
| `strCountry` | `string` |  |
| `strCountryCode` | `string` |  |
| `strDescriptionEN` | `string` |  |
| `strDisbanded` | `string` |  |
| `strDiscogsID` | `string` |  |
| `strFacebook` | `string` |  |
| `strGender` | `string` |  |
| `strGeniusID` | `string` |  |
| `strGenre` | `string` |  |
| `strISNIcode` | `string` |  |
| `strItunesID` | `string` |  |
| `strLabel` | `string` |  |
| `strLastFMChart` | `string` |  |
| `strLocation` | `string` |  |
| `strLocked` | `string` |  |
| `strLyricWikiID` | `string` |  |
| `strMood` | `string` |  |
| `strMusicBrainzAlbumID` | `string` |  |
| `strMusicBrainzArtistID` | `string` |  |
| `strMusicBrainzID` | `string` |  |
| `strMusicMozID` | `string` |  |
| `strMusicVid` | `string` |  |
| `strMusicVidCompany` | `string` |  |
| `strMusicVidDirector` | `string` |  |
| `strMusicVidScreen1` | `string` |  |
| `strMusicVidScreen2` | `string` |  |
| `strMusicVidScreen3` | `string` |  |
| `strRateYourMusicID` | `string` |  |
| `strReleaseFormat` | `string` |  |
| `strReview` | `string` |  |
| `strSpeed` | `string` |  |
| `strStyle` | `string` |  |
| `strTheme` | `string` |  |
| `strTrack` | `string` |  |
| `strTrack3x3` | `string` |  |
| `strTrackLyrics` | `string` |  |
| `strTrackThumb` | `string` |  |
| `strTwitter` | `string` |  |
| `strWebsite` | `string` |  |
| `strWikidataID` | `string` |  |
| `strWikipediaID` | `string` |  |

#### Example: Load

```ts
const v1_lookup = await client.V1Lookup().load({ api_key: 'api_key' })
```

#### Example: List

```ts
const v1_lookups = await client.V1Lookup().list({ api_key: "example" })
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
| `album` | `any[]` |  |
| `idAlbum` | `string` |  |
| `idArtist` | `string` |  |
| `idIMVDB` | `string` |  |
| `idLabel` | `string` |  |
| `idLyric` | `string` |  |
| `idTrack` | `string` |  |
| `intBornYear` | `string` |  |
| `intCD` | `string` |  |
| `intCharted` | `string` |  |
| `intDiedYear` | `string` |  |
| `intDuration` | `string` |  |
| `intFormedYear` | `string` |  |
| `intLoved` | `string` |  |
| `intMembers` | `string` |  |
| `intMusicVidComments` | `string` |  |
| `intMusicVidDislikes` | `string` |  |
| `intMusicVidFavorites` | `string` |  |
| `intMusicVidLikes` | `string` |  |
| `intMusicVidViews` | `string` |  |
| `intSales` | `string` |  |
| `intScore` | `string` |  |
| `intScoreVotes` | `string` |  |
| `intTotalListeners` | `string` |  |
| `intTotalPlays` | `string` |  |
| `intTrackNumber` | `string` |  |
| `intYearReleased` | `string` |  |
| `strAlbum` | `string` |  |
| `strAlbum3DCase` | `string` |  |
| `strAlbum3DFace` | `string` |  |
| `strAlbum3DFlat` | `string` |  |
| `strAlbum3DThumb` | `string` |  |
| `strAlbumCDart` | `string` |  |
| `strAlbumSpine` | `string` |  |
| `strAlbumStripped` | `string` |  |
| `strAlbumThumb` | `string` |  |
| `strAlbumThumbBack` | `string` |  |
| `strAlbumThumbHQ` | `string` |  |
| `strAllMusicID` | `string` |  |
| `strAmazonID` | `string` |  |
| `strArtist` | `string` |  |
| `strArtistAlternate` | `string` |  |
| `strArtistBanner` | `string` |  |
| `strArtistClearart` | `string` |  |
| `strArtistCutout` | `string` |  |
| `strArtistFanart` | `string` |  |
| `strArtistFanart2` | `string` |  |
| `strArtistFanart3` | `string` |  |
| `strArtistFanart4` | `string` |  |
| `strArtistLogo` | `string` |  |
| `strArtistStripped` | `string` |  |
| `strArtistThumb` | `string` |  |
| `strArtistWideThumb` | `string` |  |
| `strBBCReviewID` | `string` |  |
| `strBiographyEN` | `string` |  |
| `strCountry` | `string` |  |
| `strCountryCode` | `string` |  |
| `strDescriptionEN` | `string` |  |
| `strDisbanded` | `string` |  |
| `strDiscogsID` | `string` |  |
| `strFacebook` | `string` |  |
| `strGender` | `string` |  |
| `strGeniusID` | `string` |  |
| `strGenre` | `string` |  |
| `strISNIcode` | `string` |  |
| `strItunesID` | `string` |  |
| `strLabel` | `string` |  |
| `strLastFMChart` | `string` |  |
| `strLocation` | `string` |  |
| `strLocked` | `string` |  |
| `strLyricWikiID` | `string` |  |
| `strMood` | `string` |  |
| `strMusicBrainzAlbumID` | `string` |  |
| `strMusicBrainzArtistID` | `string` |  |
| `strMusicBrainzID` | `string` |  |
| `strMusicMozID` | `string` |  |
| `strMusicVid` | `string` |  |
| `strMusicVidCompany` | `string` |  |
| `strMusicVidDirector` | `string` |  |
| `strMusicVidScreen1` | `string` |  |
| `strMusicVidScreen2` | `string` |  |
| `strMusicVidScreen3` | `string` |  |
| `strRateYourMusicID` | `string` |  |
| `strReleaseFormat` | `string` |  |
| `strReview` | `string` |  |
| `strSpeed` | `string` |  |
| `strStyle` | `string` |  |
| `strTheme` | `string` |  |
| `strTrack` | `string` |  |
| `strTrack3x3` | `string` |  |
| `strTrackLyrics` | `string` |  |
| `strTrackThumb` | `string` |  |
| `strTwitter` | `string` |  |
| `strWebsite` | `string` |  |
| `strWikidataID` | `string` |  |
| `strWikipediaID` | `string` |  |

#### Example: Load

```ts
const v1_search = await client.V1Search().load({ api_key: 'api_key' })
```

#### Example: List

```ts
const v1_searchs = await client.V1Search().list({ api_key: "example" })
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
| `album` | `any[]` |  |

#### Example: Load

```ts
const v2_list = await client.V2List().load({ id_artist: 1 })
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
| `album` | `any[]` |  |
| `artists` | `any[]` |  |
| `track` | `any[]` |  |

#### Example: Load

```ts
const v2_lookup = await client.V2Lookup().load({ id_album: 1 })
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
| `album` | `any[]` |  |
| `artists` | `any[]` |  |
| `track` | `any[]` |  |

#### Example: Load

```ts
const v2_search = await client.V2Search().load({ album_name: 'album_name' })
```


## Advanced

> The sections above cover everyday use. The material below explains the
> SDK's internals — useful when extending it with custom features, but not
> needed for normal use.

### The operation pipeline

Every entity operation follows a six-stage pipeline. Each stage fires a
feature hook before executing:

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

If any stage errors, the pipeline short-circuits and the error surfaces
to the caller — see [Error handling](#error-handling) for how that looks
in this language.

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
const v2lookup = client.V2Lookup()
await v2lookup.load({ id_album: 1 })

// v2lookup.data() now returns the v2lookup data from the last `load`
// v2lookup.match() returns the last match criteria
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
