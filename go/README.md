# FreeMusic Golang SDK



The Golang SDK for the FreeMusic API — an entity-oriented client using standard Go conventions. No generics required; data flows as `map[string]any`.

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

### 1. Create a client

```go
package main

import (
    "fmt"
    "os"

    sdk "github.com/voxgig-sdk/free-music-sdk/go"
    "github.com/voxgig-sdk/free-music-sdk/go/core"
)

func main() {
    client := sdk.NewFreeMusicSDK(map[string]any{
        "apikey": os.Getenv("FREE_MUSIC_APIKEY"),
    })
```

### 2. List v1lists

```go
    result, err := client.V1List(nil).List(nil, nil)
    if err != nil {
        panic(err)
    }

    rm := core.ToMapAny(result)
    if rm["ok"] == true {
        for _, item := range rm["data"].([]any) {
            p := core.ToMapAny(item)
            fmt.Println(p["id"], p["name"])
        }
    }
```

### 3. Load a v1list

```go
    result, err = client.V1List(nil).Load(
        map[string]any{"id": "example_id"}, nil,
    )
    if err != nil {
        panic(err)
    }

    rm = core.ToMapAny(result)
    if rm["ok"] == true {
        fmt.Println(rm["data"])
    }
}
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

result, err := client.V1List(nil).Load(
    map[string]any{"id": "test01"}, nil,
)
// result contains mock response data
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
| `Create` | `(reqdata, ctrl map[string]any) (any, error)` | Create a new entity. |
| `Update` | `(reqdata, ctrl map[string]any) (any, error)` | Update an existing entity. |
| `Remove` | `(reqmatch, ctrl map[string]any) (any, error)` | Remove an entity. |
| `Data` | `(args ...any) any` | Get or set entity data. |
| `Match` | `(args ...any) any` | Get or set entity match criteria. |
| `Make` | `() Entity` | Create a new instance with the same options. |
| `GetName` | `() string` | Return the entity name. |

### Result shape

Entity operations return `(any, error)`. The `any` value is a
`map[string]any` with these keys:

| Key | Type | Description |
| --- | --- | --- |
| `"ok"` | `bool` | `true` if the HTTP status is 2xx. |
| `"status"` | `int` | HTTP status code. |
| `"headers"` | `map[string]any` | Response headers. |
| `"data"` | `any` | Parsed JSON response body. |

On error, `"ok"` is `false` and `"err"` contains the error value.

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

```go
result, err := client.V1List(nil).Load(map[string]any{"id": "v1_list_id"}, nil)
```

#### Example: List

```go
results, err := client.V1List(nil).List(nil, nil)
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

```go
result, err := client.V1Lookup(nil).Load(map[string]any{"id": "v1_lookup_id"}, nil)
```

#### Example: List

```go
results, err := client.V1Lookup(nil).List(nil, nil)
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

```go
result, err := client.V1Search(nil).Load(map[string]any{"id": "v1_search_id"}, nil)
```

#### Example: List

```go
results, err := client.V1Search(nil).List(nil, nil)
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
| `album` | ``$ARRAY`` |  |

#### Example: Load

```go
result, err := client.V2List(nil).Load(map[string]any{"id": "v2_list_id"}, nil)
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
| `album` | ``$ARRAY`` |  |
| `artist` | ``$ARRAY`` |  |
| `track` | ``$ARRAY`` |  |

#### Example: Load

```go
result, err := client.V2Lookup(nil).Load(map[string]any{"id": "v2_lookup_id"}, nil)
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
| `album` | ``$ARRAY`` |  |
| `artist` | ``$ARRAY`` |  |
| `track` | ``$ARRAY`` |  |

#### Example: Load

```go
result, err := client.V2Search(nil).Load(map[string]any{"id": "v2_search_id"}, nil)
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
error is returned to the caller. An unexpected panic triggers the
`PreUnexpected` hook.

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

Entity instances are stateful. After a successful `Load`, the entity
stores the returned data and match criteria internally.

```go
v1list := client.V1List(nil)
v1list.Load(map[string]any{"id": "example_id"}, nil)

// v1list.Data() now returns the loaded v1list data
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
