# FreeMusic SDK

Look up artists, albums, tracks, and music videos through TheAudioDB's community-maintained music database

> TypeScript, Python, PHP, Golang, Ruby, Lua SDKs, a CLI, an interactive REPL, and an MCP server for AI agents — all generated from one OpenAPI spec by [@voxgig/sdkgen](https://github.com/voxgig/sdkgen).

## About Free Music API

[TheAudioDB](https://www.theaudiodb.com/) is a community-maintained music metadata database that exposes its catalogue as a JSON HTTP API. It is run as a sister project to TheSportsDB and TheMealDB, and is widely used by hobby and media apps that need artist, album, and track information without paying for a commercial music service.

What you get from the API:

- Artist, album, and track records, looked up by ID or searched by name.
- Music videos linked to an artist.
- Top tracks for an artist, plus "most loved" and country-specific trending lists.
- A v2 discography listing that returns an artist's albums.

Authentication is by API key. The v1 endpoints under `https://www.theaudiodb.com/api/v1/json/{key}/...` accept the key as a path segment (the shared test key `123` is documented for development). The v2 endpoints under `https://www.theaudiodb.com/api/v2/json/...` expect the key in an `X-API-KEY` header. Free keys are rate-limited to roughly 30 requests/minute; CORS is enabled.

## Try it

**TypeScript**
```bash
npm install free-music
```

**Python**
```bash
pip install free-music-sdk
```

**PHP**
```bash
composer require voxgig/free-music-sdk
```

**Golang**
```bash
go get github.com/voxgig-sdk/free-music-sdk/go
```

**Ruby**
```bash
gem install free-music-sdk
```

**Lua**
```bash
luarocks install free-music-sdk
```

## 30-second quickstart

### TypeScript

```ts
import { FreeMusicSDK } from 'free-music'

const client = new FreeMusicSDK({})

// List all v1lists
const v1lists = await client.V1List().list()
```

See the [TypeScript README](ts/README.md) for the
full guide, or scroll down for the same example in other languages.

## What's in the box

| Surface | Use it for | Path |
| --- | --- | --- |
| **SDK** (TypeScript, Python, PHP, Golang, Ruby, Lua) | App integration | `ts/` `py/` `php/` `go/` `rb/` `lua/` |
| **CLI** | Scripts, CI, ops, one-off API calls | `go-cli/` |
| **MCP server** | AI agents (Claude, Cursor, Cline) | `go-mcp/` |

## Use it from an AI agent (MCP)

The generated MCP server exposes every operation in this SDK as an
[MCP](https://modelcontextprotocol.io) tool that Claude, Cursor or Cline
can call directly. Build and register it:

```bash
cd go-mcp && go build -o free-music-mcp .
```

Then add it to your agent's MCP config (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "free-music": {
      "command": "/abs/path/to/free-music-mcp"
    }
  }
}
```

## Entities

The API exposes 6 entities:

| Entity | Description | API path |
| --- | --- | --- |
| **V1List** | v1 list-style endpoints that return collections of items rather than a single record — music videos for an artist (`/mvid.php`), an artist's top 10 tracks (`/track-top10.php`), and trending/most-loved feeds (`/trending.php`, `/mostloved.php`). | `/{apiKey}/trending.php` |
| **V1Lookup** | v1 lookup endpoints that fetch a single record by ID — `/artist.php?i=...`, `/album.php?i=...` or `?m=...`, and `/track.php?h=...`. | `/{apiKey}/track.php` |
| **V1Search** | v1 search endpoints that match by name — artists via `/search.php?s=...`, albums via `/searchalbum.php?s=...&a=...`, and tracks via `/searchtrack.php?s=...&t=...`. | `/{apiKey}/searchalbum.php` |
| **V2List** | v2 list endpoints, currently the artist discography at `/list/discography/{artistid}`. | `/list/discography/{idArtist}` |
| **V2Lookup** | v2 lookup endpoints with cleaner REST-style paths — `/lookup/artist/{id}`, `/lookup/album/{id}`, and `/lookup/track/{id}`. | `/lookup/album/{idAlbum}` |
| **V2Search** | v2 search endpoints — `/search/artist/{name}`, `/search/album/{name}`, and `/search/track/{name}`, authenticated via the `X-API-KEY` header. | `/search/album/{albumName}` |

Each entity supports the following operations where available: **load**,
**list**, **create**, **update**, and **remove**.

## Quickstart in other languages

### Python

```python
from freemusic_sdk import FreeMusicSDK

client = FreeMusicSDK({})

# List all v1lists
v1lists, err = client.V1List(None).list(None, None)

# Load a specific v1list
v1list, err = client.V1List(None).load(
    {"id": "example_id"}, None
)
```

### PHP

```php
<?php
require_once 'freemusic_sdk.php';

$client = new FreeMusicSDK([]);

// List all v1lists
[$v1lists, $err] = $client->V1List(null)->list(null, null);

// Load a specific v1list
[$v1list, $err] = $client->V1List(null)->load(
    ["id" => "example_id"], null
);
```

### Golang

```go
import sdk "github.com/voxgig-sdk/free-music-sdk/go"

client := sdk.NewFreeMusicSDK(map[string]any{})

// List all v1lists
v1lists, err := client.V1List(nil).List(nil, nil)
```

### Ruby

```ruby
require_relative "FreeMusic_sdk"

client = FreeMusicSDK.new({})

# List all v1lists
v1lists, err = client.V1List(nil).list(nil, nil)

# Load a specific v1list
v1list, err = client.V1List(nil).load(
  { "id" => "example_id" }, nil
)
```

### Lua

```lua
local sdk = require("free-music_sdk")

local client = sdk.new({})

-- List all v1lists
local v1lists, err = client:V1List(nil):list(nil, nil)

-- Load a specific v1list
local v1list, err = client:V1List(nil):load(
  { id = "example_id" }, nil
)
```

## Unit testing in offline mode

Every SDK ships a test mode that swaps the HTTP transport for an
in-memory mock, so unit tests run offline.

### TypeScript

```ts
const client = FreeMusicSDK.test()
const result = await client.V1List().load({ id: 'test01' })
// result.ok === true, result.data contains mock data
```

### Python

```python
client = FreeMusicSDK.test(None, None)
result, err = client.V1List(None).load(
    {"id": "test01"}, None
)
```

### PHP

```php
$client = FreeMusicSDK::test(null, null);
[$result, $err] = $client->V1List(null)->load(
    ["id" => "test01"], null
);
```

### Golang

```go
client := sdk.TestSDK(nil, nil)
result, err := client.V1List(nil).Load(
    map[string]any{"id": "test01"}, nil,
)
```

### Ruby

```ruby
client = FreeMusicSDK.test(nil, nil)
result, err = client.V1List(nil).load(
  { "id" => "test01" }, nil
)
```

### Lua

```lua
local client = sdk.test(nil, nil)
local result, err = client:V1List(nil):load(
  { id = "test01" }, nil
)
```

## How it works

Every SDK call runs the same five-stage pipeline:

1. **Point** — resolve the API endpoint from the operation definition.
2. **Spec** — build the HTTP specification (URL, method, headers, body).
3. **Request** — send the HTTP request.
4. **Response** — receive and parse the response.
5. **Result** — extract the result data for the caller.

A feature hook fires at each stage (e.g. `PrePoint`, `PreSpec`,
`PreRequest`), so features can inspect or modify the pipeline without
forking the SDK.

### Features

| Feature | Purpose |
| --- | --- |
| **TestFeature** | In-memory mock transport for testing without a live server |

Pass custom features via the `extend` option at construction time.

### Direct and Prepare

For endpoints the entity model doesn't cover, use the low-level methods:

- **`direct(fetchargs)`** — build and send an HTTP request in one step.
- **`prepare(fetchargs)`** — build the request without sending it.

Both accept a map with `path`, `method`, `params`, `query`,
`headers`, and `body`. See the [How-to guides](#how-to-guides) below.

## How-to guides

### Make a direct API call

When the entity interface does not cover an endpoint, use `direct`:

**TypeScript:**
```ts
const result = await client.direct({
  path: '/api/resource/{id}',
  method: 'GET',
  params: { id: 'example' },
})
console.log(result.data)
```

**Python:**
```python
result, err = client.direct({
    "path": "/api/resource/{id}",
    "method": "GET",
    "params": {"id": "example"},
})
```

**PHP:**
```php
[$result, $err] = $client->direct([
    "path" => "/api/resource/{id}",
    "method" => "GET",
    "params" => ["id" => "example"],
]);
```

**Go:**
```go
result, err := client.Direct(map[string]any{
    "path":   "/api/resource/{id}",
    "method": "GET",
    "params": map[string]any{"id": "example"},
})
```

**Ruby:**
```ruby
result, err = client.direct({
  "path" => "/api/resource/{id}",
  "method" => "GET",
  "params" => { "id" => "example" },
})
```

**Lua:**
```lua
local result, err = client:direct({
  path = "/api/resource/{id}",
  method = "GET",
  params = { id = "example" },
})
```

## Per-language documentation

- [TypeScript](ts/README.md)
- [Python](py/README.md)
- [PHP](php/README.md)
- [Golang](go/README.md)
- [Ruby](rb/README.md)
- [Lua](lua/README.md)

## Using the Free Music API

- Upstream: [https://www.theaudiodb.com/](https://www.theaudiodb.com/)
- API docs: [https://www.theaudiodb.com/free_music_api](https://www.theaudiodb.com/free_music_api)

- Free public tier uses the shared test API key `123`, suitable for development and testing.
- Higher-volume access (Premium / Business) requires a paid key.
- No explicit open-source licence is declared; usage is governed by TheAudioDB's site terms.

---

Generated from the Free Music API OpenAPI spec by [@voxgig/sdkgen](https://github.com/voxgig/sdkgen).
