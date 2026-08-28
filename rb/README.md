# FreeMusic Ruby SDK



The Ruby SDK for the FreeMusic API — an entity-oriented client using idiomatic Ruby conventions.

The SDK exposes the API as capitalised, semantic **Entities** — for example `client.V1List` — with named operations (`list`/`load`) instead of raw URL paths and query strings. Working with resources and verbs keeps call sites self-describing and reduces cognitive load.

> Other languages, the CLI, and MCP server live alongside this one — see
> the [top-level README](../README.md).


## Install
This package is not yet published to RubyGems. Install it from the
GitHub release tag (`rb/vX.Y.Z`):

- Releases: [https://github.com/voxgig-sdk/free-music-sdk/releases](https://github.com/voxgig-sdk/free-music-sdk/releases)


## Tutorial: your first API call

This tutorial walks through creating a client, listing entities, and
loading a specific record.

### 1. Create a client

```ruby
require_relative "FreeMusic_sdk"

client = FreeMusicSDK.new({
  "apikey" => ENV["FREE_MUSIC_APIKEY"],
})
```

### 2. List v1list records

```ruby
begin
  # list returns an Array of V1List records — iterate directly.
  v1lists = client.V1List.list
  v1lists.each do |item|
    puts "#{item["idAlbum"]}"
  end
rescue => err
  warn "list failed: #{err}"
end
```

### 3. Load a v2list

V2List is nested under id_artist, so provide the `id_artist`.

```ruby
begin
  # load returns the ENTITY — call data_get for the V2List record (raises on error).
  v2list = client.V2List.load({ "id_artist" => 1 })
  puts v2list
rescue => err
  warn "load failed: #{err}"
end
```


## Error handling

Entity operations raise on failure, so rescue them:

```ruby
begin
  v2lookup = client.V2Lookup.load({ "id_album" => 1 })
rescue => err
  warn "load failed: #{err}"
end
```

`direct` does **not** raise — it returns the result hash. Branch on
`ok`; on failure `status` holds the HTTP status (for error responses) and
`err` holds a transport error, so read both defensively:

```ruby
result = client.direct({
  "path" => "/api/resource/{id}",
  "method" => "GET",
  "params" => { "id" => "example_id" },
})

warn "request failed: #{result["err"] || "HTTP #{result["status"]}"}" unless result["ok"]
```


## How-to guides

### Make a direct HTTP request

For endpoints not covered by entity methods:

```ruby
result = client.direct({
  "path" => "/api/resource/{id}",
  "method" => "GET",
  "params" => { "id" => "example" },
})

if result["ok"]
  puts result["status"]  # 200
  puts result["data"]    # response body
else
  # On an HTTP error status there is no err (only a transport failure sets
  # it), so fall back to the status code.
  warn(result["err"] || "HTTP #{result["status"]}")
end
```

### Prepare a request without sending it

```ruby
begin
  fetchdef = client.prepare({
    "path" => "/api/resource/{id}",
    "method" => "DELETE",
    "params" => { "id" => "example" },
  })
  puts fetchdef["url"]
  puts fetchdef["method"]
  puts fetchdef["headers"]
rescue => err
  warn "prepare failed: #{err}"
end
```

### Use test mode

Create a mock client for unit testing — no server required:

```ruby
client = FreeMusicSDK.test

# Entity ops return the ENTITY (raises on error);
# call data_get for the mock record.
v2lookup = client.V2Lookup.load({ "id_album" => 1 })
puts v2lookup
```

### Use a custom fetch function

Replace the HTTP transport with your own function:

```ruby
mock_fetch = ->(url, init) {
  return {
    "status" => 200,
    "statusText" => "OK",
    "headers" => {},
    "json" => ->() { { "id" => "mock01" } },
  }, nil
}

client = FreeMusicSDK.new({
  "base" => "http://localhost:8080",
  "system" => {
    "fetch" => mock_fetch,
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
cd rb && ruby -Itest -e "Dir['test/*_test.rb'].each { |f| require_relative f }"
```


## Reference

### FreeMusicSDK

```ruby
require_relative "FreeMusic_sdk"
client = FreeMusicSDK.new(options)
```

Creates a new SDK client.

| Option | Type | Description |
| --- | --- | --- |
| `apikey` | `String` | API key for authentication. |
| `base` | `String` | Base URL of the API server. |
| `prefix` | `String` | URL path prefix prepended to all requests. |
| `suffix` | `String` | URL path suffix appended to all requests. |
| `feature` | `Hash` | Feature activation flags. |
| `extend` | `Hash` | Additional Feature instances to load. |
| `system` | `Hash` | System overrides (e.g. custom `fetch` lambda). |

### test

```ruby
client = FreeMusicSDK.test(testopts, sdkopts)
```

Creates a test-mode client with mock transport. Both arguments may be `nil`.

### FreeMusicSDK methods

| Method | Signature | Description |
| --- | --- | --- |
| `options_map` | `() -> Hash` | Deep copy of current SDK options. |
| `get_utility` | `() -> Utility` | Copy of the SDK utility object. |
| `prepare` | `(fetchargs) -> Hash` | Build an HTTP request definition without sending. Raises on error. |
| `direct` | `(fetchargs) -> Hash` | Build and send an HTTP request. Returns a result hash (`result["ok"]`); does not raise. |
| `V1List` | `(data) -> V1ListEntity` | Create a V1List entity instance. |
| `V1Lookup` | `(data) -> V1LookupEntity` | Create a V1Lookup entity instance. |
| `V1Search` | `(data) -> V1SearchEntity` | Create a V1Search entity instance. |
| `V2List` | `(data) -> V2ListEntity` | Create a V2List entity instance. |
| `V2Lookup` | `(data) -> V2LookupEntity` | Create a V2Lookup entity instance. |
| `V2Search` | `(data) -> V2SearchEntity` | Create a V2Search entity instance. |

### Entity interface

All entities share the same interface.

| Method | Signature | Description |
| --- | --- | --- |
| `load` | `(reqmatch, ctrl) -> any` | Load a single entity by match criteria. Raises on error. |
| `list` | `(reqmatch = nil, ctrl) -> Array` | List entities matching the criteria (call with no argument to list all). Raises on error. |
| `data_get` | `() -> Hash` | Get entity data. |
| `data_set` | `(data)` | Set entity data. |
| `match_get` | `() -> Hash` | Get entity match criteria. |
| `match_set` | `(match)` | Set entity match criteria. |
| `make` | `() -> Entity` | Create a new instance with the same options. |
| `get_name` | `() -> String` | Return the entity name. |

### Result shape

Entity operations return the result data directly. On failure they
raise a `FreeMusicError` (a `StandardError` subclass), so wrap
calls in `begin`/`rescue` where you need to handle errors.

The `direct` escape hatch is the exception: it never raises and instead
returns a result `Hash` with these keys:

| Key | Type | Description |
| --- | --- | --- |
| `ok` | `Boolean` | `true` if the HTTP status is 2xx. |
| `status` | `Integer` | HTTP status code. |
| `headers` | `Hash` | Response headers. |
| `data` | `any` | Parsed JSON response body. |
| `err` | `Error` | Present when `ok` is `false`. |

### Entities

#### V1List

| Field | Description |
| --- | --- |
| `idAlbum` | Album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intCD` | CD number |
| `intDuration` | Track duration in milliseconds |
| `intLoved` | Number of loves/likes |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intScore` | Track score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `strAlbum` | Album name |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strDescriptionEN` | Track description in English |
| `strGenre` | Musical genre |
| `strLocked` | Lock status |
| `strMood` | Track mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Recording ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strStyle` | Musical style |
| `strTheme` | Track theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `trending` |  |

Operations: List, Load.

API path: `/{apiKey}/trending.php`

#### V1Lookup

| Field | Description |
| --- | --- |
| `idAlbum` | Album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLabel` | Label ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intBornYear` | Birth year (for solo artists) |
| `intCD` | CD number |
| `intCharted` | Chart position |
| `intDiedYear` | Death year (if applicable) |
| `intDuration` | Track duration in milliseconds |
| `intFormedYear` | Year the artist was formed |
| `intLoved` | Number of loves/likes |
| `intMembers` | Number of band members |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intSales` | Sales figures |
| `intScore` | Track score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `intYearReleased` | Release year |
| `strAlbum` | Album name |
| `strAlbum3DCase` | 3D case image URL |
| `strAlbum3DFace` | 3D face image URL |
| `strAlbum3DFlat` | 3D flat image URL |
| `strAlbum3DThumb` | 3D thumbnail URL |
| `strAlbumCDart` | CD art URL |
| `strAlbumSpine` | Album spine image URL |
| `strAlbumStripped` | Album name stripped of special characters |
| `strAlbumThumb` | Album thumbnail URL |
| `strAlbumThumbBack` | Album back cover URL |
| `strAlbumThumbHQ` | High quality album thumbnail URL |
| `strAllMusicID` | AllMusic ID |
| `strAmazonID` | Amazon ID |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strArtistBanner` | Banner image URL |
| `strArtistClearart` | Clear art image URL |
| `strArtistCutout` | Cutout image URL |
| `strArtistFanart` | Fan art image URL |
| `strArtistFanart2` | Additional fan art image URL |
| `strArtistFanart3` | Additional fan art image URL |
| `strArtistFanart4` | Additional fan art image URL |
| `strArtistLogo` | Logo image URL |
| `strArtistStripped` | Artist name stripped |
| `strArtistThumb` | Thumbnail image URL |
| `strArtistWideThumb` | Wide thumbnail image URL |
| `strBBCReviewID` | BBC Review ID |
| `strBiographyEN` | Biography in English |
| `strCountry` | Country of origin |
| `strCountryCode` | Country code |
| `strDescriptionEN` | Track description in English |
| `strDisbanded` | Disbandment status |
| `strDiscogsID` | Discogs ID |
| `strFacebook` | Facebook URL |
| `strGender` | Gender |
| `strGeniusID` | Genius ID |
| `strGenre` | Musical genre |
| `strISNIcode` | ISNI code |
| `strItunesID` | iTunes ID |
| `strLabel` | Record label |
| `strLastFMChart` | Last.fm chart URL |
| `strLocation` | Recording location |
| `strLocked` | Lock status |
| `strLyricWikiID` | LyricWiki ID |
| `strMood` | Track mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Recording ID |
| `strMusicMozID` | MusicMoz ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strRateYourMusicID` | Rate Your Music ID |
| `strReleaseFormat` | Release format (CD, Vinyl, etc.) |
| `strReview` | Album review |
| `strSpeed` | Album speed/tempo |
| `strStyle` | Musical style |
| `strTheme` | Track theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `strTwitter` | Twitter handle |
| `strWebsite` | Official website URL |
| `strWikidataID` | Wikidata ID |
| `strWikipediaID` | Wikipedia ID |

Operations: List, Load.

API path: `/{apiKey}/track.php`

#### V1Search

| Field | Description |
| --- | --- |
| `album` |  |
| `idAlbum` | Unique album ID |
| `idArtist` | Artist ID |
| `idIMVDB` | IMVDB ID |
| `idLabel` | Label ID |
| `idLyric` | Lyrics ID |
| `idTrack` | Unique track ID |
| `intBornYear` | Birth year (for solo artists) |
| `intCD` | CD number |
| `intCharted` | Chart position |
| `intDiedYear` | Death year (if applicable) |
| `intDuration` | Track duration in milliseconds |
| `intFormedYear` | Year the artist was formed |
| `intLoved` | Number of loves/likes |
| `intMembers` | Number of band members |
| `intMusicVidComments` | Music video comment count |
| `intMusicVidDislikes` | Music video dislike count |
| `intMusicVidFavorites` | Music video favorite count |
| `intMusicVidLikes` | Music video like count |
| `intMusicVidViews` | Music video view count |
| `intSales` | Sales figures |
| `intScore` | Album score/rating |
| `intScoreVotes` | Number of score votes |
| `intTotalListeners` | Total listener count |
| `intTotalPlays` | Total play count |
| `intTrackNumber` | Track number on album |
| `intYearReleased` | Release year |
| `strAlbum` | Album name |
| `strAlbum3DCase` | 3D case image URL |
| `strAlbum3DFace` | 3D face image URL |
| `strAlbum3DFlat` | 3D flat image URL |
| `strAlbum3DThumb` | 3D thumbnail URL |
| `strAlbumCDart` | CD art URL |
| `strAlbumSpine` | Album spine image URL |
| `strAlbumStripped` | Album name stripped of special characters |
| `strAlbumThumb` | Album thumbnail URL |
| `strAlbumThumbBack` | Album back cover URL |
| `strAlbumThumbHQ` | High quality album thumbnail URL |
| `strAllMusicID` | AllMusic ID |
| `strAmazonID` | Amazon ID |
| `strArtist` | Artist name |
| `strArtistAlternate` | Alternative artist name |
| `strArtistBanner` | Banner image URL |
| `strArtistClearart` | Clear art image URL |
| `strArtistCutout` | Cutout image URL |
| `strArtistFanart` | Fan art image URL |
| `strArtistFanart2` | Additional fan art image URL |
| `strArtistFanart3` | Additional fan art image URL |
| `strArtistFanart4` | Additional fan art image URL |
| `strArtistLogo` | Logo image URL |
| `strArtistStripped` | Artist name stripped |
| `strArtistThumb` | Thumbnail image URL |
| `strArtistWideThumb` | Wide thumbnail image URL |
| `strBBCReviewID` | BBC Review ID |
| `strBiographyEN` | Biography in English |
| `strCountry` | Country of origin |
| `strCountryCode` | Country code |
| `strDescriptionEN` | Album description in English |
| `strDisbanded` | Disbandment status |
| `strDiscogsID` | Discogs ID |
| `strFacebook` | Facebook URL |
| `strGender` | Gender |
| `strGeniusID` | Genius ID |
| `strGenre` | Musical genre |
| `strISNIcode` | ISNI code |
| `strItunesID` | iTunes ID |
| `strLabel` | Record label |
| `strLastFMChart` | Last.fm chart URL |
| `strLocation` | Recording location |
| `strLocked` | Lock status |
| `strLyricWikiID` | LyricWiki ID |
| `strMood` | Album mood |
| `strMusicBrainzAlbumID` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | MusicBrainz Artist ID |
| `strMusicBrainzID` | MusicBrainz Release Group ID |
| `strMusicMozID` | MusicMoz ID |
| `strMusicVid` | Music video URL |
| `strMusicVidCompany` | Music video production company |
| `strMusicVidDirector` | Music video director |
| `strMusicVidScreen1` | Music video screenshot 1 |
| `strMusicVidScreen2` | Music video screenshot 2 |
| `strMusicVidScreen3` | Music video screenshot 3 |
| `strRateYourMusicID` | Rate Your Music ID |
| `strReleaseFormat` | Release format (CD, Vinyl, etc.) |
| `strReview` | Album review |
| `strSpeed` | Album speed/tempo |
| `strStyle` | Musical style |
| `strTheme` | Album theme |
| `strTrack` | Track name |
| `strTrack3x3` | 3x3 track image URL |
| `strTrackLyrics` | Track lyrics |
| `strTrackThumb` | Track thumbnail URL |
| `strTwitter` | Twitter handle |
| `strWebsite` | Official website URL |
| `strWikidataID` | Wikidata ID |
| `strWikipediaID` | Wikipedia ID |

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
| `artists` |  |
| `track` |  |

Operations: Load.

API path: `/lookup/album/{idAlbum}`

#### V2Search

| Field | Description |
| --- | --- |
| `album` |  |
| `artists` |  |
| `track` |  |

Operations: Load.

API path: `/search/album/{albumName}`



## Entities


### V1List

Create an instance: `v1_list = client.V1List`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `String` | Album ID |
| `idArtist` | `String` | Artist ID |
| `idIMVDB` | `String` | IMVDB ID |
| `idLyric` | `String` | Lyrics ID |
| `idTrack` | `String` | Unique track ID |
| `intCD` | `String` | CD number |
| `intDuration` | `String` | Track duration in milliseconds |
| `intLoved` | `String` | Number of loves/likes |
| `intMusicVidComments` | `String` | Music video comment count |
| `intMusicVidDislikes` | `String` | Music video dislike count |
| `intMusicVidFavorites` | `String` | Music video favorite count |
| `intMusicVidLikes` | `String` | Music video like count |
| `intMusicVidViews` | `String` | Music video view count |
| `intScore` | `String` | Track score/rating |
| `intScoreVotes` | `String` | Number of score votes |
| `intTotalListeners` | `String` | Total listener count |
| `intTotalPlays` | `String` | Total play count |
| `intTrackNumber` | `String` | Track number on album |
| `strAlbum` | `String` | Album name |
| `strArtist` | `String` | Artist name |
| `strArtistAlternate` | `String` | Alternative artist name |
| `strDescriptionEN` | `String` | Track description in English |
| `strGenre` | `String` | Musical genre |
| `strLocked` | `String` | Lock status |
| `strMood` | `String` | Track mood |
| `strMusicBrainzAlbumID` | `String` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | MusicBrainz Recording ID |
| `strMusicVid` | `String` | Music video URL |
| `strMusicVidCompany` | `String` | Music video production company |
| `strMusicVidDirector` | `String` | Music video director |
| `strMusicVidScreen1` | `String` | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | Music video screenshot 3 |
| `strStyle` | `String` | Musical style |
| `strTheme` | `String` | Track theme |
| `strTrack` | `String` | Track name |
| `strTrack3x3` | `String` | 3x3 track image URL |
| `strTrackLyrics` | `String` | Track lyrics |
| `strTrackThumb` | `String` | Track thumbnail URL |
| `trending` | `Array` |  |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V1List record (raises on error).
v1_list = client.V1List.load({ "api_key" => "api_key" })
```

#### Example: List

```ruby
# list returns an Array of V1List records (raises on error).
v1_lists = client.V1List.list
```


### V1Lookup

Create an instance: `v1_lookup = client.V1Lookup`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `idAlbum` | `String` | Album ID |
| `idArtist` | `String` | Artist ID |
| `idIMVDB` | `String` | IMVDB ID |
| `idLabel` | `String` | Label ID |
| `idLyric` | `String` | Lyrics ID |
| `idTrack` | `String` | Unique track ID |
| `intBornYear` | `String` | Birth year (for solo artists) |
| `intCD` | `String` | CD number |
| `intCharted` | `String` | Chart position |
| `intDiedYear` | `String` | Death year (if applicable) |
| `intDuration` | `String` | Track duration in milliseconds |
| `intFormedYear` | `String` | Year the artist was formed |
| `intLoved` | `String` | Number of loves/likes |
| `intMembers` | `String` | Number of band members |
| `intMusicVidComments` | `String` | Music video comment count |
| `intMusicVidDislikes` | `String` | Music video dislike count |
| `intMusicVidFavorites` | `String` | Music video favorite count |
| `intMusicVidLikes` | `String` | Music video like count |
| `intMusicVidViews` | `String` | Music video view count |
| `intSales` | `String` | Sales figures |
| `intScore` | `String` | Track score/rating |
| `intScoreVotes` | `String` | Number of score votes |
| `intTotalListeners` | `String` | Total listener count |
| `intTotalPlays` | `String` | Total play count |
| `intTrackNumber` | `String` | Track number on album |
| `intYearReleased` | `String` | Release year |
| `strAlbum` | `String` | Album name |
| `strAlbum3DCase` | `String` | 3D case image URL |
| `strAlbum3DFace` | `String` | 3D face image URL |
| `strAlbum3DFlat` | `String` | 3D flat image URL |
| `strAlbum3DThumb` | `String` | 3D thumbnail URL |
| `strAlbumCDart` | `String` | CD art URL |
| `strAlbumSpine` | `String` | Album spine image URL |
| `strAlbumStripped` | `String` | Album name stripped of special characters |
| `strAlbumThumb` | `String` | Album thumbnail URL |
| `strAlbumThumbBack` | `String` | Album back cover URL |
| `strAlbumThumbHQ` | `String` | High quality album thumbnail URL |
| `strAllMusicID` | `String` | AllMusic ID |
| `strAmazonID` | `String` | Amazon ID |
| `strArtist` | `String` | Artist name |
| `strArtistAlternate` | `String` | Alternative artist name |
| `strArtistBanner` | `String` | Banner image URL |
| `strArtistClearart` | `String` | Clear art image URL |
| `strArtistCutout` | `String` | Cutout image URL |
| `strArtistFanart` | `String` | Fan art image URL |
| `strArtistFanart2` | `String` | Additional fan art image URL |
| `strArtistFanart3` | `String` | Additional fan art image URL |
| `strArtistFanart4` | `String` | Additional fan art image URL |
| `strArtistLogo` | `String` | Logo image URL |
| `strArtistStripped` | `String` | Artist name stripped |
| `strArtistThumb` | `String` | Thumbnail image URL |
| `strArtistWideThumb` | `String` | Wide thumbnail image URL |
| `strBBCReviewID` | `String` | BBC Review ID |
| `strBiographyEN` | `String` | Biography in English |
| `strCountry` | `String` | Country of origin |
| `strCountryCode` | `String` | Country code |
| `strDescriptionEN` | `String` | Track description in English |
| `strDisbanded` | `String` | Disbandment status |
| `strDiscogsID` | `String` | Discogs ID |
| `strFacebook` | `String` | Facebook URL |
| `strGender` | `String` | Gender |
| `strGeniusID` | `String` | Genius ID |
| `strGenre` | `String` | Musical genre |
| `strISNIcode` | `String` | ISNI code |
| `strItunesID` | `String` | iTunes ID |
| `strLabel` | `String` | Record label |
| `strLastFMChart` | `String` | Last.fm chart URL |
| `strLocation` | `String` | Recording location |
| `strLocked` | `String` | Lock status |
| `strLyricWikiID` | `String` | LyricWiki ID |
| `strMood` | `String` | Track mood |
| `strMusicBrainzAlbumID` | `String` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | MusicBrainz Recording ID |
| `strMusicMozID` | `String` | MusicMoz ID |
| `strMusicVid` | `String` | Music video URL |
| `strMusicVidCompany` | `String` | Music video production company |
| `strMusicVidDirector` | `String` | Music video director |
| `strMusicVidScreen1` | `String` | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | Music video screenshot 3 |
| `strRateYourMusicID` | `String` | Rate Your Music ID |
| `strReleaseFormat` | `String` | Release format (CD, Vinyl, etc.) |
| `strReview` | `String` | Album review |
| `strSpeed` | `String` | Album speed/tempo |
| `strStyle` | `String` | Musical style |
| `strTheme` | `String` | Track theme |
| `strTrack` | `String` | Track name |
| `strTrack3x3` | `String` | 3x3 track image URL |
| `strTrackLyrics` | `String` | Track lyrics |
| `strTrackThumb` | `String` | Track thumbnail URL |
| `strTwitter` | `String` | Twitter handle |
| `strWebsite` | `String` | Official website URL |
| `strWikidataID` | `String` | Wikidata ID |
| `strWikipediaID` | `String` | Wikipedia ID |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V1Lookup record (raises on error).
v1_lookup = client.V1Lookup.load({ "api_key" => "api_key", "i" => "i" })
```

#### Example: List

```ruby
# list returns an Array of V1Lookup records (raises on error).
v1_lookups = client.V1Lookup.list
```


### V1Search

Create an instance: `v1_search = client.V1Search`

#### Operations

| Method | Description |
| --- | --- |
| `list(match)` | List entities matching the criteria. |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `Array` |  |
| `idAlbum` | `String` | Unique album ID |
| `idArtist` | `String` | Artist ID |
| `idIMVDB` | `String` | IMVDB ID |
| `idLabel` | `String` | Label ID |
| `idLyric` | `String` | Lyrics ID |
| `idTrack` | `String` | Unique track ID |
| `intBornYear` | `String` | Birth year (for solo artists) |
| `intCD` | `String` | CD number |
| `intCharted` | `String` | Chart position |
| `intDiedYear` | `String` | Death year (if applicable) |
| `intDuration` | `String` | Track duration in milliseconds |
| `intFormedYear` | `String` | Year the artist was formed |
| `intLoved` | `String` | Number of loves/likes |
| `intMembers` | `String` | Number of band members |
| `intMusicVidComments` | `String` | Music video comment count |
| `intMusicVidDislikes` | `String` | Music video dislike count |
| `intMusicVidFavorites` | `String` | Music video favorite count |
| `intMusicVidLikes` | `String` | Music video like count |
| `intMusicVidViews` | `String` | Music video view count |
| `intSales` | `String` | Sales figures |
| `intScore` | `String` | Album score/rating |
| `intScoreVotes` | `String` | Number of score votes |
| `intTotalListeners` | `String` | Total listener count |
| `intTotalPlays` | `String` | Total play count |
| `intTrackNumber` | `String` | Track number on album |
| `intYearReleased` | `String` | Release year |
| `strAlbum` | `String` | Album name |
| `strAlbum3DCase` | `String` | 3D case image URL |
| `strAlbum3DFace` | `String` | 3D face image URL |
| `strAlbum3DFlat` | `String` | 3D flat image URL |
| `strAlbum3DThumb` | `String` | 3D thumbnail URL |
| `strAlbumCDart` | `String` | CD art URL |
| `strAlbumSpine` | `String` | Album spine image URL |
| `strAlbumStripped` | `String` | Album name stripped of special characters |
| `strAlbumThumb` | `String` | Album thumbnail URL |
| `strAlbumThumbBack` | `String` | Album back cover URL |
| `strAlbumThumbHQ` | `String` | High quality album thumbnail URL |
| `strAllMusicID` | `String` | AllMusic ID |
| `strAmazonID` | `String` | Amazon ID |
| `strArtist` | `String` | Artist name |
| `strArtistAlternate` | `String` | Alternative artist name |
| `strArtistBanner` | `String` | Banner image URL |
| `strArtistClearart` | `String` | Clear art image URL |
| `strArtistCutout` | `String` | Cutout image URL |
| `strArtistFanart` | `String` | Fan art image URL |
| `strArtistFanart2` | `String` | Additional fan art image URL |
| `strArtistFanart3` | `String` | Additional fan art image URL |
| `strArtistFanart4` | `String` | Additional fan art image URL |
| `strArtistLogo` | `String` | Logo image URL |
| `strArtistStripped` | `String` | Artist name stripped |
| `strArtistThumb` | `String` | Thumbnail image URL |
| `strArtistWideThumb` | `String` | Wide thumbnail image URL |
| `strBBCReviewID` | `String` | BBC Review ID |
| `strBiographyEN` | `String` | Biography in English |
| `strCountry` | `String` | Country of origin |
| `strCountryCode` | `String` | Country code |
| `strDescriptionEN` | `String` | Album description in English |
| `strDisbanded` | `String` | Disbandment status |
| `strDiscogsID` | `String` | Discogs ID |
| `strFacebook` | `String` | Facebook URL |
| `strGender` | `String` | Gender |
| `strGeniusID` | `String` | Genius ID |
| `strGenre` | `String` | Musical genre |
| `strISNIcode` | `String` | ISNI code |
| `strItunesID` | `String` | iTunes ID |
| `strLabel` | `String` | Record label |
| `strLastFMChart` | `String` | Last.fm chart URL |
| `strLocation` | `String` | Recording location |
| `strLocked` | `String` | Lock status |
| `strLyricWikiID` | `String` | LyricWiki ID |
| `strMood` | `String` | Album mood |
| `strMusicBrainzAlbumID` | `String` | MusicBrainz Album ID |
| `strMusicBrainzArtistID` | `String` | MusicBrainz Artist ID |
| `strMusicBrainzID` | `String` | MusicBrainz Release Group ID |
| `strMusicMozID` | `String` | MusicMoz ID |
| `strMusicVid` | `String` | Music video URL |
| `strMusicVidCompany` | `String` | Music video production company |
| `strMusicVidDirector` | `String` | Music video director |
| `strMusicVidScreen1` | `String` | Music video screenshot 1 |
| `strMusicVidScreen2` | `String` | Music video screenshot 2 |
| `strMusicVidScreen3` | `String` | Music video screenshot 3 |
| `strRateYourMusicID` | `String` | Rate Your Music ID |
| `strReleaseFormat` | `String` | Release format (CD, Vinyl, etc.) |
| `strReview` | `String` | Album review |
| `strSpeed` | `String` | Album speed/tempo |
| `strStyle` | `String` | Musical style |
| `strTheme` | `String` | Album theme |
| `strTrack` | `String` | Track name |
| `strTrack3x3` | `String` | 3x3 track image URL |
| `strTrackLyrics` | `String` | Track lyrics |
| `strTrackThumb` | `String` | Track thumbnail URL |
| `strTwitter` | `String` | Twitter handle |
| `strWebsite` | `String` | Official website URL |
| `strWikidataID` | `String` | Wikidata ID |
| `strWikipediaID` | `String` | Wikipedia ID |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V1Search record (raises on error).
v1_search = client.V1Search.load({ "api_key" => "api_key", "s" => "s" })
```

#### Example: List

```ruby
# list returns an Array of V1Search records (raises on error).
v1_searchs = client.V1Search.list
```


### V2List

Create an instance: `v2_list = client.V2List`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `Array` |  |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V2List record (raises on error).
v2_list = client.V2List.load({ "id_artist" => 1 })
```


### V2Lookup

Create an instance: `v2_lookup = client.V2Lookup`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `Array` |  |
| `artists` | `Array` |  |
| `track` | `Array` |  |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V2Lookup record (raises on error).
v2_lookup = client.V2Lookup.load({ "id_album" => 1 })
```


### V2Search

Create an instance: `v2_search = client.V2Search`

#### Operations

| Method | Description |
| --- | --- |
| `load(match)` | Load a single entity by match criteria. |

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| `album` | `Array` |  |
| `artists` | `Array` |  |
| `track` | `Array` |  |

#### Example: Load

```ruby
# load returns the ENTITY — call data_get for the V2Search record (raises on error).
v2_search = client.V2Search.load({ "album_name" => "album_name" })
```

## Features

This SDK ships 1 optional features. Each is **inactive until you
switch it on**, so an SDK you have not configured behaves exactly as if none of
them existed — no retries, no cache, no logging, no measurable overhead.

Activate a feature by name in the client options, alongside the options shown
above:

| Feature | What it does |
|---|---|
| [`test`](#test) | In-memory mock transport for testing without a live server |

### test

In-memory mock transport for testing without a live server.

| Option | Default |
|---|---|
| `active` | `false` |

Set `feature.test.active` to enable it, then override any of the options above.


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

Features are the extension mechanism. A feature is a Ruby class
with hook methods named after pipeline stages (e.g. `PrePoint`,
`PreSpec`). Each method receives the context.

The SDK ships with built-in features:

- **TestFeature**: In-memory mock transport for testing without a live server

Features are initialized in order. Hooks fire in the order features
were added, so later features can override earlier ones.

### Data as hashes

The Ruby SDK uses plain Ruby hashes throughout rather than typed
objects. This mirrors the dynamic nature of the API and keeps the
SDK flexible — no code generation is needed when the API schema
changes.

Use `Helpers.to_map()` to safely validate that a value is a hash.

### Module structure

```
rb/
├── FreeMusic_sdk.rb       -- Main SDK module
├── config.rb                  -- Configuration
├── features.rb                -- Feature factory
├── core/                      -- Core types and context
├── entity/                    -- Entity implementations
├── feature/                   -- Built-in features (Base, Test, Log)
├── utility/                   -- Utility functions and struct library
└── test/                      -- Test suites
```

The main module (`FreeMusic_sdk`) exports the SDK class
and test helper. Import entity or utility modules directly only
when needed.

### Entity state

Entity instances are stateful. After a successful `load`, the entity
stores the returned data and match criteria internally.

```ruby
v2lookup = client.V2Lookup
v2lookup.load({ "id_album" => 1 })

# v2lookup.data_get now returns the v2lookup data from the last load
# v2lookup.match_get returns the last match criteria
```

Call `make` to create a fresh instance with the same configuration
but no stored state.

### Direct vs entity access

The entity interface handles URL construction, parameter placement,
and response parsing automatically. Use it for standard CRUD operations.

`direct` gives full control over the HTTP request. Use it for
non-standard endpoints, bulk operations, or any path not modelled as
an entity. `prepare` builds the request without sending it — useful
for debugging or custom transport.


## Full Reference

See [REFERENCE.md](REFERENCE.md) for complete API reference
documentation including all method signatures, entity field schemas,
and detailed usage examples.
