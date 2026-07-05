# FreeMusic Golang SDK



The Golang SDK for the FreeMusic API — an entity-oriented client using standard Go conventions. No generics required; data flows as `map[string]any`.

It exposes the API as capitalised, semantic **Entities** — e.g. `client.V1List(nil)` — each with the same small set of operations (`List`, `Load`) instead of raw URL paths and query strings. You call meaning, not endpoints, which keeps the cognitive load low.

> Other languages, the CLI, and MCP server live alongside this one — see
> the [top-level README](../README.md).


## Install
```bash
go get github.com/voxgig-sdk/free-music-sdk/go@latest
```

The Go module proxy resolves the version from the `go/vX.Y.Z` GitHub
release tag — see [Releases](https://github.com/voxgig-sdk/free-music-sdk/releases) for the available versions.

To vendor from a local checkout instead, clone this repo alongside your
project and add a `replace` directive pointing at the checked-out
`go/` directory:

```bash
go mod edit -replace github.com/voxgig-sdk/free-music-sdk/go=../free-music-sdk/go
```


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### Quickstart

A complete program: create a client, then call the entity operations.
Each operation returns `(value, error)` — the value is the data itself
(there is no `{ok, data}` wrapper), so check `err` and use the value
directly.

```go
package main

import (
    "fmt"
    "os"
    sdk "github.com/voxgig-sdk/free-music-sdk/go"
)

func main() {
    client := sdk.NewFreeMusicSDK(map[string]any{
        "apikey": os.Getenv("FREE_MUSIC_APIKEY"),
    })

    // List v1list records — the value is the array of records itself.
    v1lists, err := client.V1List(nil).List(nil, nil)
    if err != nil {
        panic(err)
    }
    for _, item := range v1lists.([]any) {
        fmt.Println(item)
    }

    // Load a single v1list — the value is the loaded record.
    v1list, err := client.V1List(nil).Load(nil, nil)
    if err != nil {
        panic(err)
    }
    fmt.Println(v1list)
}
```


## Error handling

Every entity operation returns `(value, error)`. Check `err` before
using the value — there is no exception to catch:

```go
v1lists, err := client.V1List(nil).List(nil, nil)
if err != nil {
    // handle err
    return
}
_ = v1lists
```

`Direct` follows the same `(value, error)` convention:

```go
result, err := client.Direct(map[string]any{
    "path":   "/api/resource/{id}",
    "method": "GET",
    "params": map[string]any{"id": "example_id"},
})
if err != nil {
    // handle err
}
_ = result
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```go
result, err := client.Direct(map[string]any{
    "path":   "/api/resource/{id}",
    "method": "GET",
    "params": map[string]any{"id": "example"},
})
if err != nil {
    panic(err)
}

if result["ok"] == true {
    fmt.Println(result["status"]) // 200
    fmt.Println(result["data"])   // response body
}
```

### Prepare a request without sending it

```go
fetchdef, err := client.Prepare(map[string]any{
    "path":   "/api/resource/{id}",
    "method": "DELETE",
    "params": map[string]any{"id": "example"},
})
if err != nil {
    panic(err)
}

fmt.Println(fetchdef["url"])
fmt.Println(fetchdef["method"])
fmt.Println(fetchdef["headers"])
```

### Use test mode

Create a mock client for unit testing — no server required:

```go
client := sdk.Test()

v1list, err := client.V1List(nil).List(
    nil, nil,
)
if err != nil {
    panic(err)
}
fmt.Println(v1list) // the returned mock data
```

### Use a custom fetch function

Replace the HTTP transport with your own function:

```go
mockFetch := func(url string, init map[string]any) (map[string]any, error) {
    return map[string]any{
        "status":     200,
        "statusText": "OK",
        "headers":    map[string]any{},
        "json": (func() any)(func() any {
            return map[string]any{"id": "mock01"}
        }),
    }, nil
}

client := sdk.NewFreeMusicSDK(map[string]any{
    "base": "http://localhost:8080",
    "system": map[string]any{
        "fetch": (func(string, map[string]any) (map[string]any, error))(mockFetch),
    },
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
cd go && go test ./test/...
```


## Reference

### NewFreeMusicSDK

```go
func NewFreeMusicSDK(options map[string]any) *FreeMusicSDK
```

Creates a new SDK client.

| Option | Type | Description |
| --- | --- | --- |
| `"apikey"` | `string` | API key for authentication. |
| `"base"` | `string` | Base URL of the API server. |
| `"prefix"` | `string` | URL path prefix prepended to all requests. |
| `"suffix"` | `string` | URL path suffix appended to all requests. |
| `"feature"` | `map[string]any` | Feature activation flags. |
| `"extend"` | `[]any` | Additional Feature instances to load. |
| `"system"` | `map[string]any` | System overrides (e.g. custom `"fetch"` function). |

### TestSDK

```go
func TestSDK(testopts map[string]any, sdkopts map[string]any) *FreeMusicSDK
```

Creates a test-mode client with mock transport. Both arguments may be `nil`.

### FreeMusicSDK methods

| Method | Signature | Description |
| --- | --- | --- |
| `OptionsMap` | `() map[string]any` | Deep copy of current SDK options. |
| `GetUtility` | `() *Utility` | Copy of the SDK utility object. |
| `Prepare` | `(fetchargs map[string]any) (map[string]any, error)` | Build an HTTP request definition without sending. |
| `Direct` | `(fetchargs map[string]any) (map[string]any, error)` | Build and send an HTTP request. |
| `V1List` | `(data map[string]any) FreeMusicEntity` | Create a V1List entity instance. |
| `V1Lookup` | `(data map[string]any) FreeMusicEntity` | Create a V1Lookup entity instance. |
| `V1Search` | `(data map[string]any) FreeMusicEntity` | Create a V1Search entity instance. |
| `V2List` | `(data map[string]any) FreeMusicEntity` | Create a V2List entity instance. |
| `V2Lookup` | `(data map[string]any) FreeMusicEntity` | Create a V2Lookup entity instance. |
| `V2Search` | `(data map[string]any) FreeMusicEntity` | Create a V2Search entity instance. |

### Entity interface (FreeMusicEntity)

All entities implement the `FreeMusicEntity` interface.

| Method | Signature | Description |
| --- | --- | --- |
| `Load` | `(reqmatch, ctrl map[string]any) (any, error)` | Load a single entity by match criteria. |
| `List` | `(reqmatch, ctrl map[string]any) (any, error)` | List entities matching the criteria. |
| `Data` | `(args ...any) any` | Get or set entity data. |
| `Match` | `(args ...any) any` | Get or set entity match criteria. |
| `Make` | `() Entity` | Create a new instance with the same options. |
| `GetName` | `() string` | Return the entity name. |

### Result shape

Entity operations return `(value, error)`. The `value` is the
operation's data **directly** — there is no wrapper:

| Operation | `value` |
| --- | --- |
| `Load` | the entity record (`map[string]any`) |
| `List` | a `[]any` of entity records |

Check `err` first, then use the value directly (or the typed
`...Typed` variants, which return the entity's model struct and a typed
slice):

    v1list, err := client.V1List(nil).List(map[string]any{/* fields */}, nil)
    if err != nil { /* handle */ }
    // v1list is the returned record

Only `Direct()` returns a response envelope — a `map[string]any` with
`"ok"`, `"status"`, `"headers"`, and `"data"` keys.

### Entities

#### V1List

| Field | Description |
| --- | --- |
| `"id_album"` |  |
| `"id_artist"` |  |
| `"id_imvdb"` |  |
| `"id_lyric"` |  |
| `"id_track"` |  |
| `"int_cd"` |  |
| `"int_duration"` |  |
| `"int_loved"` |  |
| `"int_music_vid_comment"` |  |
| `"int_music_vid_dislike"` |  |
| `"int_music_vid_favorite"` |  |
| `"int_music_vid_like"` |  |
| `"int_music_vid_view"` |  |
| `"int_score"` |  |
| `"int_score_vote"` |  |
| `"int_total_listener"` |  |
| `"int_total_play"` |  |
| `"int_track_number"` |  |
| `"str_album"` |  |
| `"str_artist"` |  |
| `"str_artist_alternate"` |  |
| `"str_description_en"` |  |
| `"str_genre"` |  |
| `"str_locked"` |  |
| `"str_mood"` |  |
| `"str_music_brainz_album_id"` |  |
| `"str_music_brainz_artist_id"` |  |
| `"str_music_brainz_id"` |  |
| `"str_music_vid"` |  |
| `"str_music_vid_company"` |  |
| `"str_music_vid_director"` |  |
| `"str_music_vid_screen1"` |  |
| `"str_music_vid_screen2"` |  |
| `"str_music_vid_screen3"` |  |
| `"str_style"` |  |
| `"str_theme"` |  |
| `"str_track"` |  |
| `"str_track3x3"` |  |
| `"str_track_lyric"` |  |
| `"str_track_thumb"` |  |
| `"trending"` |  |

Operations: List, Load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `"id_album"` |  |
| `"id_artist"` |  |
| `"id_imvdb"` |  |
| `"id_label"` |  |
| `"id_lyric"` |  |
| `"id_track"` |  |
| `"int_born_year"` |  |
| `"int_cd"` |  |
| `"int_charted"` |  |
| `"int_died_year"` |  |
| `"int_duration"` |  |
| `"int_formed_year"` |  |
| `"int_loved"` |  |
| `"int_member"` |  |
| `"int_music_vid_comment"` |  |
| `"int_music_vid_dislike"` |  |
| `"int_music_vid_favorite"` |  |
| `"int_music_vid_like"` |  |
| `"int_music_vid_view"` |  |
| `"int_sale"` |  |
| `"int_score"` |  |
| `"int_score_vote"` |  |
| `"int_total_listener"` |  |
| `"int_total_play"` |  |
| `"int_track_number"` |  |
| `"int_year_released"` |  |
| `"str_album"` |  |
| `"str_album3_d_case"` |  |
| `"str_album3_d_face"` |  |
| `"str_album3_d_flat"` |  |
| `"str_album3_d_thumb"` |  |
| `"str_album_c_dart"` |  |
| `"str_album_spine"` |  |
| `"str_album_stripped"` |  |
| `"str_album_thumb"` |  |
| `"str_album_thumb_back"` |  |
| `"str_album_thumb_hq"` |  |
| `"str_all_music_id"` |  |
| `"str_amazon_id"` |  |
| `"str_artist"` |  |
| `"str_artist_alternate"` |  |
| `"str_artist_banner"` |  |
| `"str_artist_clearart"` |  |
| `"str_artist_cutout"` |  |
| `"str_artist_fanart"` |  |
| `"str_artist_fanart2"` |  |
| `"str_artist_fanart3"` |  |
| `"str_artist_fanart4"` |  |
| `"str_artist_logo"` |  |
| `"str_artist_stripped"` |  |
| `"str_artist_thumb"` |  |
| `"str_artist_wide_thumb"` |  |
| `"str_bbc_review_id"` |  |
| `"str_biography_en"` |  |
| `"str_country"` |  |
| `"str_country_code"` |  |
| `"str_description_en"` |  |
| `"str_disbanded"` |  |
| `"str_discogs_id"` |  |
| `"str_facebook"` |  |
| `"str_gender"` |  |
| `"str_genius_id"` |  |
| `"str_genre"` |  |
| `"str_isn_icode"` |  |
| `"str_itunes_id"` |  |
| `"str_label"` |  |
| `"str_last_fm_chart"` |  |
| `"str_location"` |  |
| `"str_locked"` |  |
| `"str_lyric_wiki_id"` |  |
| `"str_mood"` |  |
| `"str_music_brainz_album_id"` |  |
| `"str_music_brainz_artist_id"` |  |
| `"str_music_brainz_id"` |  |
| `"str_music_moz_id"` |  |
| `"str_music_vid"` |  |
| `"str_music_vid_company"` |  |
| `"str_music_vid_director"` |  |
| `"str_music_vid_screen1"` |  |
| `"str_music_vid_screen2"` |  |
| `"str_music_vid_screen3"` |  |
| `"str_rate_your_music_id"` |  |
| `"str_release_format"` |  |
| `"str_review"` |  |
| `"str_speed"` |  |
| `"str_style"` |  |
| `"str_theme"` |  |
| `"str_track"` |  |
| `"str_track3x3"` |  |
| `"str_track_lyric"` |  |
| `"str_track_thumb"` |  |
| `"str_twitter"` |  |
| `"str_website"` |  |
| `"str_wikidata_id"` |  |
| `"str_wikipedia_id"` |  |

Operations: List, Load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `"album"` |  |
| `"id_album"` |  |
| `"id_artist"` |  |
| `"id_imvdb"` |  |
| `"id_label"` |  |
| `"id_lyric"` |  |
| `"id_track"` |  |
| `"int_born_year"` |  |
| `"int_cd"` |  |
| `"int_charted"` |  |
| `"int_died_year"` |  |
| `"int_duration"` |  |
| `"int_formed_year"` |  |
| `"int_loved"` |  |
| `"int_member"` |  |
| `"int_music_vid_comment"` |  |
| `"int_music_vid_dislike"` |  |
| `"int_music_vid_favorite"` |  |
| `"int_music_vid_like"` |  |
| `"int_music_vid_view"` |  |
| `"int_sale"` |  |
| `"int_score"` |  |
| `"int_score_vote"` |  |
| `"int_total_listener"` |  |
| `"int_total_play"` |  |
| `"int_track_number"` |  |
| `"int_year_released"` |  |
| `"str_album"` |  |
| `"str_album3_d_case"` |  |
| `"str_album3_d_face"` |  |
| `"str_album3_d_flat"` |  |
| `"str_album3_d_thumb"` |  |
| `"str_album_c_dart"` |  |
| `"str_album_spine"` |  |
| `"str_album_stripped"` |  |
| `"str_album_thumb"` |  |
| `"str_album_thumb_back"` |  |
| `"str_album_thumb_hq"` |  |
| `"str_all_music_id"` |  |
| `"str_amazon_id"` |  |
| `"str_artist"` |  |
| `"str_artist_alternate"` |  |
| `"str_artist_banner"` |  |
| `"str_artist_clearart"` |  |
| `"str_artist_cutout"` |  |
| `"str_artist_fanart"` |  |
| `"str_artist_fanart2"` |  |
| `"str_artist_fanart3"` |  |
| `"str_artist_fanart4"` |  |
| `"str_artist_logo"` |  |
| `"str_artist_stripped"` |  |
| `"str_artist_thumb"` |  |
| `"str_artist_wide_thumb"` |  |
| `"str_bbc_review_id"` |  |
| `"str_biography_en"` |  |
| `"str_country"` |  |
| `"str_country_code"` |  |
| `"str_description_en"` |  |
| `"str_disbanded"` |  |
| `"str_discogs_id"` |  |
| `"str_facebook"` |  |
| `"str_gender"` |  |
| `"str_genius_id"` |  |
| `"str_genre"` |  |
| `"str_isn_icode"` |  |
| `"str_itunes_id"` |  |
| `"str_label"` |  |
| `"str_last_fm_chart"` |  |
| `"str_location"` |  |
| `"str_locked"` |  |
| `"str_lyric_wiki_id"` |  |
| `"str_mood"` |  |
| `"str_music_brainz_album_id"` |  |
| `"str_music_brainz_artist_id"` |  |
| `"str_music_brainz_id"` |  |
| `"str_music_moz_id"` |  |
| `"str_music_vid"` |  |
| `"str_music_vid_company"` |  |
| `"str_music_vid_director"` |  |
| `"str_music_vid_screen1"` |  |
| `"str_music_vid_screen2"` |  |
| `"str_music_vid_screen3"` |  |
| `"str_rate_your_music_id"` |  |
| `"str_release_format"` |  |
| `"str_review"` |  |
| `"str_speed"` |  |
| `"str_style"` |  |
| `"str_theme"` |  |
| `"str_track"` |  |
| `"str_track3x3"` |  |
| `"str_track_lyric"` |  |
| `"str_track_thumb"` |  |
| `"str_twitter"` |  |
| `"str_website"` |  |
| `"str_wikidata_id"` |  |
| `"str_wikipedia_id"` |  |

Operations: List, Load.

API path: `/{apiKey}/searchalbum.php`

#### V2List

| Field | Description |
| --- | --- |
| `"album"` |  |

Operations: Load.

API path: `/list/discography/{idArtist}`

#### V2Lookup

| Field | Description |
| --- | --- |
| `"album"` |  |
| `"artist"` |  |
| `"track"` |  |

Operations: Load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `"album"` |  |
| `"artist"` |  |
| `"track"` |  |

Operations: Load.

API path: `/search/album/{albumName}`



## Entities


### V1List

Create an instance: `v1_list := client.V1List(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `id_album` | `string` |  |
| `id_artist` | `string` |  |
| `id_imvdb` | `string` |  |
| `id_lyric` | `string` |  |
| `id_track` | `string` |  |
| `int_cd` | `string` |  |
| `int_duration` | `string` |  |
| `int_loved` | `string` |  |
| `int_music_vid_comment` | `string` |  |
| `int_music_vid_dislike` | `string` |  |
| `int_music_vid_favorite` | `string` |  |
| `int_music_vid_like` | `string` |  |
| `int_music_vid_view` | `string` |  |
| `int_score` | `string` |  |
| `int_score_vote` | `string` |  |
| `int_total_listener` | `string` |  |
| `int_total_play` | `string` |  |
| `int_track_number` | `string` |  |
| `str_album` | `string` |  |
| `str_artist` | `string` |  |
| `str_artist_alternate` | `string` |  |
| `str_description_en` | `string` |  |
| `str_genre` | `string` |  |
| `str_locked` | `string` |  |
| `str_mood` | `string` |  |
| `str_music_brainz_album_id` | `string` |  |
| `str_music_brainz_artist_id` | `string` |  |
| `str_music_brainz_id` | `string` |  |
| `str_music_vid` | `string` |  |
| `str_music_vid_company` | `string` |  |
| `str_music_vid_director` | `string` |  |
| `str_music_vid_screen1` | `string` |  |
| `str_music_vid_screen2` | `string` |  |
| `str_music_vid_screen3` | `string` |  |
| `str_style` | `string` |  |
| `str_theme` | `string` |  |
| `str_track` | `string` |  |
| `str_track3x3` | `string` |  |
| `str_track_lyric` | `string` |  |
| `str_track_thumb` | `string` |  |
| `trending` | `[]any` |  |

#### Example: Load

```go
v1_list, err := client.V1List(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_list) // the loaded record
```

#### Example: List

```go
v1_lists, err := client.V1List(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_lists) // the array of records
```


### V1Lookup

Create an instance: `v1_lookup := client.V1Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `id_album` | `string` |  |
| `id_artist` | `string` |  |
| `id_imvdb` | `string` |  |
| `id_label` | `string` |  |
| `id_lyric` | `string` |  |
| `id_track` | `string` |  |
| `int_born_year` | `string` |  |
| `int_cd` | `string` |  |
| `int_charted` | `string` |  |
| `int_died_year` | `string` |  |
| `int_duration` | `string` |  |
| `int_formed_year` | `string` |  |
| `int_loved` | `string` |  |
| `int_member` | `string` |  |
| `int_music_vid_comment` | `string` |  |
| `int_music_vid_dislike` | `string` |  |
| `int_music_vid_favorite` | `string` |  |
| `int_music_vid_like` | `string` |  |
| `int_music_vid_view` | `string` |  |
| `int_sale` | `string` |  |
| `int_score` | `string` |  |
| `int_score_vote` | `string` |  |
| `int_total_listener` | `string` |  |
| `int_total_play` | `string` |  |
| `int_track_number` | `string` |  |
| `int_year_released` | `string` |  |
| `str_album` | `string` |  |
| `str_album3_d_case` | `string` |  |
| `str_album3_d_face` | `string` |  |
| `str_album3_d_flat` | `string` |  |
| `str_album3_d_thumb` | `string` |  |
| `str_album_c_dart` | `string` |  |
| `str_album_spine` | `string` |  |
| `str_album_stripped` | `string` |  |
| `str_album_thumb` | `string` |  |
| `str_album_thumb_back` | `string` |  |
| `str_album_thumb_hq` | `string` |  |
| `str_all_music_id` | `string` |  |
| `str_amazon_id` | `string` |  |
| `str_artist` | `string` |  |
| `str_artist_alternate` | `string` |  |
| `str_artist_banner` | `string` |  |
| `str_artist_clearart` | `string` |  |
| `str_artist_cutout` | `string` |  |
| `str_artist_fanart` | `string` |  |
| `str_artist_fanart2` | `string` |  |
| `str_artist_fanart3` | `string` |  |
| `str_artist_fanart4` | `string` |  |
| `str_artist_logo` | `string` |  |
| `str_artist_stripped` | `string` |  |
| `str_artist_thumb` | `string` |  |
| `str_artist_wide_thumb` | `string` |  |
| `str_bbc_review_id` | `string` |  |
| `str_biography_en` | `string` |  |
| `str_country` | `string` |  |
| `str_country_code` | `string` |  |
| `str_description_en` | `string` |  |
| `str_disbanded` | `string` |  |
| `str_discogs_id` | `string` |  |
| `str_facebook` | `string` |  |
| `str_gender` | `string` |  |
| `str_genius_id` | `string` |  |
| `str_genre` | `string` |  |
| `str_isn_icode` | `string` |  |
| `str_itunes_id` | `string` |  |
| `str_label` | `string` |  |
| `str_last_fm_chart` | `string` |  |
| `str_location` | `string` |  |
| `str_locked` | `string` |  |
| `str_lyric_wiki_id` | `string` |  |
| `str_mood` | `string` |  |
| `str_music_brainz_album_id` | `string` |  |
| `str_music_brainz_artist_id` | `string` |  |
| `str_music_brainz_id` | `string` |  |
| `str_music_moz_id` | `string` |  |
| `str_music_vid` | `string` |  |
| `str_music_vid_company` | `string` |  |
| `str_music_vid_director` | `string` |  |
| `str_music_vid_screen1` | `string` |  |
| `str_music_vid_screen2` | `string` |  |
| `str_music_vid_screen3` | `string` |  |
| `str_rate_your_music_id` | `string` |  |
| `str_release_format` | `string` |  |
| `str_review` | `string` |  |
| `str_speed` | `string` |  |
| `str_style` | `string` |  |
| `str_theme` | `string` |  |
| `str_track` | `string` |  |
| `str_track3x3` | `string` |  |
| `str_track_lyric` | `string` |  |
| `str_track_thumb` | `string` |  |
| `str_twitter` | `string` |  |
| `str_website` | `string` |  |
| `str_wikidata_id` | `string` |  |
| `str_wikipedia_id` | `string` |  |

#### Example: Load

```go
v1_lookup, err := client.V1Lookup(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_lookup) // the loaded record
```

#### Example: List

```go
v1_lookups, err := client.V1Lookup(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_lookups) // the array of records
```


### V1Search

Create an instance: `v1_search := client.V1Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `id_album` | `string` |  |
| `id_artist` | `string` |  |
| `id_imvdb` | `string` |  |
| `id_label` | `string` |  |
| `id_lyric` | `string` |  |
| `id_track` | `string` |  |
| `int_born_year` | `string` |  |
| `int_cd` | `string` |  |
| `int_charted` | `string` |  |
| `int_died_year` | `string` |  |
| `int_duration` | `string` |  |
| `int_formed_year` | `string` |  |
| `int_loved` | `string` |  |
| `int_member` | `string` |  |
| `int_music_vid_comment` | `string` |  |
| `int_music_vid_dislike` | `string` |  |
| `int_music_vid_favorite` | `string` |  |
| `int_music_vid_like` | `string` |  |
| `int_music_vid_view` | `string` |  |
| `int_sale` | `string` |  |
| `int_score` | `string` |  |
| `int_score_vote` | `string` |  |
| `int_total_listener` | `string` |  |
| `int_total_play` | `string` |  |
| `int_track_number` | `string` |  |
| `int_year_released` | `string` |  |
| `str_album` | `string` |  |
| `str_album3_d_case` | `string` |  |
| `str_album3_d_face` | `string` |  |
| `str_album3_d_flat` | `string` |  |
| `str_album3_d_thumb` | `string` |  |
| `str_album_c_dart` | `string` |  |
| `str_album_spine` | `string` |  |
| `str_album_stripped` | `string` |  |
| `str_album_thumb` | `string` |  |
| `str_album_thumb_back` | `string` |  |
| `str_album_thumb_hq` | `string` |  |
| `str_all_music_id` | `string` |  |
| `str_amazon_id` | `string` |  |
| `str_artist` | `string` |  |
| `str_artist_alternate` | `string` |  |
| `str_artist_banner` | `string` |  |
| `str_artist_clearart` | `string` |  |
| `str_artist_cutout` | `string` |  |
| `str_artist_fanart` | `string` |  |
| `str_artist_fanart2` | `string` |  |
| `str_artist_fanart3` | `string` |  |
| `str_artist_fanart4` | `string` |  |
| `str_artist_logo` | `string` |  |
| `str_artist_stripped` | `string` |  |
| `str_artist_thumb` | `string` |  |
| `str_artist_wide_thumb` | `string` |  |
| `str_bbc_review_id` | `string` |  |
| `str_biography_en` | `string` |  |
| `str_country` | `string` |  |
| `str_country_code` | `string` |  |
| `str_description_en` | `string` |  |
| `str_disbanded` | `string` |  |
| `str_discogs_id` | `string` |  |
| `str_facebook` | `string` |  |
| `str_gender` | `string` |  |
| `str_genius_id` | `string` |  |
| `str_genre` | `string` |  |
| `str_isn_icode` | `string` |  |
| `str_itunes_id` | `string` |  |
| `str_label` | `string` |  |
| `str_last_fm_chart` | `string` |  |
| `str_location` | `string` |  |
| `str_locked` | `string` |  |
| `str_lyric_wiki_id` | `string` |  |
| `str_mood` | `string` |  |
| `str_music_brainz_album_id` | `string` |  |
| `str_music_brainz_artist_id` | `string` |  |
| `str_music_brainz_id` | `string` |  |
| `str_music_moz_id` | `string` |  |
| `str_music_vid` | `string` |  |
| `str_music_vid_company` | `string` |  |
| `str_music_vid_director` | `string` |  |
| `str_music_vid_screen1` | `string` |  |
| `str_music_vid_screen2` | `string` |  |
| `str_music_vid_screen3` | `string` |  |
| `str_rate_your_music_id` | `string` |  |
| `str_release_format` | `string` |  |
| `str_review` | `string` |  |
| `str_speed` | `string` |  |
| `str_style` | `string` |  |
| `str_theme` | `string` |  |
| `str_track` | `string` |  |
| `str_track3x3` | `string` |  |
| `str_track_lyric` | `string` |  |
| `str_track_thumb` | `string` |  |
| `str_twitter` | `string` |  |
| `str_website` | `string` |  |
| `str_wikidata_id` | `string` |  |
| `str_wikipedia_id` | `string` |  |

#### Example: Load

```go
v1_search, err := client.V1Search(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_search) // the loaded record
```

#### Example: List

```go
v1_searchs, err := client.V1Search(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1_searchs) // the array of records
```


### V2List

Create an instance: `v2_list := client.V2List(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |

#### Example: Load

```go
v2_list, err := client.V2List(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2_list) // the loaded record
```


### V2Lookup

Create an instance: `v2_lookup := client.V2Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `artist` | `[]any` |  |
| `track` | `[]any` |  |

#### Example: Load

```go
v2_lookup, err := client.V2Lookup(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2_lookup) // the loaded record
```


### V2Search

Create an instance: `v2_search := client.V2Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `artist` | `[]any` |  |
| `track` | `[]any` |  |

#### Example: Load

```go
v2_search, err := client.V2Search(nil).Load(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2_search) // the loaded record
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

Features are the extension mechanism. A feature implements the
`Feature` interface and provides hooks — functions keyed by pipeline
stage names.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Data as maps

The Go SDK uses `map[string]any` throughout rather than typed structs.
This mirrors the dynamic nature of the API and keeps the SDK
flexible — no code generation is needed when the API schema changes.

Use `core.ToMapAny()` to safely cast results and nested data.

### Package structure

```
github.com/voxgig-sdk/free-music-sdk/go/
├── free-music.go        # Root package — type aliases and constructors
├── core/               # SDK core — client, types, pipeline
├── entity/             # Entity implementations
├── feature/            # Built-in features (Base, Test, Log)
├── utility/            # Utility functions and struct library
└── test/               # Test suites
```

The root package (`github.com/voxgig-sdk/free-music-sdk/go`) re-exports everything needed
for normal use. Import sub-packages only when you need specific types
like `core.ToMapAny`.

### Entity state

Entity instances are stateful. After a successful `List`, the entity
stores the returned data and match criteria internally.

```go
v1list := client.V1List(nil)
v1list.List(nil, nil)

// v1list.Data() now returns the v1list data from the last list
// v1list.Match() returns the last match criteria
```

Call `Make()` to create a fresh instance with the same configuration
but no stored state.

### Direct vs entity access

The entity interface handles URL construction, parameter placement,
and response parsing automatically. Use it for standard CRUD operations.

`Direct()` gives full control over the HTTP request. Use it for
non-standard endpoints, bulk operations, or any path not modelled as
an entity. `Prepare()` builds the request without sending it — useful
for debugging or custom transport.


## Full Reference

See [REFERENCE.md](REFERENCE.md) for complete API reference
documentation including all method signatures, entity field schemas,
and detailed usage examples.
