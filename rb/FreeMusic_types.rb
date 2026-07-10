# frozen_string_literal: true

# Typed models for the FreeMusic SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Member types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Ruby types are unenforced; these YARD
# annotations document the shapes. Do not edit by hand.

# V1List entity data model.
#
# @!attribute [rw] id_album
#   @return [String, nil]
#
# @!attribute [rw] id_artist
#   @return [String, nil]
#
# @!attribute [rw] id_imvdb
#   @return [String, nil]
#
# @!attribute [rw] id_lyric
#   @return [String, nil]
#
# @!attribute [rw] id_track
#   @return [String, nil]
#
# @!attribute [rw] int_cd
#   @return [String, nil]
#
# @!attribute [rw] int_duration
#   @return [String, nil]
#
# @!attribute [rw] int_loved
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_comment
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_dislike
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_favorite
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_like
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_view
#   @return [String, nil]
#
# @!attribute [rw] int_score
#   @return [String, nil]
#
# @!attribute [rw] int_score_vote
#   @return [String, nil]
#
# @!attribute [rw] int_total_listener
#   @return [String, nil]
#
# @!attribute [rw] int_total_play
#   @return [String, nil]
#
# @!attribute [rw] int_track_number
#   @return [String, nil]
#
# @!attribute [rw] str_album
#   @return [String, nil]
#
# @!attribute [rw] str_artist
#   @return [String, nil]
#
# @!attribute [rw] str_artist_alternate
#   @return [String, nil]
#
# @!attribute [rw] str_description_en
#   @return [String, nil]
#
# @!attribute [rw] str_genre
#   @return [String, nil]
#
# @!attribute [rw] str_locked
#   @return [String, nil]
#
# @!attribute [rw] str_mood
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_album_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_artist_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_company
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_director
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen1
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen2
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen3
#   @return [String, nil]
#
# @!attribute [rw] str_style
#   @return [String, nil]
#
# @!attribute [rw] str_theme
#   @return [String, nil]
#
# @!attribute [rw] str_track
#   @return [String, nil]
#
# @!attribute [rw] str_track3x3
#   @return [String, nil]
#
# @!attribute [rw] str_track_lyric
#   @return [String, nil]
#
# @!attribute [rw] str_track_thumb
#   @return [String, nil]
#
# @!attribute [rw] trending
#   @return [Array, nil]
V1List = Struct.new(
  :id_album,
  :id_artist,
  :id_imvdb,
  :id_lyric,
  :id_track,
  :int_cd,
  :int_duration,
  :int_loved,
  :int_music_vid_comment,
  :int_music_vid_dislike,
  :int_music_vid_favorite,
  :int_music_vid_like,
  :int_music_vid_view,
  :int_score,
  :int_score_vote,
  :int_total_listener,
  :int_total_play,
  :int_track_number,
  :str_album,
  :str_artist,
  :str_artist_alternate,
  :str_description_en,
  :str_genre,
  :str_locked,
  :str_mood,
  :str_music_brainz_album_id,
  :str_music_brainz_artist_id,
  :str_music_brainz_id,
  :str_music_vid,
  :str_music_vid_company,
  :str_music_vid_director,
  :str_music_vid_screen1,
  :str_music_vid_screen2,
  :str_music_vid_screen3,
  :str_style,
  :str_theme,
  :str_track,
  :str_track3x3,
  :str_track_lyric,
  :str_track_thumb,
  :trending,
  keyword_init: true
)

# Request payload for V1List#load.
#
# @!attribute [rw] api_key
#   @return [String]
V1ListLoadMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# Request payload for V1List#list.
#
# @!attribute [rw] api_key
#   @return [String]
V1ListListMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# V1Lookup entity data model.
#
# @!attribute [rw] id_album
#   @return [String, nil]
#
# @!attribute [rw] id_artist
#   @return [String, nil]
#
# @!attribute [rw] id_imvdb
#   @return [String, nil]
#
# @!attribute [rw] id_label
#   @return [String, nil]
#
# @!attribute [rw] id_lyric
#   @return [String, nil]
#
# @!attribute [rw] id_track
#   @return [String, nil]
#
# @!attribute [rw] int_born_year
#   @return [String, nil]
#
# @!attribute [rw] int_cd
#   @return [String, nil]
#
# @!attribute [rw] int_charted
#   @return [String, nil]
#
# @!attribute [rw] int_died_year
#   @return [String, nil]
#
# @!attribute [rw] int_duration
#   @return [String, nil]
#
# @!attribute [rw] int_formed_year
#   @return [String, nil]
#
# @!attribute [rw] int_loved
#   @return [String, nil]
#
# @!attribute [rw] int_member
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_comment
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_dislike
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_favorite
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_like
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_view
#   @return [String, nil]
#
# @!attribute [rw] int_sale
#   @return [String, nil]
#
# @!attribute [rw] int_score
#   @return [String, nil]
#
# @!attribute [rw] int_score_vote
#   @return [String, nil]
#
# @!attribute [rw] int_total_listener
#   @return [String, nil]
#
# @!attribute [rw] int_total_play
#   @return [String, nil]
#
# @!attribute [rw] int_track_number
#   @return [String, nil]
#
# @!attribute [rw] int_year_released
#   @return [String, nil]
#
# @!attribute [rw] str_album
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_case
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_face
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_flat
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_album_c_dart
#   @return [String, nil]
#
# @!attribute [rw] str_album_spine
#   @return [String, nil]
#
# @!attribute [rw] str_album_stripped
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb_back
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb_hq
#   @return [String, nil]
#
# @!attribute [rw] str_all_music_id
#   @return [String, nil]
#
# @!attribute [rw] str_amazon_id
#   @return [String, nil]
#
# @!attribute [rw] str_artist
#   @return [String, nil]
#
# @!attribute [rw] str_artist_alternate
#   @return [String, nil]
#
# @!attribute [rw] str_artist_banner
#   @return [String, nil]
#
# @!attribute [rw] str_artist_clearart
#   @return [String, nil]
#
# @!attribute [rw] str_artist_cutout
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart2
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart3
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart4
#   @return [String, nil]
#
# @!attribute [rw] str_artist_logo
#   @return [String, nil]
#
# @!attribute [rw] str_artist_stripped
#   @return [String, nil]
#
# @!attribute [rw] str_artist_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_artist_wide_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_bbc_review_id
#   @return [String, nil]
#
# @!attribute [rw] str_biography_en
#   @return [String, nil]
#
# @!attribute [rw] str_country
#   @return [String, nil]
#
# @!attribute [rw] str_country_code
#   @return [String, nil]
#
# @!attribute [rw] str_description_en
#   @return [String, nil]
#
# @!attribute [rw] str_disbanded
#   @return [String, nil]
#
# @!attribute [rw] str_discogs_id
#   @return [String, nil]
#
# @!attribute [rw] str_facebook
#   @return [String, nil]
#
# @!attribute [rw] str_gender
#   @return [String, nil]
#
# @!attribute [rw] str_genius_id
#   @return [String, nil]
#
# @!attribute [rw] str_genre
#   @return [String, nil]
#
# @!attribute [rw] str_isn_icode
#   @return [String, nil]
#
# @!attribute [rw] str_itunes_id
#   @return [String, nil]
#
# @!attribute [rw] str_label
#   @return [String, nil]
#
# @!attribute [rw] str_last_fm_chart
#   @return [String, nil]
#
# @!attribute [rw] str_location
#   @return [String, nil]
#
# @!attribute [rw] str_locked
#   @return [String, nil]
#
# @!attribute [rw] str_lyric_wiki_id
#   @return [String, nil]
#
# @!attribute [rw] str_mood
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_album_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_artist_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_moz_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_company
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_director
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen1
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen2
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen3
#   @return [String, nil]
#
# @!attribute [rw] str_rate_your_music_id
#   @return [String, nil]
#
# @!attribute [rw] str_release_format
#   @return [String, nil]
#
# @!attribute [rw] str_review
#   @return [String, nil]
#
# @!attribute [rw] str_speed
#   @return [String, nil]
#
# @!attribute [rw] str_style
#   @return [String, nil]
#
# @!attribute [rw] str_theme
#   @return [String, nil]
#
# @!attribute [rw] str_track
#   @return [String, nil]
#
# @!attribute [rw] str_track3x3
#   @return [String, nil]
#
# @!attribute [rw] str_track_lyric
#   @return [String, nil]
#
# @!attribute [rw] str_track_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_twitter
#   @return [String, nil]
#
# @!attribute [rw] str_website
#   @return [String, nil]
#
# @!attribute [rw] str_wikidata_id
#   @return [String, nil]
#
# @!attribute [rw] str_wikipedia_id
#   @return [String, nil]
V1Lookup = Struct.new(
  :id_album,
  :id_artist,
  :id_imvdb,
  :id_label,
  :id_lyric,
  :id_track,
  :int_born_year,
  :int_cd,
  :int_charted,
  :int_died_year,
  :int_duration,
  :int_formed_year,
  :int_loved,
  :int_member,
  :int_music_vid_comment,
  :int_music_vid_dislike,
  :int_music_vid_favorite,
  :int_music_vid_like,
  :int_music_vid_view,
  :int_sale,
  :int_score,
  :int_score_vote,
  :int_total_listener,
  :int_total_play,
  :int_track_number,
  :int_year_released,
  :str_album,
  :str_album3_d_case,
  :str_album3_d_face,
  :str_album3_d_flat,
  :str_album3_d_thumb,
  :str_album_c_dart,
  :str_album_spine,
  :str_album_stripped,
  :str_album_thumb,
  :str_album_thumb_back,
  :str_album_thumb_hq,
  :str_all_music_id,
  :str_amazon_id,
  :str_artist,
  :str_artist_alternate,
  :str_artist_banner,
  :str_artist_clearart,
  :str_artist_cutout,
  :str_artist_fanart,
  :str_artist_fanart2,
  :str_artist_fanart3,
  :str_artist_fanart4,
  :str_artist_logo,
  :str_artist_stripped,
  :str_artist_thumb,
  :str_artist_wide_thumb,
  :str_bbc_review_id,
  :str_biography_en,
  :str_country,
  :str_country_code,
  :str_description_en,
  :str_disbanded,
  :str_discogs_id,
  :str_facebook,
  :str_gender,
  :str_genius_id,
  :str_genre,
  :str_isn_icode,
  :str_itunes_id,
  :str_label,
  :str_last_fm_chart,
  :str_location,
  :str_locked,
  :str_lyric_wiki_id,
  :str_mood,
  :str_music_brainz_album_id,
  :str_music_brainz_artist_id,
  :str_music_brainz_id,
  :str_music_moz_id,
  :str_music_vid,
  :str_music_vid_company,
  :str_music_vid_director,
  :str_music_vid_screen1,
  :str_music_vid_screen2,
  :str_music_vid_screen3,
  :str_rate_your_music_id,
  :str_release_format,
  :str_review,
  :str_speed,
  :str_style,
  :str_theme,
  :str_track,
  :str_track3x3,
  :str_track_lyric,
  :str_track_thumb,
  :str_twitter,
  :str_website,
  :str_wikidata_id,
  :str_wikipedia_id,
  keyword_init: true
)

# Request payload for V1Lookup#load.
#
# @!attribute [rw] api_key
#   @return [String]
V1LookupLoadMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# Request payload for V1Lookup#list.
#
# @!attribute [rw] api_key
#   @return [String]
V1LookupListMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# V1Search entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
#
# @!attribute [rw] id_album
#   @return [String, nil]
#
# @!attribute [rw] id_artist
#   @return [String, nil]
#
# @!attribute [rw] id_imvdb
#   @return [String, nil]
#
# @!attribute [rw] id_label
#   @return [String, nil]
#
# @!attribute [rw] id_lyric
#   @return [String, nil]
#
# @!attribute [rw] id_track
#   @return [String, nil]
#
# @!attribute [rw] int_born_year
#   @return [String, nil]
#
# @!attribute [rw] int_cd
#   @return [String, nil]
#
# @!attribute [rw] int_charted
#   @return [String, nil]
#
# @!attribute [rw] int_died_year
#   @return [String, nil]
#
# @!attribute [rw] int_duration
#   @return [String, nil]
#
# @!attribute [rw] int_formed_year
#   @return [String, nil]
#
# @!attribute [rw] int_loved
#   @return [String, nil]
#
# @!attribute [rw] int_member
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_comment
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_dislike
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_favorite
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_like
#   @return [String, nil]
#
# @!attribute [rw] int_music_vid_view
#   @return [String, nil]
#
# @!attribute [rw] int_sale
#   @return [String, nil]
#
# @!attribute [rw] int_score
#   @return [String, nil]
#
# @!attribute [rw] int_score_vote
#   @return [String, nil]
#
# @!attribute [rw] int_total_listener
#   @return [String, nil]
#
# @!attribute [rw] int_total_play
#   @return [String, nil]
#
# @!attribute [rw] int_track_number
#   @return [String, nil]
#
# @!attribute [rw] int_year_released
#   @return [String, nil]
#
# @!attribute [rw] str_album
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_case
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_face
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_flat
#   @return [String, nil]
#
# @!attribute [rw] str_album3_d_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_album_c_dart
#   @return [String, nil]
#
# @!attribute [rw] str_album_spine
#   @return [String, nil]
#
# @!attribute [rw] str_album_stripped
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb_back
#   @return [String, nil]
#
# @!attribute [rw] str_album_thumb_hq
#   @return [String, nil]
#
# @!attribute [rw] str_all_music_id
#   @return [String, nil]
#
# @!attribute [rw] str_amazon_id
#   @return [String, nil]
#
# @!attribute [rw] str_artist
#   @return [String, nil]
#
# @!attribute [rw] str_artist_alternate
#   @return [String, nil]
#
# @!attribute [rw] str_artist_banner
#   @return [String, nil]
#
# @!attribute [rw] str_artist_clearart
#   @return [String, nil]
#
# @!attribute [rw] str_artist_cutout
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart2
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart3
#   @return [String, nil]
#
# @!attribute [rw] str_artist_fanart4
#   @return [String, nil]
#
# @!attribute [rw] str_artist_logo
#   @return [String, nil]
#
# @!attribute [rw] str_artist_stripped
#   @return [String, nil]
#
# @!attribute [rw] str_artist_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_artist_wide_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_bbc_review_id
#   @return [String, nil]
#
# @!attribute [rw] str_biography_en
#   @return [String, nil]
#
# @!attribute [rw] str_country
#   @return [String, nil]
#
# @!attribute [rw] str_country_code
#   @return [String, nil]
#
# @!attribute [rw] str_description_en
#   @return [String, nil]
#
# @!attribute [rw] str_disbanded
#   @return [String, nil]
#
# @!attribute [rw] str_discogs_id
#   @return [String, nil]
#
# @!attribute [rw] str_facebook
#   @return [String, nil]
#
# @!attribute [rw] str_gender
#   @return [String, nil]
#
# @!attribute [rw] str_genius_id
#   @return [String, nil]
#
# @!attribute [rw] str_genre
#   @return [String, nil]
#
# @!attribute [rw] str_isn_icode
#   @return [String, nil]
#
# @!attribute [rw] str_itunes_id
#   @return [String, nil]
#
# @!attribute [rw] str_label
#   @return [String, nil]
#
# @!attribute [rw] str_last_fm_chart
#   @return [String, nil]
#
# @!attribute [rw] str_location
#   @return [String, nil]
#
# @!attribute [rw] str_locked
#   @return [String, nil]
#
# @!attribute [rw] str_lyric_wiki_id
#   @return [String, nil]
#
# @!attribute [rw] str_mood
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_album_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_artist_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_brainz_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_moz_id
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_company
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_director
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen1
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen2
#   @return [String, nil]
#
# @!attribute [rw] str_music_vid_screen3
#   @return [String, nil]
#
# @!attribute [rw] str_rate_your_music_id
#   @return [String, nil]
#
# @!attribute [rw] str_release_format
#   @return [String, nil]
#
# @!attribute [rw] str_review
#   @return [String, nil]
#
# @!attribute [rw] str_speed
#   @return [String, nil]
#
# @!attribute [rw] str_style
#   @return [String, nil]
#
# @!attribute [rw] str_theme
#   @return [String, nil]
#
# @!attribute [rw] str_track
#   @return [String, nil]
#
# @!attribute [rw] str_track3x3
#   @return [String, nil]
#
# @!attribute [rw] str_track_lyric
#   @return [String, nil]
#
# @!attribute [rw] str_track_thumb
#   @return [String, nil]
#
# @!attribute [rw] str_twitter
#   @return [String, nil]
#
# @!attribute [rw] str_website
#   @return [String, nil]
#
# @!attribute [rw] str_wikidata_id
#   @return [String, nil]
#
# @!attribute [rw] str_wikipedia_id
#   @return [String, nil]
V1Search = Struct.new(
  :album,
  :id_album,
  :id_artist,
  :id_imvdb,
  :id_label,
  :id_lyric,
  :id_track,
  :int_born_year,
  :int_cd,
  :int_charted,
  :int_died_year,
  :int_duration,
  :int_formed_year,
  :int_loved,
  :int_member,
  :int_music_vid_comment,
  :int_music_vid_dislike,
  :int_music_vid_favorite,
  :int_music_vid_like,
  :int_music_vid_view,
  :int_sale,
  :int_score,
  :int_score_vote,
  :int_total_listener,
  :int_total_play,
  :int_track_number,
  :int_year_released,
  :str_album,
  :str_album3_d_case,
  :str_album3_d_face,
  :str_album3_d_flat,
  :str_album3_d_thumb,
  :str_album_c_dart,
  :str_album_spine,
  :str_album_stripped,
  :str_album_thumb,
  :str_album_thumb_back,
  :str_album_thumb_hq,
  :str_all_music_id,
  :str_amazon_id,
  :str_artist,
  :str_artist_alternate,
  :str_artist_banner,
  :str_artist_clearart,
  :str_artist_cutout,
  :str_artist_fanart,
  :str_artist_fanart2,
  :str_artist_fanart3,
  :str_artist_fanart4,
  :str_artist_logo,
  :str_artist_stripped,
  :str_artist_thumb,
  :str_artist_wide_thumb,
  :str_bbc_review_id,
  :str_biography_en,
  :str_country,
  :str_country_code,
  :str_description_en,
  :str_disbanded,
  :str_discogs_id,
  :str_facebook,
  :str_gender,
  :str_genius_id,
  :str_genre,
  :str_isn_icode,
  :str_itunes_id,
  :str_label,
  :str_last_fm_chart,
  :str_location,
  :str_locked,
  :str_lyric_wiki_id,
  :str_mood,
  :str_music_brainz_album_id,
  :str_music_brainz_artist_id,
  :str_music_brainz_id,
  :str_music_moz_id,
  :str_music_vid,
  :str_music_vid_company,
  :str_music_vid_director,
  :str_music_vid_screen1,
  :str_music_vid_screen2,
  :str_music_vid_screen3,
  :str_rate_your_music_id,
  :str_release_format,
  :str_review,
  :str_speed,
  :str_style,
  :str_theme,
  :str_track,
  :str_track3x3,
  :str_track_lyric,
  :str_track_thumb,
  :str_twitter,
  :str_website,
  :str_wikidata_id,
  :str_wikipedia_id,
  keyword_init: true
)

# Request payload for V1Search#load.
#
# @!attribute [rw] api_key
#   @return [String]
V1SearchLoadMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# Request payload for V1Search#list.
#
# @!attribute [rw] api_key
#   @return [String]
V1SearchListMatch = Struct.new(
  :api_key,
  keyword_init: true
)

# V2List entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
V2List = Struct.new(
  :album,
  keyword_init: true
)

# Request payload for V2List#load.
#
# @!attribute [rw] id_artist
#   @return [Integer]
V2ListLoadMatch = Struct.new(
  :id_artist,
  keyword_init: true
)

# V2Lookup entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
#
# @!attribute [rw] artist
#   @return [Array, nil]
#
# @!attribute [rw] track
#   @return [Array, nil]
V2Lookup = Struct.new(
  :album,
  :artist,
  :track,
  keyword_init: true
)

# Request payload for V2Lookup#load.
#
# @!attribute [rw] id_album
#   @return [Integer, nil]
#
# @!attribute [rw] id_artist
#   @return [Integer, nil]
#
# @!attribute [rw] id_track
#   @return [Integer, nil]
#
# @!attribute [rw] music_brainz_id
#   @return [String, nil]
V2LookupLoadMatch = Struct.new(
  :id_album,
  :id_artist,
  :id_track,
  :music_brainz_id,
  keyword_init: true
)

# V2Search entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
#
# @!attribute [rw] artist
#   @return [Array, nil]
#
# @!attribute [rw] track
#   @return [Array, nil]
V2Search = Struct.new(
  :album,
  :artist,
  :track,
  keyword_init: true
)

# Request payload for V2Search#load.
#
# @!attribute [rw] album_name
#   @return [String, nil]
#
# @!attribute [rw] artist_name
#   @return [String, nil]
#
# @!attribute [rw] track_name
#   @return [String, nil]
V2SearchLoadMatch = Struct.new(
  :album_name,
  :artist_name,
  :track_name,
  keyword_init: true
)

