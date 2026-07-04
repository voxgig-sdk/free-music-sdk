// Typed models for the FreeMusic SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.

export interface V1List {
  id_album?: string
  id_artist?: string
  id_imvdb?: string
  id_lyric?: string
  id_track?: string
  int_cd?: string
  int_duration?: string
  int_loved?: string
  int_music_vid_comment?: string
  int_music_vid_dislike?: string
  int_music_vid_favorite?: string
  int_music_vid_like?: string
  int_music_vid_view?: string
  int_score?: string
  int_score_vote?: string
  int_total_listener?: string
  int_total_play?: string
  int_track_number?: string
  str_album?: string
  str_artist?: string
  str_artist_alternate?: string
  str_description_en?: string
  str_genre?: string
  str_locked?: string
  str_mood?: string
  str_music_brainz_album_id?: string
  str_music_brainz_artist_id?: string
  str_music_brainz_id?: string
  str_music_vid?: string
  str_music_vid_company?: string
  str_music_vid_director?: string
  str_music_vid_screen1?: string
  str_music_vid_screen2?: string
  str_music_vid_screen3?: string
  str_style?: string
  str_theme?: string
  str_track?: string
  str_track3x3?: string
  str_track_lyric?: string
  str_track_thumb?: string
  trending?: any[]
}

export interface V1ListLoadMatch {
  api_key: string
}

export interface V1ListListMatch {
  api_key: string
}

export interface V1Lookup {
  id_album?: string
  id_artist?: string
  id_imvdb?: string
  id_label?: string
  id_lyric?: string
  id_track?: string
  int_born_year?: string
  int_cd?: string
  int_charted?: string
  int_died_year?: string
  int_duration?: string
  int_formed_year?: string
  int_loved?: string
  int_member?: string
  int_music_vid_comment?: string
  int_music_vid_dislike?: string
  int_music_vid_favorite?: string
  int_music_vid_like?: string
  int_music_vid_view?: string
  int_sale?: string
  int_score?: string
  int_score_vote?: string
  int_total_listener?: string
  int_total_play?: string
  int_track_number?: string
  int_year_released?: string
  str_album?: string
  str_album3_d_case?: string
  str_album3_d_face?: string
  str_album3_d_flat?: string
  str_album3_d_thumb?: string
  str_album_c_dart?: string
  str_album_spine?: string
  str_album_stripped?: string
  str_album_thumb?: string
  str_album_thumb_back?: string
  str_album_thumb_hq?: string
  str_all_music_id?: string
  str_amazon_id?: string
  str_artist?: string
  str_artist_alternate?: string
  str_artist_banner?: string
  str_artist_clearart?: string
  str_artist_cutout?: string
  str_artist_fanart?: string
  str_artist_fanart2?: string
  str_artist_fanart3?: string
  str_artist_fanart4?: string
  str_artist_logo?: string
  str_artist_stripped?: string
  str_artist_thumb?: string
  str_artist_wide_thumb?: string
  str_bbc_review_id?: string
  str_biography_en?: string
  str_country?: string
  str_country_code?: string
  str_description_en?: string
  str_disbanded?: string
  str_discogs_id?: string
  str_facebook?: string
  str_gender?: string
  str_genius_id?: string
  str_genre?: string
  str_isn_icode?: string
  str_itunes_id?: string
  str_label?: string
  str_last_fm_chart?: string
  str_location?: string
  str_locked?: string
  str_lyric_wiki_id?: string
  str_mood?: string
  str_music_brainz_album_id?: string
  str_music_brainz_artist_id?: string
  str_music_brainz_id?: string
  str_music_moz_id?: string
  str_music_vid?: string
  str_music_vid_company?: string
  str_music_vid_director?: string
  str_music_vid_screen1?: string
  str_music_vid_screen2?: string
  str_music_vid_screen3?: string
  str_rate_your_music_id?: string
  str_release_format?: string
  str_review?: string
  str_speed?: string
  str_style?: string
  str_theme?: string
  str_track?: string
  str_track3x3?: string
  str_track_lyric?: string
  str_track_thumb?: string
  str_twitter?: string
  str_website?: string
  str_wikidata_id?: string
  str_wikipedia_id?: string
}

export interface V1LookupLoadMatch {
  api_key: string
}

export interface V1LookupListMatch {
  api_key: string
}

export interface V1Search {
  album?: any[]
  id_album?: string
  id_artist?: string
  id_imvdb?: string
  id_label?: string
  id_lyric?: string
  id_track?: string
  int_born_year?: string
  int_cd?: string
  int_charted?: string
  int_died_year?: string
  int_duration?: string
  int_formed_year?: string
  int_loved?: string
  int_member?: string
  int_music_vid_comment?: string
  int_music_vid_dislike?: string
  int_music_vid_favorite?: string
  int_music_vid_like?: string
  int_music_vid_view?: string
  int_sale?: string
  int_score?: string
  int_score_vote?: string
  int_total_listener?: string
  int_total_play?: string
  int_track_number?: string
  int_year_released?: string
  str_album?: string
  str_album3_d_case?: string
  str_album3_d_face?: string
  str_album3_d_flat?: string
  str_album3_d_thumb?: string
  str_album_c_dart?: string
  str_album_spine?: string
  str_album_stripped?: string
  str_album_thumb?: string
  str_album_thumb_back?: string
  str_album_thumb_hq?: string
  str_all_music_id?: string
  str_amazon_id?: string
  str_artist?: string
  str_artist_alternate?: string
  str_artist_banner?: string
  str_artist_clearart?: string
  str_artist_cutout?: string
  str_artist_fanart?: string
  str_artist_fanart2?: string
  str_artist_fanart3?: string
  str_artist_fanart4?: string
  str_artist_logo?: string
  str_artist_stripped?: string
  str_artist_thumb?: string
  str_artist_wide_thumb?: string
  str_bbc_review_id?: string
  str_biography_en?: string
  str_country?: string
  str_country_code?: string
  str_description_en?: string
  str_disbanded?: string
  str_discogs_id?: string
  str_facebook?: string
  str_gender?: string
  str_genius_id?: string
  str_genre?: string
  str_isn_icode?: string
  str_itunes_id?: string
  str_label?: string
  str_last_fm_chart?: string
  str_location?: string
  str_locked?: string
  str_lyric_wiki_id?: string
  str_mood?: string
  str_music_brainz_album_id?: string
  str_music_brainz_artist_id?: string
  str_music_brainz_id?: string
  str_music_moz_id?: string
  str_music_vid?: string
  str_music_vid_company?: string
  str_music_vid_director?: string
  str_music_vid_screen1?: string
  str_music_vid_screen2?: string
  str_music_vid_screen3?: string
  str_rate_your_music_id?: string
  str_release_format?: string
  str_review?: string
  str_speed?: string
  str_style?: string
  str_theme?: string
  str_track?: string
  str_track3x3?: string
  str_track_lyric?: string
  str_track_thumb?: string
  str_twitter?: string
  str_website?: string
  str_wikidata_id?: string
  str_wikipedia_id?: string
}

export interface V1SearchLoadMatch {
  api_key: string
}

export interface V1SearchListMatch {
  api_key: string
}

export interface V2List {
  album?: any[]
}

export interface V2ListLoadMatch {
  id_artist: number
}

export interface V2Lookup {
  album?: any[]
  artist?: any[]
  track?: any[]
}

export interface V2LookupLoadMatch {
  id_album: number
  id_artist: number
  id_track: number
  music_brainz_id: string
}

export interface V2Search {
  album?: any[]
  artist?: any[]
  track?: any[]
}

export interface V2SearchLoadMatch {
  album_name: string
  artist_name: string
  track_name: string
}

