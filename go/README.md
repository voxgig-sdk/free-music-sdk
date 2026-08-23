# FreeMusic Golang SDK



The Golang SDK for the FreeMusic API — an entity-oriented client using standard Go conventions. No generics required; data flows as `map[string]any`.

It exposes the API as capitalised, semantic **Entities** — e.g. `client.V1List(nil)` — each with the same small set of operations (`List`, `Load`) instead of raw URL paths and query strings. You call meaning, not endpoints, which keeps the cognitive load low.

> Also generated from this model: `go-cli`, `go-mcp`, `lua`, `php`, `py`, `rb`, `ts` — see
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

    // List v1List records — the value is the array of records itself.
    v1Lists, err := client.V1List(nil).List(nil, nil)
    if err != nil {
        panic(err)
    }
    for _, item := range v1Lists.([]any) {
        fmt.Println(item)
    }

    // Load a single v1List — the value is the loaded record.
    v1List, err := client.V1List(nil).Load(map[string]any{"api_key": "example_api_key"}, nil)
    if err != nil {
        panic(err)
    }
    fmt.Println(v1List)
}
```


## Error handling

Every entity operation returns `(value, error)`. Check `err` before
using the value — there is no exception to catch:

```go
v2lookup, err := client.V2Lookup(nil).Load(map[string]any{"id_album": 1}, nil)
if err != nil {
    // handle err
    return
}
_ = v2lookup
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

v2Lookup, err := client.V2Lookup(nil).Load(
    map[string]any{"id_album": 1}, nil,
)
if err != nil {
    panic(err)
}
fmt.Println(v2Lookup) // the returned mock data
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

    v1List, err := client.V1List(nil).List(map[string]any{/* fields */}, nil)
    if err != nil { /* handle */ }
    // v1List is the returned record

Only `Direct()` returns a response envelope — a `map[string]any` with
`"ok"`, `"status"`, `"headers"`, and `"data"` keys.

### Entities

#### V1List

| Field | Description |
| --- | --- |
| `"idAlbum"` | Album ID |
| `"idArtist"` | Artist ID |
| `"idIMVDB"` | IMVDB ID |
| `"idLyric"` | Lyrics ID |
| `"idTrack"` | Unique track ID |
| `"intCD"` | CD number |
| `"intDuration"` | Track duration in milliseconds |
| `"intLoved"` | Number of loves/likes |
| `"intMusicVidComments"` | Music video comment count |
| `"intMusicVidDislikes"` | Music video dislike count |
| `"intMusicVidFavorites"` | Music video favorite count |
| `"intMusicVidLikes"` | Music video like count |
| `"intMusicVidViews"` | Music video view count |
| `"intScore"` | Track score/rating |
| `"intScoreVotes"` | Number of score votes |
| `"intTotalListeners"` | Total listener count |
| `"intTotalPlays"` | Total play count |
| `"intTrackNumber"` | Track number on album |
| `"strAlbum"` | Album name |
| `"strArtist"` | Artist name |
| `"strArtistAlternate"` | Alternative artist name |
| `"strDescriptionEN"` | Track description in English |
| `"strGenre"` | Musical genre |
| `"strLocked"` | Lock status |
| `"strMood"` | Track mood |
| `"strMusicBrainzAlbumID"` | MusicBrainz Album ID |
| `"strMusicBrainzArtistID"` | MusicBrainz Artist ID |
| `"strMusicBrainzID"` | MusicBrainz Recording ID |
| `"strMusicVid"` | Music video URL |
| `"strMusicVidCompany"` | Music video production company |
| `"strMusicVidDirector"` | Music video director |
| `"strMusicVidScreen1"` | Music video screenshot 1 |
| `"strMusicVidScreen2"` | Music video screenshot 2 |
| `"strMusicVidScreen3"` | Music video screenshot 3 |
| `"strStyle"` | Musical style |
| `"strTheme"` | Track theme |
| `"strTrack"` | Track name |
| `"strTrack3x3"` | 3x3 track image URL |
| `"strTrackLyrics"` | Track lyrics |
| `"strTrackThumb"` | Track thumbnail URL |
| `"trending"` |  |

Operations: List, Load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `"idAlbum"` | Album ID |
| `"idArtist"` | Artist ID |
| `"idIMVDB"` | IMVDB ID |
| `"idLabel"` | Label ID |
| `"idLyric"` | Lyrics ID |
| `"idTrack"` | Unique track ID |
| `"intBornYear"` | Birth year (for solo artists) |
| `"intCD"` | CD number |
| `"intCharted"` | Chart position |
| `"intDiedYear"` | Death year (if applicable) |
| `"intDuration"` | Track duration in milliseconds |
| `"intFormedYear"` | Year the artist was formed |
| `"intLoved"` | Number of loves/likes |
| `"intMembers"` | Number of band members |
| `"intMusicVidComments"` | Music video comment count |
| `"intMusicVidDislikes"` | Music video dislike count |
| `"intMusicVidFavorites"` | Music video favorite count |
| `"intMusicVidLikes"` | Music video like count |
| `"intMusicVidViews"` | Music video view count |
| `"intSales"` | Sales figures |
| `"intScore"` | Track score/rating |
| `"intScoreVotes"` | Number of score votes |
| `"intTotalListeners"` | Total listener count |
| `"intTotalPlays"` | Total play count |
| `"intTrackNumber"` | Track number on album |
| `"intYearReleased"` | Release year |
| `"strAlbum"` | Album name |
| `"strAlbum3DCase"` | 3D case image URL |
| `"strAlbum3DFace"` | 3D face image URL |
| `"strAlbum3DFlat"` | 3D flat image URL |
| `"strAlbum3DThumb"` | 3D thumbnail URL |
| `"strAlbumCDart"` | CD art URL |
| `"strAlbumSpine"` | Album spine image URL |
| `"strAlbumStripped"` | Album name stripped of special characters |
| `"strAlbumThumb"` | Album thumbnail URL |
| `"strAlbumThumbBack"` | Album back cover URL |
| `"strAlbumThumbHQ"` | High quality album thumbnail URL |
| `"strAllMusicID"` | AllMusic ID |
| `"strAmazonID"` | Amazon ID |
| `"strArtist"` | Artist name |
| `"strArtistAlternate"` | Alternative artist name |
| `"strArtistBanner"` | Banner image URL |
| `"strArtistClearart"` | Clear art image URL |
| `"strArtistCutout"` | Cutout image URL |
| `"strArtistFanart"` | Fan art image URL |
| `"strArtistFanart2"` | Additional fan art image URL |
| `"strArtistFanart3"` | Additional fan art image URL |
| `"strArtistFanart4"` | Additional fan art image URL |
| `"strArtistLogo"` | Logo image URL |
| `"strArtistStripped"` | Artist name stripped |
| `"strArtistThumb"` | Thumbnail image URL |
| `"strArtistWideThumb"` | Wide thumbnail image URL |
| `"strBBCReviewID"` | BBC Review ID |
| `"strBiographyEN"` | Biography in English |
| `"strCountry"` | Country of origin |
| `"strCountryCode"` | Country code |
| `"strDescriptionEN"` | Track description in English |
| `"strDisbanded"` | Disbandment status |
| `"strDiscogsID"` | Discogs ID |
| `"strFacebook"` | Facebook URL |
| `"strGender"` | Gender |
| `"strGeniusID"` | Genius ID |
| `"strGenre"` | Musical genre |
| `"strISNIcode"` | ISNI code |
| `"strItunesID"` | iTunes ID |
| `"strLabel"` | Record label |
| `"strLastFMChart"` | Last.fm chart URL |
| `"strLocation"` | Recording location |
| `"strLocked"` | Lock status |
| `"strLyricWikiID"` | LyricWiki ID |
| `"strMood"` | Track mood |
| `"strMusicBrainzAlbumID"` | MusicBrainz Album ID |
| `"strMusicBrainzArtistID"` | MusicBrainz Artist ID |
| `"strMusicBrainzID"` | MusicBrainz Recording ID |
| `"strMusicMozID"` | MusicMoz ID |
| `"strMusicVid"` | Music video URL |
| `"strMusicVidCompany"` | Music video production company |
| `"strMusicVidDirector"` | Music video director |
| `"strMusicVidScreen1"` | Music video screenshot 1 |
| `"strMusicVidScreen2"` | Music video screenshot 2 |
| `"strMusicVidScreen3"` | Music video screenshot 3 |
| `"strRateYourMusicID"` | Rate Your Music ID |
| `"strReleaseFormat"` | Release format (CD, Vinyl, etc.) |
| `"strReview"` | Album review |
| `"strSpeed"` | Album speed/tempo |
| `"strStyle"` | Musical style |
| `"strTheme"` | Track theme |
| `"strTrack"` | Track name |
| `"strTrack3x3"` | 3x3 track image URL |
| `"strTrackLyrics"` | Track lyrics |
| `"strTrackThumb"` | Track thumbnail URL |
| `"strTwitter"` | Twitter handle |
| `"strWebsite"` | Official website URL |
| `"strWikidataID"` | Wikidata ID |
| `"strWikipediaID"` | Wikipedia ID |

Operations: List, Load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `"album"` |  |
| `"idAlbum"` | Unique album ID |
| `"idArtist"` | Artist ID |
| `"idIMVDB"` | IMVDB ID |
| `"idLabel"` | Label ID |
| `"idLyric"` | Lyrics ID |
| `"idTrack"` | Unique track ID |
| `"intBornYear"` | Birth year (for solo artists) |
| `"intCD"` | CD number |
| `"intCharted"` | Chart position |
| `"intDiedYear"` | Death year (if applicable) |
| `"intDuration"` | Track duration in milliseconds |
| `"intFormedYear"` | Year the artist was formed |
| `"intLoved"` | Number of loves/likes |
| `"intMembers"` | Number of band members |
| `"intMusicVidComments"` | Music video comment count |
| `"intMusicVidDislikes"` | Music video dislike count |
| `"intMusicVidFavorites"` | Music video favorite count |
| `"intMusicVidLikes"` | Music video like count |
| `"intMusicVidViews"` | Music video view count |
| `"intSales"` | Sales figures |
| `"intScore"` | Album score/rating |
| `"intScoreVotes"` | Number of score votes |
| `"intTotalListeners"` | Total listener count |
| `"intTotalPlays"` | Total play count |
| `"intTrackNumber"` | Track number on album |
| `"intYearReleased"` | Release year |
| `"strAlbum"` | Album name |
| `"strAlbum3DCase"` | 3D case image URL |
| `"strAlbum3DFace"` | 3D face image URL |
| `"strAlbum3DFlat"` | 3D flat image URL |
| `"strAlbum3DThumb"` | 3D thumbnail URL |
| `"strAlbumCDart"` | CD art URL |
| `"strAlbumSpine"` | Album spine image URL |
| `"strAlbumStripped"` | Album name stripped of special characters |
| `"strAlbumThumb"` | Album thumbnail URL |
| `"strAlbumThumbBack"` | Album back cover URL |
| `"strAlbumThumbHQ"` | High quality album thumbnail URL |
| `"strAllMusicID"` | AllMusic ID |
| `"strAmazonID"` | Amazon ID |
| `"strArtist"` | Artist name |
| `"strArtistAlternate"` | Alternative artist name |
| `"strArtistBanner"` | Banner image URL |
| `"strArtistClearart"` | Clear art image URL |
| `"strArtistCutout"` | Cutout image URL |
| `"strArtistFanart"` | Fan art image URL |
| `"strArtistFanart2"` | Additional fan art image URL |
| `"strArtistFanart3"` | Additional fan art image URL |
| `"strArtistFanart4"` | Additional fan art image URL |
| `"strArtistLogo"` | Logo image URL |
| `"strArtistStripped"` | Artist name stripped |
| `"strArtistThumb"` | Thumbnail image URL |
| `"strArtistWideThumb"` | Wide thumbnail image URL |
| `"strBBCReviewID"` | BBC Review ID |
| `"strBiographyEN"` | Biography in English |
| `"strCountry"` | Country of origin |
| `"strCountryCode"` | Country code |
| `"strDescriptionEN"` | Album description in English |
| `"strDisbanded"` | Disbandment status |
| `"strDiscogsID"` | Discogs ID |
| `"strFacebook"` | Facebook URL |
| `"strGender"` | Gender |
| `"strGeniusID"` | Genius ID |
| `"strGenre"` | Musical genre |
| `"strISNIcode"` | ISNI code |
| `"strItunesID"` | iTunes ID |
| `"strLabel"` | Record label |
| `"strLastFMChart"` | Last.fm chart URL |
| `"strLocation"` | Recording location |
| `"strLocked"` | Lock status |
| `"strLyricWikiID"` | LyricWiki ID |
| `"strMood"` | Album mood |
| `"strMusicBrainzAlbumID"` | MusicBrainz Album ID |
| `"strMusicBrainzArtistID"` | MusicBrainz Artist ID |
| `"strMusicBrainzID"` | MusicBrainz Release Group ID |
| `"strMusicMozID"` | MusicMoz ID |
| `"strMusicVid"` | Music video URL |
| `"strMusicVidCompany"` | Music video production company |
| `"strMusicVidDirector"` | Music video director |
| `"strMusicVidScreen1"` | Music video screenshot 1 |
| `"strMusicVidScreen2"` | Music video screenshot 2 |
| `"strMusicVidScreen3"` | Music video screenshot 3 |
| `"strRateYourMusicID"` | Rate Your Music ID |
| `"strReleaseFormat"` | Release format (CD, Vinyl, etc.) |
| `"strReview"` | Album review |
| `"strSpeed"` | Album speed/tempo |
| `"strStyle"` | Musical style |
| `"strTheme"` | Album theme |
| `"strTrack"` | Track name |
| `"strTrack3x3"` | 3x3 track image URL |
| `"strTrackLyrics"` | Track lyrics |
| `"strTrackThumb"` | Track thumbnail URL |
| `"strTwitter"` | Twitter handle |
| `"strWebsite"` | Official website URL |
| `"strWikidataID"` | Wikidata ID |
| `"strWikipediaID"` | Wikipedia ID |

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
| `"artists"` |  |
| `"track"` |  |

Operations: Load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `"album"` |  |
| `"artists"` |  |
| `"track"` |  |

Operations: Load.

API path: `/search/album/{albumName}`



## Entities


### V1List

Create an instance: `v1List := client.V1List(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `string` | Album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intCD` | `string` | CD number |
| `intDuration` | `string` | Track duration in milliseconds |
| `intLoved` | `string` | Number of loves/likes |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intScore` | `string` | Track score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `strAlbum` | `string` | Album name |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strDescriptionEN` | `string` | Track description in English |
| `strGenre` | `string` | Musical genre |
| `strLocked` | `string` | Lock status |
| `strMood` | `string` | Track mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Recording ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Track theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `trending` | `[]any` |  |

#### Example: Load

```go
v1List, err := client.V1List(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1List) // the loaded record
```

#### Example: List

```go
v1Lists, err := client.V1List(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1Lists) // the array of records
```


### V1Lookup

Create an instance: `v1Lookup := client.V1Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `string` | Album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLabel` | `string` | Label ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intBornYear` | `string` | Birth year (for solo artists) |
| `intCD` | `string` | CD number |
| `intCharted` | `string` | Chart position |
| `intDiedYear` | `string` | Death year (if applicable) |
| `intDuration` | `string` | Track duration in milliseconds |
| `intFormedYear` | `string` | Year the artist was formed |
| `intLoved` | `string` | Number of loves/likes |
| `intMembers` | `string` | Number of band members |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intSales` | `string` | Sales figures |
| `intScore` | `string` | Track score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `intYearReleased` | `string` | Release year |
| `strAlbum` | `string` | Album name |
| `strAlbum3DCase` | `string` | 3D case image URL |
| `strAlbum3DFace` | `string` | 3D face image URL |
| `strAlbum3DFlat` | `string` | 3D flat image URL |
| `strAlbum3DThumb` | `string` | 3D thumbnail URL |
| `strAlbumCDart` | `string` | CD art URL |
| `strAlbumSpine` | `string` | Album spine image URL |
| `strAlbumStripped` | `string` | Album name stripped of special characters |
| `strAlbumThumb` | `string` | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | Album back cover URL |
| `strAlbumThumbHQ` | `string` | High quality album thumbnail URL |
| `strAllMusicID` | `string` | AllMusic ID |
| `strAmazonID` | `string` | Amazon ID |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strArtistBanner` | `string` | Banner image URL |
| `strArtistClearart` | `string` | Clear art image URL |
| `strArtistCutout` | `string` | Cutout image URL |
| `strArtistFanart` | `string` | Fan art image URL |
| `strArtistFanart2` | `string` | Additional fan art image URL |
| `strArtistFanart3` | `string` | Additional fan art image URL |
| `strArtistFanart4` | `string` | Additional fan art image URL |
| `strArtistLogo` | `string` | Logo image URL |
| `strArtistStripped` | `string` | Artist name stripped |
| `strArtistThumb` | `string` | Thumbnail image URL |
| `strArtistWideThumb` | `string` | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | BBC Review ID |
| `strBiographyEN` | `string` | Biography in English |
| `strCountry` | `string` | Country of origin |
| `strCountryCode` | `string` | Country code |
| `strDescriptionEN` | `string` | Track description in English |
| `strDisbanded` | `string` | Disbandment status |
| `strDiscogsID` | `string` | Discogs ID |
| `strFacebook` | `string` | Facebook URL |
| `strGender` | `string` | Gender |
| `strGeniusID` | `string` | Genius ID |
| `strGenre` | `string` | Musical genre |
| `strISNIcode` | `string` | ISNI code |
| `strItunesID` | `string` | iTunes ID |
| `strLabel` | `string` | Record label |
| `strLastFMChart` | `string` | Last.fm chart URL |
| `strLocation` | `string` | Recording location |
| `strLocked` | `string` | Lock status |
| `strLyricWikiID` | `string` | LyricWiki ID |
| `strMood` | `string` | Track mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Recording ID |
| `strMusicMozID` | `string` | MusicMoz ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | Rate Your Music ID |
| `strReleaseFormat` | `string` | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | Album review |
| `strSpeed` | `string` | Album speed/tempo |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Track theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `strTwitter` | `string` | Twitter handle |
| `strWebsite` | `string` | Official website URL |
| `strWikidataID` | `string` | Wikidata ID |
| `strWikipediaID` | `string` | Wikipedia ID |

#### Example: Load

```go
v1Lookup, err := client.V1Lookup(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1Lookup) // the loaded record
```

#### Example: List

```go
v1Lookups, err := client.V1Lookup(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1Lookups) // the array of records
```


### V1Search

Create an instance: `v1Search := client.V1Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `List(match, ctrl)` | List entities matching the criteria. |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `idAlbum` | `string` | Unique album ID |
| `idArtist` | `string` | Artist ID |
| `idIMVDB` | `string` | IMVDB ID |
| `idLabel` | `string` | Label ID |
| `idLyric` | `string` | Lyrics ID |
| `idTrack` | `string` | Unique track ID |
| `intBornYear` | `string` | Birth year (for solo artists) |
| `intCD` | `string` | CD number |
| `intCharted` | `string` | Chart position |
| `intDiedYear` | `string` | Death year (if applicable) |
| `intDuration` | `string` | Track duration in milliseconds |
| `intFormedYear` | `string` | Year the artist was formed |
| `intLoved` | `string` | Number of loves/likes |
| `intMembers` | `string` | Number of band members |
| `intMusicVidComments` | `string` | Music video comment count |
| `intMusicVidDislikes` | `string` | Music video dislike count |
| `intMusicVidFavorites` | `string` | Music video favorite count |
| `intMusicVidLikes` | `string` | Music video like count |
| `intMusicVidViews` | `string` | Music video view count |
| `intSales` | `string` | Sales figures |
| `intScore` | `string` | Album score/rating |
| `intScoreVotes` | `string` | Number of score votes |
| `intTotalListeners` | `string` | Total listener count |
| `intTotalPlays` | `string` | Total play count |
| `intTrackNumber` | `string` | Track number on album |
| `intYearReleased` | `string` | Release year |
| `strAlbum` | `string` | Album name |
| `strAlbum3DCase` | `string` | 3D case image URL |
| `strAlbum3DFace` | `string` | 3D face image URL |
| `strAlbum3DFlat` | `string` | 3D flat image URL |
| `strAlbum3DThumb` | `string` | 3D thumbnail URL |
| `strAlbumCDart` | `string` | CD art URL |
| `strAlbumSpine` | `string` | Album spine image URL |
| `strAlbumStripped` | `string` | Album name stripped of special characters |
| `strAlbumThumb` | `string` | Album thumbnail URL |
| `strAlbumThumbBack` | `string` | Album back cover URL |
| `strAlbumThumbHQ` | `string` | High quality album thumbnail URL |
| `strAllMusicID` | `string` | AllMusic ID |
| `strAmazonID` | `string` | Amazon ID |
| `strArtist` | `string` | Artist name |
| `strArtistAlternate` | `string` | Alternative artist name |
| `strArtistBanner` | `string` | Banner image URL |
| `strArtistClearart` | `string` | Clear art image URL |
| `strArtistCutout` | `string` | Cutout image URL |
| `strArtistFanart` | `string` | Fan art image URL |
| `strArtistFanart2` | `string` | Additional fan art image URL |
| `strArtistFanart3` | `string` | Additional fan art image URL |
| `strArtistFanart4` | `string` | Additional fan art image URL |
| `strArtistLogo` | `string` | Logo image URL |
| `strArtistStripped` | `string` | Artist name stripped |
| `strArtistThumb` | `string` | Thumbnail image URL |
| `strArtistWideThumb` | `string` | Wide thumbnail image URL |
| `strBBCReviewID` | `string` | BBC Review ID |
| `strBiographyEN` | `string` | Biography in English |
| `strCountry` | `string` | Country of origin |
| `strCountryCode` | `string` | Country code |
| `strDescriptionEN` | `string` | Album description in English |
| `strDisbanded` | `string` | Disbandment status |
| `strDiscogsID` | `string` | Discogs ID |
| `strFacebook` | `string` | Facebook URL |
| `strGender` | `string` | Gender |
| `strGeniusID` | `string` | Genius ID |
| `strGenre` | `string` | Musical genre |
| `strISNIcode` | `string` | ISNI code |
| `strItunesID` | `string` | iTunes ID |
| `strLabel` | `string` | Record label |
| `strLastFMChart` | `string` | Last.fm chart URL |
| `strLocation` | `string` | Recording location |
| `strLocked` | `string` | Lock status |
| `strLyricWikiID` | `string` | LyricWiki ID |
| `strMood` | `string` | Album mood |
| `strMusicBrainzAlbumID` | `string` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `string` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `string` | MusicBrainz Release Group ID |
| `strMusicMozID` | `string` | MusicMoz ID |
| `strMusicVid` | `string` | Music video URL |
| `strMusicVidCompany` | `string` | Music video production company |
| `strMusicVidDirector` | `string` | Music video director |
| `strMusicVidScreen1` | `string` | Music video screenshot 1 |
| `strMusicVidScreen2` | `string` | Music video screenshot 2 |
| `strMusicVidScreen3` | `string` | Music video screenshot 3 |
| `strRateYourMusicID` | `string` | Rate Your Music ID |
| `strReleaseFormat` | `string` | Release format (CD, Vinyl, etc.) |
| `strReview` | `string` | Album review |
| `strSpeed` | `string` | Album speed/tempo |
| `strStyle` | `string` | Musical style |
| `strTheme` | `string` | Album theme |
| `strTrack` | `string` | Track name |
| `strTrack3x3` | `string` | 3x3 track image URL |
| `strTrackLyrics` | `string` | Track lyrics |
| `strTrackThumb` | `string` | Track thumbnail URL |
| `strTwitter` | `string` | Twitter handle |
| `strWebsite` | `string` | Official website URL |
| `strWikidataID` | `string` | Wikidata ID |
| `strWikipediaID` | `string` | Wikipedia ID |

#### Example: Load

```go
v1Search, err := client.V1Search(nil).Load(map[string]any{"api_key": "api_key"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1Search) // the loaded record
```

#### Example: List

```go
v1Searchs, err := client.V1Search(nil).List(nil, nil)
if err != nil {
    panic(err)
}
fmt.Println(v1Searchs) // the array of records
```


### V2List

Create an instance: `v2List := client.V2List(nil)`

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
v2List, err := client.V2List(nil).Load(map[string]any{"id_artist": 1}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2List) // the loaded record
```


### V2Lookup

Create an instance: `v2Lookup := client.V2Lookup(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `artists` | `[]any` |  |
| `track` | `[]any` |  |

#### Example: Load

```go
v2Lookup, err := client.V2Lookup(nil).Load(map[string]any{"id_album": 1}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2Lookup) // the loaded record
```


### V2Search

Create an instance: `v2Search := client.V2Search(nil)`

#### Operations

| Method | Description |
| --- | --- |
| `Load(match, ctrl)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `[]any` |  |
| `artists` | `[]any` |  |
| `track` | `[]any` |  |

#### Example: Load

```go
v2Search, err := client.V2Search(nil).Load(map[string]any{"album_name": "album_name"}, nil)
if err != nil {
    panic(err)
}
fmt.Println(v2Search) // the loaded record
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

Entity instances are stateful. After a successful `Load`, the entity
stores the returned data and match criteria internally.

```go
v2lookup := client.V2Lookup(nil)
v2lookup.Load(map[string]any{"id_album": 1}, nil)

// v2lookup.Data() now returns the v2lookup data from the last load
// v2lookup.Match() returns the last match criteria
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
