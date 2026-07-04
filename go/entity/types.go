// Typed models for the FreeMusic SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.
package entity

import "encoding/json"

// V1List is the typed data model for the v1_list entity.
type V1List struct {
	IdAlbum *string `json:"id_album,omitempty"`
	IdArtist *string `json:"id_artist,omitempty"`
	IdImvdb *string `json:"id_imvdb,omitempty"`
	IdLyric *string `json:"id_lyric,omitempty"`
	IdTrack *string `json:"id_track,omitempty"`
	IntCd *string `json:"int_cd,omitempty"`
	IntDuration *string `json:"int_duration,omitempty"`
	IntLoved *string `json:"int_loved,omitempty"`
	IntMusicVidComment *string `json:"int_music_vid_comment,omitempty"`
	IntMusicVidDislike *string `json:"int_music_vid_dislike,omitempty"`
	IntMusicVidFavorite *string `json:"int_music_vid_favorite,omitempty"`
	IntMusicVidLike *string `json:"int_music_vid_like,omitempty"`
	IntMusicVidView *string `json:"int_music_vid_view,omitempty"`
	IntScore *string `json:"int_score,omitempty"`
	IntScoreVote *string `json:"int_score_vote,omitempty"`
	IntTotalListener *string `json:"int_total_listener,omitempty"`
	IntTotalPlay *string `json:"int_total_play,omitempty"`
	IntTrackNumber *string `json:"int_track_number,omitempty"`
	StrAlbum *string `json:"str_album,omitempty"`
	StrArtist *string `json:"str_artist,omitempty"`
	StrArtistAlternate *string `json:"str_artist_alternate,omitempty"`
	StrDescriptionEn *string `json:"str_description_en,omitempty"`
	StrGenre *string `json:"str_genre,omitempty"`
	StrLocked *string `json:"str_locked,omitempty"`
	StrMood *string `json:"str_mood,omitempty"`
	StrMusicBrainzAlbumId *string `json:"str_music_brainz_album_id,omitempty"`
	StrMusicBrainzArtistId *string `json:"str_music_brainz_artist_id,omitempty"`
	StrMusicBrainzId *string `json:"str_music_brainz_id,omitempty"`
	StrMusicVid *string `json:"str_music_vid,omitempty"`
	StrMusicVidCompany *string `json:"str_music_vid_company,omitempty"`
	StrMusicVidDirector *string `json:"str_music_vid_director,omitempty"`
	StrMusicVidScreen1 *string `json:"str_music_vid_screen1,omitempty"`
	StrMusicVidScreen2 *string `json:"str_music_vid_screen2,omitempty"`
	StrMusicVidScreen3 *string `json:"str_music_vid_screen3,omitempty"`
	StrStyle *string `json:"str_style,omitempty"`
	StrTheme *string `json:"str_theme,omitempty"`
	StrTrack *string `json:"str_track,omitempty"`
	StrTrack3x3 *string `json:"str_track3x3,omitempty"`
	StrTrackLyric *string `json:"str_track_lyric,omitempty"`
	StrTrackThumb *string `json:"str_track_thumb,omitempty"`
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
	IdAlbum *string `json:"id_album,omitempty"`
	IdArtist *string `json:"id_artist,omitempty"`
	IdImvdb *string `json:"id_imvdb,omitempty"`
	IdLabel *string `json:"id_label,omitempty"`
	IdLyric *string `json:"id_lyric,omitempty"`
	IdTrack *string `json:"id_track,omitempty"`
	IntBornYear *string `json:"int_born_year,omitempty"`
	IntCd *string `json:"int_cd,omitempty"`
	IntCharted *string `json:"int_charted,omitempty"`
	IntDiedYear *string `json:"int_died_year,omitempty"`
	IntDuration *string `json:"int_duration,omitempty"`
	IntFormedYear *string `json:"int_formed_year,omitempty"`
	IntLoved *string `json:"int_loved,omitempty"`
	IntMember *string `json:"int_member,omitempty"`
	IntMusicVidComment *string `json:"int_music_vid_comment,omitempty"`
	IntMusicVidDislike *string `json:"int_music_vid_dislike,omitempty"`
	IntMusicVidFavorite *string `json:"int_music_vid_favorite,omitempty"`
	IntMusicVidLike *string `json:"int_music_vid_like,omitempty"`
	IntMusicVidView *string `json:"int_music_vid_view,omitempty"`
	IntSale *string `json:"int_sale,omitempty"`
	IntScore *string `json:"int_score,omitempty"`
	IntScoreVote *string `json:"int_score_vote,omitempty"`
	IntTotalListener *string `json:"int_total_listener,omitempty"`
	IntTotalPlay *string `json:"int_total_play,omitempty"`
	IntTrackNumber *string `json:"int_track_number,omitempty"`
	IntYearReleased *string `json:"int_year_released,omitempty"`
	StrAlbum *string `json:"str_album,omitempty"`
	StrAlbum3DCase *string `json:"str_album3_d_case,omitempty"`
	StrAlbum3DFace *string `json:"str_album3_d_face,omitempty"`
	StrAlbum3DFlat *string `json:"str_album3_d_flat,omitempty"`
	StrAlbum3DThumb *string `json:"str_album3_d_thumb,omitempty"`
	StrAlbumCDart *string `json:"str_album_c_dart,omitempty"`
	StrAlbumSpine *string `json:"str_album_spine,omitempty"`
	StrAlbumStripped *string `json:"str_album_stripped,omitempty"`
	StrAlbumThumb *string `json:"str_album_thumb,omitempty"`
	StrAlbumThumbBack *string `json:"str_album_thumb_back,omitempty"`
	StrAlbumThumbHq *string `json:"str_album_thumb_hq,omitempty"`
	StrAllMusicId *string `json:"str_all_music_id,omitempty"`
	StrAmazonId *string `json:"str_amazon_id,omitempty"`
	StrArtist *string `json:"str_artist,omitempty"`
	StrArtistAlternate *string `json:"str_artist_alternate,omitempty"`
	StrArtistBanner *string `json:"str_artist_banner,omitempty"`
	StrArtistClearart *string `json:"str_artist_clearart,omitempty"`
	StrArtistCutout *string `json:"str_artist_cutout,omitempty"`
	StrArtistFanart *string `json:"str_artist_fanart,omitempty"`
	StrArtistFanart2 *string `json:"str_artist_fanart2,omitempty"`
	StrArtistFanart3 *string `json:"str_artist_fanart3,omitempty"`
	StrArtistFanart4 *string `json:"str_artist_fanart4,omitempty"`
	StrArtistLogo *string `json:"str_artist_logo,omitempty"`
	StrArtistStripped *string `json:"str_artist_stripped,omitempty"`
	StrArtistThumb *string `json:"str_artist_thumb,omitempty"`
	StrArtistWideThumb *string `json:"str_artist_wide_thumb,omitempty"`
	StrBbcReviewId *string `json:"str_bbc_review_id,omitempty"`
	StrBiographyEn *string `json:"str_biography_en,omitempty"`
	StrCountry *string `json:"str_country,omitempty"`
	StrCountryCode *string `json:"str_country_code,omitempty"`
	StrDescriptionEn *string `json:"str_description_en,omitempty"`
	StrDisbanded *string `json:"str_disbanded,omitempty"`
	StrDiscogsId *string `json:"str_discogs_id,omitempty"`
	StrFacebook *string `json:"str_facebook,omitempty"`
	StrGender *string `json:"str_gender,omitempty"`
	StrGeniusId *string `json:"str_genius_id,omitempty"`
	StrGenre *string `json:"str_genre,omitempty"`
	StrIsnIcode *string `json:"str_isn_icode,omitempty"`
	StrItunesId *string `json:"str_itunes_id,omitempty"`
	StrLabel *string `json:"str_label,omitempty"`
	StrLastFmChart *string `json:"str_last_fm_chart,omitempty"`
	StrLocation *string `json:"str_location,omitempty"`
	StrLocked *string `json:"str_locked,omitempty"`
	StrLyricWikiId *string `json:"str_lyric_wiki_id,omitempty"`
	StrMood *string `json:"str_mood,omitempty"`
	StrMusicBrainzAlbumId *string `json:"str_music_brainz_album_id,omitempty"`
	StrMusicBrainzArtistId *string `json:"str_music_brainz_artist_id,omitempty"`
	StrMusicBrainzId *string `json:"str_music_brainz_id,omitempty"`
	StrMusicMozId *string `json:"str_music_moz_id,omitempty"`
	StrMusicVid *string `json:"str_music_vid,omitempty"`
	StrMusicVidCompany *string `json:"str_music_vid_company,omitempty"`
	StrMusicVidDirector *string `json:"str_music_vid_director,omitempty"`
	StrMusicVidScreen1 *string `json:"str_music_vid_screen1,omitempty"`
	StrMusicVidScreen2 *string `json:"str_music_vid_screen2,omitempty"`
	StrMusicVidScreen3 *string `json:"str_music_vid_screen3,omitempty"`
	StrRateYourMusicId *string `json:"str_rate_your_music_id,omitempty"`
	StrReleaseFormat *string `json:"str_release_format,omitempty"`
	StrReview *string `json:"str_review,omitempty"`
	StrSpeed *string `json:"str_speed,omitempty"`
	StrStyle *string `json:"str_style,omitempty"`
	StrTheme *string `json:"str_theme,omitempty"`
	StrTrack *string `json:"str_track,omitempty"`
	StrTrack3x3 *string `json:"str_track3x3,omitempty"`
	StrTrackLyric *string `json:"str_track_lyric,omitempty"`
	StrTrackThumb *string `json:"str_track_thumb,omitempty"`
	StrTwitter *string `json:"str_twitter,omitempty"`
	StrWebsite *string `json:"str_website,omitempty"`
	StrWikidataId *string `json:"str_wikidata_id,omitempty"`
	StrWikipediaId *string `json:"str_wikipedia_id,omitempty"`
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
	IdAlbum *string `json:"id_album,omitempty"`
	IdArtist *string `json:"id_artist,omitempty"`
	IdImvdb *string `json:"id_imvdb,omitempty"`
	IdLabel *string `json:"id_label,omitempty"`
	IdLyric *string `json:"id_lyric,omitempty"`
	IdTrack *string `json:"id_track,omitempty"`
	IntBornYear *string `json:"int_born_year,omitempty"`
	IntCd *string `json:"int_cd,omitempty"`
	IntCharted *string `json:"int_charted,omitempty"`
	IntDiedYear *string `json:"int_died_year,omitempty"`
	IntDuration *string `json:"int_duration,omitempty"`
	IntFormedYear *string `json:"int_formed_year,omitempty"`
	IntLoved *string `json:"int_loved,omitempty"`
	IntMember *string `json:"int_member,omitempty"`
	IntMusicVidComment *string `json:"int_music_vid_comment,omitempty"`
	IntMusicVidDislike *string `json:"int_music_vid_dislike,omitempty"`
	IntMusicVidFavorite *string `json:"int_music_vid_favorite,omitempty"`
	IntMusicVidLike *string `json:"int_music_vid_like,omitempty"`
	IntMusicVidView *string `json:"int_music_vid_view,omitempty"`
	IntSale *string `json:"int_sale,omitempty"`
	IntScore *string `json:"int_score,omitempty"`
	IntScoreVote *string `json:"int_score_vote,omitempty"`
	IntTotalListener *string `json:"int_total_listener,omitempty"`
	IntTotalPlay *string `json:"int_total_play,omitempty"`
	IntTrackNumber *string `json:"int_track_number,omitempty"`
	IntYearReleased *string `json:"int_year_released,omitempty"`
	StrAlbum *string `json:"str_album,omitempty"`
	StrAlbum3DCase *string `json:"str_album3_d_case,omitempty"`
	StrAlbum3DFace *string `json:"str_album3_d_face,omitempty"`
	StrAlbum3DFlat *string `json:"str_album3_d_flat,omitempty"`
	StrAlbum3DThumb *string `json:"str_album3_d_thumb,omitempty"`
	StrAlbumCDart *string `json:"str_album_c_dart,omitempty"`
	StrAlbumSpine *string `json:"str_album_spine,omitempty"`
	StrAlbumStripped *string `json:"str_album_stripped,omitempty"`
	StrAlbumThumb *string `json:"str_album_thumb,omitempty"`
	StrAlbumThumbBack *string `json:"str_album_thumb_back,omitempty"`
	StrAlbumThumbHq *string `json:"str_album_thumb_hq,omitempty"`
	StrAllMusicId *string `json:"str_all_music_id,omitempty"`
	StrAmazonId *string `json:"str_amazon_id,omitempty"`
	StrArtist *string `json:"str_artist,omitempty"`
	StrArtistAlternate *string `json:"str_artist_alternate,omitempty"`
	StrArtistBanner *string `json:"str_artist_banner,omitempty"`
	StrArtistClearart *string `json:"str_artist_clearart,omitempty"`
	StrArtistCutout *string `json:"str_artist_cutout,omitempty"`
	StrArtistFanart *string `json:"str_artist_fanart,omitempty"`
	StrArtistFanart2 *string `json:"str_artist_fanart2,omitempty"`
	StrArtistFanart3 *string `json:"str_artist_fanart3,omitempty"`
	StrArtistFanart4 *string `json:"str_artist_fanart4,omitempty"`
	StrArtistLogo *string `json:"str_artist_logo,omitempty"`
	StrArtistStripped *string `json:"str_artist_stripped,omitempty"`
	StrArtistThumb *string `json:"str_artist_thumb,omitempty"`
	StrArtistWideThumb *string `json:"str_artist_wide_thumb,omitempty"`
	StrBbcReviewId *string `json:"str_bbc_review_id,omitempty"`
	StrBiographyEn *string `json:"str_biography_en,omitempty"`
	StrCountry *string `json:"str_country,omitempty"`
	StrCountryCode *string `json:"str_country_code,omitempty"`
	StrDescriptionEn *string `json:"str_description_en,omitempty"`
	StrDisbanded *string `json:"str_disbanded,omitempty"`
	StrDiscogsId *string `json:"str_discogs_id,omitempty"`
	StrFacebook *string `json:"str_facebook,omitempty"`
	StrGender *string `json:"str_gender,omitempty"`
	StrGeniusId *string `json:"str_genius_id,omitempty"`
	StrGenre *string `json:"str_genre,omitempty"`
	StrIsnIcode *string `json:"str_isn_icode,omitempty"`
	StrItunesId *string `json:"str_itunes_id,omitempty"`
	StrLabel *string `json:"str_label,omitempty"`
	StrLastFmChart *string `json:"str_last_fm_chart,omitempty"`
	StrLocation *string `json:"str_location,omitempty"`
	StrLocked *string `json:"str_locked,omitempty"`
	StrLyricWikiId *string `json:"str_lyric_wiki_id,omitempty"`
	StrMood *string `json:"str_mood,omitempty"`
	StrMusicBrainzAlbumId *string `json:"str_music_brainz_album_id,omitempty"`
	StrMusicBrainzArtistId *string `json:"str_music_brainz_artist_id,omitempty"`
	StrMusicBrainzId *string `json:"str_music_brainz_id,omitempty"`
	StrMusicMozId *string `json:"str_music_moz_id,omitempty"`
	StrMusicVid *string `json:"str_music_vid,omitempty"`
	StrMusicVidCompany *string `json:"str_music_vid_company,omitempty"`
	StrMusicVidDirector *string `json:"str_music_vid_director,omitempty"`
	StrMusicVidScreen1 *string `json:"str_music_vid_screen1,omitempty"`
	StrMusicVidScreen2 *string `json:"str_music_vid_screen2,omitempty"`
	StrMusicVidScreen3 *string `json:"str_music_vid_screen3,omitempty"`
	StrRateYourMusicId *string `json:"str_rate_your_music_id,omitempty"`
	StrReleaseFormat *string `json:"str_release_format,omitempty"`
	StrReview *string `json:"str_review,omitempty"`
	StrSpeed *string `json:"str_speed,omitempty"`
	StrStyle *string `json:"str_style,omitempty"`
	StrTheme *string `json:"str_theme,omitempty"`
	StrTrack *string `json:"str_track,omitempty"`
	StrTrack3x3 *string `json:"str_track3x3,omitempty"`
	StrTrackLyric *string `json:"str_track_lyric,omitempty"`
	StrTrackThumb *string `json:"str_track_thumb,omitempty"`
	StrTwitter *string `json:"str_twitter,omitempty"`
	StrWebsite *string `json:"str_website,omitempty"`
	StrWikidataId *string `json:"str_wikidata_id,omitempty"`
	StrWikipediaId *string `json:"str_wikipedia_id,omitempty"`
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
	Artist *[]any `json:"artist,omitempty"`
	Track *[]any `json:"track,omitempty"`
}

// V2LookupLoadMatch is the typed request payload for V2Lookup.LoadTyped.
type V2LookupLoadMatch struct {
	IdAlbum int `json:"id_album"`
	IdArtist int `json:"id_artist"`
	IdTrack int `json:"id_track"`
	MusicBrainzId string `json:"music_brainz_id"`
}

// V2Search is the typed data model for the v2_search entity.
type V2Search struct {
	Album *[]any `json:"album,omitempty"`
	Artist *[]any `json:"artist,omitempty"`
	Track *[]any `json:"track,omitempty"`
}

// V2SearchLoadMatch is the typed request payload for V2Search.LoadTyped.
type V2SearchLoadMatch struct {
	AlbumName string `json:"album_name"`
	ArtistName string `json:"artist_name"`
	TrackName string `json:"track_name"`
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

// typedFrom decodes a runtime value (a map[string]any produced by the op
// pipeline) into a typed model T via a JSON round-trip. On any error it
// returns the zero value of T; the op's own (value, error) tuple carries the
// real error.
func typedFrom[T any](v any) T {
	var out T
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

// typedSliceFrom decodes a runtime list value ([]any of maps) into a typed
// slice []T via a JSON round-trip, for list ops.
func typedSliceFrom[T any](v any) []T {
	var out []T
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
