# Typed models for the FreeMusic SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Field/param types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Do not edit by hand.
#
# These are TypedDicts, not dataclasses: the SDK ops return/accept plain dicts
# at runtime, and a TypedDict IS a dict shape, so the types match the runtime.
# Optional (req:false) keys are modelled as TypedDict key-optionality
# (total=False), split into a required base + total=False subclass when a type
# has both required and optional keys.

from __future__ import annotations

from typing import TypedDict, Any


class V1List(TypedDict, total=False):
    idAlbum: str
    idArtist: str
    idIMVDB: str
    idLyric: str
    idTrack: str
    intCD: str
    intDuration: str
    intLoved: str
    intMusicVidComments: str
    intMusicVidDislikes: str
    intMusicVidFavorites: str
    intMusicVidLikes: str
    intMusicVidViews: str
    intScore: str
    intScoreVotes: str
    intTotalListeners: str
    intTotalPlays: str
    intTrackNumber: str
    strAlbum: str
    strArtist: str
    strArtistAlternate: str
    strDescriptionEN: str
    strGenre: str
    strLocked: str
    strMood: str
    strMusicBrainzAlbumID: str
    strMusicBrainzArtistID: str
    strMusicBrainzID: str
    strMusicVid: str
    strMusicVidCompany: str
    strMusicVidDirector: str
    strMusicVidScreen1: str
    strMusicVidScreen2: str
    strMusicVidScreen3: str
    strStyle: str
    strTheme: str
    strTrack: str
    strTrack3x3: str
    strTrackLyrics: str
    strTrackThumb: str
    trending: list


class V1ListLoadMatch(TypedDict):
    api_key: str


class V1ListListMatch(TypedDict):
    api_key: str


class V1Lookup(TypedDict, total=False):
    idAlbum: str
    idArtist: str
    idIMVDB: str
    idLabel: str
    idLyric: str
    idTrack: str
    intBornYear: str
    intCD: str
    intCharted: str
    intDiedYear: str
    intDuration: str
    intFormedYear: str
    intLoved: str
    intMembers: str
    intMusicVidComments: str
    intMusicVidDislikes: str
    intMusicVidFavorites: str
    intMusicVidLikes: str
    intMusicVidViews: str
    intSales: str
    intScore: str
    intScoreVotes: str
    intTotalListeners: str
    intTotalPlays: str
    intTrackNumber: str
    intYearReleased: str
    strAlbum: str
    strAlbum3DCase: str
    strAlbum3DFace: str
    strAlbum3DFlat: str
    strAlbum3DThumb: str
    strAlbumCDart: str
    strAlbumSpine: str
    strAlbumStripped: str
    strAlbumThumb: str
    strAlbumThumbBack: str
    strAlbumThumbHQ: str
    strAllMusicID: str
    strAmazonID: str
    strArtist: str
    strArtistAlternate: str
    strArtistBanner: str
    strArtistClearart: str
    strArtistCutout: str
    strArtistFanart: str
    strArtistFanart2: str
    strArtistFanart3: str
    strArtistFanart4: str
    strArtistLogo: str
    strArtistStripped: str
    strArtistThumb: str
    strArtistWideThumb: str
    strBBCReviewID: str
    strBiographyEN: str
    strCountry: str
    strCountryCode: str
    strDescriptionEN: str
    strDisbanded: str
    strDiscogsID: str
    strFacebook: str
    strGender: str
    strGeniusID: str
    strGenre: str
    strISNIcode: str
    strItunesID: str
    strLabel: str
    strLastFMChart: str
    strLocation: str
    strLocked: str
    strLyricWikiID: str
    strMood: str
    strMusicBrainzAlbumID: str
    strMusicBrainzArtistID: str
    strMusicBrainzID: str
    strMusicMozID: str
    strMusicVid: str
    strMusicVidCompany: str
    strMusicVidDirector: str
    strMusicVidScreen1: str
    strMusicVidScreen2: str
    strMusicVidScreen3: str
    strRateYourMusicID: str
    strReleaseFormat: str
    strReview: str
    strSpeed: str
    strStyle: str
    strTheme: str
    strTrack: str
    strTrack3x3: str
    strTrackLyrics: str
    strTrackThumb: str
    strTwitter: str
    strWebsite: str
    strWikidataID: str
    strWikipediaID: str


class V1LookupLoadMatch(TypedDict):
    api_key: str


class V1LookupListMatch(TypedDict):
    api_key: str


class V1Search(TypedDict, total=False):
    album: list
    idAlbum: str
    idArtist: str
    idIMVDB: str
    idLabel: str
    idLyric: str
    idTrack: str
    intBornYear: str
    intCD: str
    intCharted: str
    intDiedYear: str
    intDuration: str
    intFormedYear: str
    intLoved: str
    intMembers: str
    intMusicVidComments: str
    intMusicVidDislikes: str
    intMusicVidFavorites: str
    intMusicVidLikes: str
    intMusicVidViews: str
    intSales: str
    intScore: str
    intScoreVotes: str
    intTotalListeners: str
    intTotalPlays: str
    intTrackNumber: str
    intYearReleased: str
    strAlbum: str
    strAlbum3DCase: str
    strAlbum3DFace: str
    strAlbum3DFlat: str
    strAlbum3DThumb: str
    strAlbumCDart: str
    strAlbumSpine: str
    strAlbumStripped: str
    strAlbumThumb: str
    strAlbumThumbBack: str
    strAlbumThumbHQ: str
    strAllMusicID: str
    strAmazonID: str
    strArtist: str
    strArtistAlternate: str
    strArtistBanner: str
    strArtistClearart: str
    strArtistCutout: str
    strArtistFanart: str
    strArtistFanart2: str
    strArtistFanart3: str
    strArtistFanart4: str
    strArtistLogo: str
    strArtistStripped: str
    strArtistThumb: str
    strArtistWideThumb: str
    strBBCReviewID: str
    strBiographyEN: str
    strCountry: str
    strCountryCode: str
    strDescriptionEN: str
    strDisbanded: str
    strDiscogsID: str
    strFacebook: str
    strGender: str
    strGeniusID: str
    strGenre: str
    strISNIcode: str
    strItunesID: str
    strLabel: str
    strLastFMChart: str
    strLocation: str
    strLocked: str
    strLyricWikiID: str
    strMood: str
    strMusicBrainzAlbumID: str
    strMusicBrainzArtistID: str
    strMusicBrainzID: str
    strMusicMozID: str
    strMusicVid: str
    strMusicVidCompany: str
    strMusicVidDirector: str
    strMusicVidScreen1: str
    strMusicVidScreen2: str
    strMusicVidScreen3: str
    strRateYourMusicID: str
    strReleaseFormat: str
    strReview: str
    strSpeed: str
    strStyle: str
    strTheme: str
    strTrack: str
    strTrack3x3: str
    strTrackLyrics: str
    strTrackThumb: str
    strTwitter: str
    strWebsite: str
    strWikidataID: str
    strWikipediaID: str


class V1SearchLoadMatch(TypedDict):
    api_key: str


class V1SearchListMatch(TypedDict):
    api_key: str


class V2List(TypedDict, total=False):
    album: list


class V2ListLoadMatch(TypedDict):
    id_artist: int


class V2Lookup(TypedDict, total=False):
    album: list
    artists: list
    track: list


class V2LookupLoadMatch(TypedDict, total=False):
    id_album: int
    id_artist: int
    id_track: int
    music_brainz_id: str


class V2Search(TypedDict, total=False):
    album: list
    artists: list
    track: list


class V2SearchLoadMatch(TypedDict, total=False):
    album_name: str
    artist_name: str
    track_name: str
