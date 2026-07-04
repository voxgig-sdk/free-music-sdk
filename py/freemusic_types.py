# Typed models for the FreeMusic SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Field/param types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Do not edit by hand.

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class V1List:
    id_album: Optional[str] = None
    id_artist: Optional[str] = None
    id_imvdb: Optional[str] = None
    id_lyric: Optional[str] = None
    id_track: Optional[str] = None
    int_cd: Optional[str] = None
    int_duration: Optional[str] = None
    int_loved: Optional[str] = None
    int_music_vid_comment: Optional[str] = None
    int_music_vid_dislike: Optional[str] = None
    int_music_vid_favorite: Optional[str] = None
    int_music_vid_like: Optional[str] = None
    int_music_vid_view: Optional[str] = None
    int_score: Optional[str] = None
    int_score_vote: Optional[str] = None
    int_total_listener: Optional[str] = None
    int_total_play: Optional[str] = None
    int_track_number: Optional[str] = None
    str_album: Optional[str] = None
    str_artist: Optional[str] = None
    str_artist_alternate: Optional[str] = None
    str_description_en: Optional[str] = None
    str_genre: Optional[str] = None
    str_locked: Optional[str] = None
    str_mood: Optional[str] = None
    str_music_brainz_album_id: Optional[str] = None
    str_music_brainz_artist_id: Optional[str] = None
    str_music_brainz_id: Optional[str] = None
    str_music_vid: Optional[str] = None
    str_music_vid_company: Optional[str] = None
    str_music_vid_director: Optional[str] = None
    str_music_vid_screen1: Optional[str] = None
    str_music_vid_screen2: Optional[str] = None
    str_music_vid_screen3: Optional[str] = None
    str_style: Optional[str] = None
    str_theme: Optional[str] = None
    str_track: Optional[str] = None
    str_track3x3: Optional[str] = None
    str_track_lyric: Optional[str] = None
    str_track_thumb: Optional[str] = None
    trending: Optional[list] = None


@dataclass
class V1ListLoadMatch:
    api_key: str


@dataclass
class V1ListListMatch:
    api_key: str


@dataclass
class V1Lookup:
    id_album: Optional[str] = None
    id_artist: Optional[str] = None
    id_imvdb: Optional[str] = None
    id_label: Optional[str] = None
    id_lyric: Optional[str] = None
    id_track: Optional[str] = None
    int_born_year: Optional[str] = None
    int_cd: Optional[str] = None
    int_charted: Optional[str] = None
    int_died_year: Optional[str] = None
    int_duration: Optional[str] = None
    int_formed_year: Optional[str] = None
    int_loved: Optional[str] = None
    int_member: Optional[str] = None
    int_music_vid_comment: Optional[str] = None
    int_music_vid_dislike: Optional[str] = None
    int_music_vid_favorite: Optional[str] = None
    int_music_vid_like: Optional[str] = None
    int_music_vid_view: Optional[str] = None
    int_sale: Optional[str] = None
    int_score: Optional[str] = None
    int_score_vote: Optional[str] = None
    int_total_listener: Optional[str] = None
    int_total_play: Optional[str] = None
    int_track_number: Optional[str] = None
    int_year_released: Optional[str] = None
    str_album: Optional[str] = None
    str_album3_d_case: Optional[str] = None
    str_album3_d_face: Optional[str] = None
    str_album3_d_flat: Optional[str] = None
    str_album3_d_thumb: Optional[str] = None
    str_album_c_dart: Optional[str] = None
    str_album_spine: Optional[str] = None
    str_album_stripped: Optional[str] = None
    str_album_thumb: Optional[str] = None
    str_album_thumb_back: Optional[str] = None
    str_album_thumb_hq: Optional[str] = None
    str_all_music_id: Optional[str] = None
    str_amazon_id: Optional[str] = None
    str_artist: Optional[str] = None
    str_artist_alternate: Optional[str] = None
    str_artist_banner: Optional[str] = None
    str_artist_clearart: Optional[str] = None
    str_artist_cutout: Optional[str] = None
    str_artist_fanart: Optional[str] = None
    str_artist_fanart2: Optional[str] = None
    str_artist_fanart3: Optional[str] = None
    str_artist_fanart4: Optional[str] = None
    str_artist_logo: Optional[str] = None
    str_artist_stripped: Optional[str] = None
    str_artist_thumb: Optional[str] = None
    str_artist_wide_thumb: Optional[str] = None
    str_bbc_review_id: Optional[str] = None
    str_biography_en: Optional[str] = None
    str_country: Optional[str] = None
    str_country_code: Optional[str] = None
    str_description_en: Optional[str] = None
    str_disbanded: Optional[str] = None
    str_discogs_id: Optional[str] = None
    str_facebook: Optional[str] = None
    str_gender: Optional[str] = None
    str_genius_id: Optional[str] = None
    str_genre: Optional[str] = None
    str_isn_icode: Optional[str] = None
    str_itunes_id: Optional[str] = None
    str_label: Optional[str] = None
    str_last_fm_chart: Optional[str] = None
    str_location: Optional[str] = None
    str_locked: Optional[str] = None
    str_lyric_wiki_id: Optional[str] = None
    str_mood: Optional[str] = None
    str_music_brainz_album_id: Optional[str] = None
    str_music_brainz_artist_id: Optional[str] = None
    str_music_brainz_id: Optional[str] = None
    str_music_moz_id: Optional[str] = None
    str_music_vid: Optional[str] = None
    str_music_vid_company: Optional[str] = None
    str_music_vid_director: Optional[str] = None
    str_music_vid_screen1: Optional[str] = None
    str_music_vid_screen2: Optional[str] = None
    str_music_vid_screen3: Optional[str] = None
    str_rate_your_music_id: Optional[str] = None
    str_release_format: Optional[str] = None
    str_review: Optional[str] = None
    str_speed: Optional[str] = None
    str_style: Optional[str] = None
    str_theme: Optional[str] = None
    str_track: Optional[str] = None
    str_track3x3: Optional[str] = None
    str_track_lyric: Optional[str] = None
    str_track_thumb: Optional[str] = None
    str_twitter: Optional[str] = None
    str_website: Optional[str] = None
    str_wikidata_id: Optional[str] = None
    str_wikipedia_id: Optional[str] = None


@dataclass
class V1LookupLoadMatch:
    api_key: str


@dataclass
class V1LookupListMatch:
    api_key: str


@dataclass
class V1Search:
    album: Optional[list] = None
    id_album: Optional[str] = None
    id_artist: Optional[str] = None
    id_imvdb: Optional[str] = None
    id_label: Optional[str] = None
    id_lyric: Optional[str] = None
    id_track: Optional[str] = None
    int_born_year: Optional[str] = None
    int_cd: Optional[str] = None
    int_charted: Optional[str] = None
    int_died_year: Optional[str] = None
    int_duration: Optional[str] = None
    int_formed_year: Optional[str] = None
    int_loved: Optional[str] = None
    int_member: Optional[str] = None
    int_music_vid_comment: Optional[str] = None
    int_music_vid_dislike: Optional[str] = None
    int_music_vid_favorite: Optional[str] = None
    int_music_vid_like: Optional[str] = None
    int_music_vid_view: Optional[str] = None
    int_sale: Optional[str] = None
    int_score: Optional[str] = None
    int_score_vote: Optional[str] = None
    int_total_listener: Optional[str] = None
    int_total_play: Optional[str] = None
    int_track_number: Optional[str] = None
    int_year_released: Optional[str] = None
    str_album: Optional[str] = None
    str_album3_d_case: Optional[str] = None
    str_album3_d_face: Optional[str] = None
    str_album3_d_flat: Optional[str] = None
    str_album3_d_thumb: Optional[str] = None
    str_album_c_dart: Optional[str] = None
    str_album_spine: Optional[str] = None
    str_album_stripped: Optional[str] = None
    str_album_thumb: Optional[str] = None
    str_album_thumb_back: Optional[str] = None
    str_album_thumb_hq: Optional[str] = None
    str_all_music_id: Optional[str] = None
    str_amazon_id: Optional[str] = None
    str_artist: Optional[str] = None
    str_artist_alternate: Optional[str] = None
    str_artist_banner: Optional[str] = None
    str_artist_clearart: Optional[str] = None
    str_artist_cutout: Optional[str] = None
    str_artist_fanart: Optional[str] = None
    str_artist_fanart2: Optional[str] = None
    str_artist_fanart3: Optional[str] = None
    str_artist_fanart4: Optional[str] = None
    str_artist_logo: Optional[str] = None
    str_artist_stripped: Optional[str] = None
    str_artist_thumb: Optional[str] = None
    str_artist_wide_thumb: Optional[str] = None
    str_bbc_review_id: Optional[str] = None
    str_biography_en: Optional[str] = None
    str_country: Optional[str] = None
    str_country_code: Optional[str] = None
    str_description_en: Optional[str] = None
    str_disbanded: Optional[str] = None
    str_discogs_id: Optional[str] = None
    str_facebook: Optional[str] = None
    str_gender: Optional[str] = None
    str_genius_id: Optional[str] = None
    str_genre: Optional[str] = None
    str_isn_icode: Optional[str] = None
    str_itunes_id: Optional[str] = None
    str_label: Optional[str] = None
    str_last_fm_chart: Optional[str] = None
    str_location: Optional[str] = None
    str_locked: Optional[str] = None
    str_lyric_wiki_id: Optional[str] = None
    str_mood: Optional[str] = None
    str_music_brainz_album_id: Optional[str] = None
    str_music_brainz_artist_id: Optional[str] = None
    str_music_brainz_id: Optional[str] = None
    str_music_moz_id: Optional[str] = None
    str_music_vid: Optional[str] = None
    str_music_vid_company: Optional[str] = None
    str_music_vid_director: Optional[str] = None
    str_music_vid_screen1: Optional[str] = None
    str_music_vid_screen2: Optional[str] = None
    str_music_vid_screen3: Optional[str] = None
    str_rate_your_music_id: Optional[str] = None
    str_release_format: Optional[str] = None
    str_review: Optional[str] = None
    str_speed: Optional[str] = None
    str_style: Optional[str] = None
    str_theme: Optional[str] = None
    str_track: Optional[str] = None
    str_track3x3: Optional[str] = None
    str_track_lyric: Optional[str] = None
    str_track_thumb: Optional[str] = None
    str_twitter: Optional[str] = None
    str_website: Optional[str] = None
    str_wikidata_id: Optional[str] = None
    str_wikipedia_id: Optional[str] = None


@dataclass
class V1SearchLoadMatch:
    api_key: str


@dataclass
class V1SearchListMatch:
    api_key: str


@dataclass
class V2List:
    album: Optional[list] = None


@dataclass
class V2ListLoadMatch:
    id_artist: int


@dataclass
class V2Lookup:
    album: Optional[list] = None
    artist: Optional[list] = None
    track: Optional[list] = None


@dataclass
class V2LookupLoadMatch:
    id_album: int
    id_artist: int
    id_track: int
    music_brainz_id: str


@dataclass
class V2Search:
    album: Optional[list] = None
    artist: Optional[list] = None
    track: Optional[list] = None


@dataclass
class V2SearchLoadMatch:
    album_name: str
    artist_name: str
    track_name: str

