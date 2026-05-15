package core

var UtilityRegistrar func(u *Utility)

var NewBaseFeatureFunc func() Feature

var NewTestFeatureFunc func() Feature

var NewV1ListEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

var NewV1LookupEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

var NewV1SearchEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

var NewV2ListEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

var NewV2LookupEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

var NewV2SearchEntityFunc func(client *FreeMusicSDK, entopts map[string]any) FreeMusicEntity

