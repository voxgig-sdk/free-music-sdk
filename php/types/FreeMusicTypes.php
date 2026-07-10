<?php
declare(strict_types=1);

// Typed models for the FreeMusic SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.
//
// These are documentation-grade value objects (PHP 8 typed properties),
// registered on the composer classmap autoload. The SDK boundary exchanges
// assoc-arrays; these classes name the shapes for tooling and typed callers.

/** V1List entity data model. */
class V1List
{
    public ?string $id_album = null;
    public ?string $id_artist = null;
    public ?string $id_imvdb = null;
    public ?string $id_lyric = null;
    public ?string $id_track = null;
    public ?string $int_cd = null;
    public ?string $int_duration = null;
    public ?string $int_loved = null;
    public ?string $int_music_vid_comment = null;
    public ?string $int_music_vid_dislike = null;
    public ?string $int_music_vid_favorite = null;
    public ?string $int_music_vid_like = null;
    public ?string $int_music_vid_view = null;
    public ?string $int_score = null;
    public ?string $int_score_vote = null;
    public ?string $int_total_listener = null;
    public ?string $int_total_play = null;
    public ?string $int_track_number = null;
    public ?string $str_album = null;
    public ?string $str_artist = null;
    public ?string $str_artist_alternate = null;
    public ?string $str_description_en = null;
    public ?string $str_genre = null;
    public ?string $str_locked = null;
    public ?string $str_mood = null;
    public ?string $str_music_brainz_album_id = null;
    public ?string $str_music_brainz_artist_id = null;
    public ?string $str_music_brainz_id = null;
    public ?string $str_music_vid = null;
    public ?string $str_music_vid_company = null;
    public ?string $str_music_vid_director = null;
    public ?string $str_music_vid_screen1 = null;
    public ?string $str_music_vid_screen2 = null;
    public ?string $str_music_vid_screen3 = null;
    public ?string $str_style = null;
    public ?string $str_theme = null;
    public ?string $str_track = null;
    public ?string $str_track3x3 = null;
    public ?string $str_track_lyric = null;
    public ?string $str_track_thumb = null;
    public ?array $trending = null;
}

/** Request payload for V1List#load. */
class V1ListLoadMatch
{
    public string $api_key;
}

/** Request payload for V1List#list. */
class V1ListListMatch
{
    public string $api_key;
}

/** V1Lookup entity data model. */
class V1Lookup
{
    public ?string $id_album = null;
    public ?string $id_artist = null;
    public ?string $id_imvdb = null;
    public ?string $id_label = null;
    public ?string $id_lyric = null;
    public ?string $id_track = null;
    public ?string $int_born_year = null;
    public ?string $int_cd = null;
    public ?string $int_charted = null;
    public ?string $int_died_year = null;
    public ?string $int_duration = null;
    public ?string $int_formed_year = null;
    public ?string $int_loved = null;
    public ?string $int_member = null;
    public ?string $int_music_vid_comment = null;
    public ?string $int_music_vid_dislike = null;
    public ?string $int_music_vid_favorite = null;
    public ?string $int_music_vid_like = null;
    public ?string $int_music_vid_view = null;
    public ?string $int_sale = null;
    public ?string $int_score = null;
    public ?string $int_score_vote = null;
    public ?string $int_total_listener = null;
    public ?string $int_total_play = null;
    public ?string $int_track_number = null;
    public ?string $int_year_released = null;
    public ?string $str_album = null;
    public ?string $str_album3_d_case = null;
    public ?string $str_album3_d_face = null;
    public ?string $str_album3_d_flat = null;
    public ?string $str_album3_d_thumb = null;
    public ?string $str_album_c_dart = null;
    public ?string $str_album_spine = null;
    public ?string $str_album_stripped = null;
    public ?string $str_album_thumb = null;
    public ?string $str_album_thumb_back = null;
    public ?string $str_album_thumb_hq = null;
    public ?string $str_all_music_id = null;
    public ?string $str_amazon_id = null;
    public ?string $str_artist = null;
    public ?string $str_artist_alternate = null;
    public ?string $str_artist_banner = null;
    public ?string $str_artist_clearart = null;
    public ?string $str_artist_cutout = null;
    public ?string $str_artist_fanart = null;
    public ?string $str_artist_fanart2 = null;
    public ?string $str_artist_fanart3 = null;
    public ?string $str_artist_fanart4 = null;
    public ?string $str_artist_logo = null;
    public ?string $str_artist_stripped = null;
    public ?string $str_artist_thumb = null;
    public ?string $str_artist_wide_thumb = null;
    public ?string $str_bbc_review_id = null;
    public ?string $str_biography_en = null;
    public ?string $str_country = null;
    public ?string $str_country_code = null;
    public ?string $str_description_en = null;
    public ?string $str_disbanded = null;
    public ?string $str_discogs_id = null;
    public ?string $str_facebook = null;
    public ?string $str_gender = null;
    public ?string $str_genius_id = null;
    public ?string $str_genre = null;
    public ?string $str_isn_icode = null;
    public ?string $str_itunes_id = null;
    public ?string $str_label = null;
    public ?string $str_last_fm_chart = null;
    public ?string $str_location = null;
    public ?string $str_locked = null;
    public ?string $str_lyric_wiki_id = null;
    public ?string $str_mood = null;
    public ?string $str_music_brainz_album_id = null;
    public ?string $str_music_brainz_artist_id = null;
    public ?string $str_music_brainz_id = null;
    public ?string $str_music_moz_id = null;
    public ?string $str_music_vid = null;
    public ?string $str_music_vid_company = null;
    public ?string $str_music_vid_director = null;
    public ?string $str_music_vid_screen1 = null;
    public ?string $str_music_vid_screen2 = null;
    public ?string $str_music_vid_screen3 = null;
    public ?string $str_rate_your_music_id = null;
    public ?string $str_release_format = null;
    public ?string $str_review = null;
    public ?string $str_speed = null;
    public ?string $str_style = null;
    public ?string $str_theme = null;
    public ?string $str_track = null;
    public ?string $str_track3x3 = null;
    public ?string $str_track_lyric = null;
    public ?string $str_track_thumb = null;
    public ?string $str_twitter = null;
    public ?string $str_website = null;
    public ?string $str_wikidata_id = null;
    public ?string $str_wikipedia_id = null;
}

/** Request payload for V1Lookup#load. */
class V1LookupLoadMatch
{
    public string $api_key;
}

/** Request payload for V1Lookup#list. */
class V1LookupListMatch
{
    public string $api_key;
}

/** V1Search entity data model. */
class V1Search
{
    public ?array $album = null;
    public ?string $id_album = null;
    public ?string $id_artist = null;
    public ?string $id_imvdb = null;
    public ?string $id_label = null;
    public ?string $id_lyric = null;
    public ?string $id_track = null;
    public ?string $int_born_year = null;
    public ?string $int_cd = null;
    public ?string $int_charted = null;
    public ?string $int_died_year = null;
    public ?string $int_duration = null;
    public ?string $int_formed_year = null;
    public ?string $int_loved = null;
    public ?string $int_member = null;
    public ?string $int_music_vid_comment = null;
    public ?string $int_music_vid_dislike = null;
    public ?string $int_music_vid_favorite = null;
    public ?string $int_music_vid_like = null;
    public ?string $int_music_vid_view = null;
    public ?string $int_sale = null;
    public ?string $int_score = null;
    public ?string $int_score_vote = null;
    public ?string $int_total_listener = null;
    public ?string $int_total_play = null;
    public ?string $int_track_number = null;
    public ?string $int_year_released = null;
    public ?string $str_album = null;
    public ?string $str_album3_d_case = null;
    public ?string $str_album3_d_face = null;
    public ?string $str_album3_d_flat = null;
    public ?string $str_album3_d_thumb = null;
    public ?string $str_album_c_dart = null;
    public ?string $str_album_spine = null;
    public ?string $str_album_stripped = null;
    public ?string $str_album_thumb = null;
    public ?string $str_album_thumb_back = null;
    public ?string $str_album_thumb_hq = null;
    public ?string $str_all_music_id = null;
    public ?string $str_amazon_id = null;
    public ?string $str_artist = null;
    public ?string $str_artist_alternate = null;
    public ?string $str_artist_banner = null;
    public ?string $str_artist_clearart = null;
    public ?string $str_artist_cutout = null;
    public ?string $str_artist_fanart = null;
    public ?string $str_artist_fanart2 = null;
    public ?string $str_artist_fanart3 = null;
    public ?string $str_artist_fanart4 = null;
    public ?string $str_artist_logo = null;
    public ?string $str_artist_stripped = null;
    public ?string $str_artist_thumb = null;
    public ?string $str_artist_wide_thumb = null;
    public ?string $str_bbc_review_id = null;
    public ?string $str_biography_en = null;
    public ?string $str_country = null;
    public ?string $str_country_code = null;
    public ?string $str_description_en = null;
    public ?string $str_disbanded = null;
    public ?string $str_discogs_id = null;
    public ?string $str_facebook = null;
    public ?string $str_gender = null;
    public ?string $str_genius_id = null;
    public ?string $str_genre = null;
    public ?string $str_isn_icode = null;
    public ?string $str_itunes_id = null;
    public ?string $str_label = null;
    public ?string $str_last_fm_chart = null;
    public ?string $str_location = null;
    public ?string $str_locked = null;
    public ?string $str_lyric_wiki_id = null;
    public ?string $str_mood = null;
    public ?string $str_music_brainz_album_id = null;
    public ?string $str_music_brainz_artist_id = null;
    public ?string $str_music_brainz_id = null;
    public ?string $str_music_moz_id = null;
    public ?string $str_music_vid = null;
    public ?string $str_music_vid_company = null;
    public ?string $str_music_vid_director = null;
    public ?string $str_music_vid_screen1 = null;
    public ?string $str_music_vid_screen2 = null;
    public ?string $str_music_vid_screen3 = null;
    public ?string $str_rate_your_music_id = null;
    public ?string $str_release_format = null;
    public ?string $str_review = null;
    public ?string $str_speed = null;
    public ?string $str_style = null;
    public ?string $str_theme = null;
    public ?string $str_track = null;
    public ?string $str_track3x3 = null;
    public ?string $str_track_lyric = null;
    public ?string $str_track_thumb = null;
    public ?string $str_twitter = null;
    public ?string $str_website = null;
    public ?string $str_wikidata_id = null;
    public ?string $str_wikipedia_id = null;
}

/** Request payload for V1Search#load. */
class V1SearchLoadMatch
{
    public string $api_key;
}

/** Request payload for V1Search#list. */
class V1SearchListMatch
{
    public string $api_key;
}

/** V2List entity data model. */
class V2List
{
    public ?array $album = null;
}

/** Request payload for V2List#load. */
class V2ListLoadMatch
{
    public int $id_artist;
}

/** V2Lookup entity data model. */
class V2Lookup
{
    public ?array $album = null;
    public ?array $artist = null;
    public ?array $track = null;
}

/** Request payload for V2Lookup#load. */
class V2LookupLoadMatch
{
    public ?int $id_album = null;
    public ?int $id_artist = null;
    public ?int $id_track = null;
    public ?string $music_brainz_id = null;
}

/** V2Search entity data model. */
class V2Search
{
    public ?array $album = null;
    public ?array $artist = null;
    public ?array $track = null;
}

/** Request payload for V2Search#load. */
class V2SearchLoadMatch
{
    public ?string $album_name = null;
    public ?string $artist_name = null;
    public ?string $track_name = null;
}

