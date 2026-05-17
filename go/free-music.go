package voxgigfreemusicsdk

import (
	"github.com/voxgig-sdk/free-music-sdk/go/core"
	"github.com/voxgig-sdk/free-music-sdk/go/entity"
	"github.com/voxgig-sdk/free-music-sdk/go/feature"
	_ "github.com/voxgig-sdk/free-music-sdk/go/utility"
)

// Type aliases preserve external API.
type FreeMusicSDK = core.FreeMusicSDK
type Context = core.Context
type Utility = core.Utility
type Feature = core.Feature
type Entity = core.Entity
type FreeMusicEntity = core.FreeMusicEntity
type FetcherFunc = core.FetcherFunc
type Spec = core.Spec
type Result = core.Result
type Response = core.Response
type Operation = core.Operation
type Control = core.Control
type FreeMusicError = core.FreeMusicError

// BaseFeature from feature package.
type BaseFeature = feature.BaseFeature

func init() {
	core.NewBaseFeatureFunc = func() core.Feature {
		return feature.NewBaseFeature()
	}
	core.NewTestFeatureFunc = func() core.Feature {
		return feature.NewTestFeature()
	}
	core.NewV1ListEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV1ListEntity(client, entopts)
	}
	core.NewV1LookupEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV1LookupEntity(client, entopts)
	}
	core.NewV1SearchEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV1SearchEntity(client, entopts)
	}
	core.NewV2ListEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV2ListEntity(client, entopts)
	}
	core.NewV2LookupEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV2LookupEntity(client, entopts)
	}
	core.NewV2SearchEntityFunc = func(client *core.FreeMusicSDK, entopts map[string]any) core.FreeMusicEntity {
		return entity.NewV2SearchEntity(client, entopts)
	}
}

// Constructor re-exports.
var NewFreeMusicSDK = core.NewFreeMusicSDK
var TestSDK = core.TestSDK
var NewContext = core.NewContext
var NewSpec = core.NewSpec
var NewResult = core.NewResult
var NewResponse = core.NewResponse
var NewOperation = core.NewOperation
var MakeConfig = core.MakeConfig
var NewBaseFeature = feature.NewBaseFeature
var NewTestFeature = feature.NewTestFeature
