package sdktest

import (
	"encoding/json"
	"os"
	"path/filepath"
	"runtime"
	"strings"
	"testing"
	"time"

	sdk "github.com/voxgig-sdk/free-music-sdk/go"
	"github.com/voxgig-sdk/free-music-sdk/go/core"

	vs "github.com/voxgig-sdk/free-music-sdk/go/utility/struct"
)

func TestV1SearchEntity(t *testing.T) {
	t.Run("instance", func(t *testing.T) {
		testsdk := sdk.TestSDK(nil, nil)
		ent := testsdk.V1Search(nil)
		if ent == nil {
			t.Fatal("expected non-nil V1SearchEntity")
		}
	})

	t.Run("basic", func(t *testing.T) {
		setup := v1_searchBasicSetup(nil)
		// Per-op sdk-test-control.json skip — basic test exercises a flow
		// with multiple ops; skipping any op skips the whole flow.
		_mode := "unit"
		if setup.live {
			_mode = "live"
		}
		for _, _op := range []string{"list", "load"} {
			if _shouldSkip, _reason := isControlSkipped("entityOp", "v1_search." + _op, _mode); _shouldSkip {
				if _reason == "" {
					_reason = "skipped via sdk-test-control.json"
				}
				t.Skip(_reason)
				return
			}
		}
		// The basic flow consumes synthetic IDs from the fixture. In live mode
		// without an *_ENTID env override, those IDs hit the live API and 4xx.
		if setup.syntheticOnly {
			t.Skip("live entity test uses synthetic IDs from fixture — set FREEMUSIC_TEST_V__SEARCH_ENTID JSON to run live")
			return
		}
		client := setup.client

		// Bootstrap entity data from existing test data (no create step in flow).
		v1SearchRef01DataRaw := vs.Items(core.ToMapAny(vs.GetPath("existing.v1_search", setup.data)))
		var v1SearchRef01Data map[string]any
		if len(v1SearchRef01DataRaw) > 0 {
			v1SearchRef01Data = core.ToMapAny(v1SearchRef01DataRaw[0][1])
		}
		// Discard guards against Go's unused-var check when the flow's steps
		// happen not to consume the bootstrap data (e.g. list-only flows).
		_ = v1SearchRef01Data

		// LIST
		v1SearchRef01Ent := client.V1Search(nil)
		v1SearchRef01Match := map[string]any{
			"api_key": setup.idmap["api_key01"],
		}

		v1SearchRef01ListResult, err := v1SearchRef01Ent.List(v1SearchRef01Match, nil)
		if err != nil {
			t.Fatalf("list failed: %v", err)
		}
		_, v1SearchRef01ListOk := v1SearchRef01ListResult.([]any)
		if !v1SearchRef01ListOk {
			t.Fatalf("expected list result to be an array, got %T", v1SearchRef01ListResult)
		}

		// LOAD
		v1SearchRef01MatchDt0 := map[string]any{}
		v1SearchRef01DataDt0Loaded, err := v1SearchRef01Ent.Load(v1SearchRef01MatchDt0, nil)
		if err != nil {
			t.Fatalf("load failed: %v", err)
		}
		if v1SearchRef01DataDt0Loaded == nil {
			t.Fatal("expected load result to be non-nil")
		}

	})
}

func v1_searchBasicSetup(extra map[string]any) *entityTestSetup {
	loadEnvLocal()

	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)

	entityDataFile := filepath.Join(dir, "..", "..", ".sdk", "test", "entity", "v1_search", "V1SearchTestData.json")

	entityDataSource, err := os.ReadFile(entityDataFile)
	if err != nil {
		panic("failed to read v1_search test data: " + err.Error())
	}

	var entityData map[string]any
	if err := json.Unmarshal(entityDataSource, &entityData); err != nil {
		panic("failed to parse v1_search test data: " + err.Error())
	}

	options := map[string]any{}
	options["entity"] = entityData["existing"]

	client := sdk.TestSDK(options, extra)

	// Generate idmap via transform, matching TS pattern.
	idmap := vs.Transform(
		[]any{"v1_search01", "v1_search02", "v1_search03", "api_key01"},
		map[string]any{
			"`$PACK`": []any{"", map[string]any{
				"`$KEY`": "`$COPY`",
				"`$VAL`": []any{"`$FORMAT`", "upper", "`$COPY`"},
			}},
		},
	)

	// Detect ENTID env override before envOverride consumes it. When live
	// mode is on without a real override, the basic test runs against synthetic
	// IDs from the fixture and 4xx's. Surface this so the test can skip.
	entidEnvRaw := os.Getenv("FREEMUSIC_TEST_V__SEARCH_ENTID")
	idmapOverridden := entidEnvRaw != "" && strings.HasPrefix(strings.TrimSpace(entidEnvRaw), "{")

	env := envOverride(map[string]any{
		"FREEMUSIC_TEST_V__SEARCH_ENTID": idmap,
		"FREEMUSIC_TEST_LIVE":      "FALSE",
		"FREEMUSIC_TEST_EXPLAIN":   "FALSE",
	})

	idmapResolved := core.ToMapAny(env["FREEMUSIC_TEST_V__SEARCH_ENTID"])
	if idmapResolved == nil {
		idmapResolved = core.ToMapAny(idmap)
	}

	if env["FREEMUSIC_TEST_LIVE"] == "TRUE" {
		mergedOpts := vs.Merge([]any{
			map[string]any{
			},
			extra,
		})
		client = sdk.NewFreeMusicSDK(core.ToMapAny(mergedOpts))
	}

	live := env["FREEMUSIC_TEST_LIVE"] == "TRUE"
	return &entityTestSetup{
		client:        client,
		data:          entityData,
		idmap:         idmapResolved,
		env:           env,
		explain:       env["FREEMUSIC_TEST_EXPLAIN"] == "TRUE",
		live:          live,
		syntheticOnly: live && !idmapOverridden,
		now:           time.Now().UnixMilli(),
	}
}
