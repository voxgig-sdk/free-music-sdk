// Typed models for the FreeMusic SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.
package entity

import (
	"encoding/json"

	"github.com/voxgig-sdk/free-music-sdk/go/core"
)

// V1List is the typed data model for the v1_list entity.
type V1List struct {
	IdAlbum *string `json:"idAlbum,omitempty"`
	IdArtist *string `json:"idArtist,omitempty"`
	IdIMVDB *string `json:"idIMVDB,omitempty"`
	IdLyric *string `json:"idLyric,omitempty"`
	IdTrack *string `json:"idTrack,omitempty"`
	IntCD *string `json:"intCD,omitempty"`
	IntDuration *string `json:"intDuration,omitempty"`
	IntLoved *string `json:"intLoved,omitempty"`
	IntMusicVidComments *string `json:"intMusicVidComments,omitempty"`
	IntMusicVidDislikes *string `json:"intMusicVidDislikes,omitempty"`
	IntMusicVidFavorites *string `json:"intMusicVidFavorites,omitempty"`
	IntMusicVidLikes *string `json:"intMusicVidLikes,omitempty"`
	IntMusicVidViews *string `json:"intMusicVidViews,omitempty"`
	IntScore *string `json:"intScore,omitempty"`
	IntScoreVotes *string `json:"intScoreVotes,omitempty"`
	IntTotalListeners *string `json:"intTotalListeners,omitempty"`
	IntTotalPlays *string `json:"intTotalPlays,omitempty"`
	IntTrackNumber *string `json:"intTrackNumber,omitempty"`
	StrAlbum *string `json:"strAlbum,omitempty"`
	StrArtist *string `json:"strArtist,omitempty"`
	StrArtistAlternate *string `json:"strArtistAlternate,omitempty"`
	StrDescriptionEN *string `json:"strDescriptionEN,omitempty"`
	StrGenre *string `json:"strGenre,omitempty"`
	StrLocked *string `json:"strLocked,omitempty"`
	StrMood *string `json:"strMood,omitempty"`
	StrMusicBrainzAlbumID *string `json:"strMusicBrainzAlbumID,omitempty"`
	StrMusicBrainzArtistID *string `json:"strMusicBrainzArtistID,omitempty"`
	StrMusicBrainzID *string `json:"strMusicBrainzID,omitempty"`
	StrMusicVid *string `json:"strMusicVid,omitempty"`
	StrMusicVidCompany *string `json:"strMusicVidCompany,omitempty"`
	StrMusicVidDirector *string `json:"strMusicVidDirector,omitempty"`
	StrMusicVidScreen1 *string `json:"strMusicVidScreen1,omitempty"`
	StrMusicVidScreen2 *string `json:"strMusicVidScreen2,omitempty"`
	StrMusicVidScreen3 *string `json:"strMusicVidScreen3,omitempty"`
	StrStyle *string `json:"strStyle,omitempty"`
	StrTheme *string `json:"strTheme,omitempty"`
	StrTrack *string `json:"strTrack,omitempty"`
	StrTrack3x3 *string `json:"strTrack3x3,omitempty"`
	StrTrackLyrics *string `json:"strTrackLyrics,omitempty"`
	StrTrackThumb *string `json:"strTrackThumb,omitempty"`
	Trending *[]any `json:"trending,omitempty"`
}

// V1ListLoadMatch is the typed request payload for V1List.LoadTyped.
type V1ListLoadMatch struct {
	ApiKey string `json:"api_key"`
}

// V1ListListMatch is the typed request payload for V1List.ListTyped.
type V1ListListMatch struct {
	ApiKey string `json:"api_key"`
}

// V1Lookup is the typed data model for the v1_lookup entity.
type V1Lookup struct {
	IdAlbum *string `json:"idAlbum,omitempty"`
	IdArtist *string `json:"idArtist,omitempty"`
	IdIMVDB *string `json:"idIMVDB,omitempty"`
	IdLabel *string `json:"idLabel,omitempty"`
	IdLyric *string `json:"idLyric,omitempty"`
	IdTrack *string `json:"idTrack,omitempty"`
	IntBornYear *string `json:"intBornYear,omitempty"`
	IntCD *string `json:"intCD,omitempty"`
	IntCharted *string `json:"intCharted,omitempty"`
	IntDiedYear *string `json:"intDiedYear,omitempty"`
	IntDuration *string `json:"intDuration,omitempty"`
	IntFormedYear *string `json:"intFormedYear,omitempty"`
	IntLoved *string `json:"intLoved,omitempty"`
	IntMembers *string `json:"intMembers,omitempty"`
	IntMusicVidComments *string `json:"intMusicVidComments,omitempty"`
	IntMusicVidDislikes *string `json:"intMusicVidDislikes,omitempty"`
	IntMusicVidFavorites *string `json:"intMusicVidFavorites,omitempty"`
	IntMusicVidLikes *string `json:"intMusicVidLikes,omitempty"`
	IntMusicVidViews *string `json:"intMusicVidViews,omitempty"`
	IntSales *string `json:"intSales,omitempty"`
	IntScore *string `json:"intScore,omitempty"`
	IntScoreVotes *string `json:"intScoreVotes,omitempty"`
	IntTotalListeners *string `json:"intTotalListeners,omitempty"`
	IntTotalPlays *string `json:"intTotalPlays,omitempty"`
	IntTrackNumber *string `json:"intTrackNumber,omitempty"`
	IntYearReleased *string `json:"intYearReleased,omitempty"`
	StrAlbum *string `json:"strAlbum,omitempty"`
	StrAlbum3DCase *string `json:"strAlbum3DCase,omitempty"`
	StrAlbum3DFace *string `json:"strAlbum3DFace,omitempty"`
	StrAlbum3DFlat *string `json:"strAlbum3DFlat,omitempty"`
	StrAlbum3DThumb *string `json:"strAlbum3DThumb,omitempty"`
	StrAlbumCDart *string `json:"strAlbumCDart,omitempty"`
	StrAlbumSpine *string `json:"strAlbumSpine,omitempty"`
	StrAlbumStripped *string `json:"strAlbumStripped,omitempty"`
	StrAlbumThumb *string `json:"strAlbumThumb,omitempty"`
	StrAlbumThumbBack *string `json:"strAlbumThumbBack,omitempty"`
	StrAlbumThumbHQ *string `json:"strAlbumThumbHQ,omitempty"`
	StrAllMusicID *string `json:"strAllMusicID,omitempty"`
	StrAmazonID *string `json:"strAmazonID,omitempty"`
	StrArtist *string `json:"strArtist,omitempty"`
	StrArtistAlternate *string `json:"strArtistAlternate,omitempty"`
	StrArtistBanner *string `json:"strArtistBanner,omitempty"`
	StrArtistClearart *string `json:"strArtistClearart,omitempty"`
	StrArtistCutout *string `json:"strArtistCutout,omitempty"`
	StrArtistFanart *string `json:"strArtistFanart,omitempty"`
	StrArtistFanart2 *string `json:"strArtistFanart2,omitempty"`
	StrArtistFanart3 *string `json:"strArtistFanart3,omitempty"`
	StrArtistFanart4 *string `json:"strArtistFanart4,omitempty"`
	StrArtistLogo *string `json:"strArtistLogo,omitempty"`
	StrArtistStripped *string `json:"strArtistStripped,omitempty"`
	StrArtistThumb *string `json:"strArtistThumb,omitempty"`
	StrArtistWideThumb *string `json:"strArtistWideThumb,omitempty"`
	StrBBCReviewID *string `json:"strBBCReviewID,omitempty"`
	StrBiographyEN *string `json:"strBiographyEN,omitempty"`
	StrCountry *string `json:"strCountry,omitempty"`
	StrCountryCode *string `json:"strCountryCode,omitempty"`
	StrDescriptionEN *string `json:"strDescriptionEN,omitempty"`
	StrDisbanded *string `json:"strDisbanded,omitempty"`
	StrDiscogsID *string `json:"strDiscogsID,omitempty"`
	StrFacebook *string `json:"strFacebook,omitempty"`
	StrGender *string `json:"strGender,omitempty"`
	StrGeniusID *string `json:"strGeniusID,omitempty"`
	StrGenre *string `json:"strGenre,omitempty"`
	StrISNIcode *string `json:"strISNIcode,omitempty"`
	StrItunesID *string `json:"strItunesID,omitempty"`
	StrLabel *string `json:"strLabel,omitempty"`
	StrLastFMChart *string `json:"strLastFMChart,omitempty"`
	StrLocation *string `json:"strLocation,omitempty"`
	StrLocked *string `json:"strLocked,omitempty"`
	StrLyricWikiID *string `json:"strLyricWikiID,omitempty"`
	StrMood *string `json:"strMood,omitempty"`
	StrMusicBrainzAlbumID *string `json:"strMusicBrainzAlbumID,omitempty"`
	StrMusicBrainzArtistID *string `json:"strMusicBrainzArtistID,omitempty"`
	StrMusicBrainzID *string `json:"strMusicBrainzID,omitempty"`
	StrMusicMozID *string `json:"strMusicMozID,omitempty"`
	StrMusicVid *string `json:"strMusicVid,omitempty"`
	StrMusicVidCompany *string `json:"strMusicVidCompany,omitempty"`
	StrMusicVidDirector *string `json:"strMusicVidDirector,omitempty"`
	StrMusicVidScreen1 *string `json:"strMusicVidScreen1,omitempty"`
	StrMusicVidScreen2 *string `json:"strMusicVidScreen2,omitempty"`
	StrMusicVidScreen3 *string `json:"strMusicVidScreen3,omitempty"`
	StrRateYourMusicID *string `json:"strRateYourMusicID,omitempty"`
	StrReleaseFormat *string `json:"strReleaseFormat,omitempty"`
	StrReview *string `json:"strReview,omitempty"`
	StrSpeed *string `json:"strSpeed,omitempty"`
	StrStyle *string `json:"strStyle,omitempty"`
	StrTheme *string `json:"strTheme,omitempty"`
	StrTrack *string `json:"strTrack,omitempty"`
	StrTrack3x3 *string `json:"strTrack3x3,omitempty"`
	StrTrackLyrics *string `json:"strTrackLyrics,omitempty"`
	StrTrackThumb *string `json:"strTrackThumb,omitempty"`
	StrTwitter *string `json:"strTwitter,omitempty"`
	StrWebsite *string `json:"strWebsite,omitempty"`
	StrWikidataID *string `json:"strWikidataID,omitempty"`
	StrWikipediaID *string `json:"strWikipediaID,omitempty"`
}

// V1LookupLoadMatch is the typed request payload for V1Lookup.LoadTyped.
type V1LookupLoadMatch struct {
	ApiKey string `json:"api_key"`
}

// V1LookupListMatch is the typed request payload for V1Lookup.ListTyped.
type V1LookupListMatch struct {
	ApiKey string `json:"api_key"`
}

// V1Search is the typed data model for the v1_search entity.
type V1Search struct {
	Album *[]any `json:"album,omitempty"`
	IdAlbum *string `json:"idAlbum,omitempty"`
	IdArtist *string `json:"idArtist,omitempty"`
	IdIMVDB *string `json:"idIMVDB,omitempty"`
	IdLabel *string `json:"idLabel,omitempty"`
	IdLyric *string `json:"idLyric,omitempty"`
	IdTrack *string `json:"idTrack,omitempty"`
	IntBornYear *string `json:"intBornYear,omitempty"`
	IntCD *string `json:"intCD,omitempty"`
	IntCharted *string `json:"intCharted,omitempty"`
	IntDiedYear *string `json:"intDiedYear,omitempty"`
	IntDuration *string `json:"intDuration,omitempty"`
	IntFormedYear *string `json:"intFormedYear,omitempty"`
	IntLoved *string `json:"intLoved,omitempty"`
	IntMembers *string `json:"intMembers,omitempty"`
	IntMusicVidComments *string `json:"intMusicVidComments,omitempty"`
	IntMusicVidDislikes *string `json:"intMusicVidDislikes,omitempty"`
	IntMusicVidFavorites *string `json:"intMusicVidFavorites,omitempty"`
	IntMusicVidLikes *string `json:"intMusicVidLikes,omitempty"`
	IntMusicVidViews *string `json:"intMusicVidViews,omitempty"`
	IntSales *string `json:"intSales,omitempty"`
	IntScore *string `json:"intScore,omitempty"`
	IntScoreVotes *string `json:"intScoreVotes,omitempty"`
	IntTotalListeners *string `json:"intTotalListeners,omitempty"`
	IntTotalPlays *string `json:"intTotalPlays,omitempty"`
	IntTrackNumber *string `json:"intTrackNumber,omitempty"`
	IntYearReleased *string `json:"intYearReleased,omitempty"`
	StrAlbum *string `json:"strAlbum,omitempty"`
	StrAlbum3DCase *string `json:"strAlbum3DCase,omitempty"`
	StrAlbum3DFace *string `json:"strAlbum3DFace,omitempty"`
	StrAlbum3DFlat *string `json:"strAlbum3DFlat,omitempty"`
	StrAlbum3DThumb *string `json:"strAlbum3DThumb,omitempty"`
	StrAlbumCDart *string `json:"strAlbumCDart,omitempty"`
	StrAlbumSpine *string `json:"strAlbumSpine,omitempty"`
	StrAlbumStripped *string `json:"strAlbumStripped,omitempty"`
	StrAlbumThumb *string `json:"strAlbumThumb,omitempty"`
	StrAlbumThumbBack *string `json:"strAlbumThumbBack,omitempty"`
	StrAlbumThumbHQ *string `json:"strAlbumThumbHQ,omitempty"`
	StrAllMusicID *string `json:"strAllMusicID,omitempty"`
	StrAmazonID *string `json:"strAmazonID,omitempty"`
	StrArtist *string `json:"strArtist,omitempty"`
	StrArtistAlternate *string `json:"strArtistAlternate,omitempty"`
	StrArtistBanner *string `json:"strArtistBanner,omitempty"`
	StrArtistClearart *string `json:"strArtistClearart,omitempty"`
	StrArtistCutout *string `json:"strArtistCutout,omitempty"`
	StrArtistFanart *string `json:"strArtistFanart,omitempty"`
	StrArtistFanart2 *string `json:"strArtistFanart2,omitempty"`
	StrArtistFanart3 *string `json:"strArtistFanart3,omitempty"`
	StrArtistFanart4 *string `json:"strArtistFanart4,omitempty"`
	StrArtistLogo *string `json:"strArtistLogo,omitempty"`
	StrArtistStripped *string `json:"strArtistStripped,omitempty"`
	StrArtistThumb *string `json:"strArtistThumb,omitempty"`
	StrArtistWideThumb *string `json:"strArtistWideThumb,omitempty"`
	StrBBCReviewID *string `json:"strBBCReviewID,omitempty"`
	StrBiographyEN *string `json:"strBiographyEN,omitempty"`
	StrCountry *string `json:"strCountry,omitempty"`
	StrCountryCode *string `json:"strCountryCode,omitempty"`
	StrDescriptionEN *string `json:"strDescriptionEN,omitempty"`
	StrDisbanded *string `json:"strDisbanded,omitempty"`
	StrDiscogsID *string `json:"strDiscogsID,omitempty"`
	StrFacebook *string `json:"strFacebook,omitempty"`
	StrGender *string `json:"strGender,omitempty"`
	StrGeniusID *string `json:"strGeniusID,omitempty"`
	StrGenre *string `json:"strGenre,omitempty"`
	StrISNIcode *string `json:"strISNIcode,omitempty"`
	StrItunesID *string `json:"strItunesID,omitempty"`
	StrLabel *string `json:"strLabel,omitempty"`
	StrLastFMChart *string `json:"strLastFMChart,omitempty"`
	StrLocation *string `json:"strLocation,omitempty"`
	StrLocked *string `json:"strLocked,omitempty"`
	StrLyricWikiID *string `json:"strLyricWikiID,omitempty"`
	StrMood *string `json:"strMood,omitempty"`
	StrMusicBrainzAlbumID *string `json:"strMusicBrainzAlbumID,omitempty"`
	StrMusicBrainzArtistID *string `json:"strMusicBrainzArtistID,omitempty"`
	StrMusicBrainzID *string `json:"strMusicBrainzID,omitempty"`
	StrMusicMozID *string `json:"strMusicMozID,omitempty"`
	StrMusicVid *string `json:"strMusicVid,omitempty"`
	StrMusicVidCompany *string `json:"strMusicVidCompany,omitempty"`
	StrMusicVidDirector *string `json:"strMusicVidDirector,omitempty"`
	StrMusicVidScreen1 *string `json:"strMusicVidScreen1,omitempty"`
	StrMusicVidScreen2 *string `json:"strMusicVidScreen2,omitempty"`
	StrMusicVidScreen3 *string `json:"strMusicVidScreen3,omitempty"`
	StrRateYourMusicID *string `json:"strRateYourMusicID,omitempty"`
	StrReleaseFormat *string `json:"strReleaseFormat,omitempty"`
	StrReview *string `json:"strReview,omitempty"`
	StrSpeed *string `json:"strSpeed,omitempty"`
	StrStyle *string `json:"strStyle,omitempty"`
	StrTheme *string `json:"strTheme,omitempty"`
	StrTrack *string `json:"strTrack,omitempty"`
	StrTrack3x3 *string `json:"strTrack3x3,omitempty"`
	StrTrackLyrics *string `json:"strTrackLyrics,omitempty"`
	StrTrackThumb *string `json:"strTrackThumb,omitempty"`
	StrTwitter *string `json:"strTwitter,omitempty"`
	StrWebsite *string `json:"strWebsite,omitempty"`
	StrWikidataID *string `json:"strWikidataID,omitempty"`
	StrWikipediaID *string `json:"strWikipediaID,omitempty"`
}

// V1SearchLoadMatch is the typed request payload for V1Search.LoadTyped.
type V1SearchLoadMatch struct {
	ApiKey string `json:"api_key"`
}

// V1SearchListMatch is the typed request payload for V1Search.ListTyped.
type V1SearchListMatch struct {
	ApiKey string `json:"api_key"`
}

// V2List is the typed data model for the v2_list entity.
type V2List struct {
	Album *[]any `json:"album,omitempty"`
}

// V2ListLoadMatch is the typed request payload for V2List.LoadTyped.
type V2ListLoadMatch struct {
	IdArtist int `json:"id_artist"`
}

// V2Lookup is the typed data model for the v2_lookup entity.
type V2Lookup struct {
	Album *[]any `json:"album,omitempty"`
	Artists *[]any `json:"artists,omitempty"`
	Track *[]any `json:"track,omitempty"`
}

// V2LookupLoadMatch is the typed request payload for V2Lookup.LoadTyped.
type V2LookupLoadMatch struct {
	IdAlbum *int `json:"id_album,omitempty"`
	IdArtist *int `json:"id_artist,omitempty"`
	IdTrack *int `json:"id_track,omitempty"`
	MusicBrainzId *string `json:"music_brainz_id,omitempty"`
}

// V2Search is the typed data model for the v2_search entity.
type V2Search struct {
	Album *[]any `json:"album,omitempty"`
	Artists *[]any `json:"artists,omitempty"`
	Track *[]any `json:"track,omitempty"`
}

// V2SearchLoadMatch is the typed request payload for V2Search.LoadTyped.
type V2SearchLoadMatch struct {
	AlbumName *string `json:"album_name,omitempty"`
	ArtistName *string `json:"artist_name,omitempty"`
	TrackName *string `json:"track_name,omitempty"`
}

// asMap turns a typed request/data struct into the map[string]any the
// runtime op pipeline consumes, honouring the json tags above.
func asMap(v any) map[string]any {
	out := map[string]any{}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}

// entityData unwraps an entity to its data map.
//
// Operations resolve to the ENTITY, not the raw data (see AGENTS.md), and an
// entity's fields are UNEXPORTED — marshalling one directly yields `{}`, so
// every typed accessor would silently hand back a zero-valued struct. The
// typed boundary therefore takes the data hop first.
func entityData(v any) any {
	if ent, ok := v.(core.Entity); ok {
		return ent.Data()
	}
	return v
}

// typedFrom decodes a runtime value (an entity, or the map[string]any the op
// pipeline produced) into a typed model T via a JSON round-trip. On any error
// it returns the zero value of T; the op's own (value, error) tuple carries
// the real error.
func typedFrom[T any](v any) T {
	var out T
	v = entityData(v)
	if v == nil {
		return out
	}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}

// typedSliceFrom decodes a runtime list value into a typed slice []T via a
// JSON round-trip, for list ops. `list` resolves to a slice of ENTITY
// instances, so each element takes the data hop.
func typedSliceFrom[T any](v any) []T {
	var out []T
	if v == nil {
		return out
	}
	if list, ok := v.([]any); ok {
		unwrapped := make([]any, 0, len(list))
		for _, item := range list {
			unwrapped = append(unwrapped, entityData(item))
		}
		v = unwrapped
	}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}
