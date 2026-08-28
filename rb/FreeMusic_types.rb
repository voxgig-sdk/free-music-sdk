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
# @!attribute [rw] idAlbum
#   @return [String, nil]
#
# @!attribute [rw] idArtist
#   @return [String, nil]
#
# @!attribute [rw] idIMVDB
#   @return [String, nil]
#
# @!attribute [rw] idLyric
#   @return [String, nil]
#
# @!attribute [rw] idTrack
#   @return [String, nil]
#
# @!attribute [rw] intCD
#   @return [String, nil]
#
# @!attribute [rw] intDuration
#   @return [String, nil]
#
# @!attribute [rw] intLoved
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidComments
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidDislikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidFavorites
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidLikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidViews
#   @return [String, nil]
#
# @!attribute [rw] intScore
#   @return [String, nil]
#
# @!attribute [rw] intScoreVotes
#   @return [String, nil]
#
# @!attribute [rw] intTotalListeners
#   @return [String, nil]
#
# @!attribute [rw] intTotalPlays
#   @return [String, nil]
#
# @!attribute [rw] intTrackNumber
#   @return [String, nil]
#
# @!attribute [rw] strAlbum
#   @return [String, nil]
#
# @!attribute [rw] strArtist
#   @return [String, nil]
#
# @!attribute [rw] strArtistAlternate
#   @return [String, nil]
#
# @!attribute [rw] strDescriptionEN
#   @return [String, nil]
#
# @!attribute [rw] strGenre
#   @return [String, nil]
#
# @!attribute [rw] strLocked
#   @return [String, nil]
#
# @!attribute [rw] strMood
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzAlbumID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzArtistID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzID
#   @return [String, nil]
#
# @!attribute [rw] strMusicVid
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidCompany
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidDirector
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen1
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen2
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen3
#   @return [String, nil]
#
# @!attribute [rw] strStyle
#   @return [String, nil]
#
# @!attribute [rw] strTheme
#   @return [String, nil]
#
# @!attribute [rw] strTrack
#   @return [String, nil]
#
# @!attribute [rw] strTrack3x3
#   @return [String, nil]
#
# @!attribute [rw] strTrackLyrics
#   @return [String, nil]
#
# @!attribute [rw] strTrackThumb
#   @return [String, nil]
#
# @!attribute [rw] trending
#   @return [Array, nil]
V1List = Struct.new(
  :idAlbum,
  :idArtist,
  :idIMVDB,
  :idLyric,
  :idTrack,
  :intCD,
  :intDuration,
  :intLoved,
  :intMusicVidComments,
  :intMusicVidDislikes,
  :intMusicVidFavorites,
  :intMusicVidLikes,
  :intMusicVidViews,
  :intScore,
  :intScoreVotes,
  :intTotalListeners,
  :intTotalPlays,
  :intTrackNumber,
  :strAlbum,
  :strArtist,
  :strArtistAlternate,
  :strDescriptionEN,
  :strGenre,
  :strLocked,
  :strMood,
  :strMusicBrainzAlbumID,
  :strMusicBrainzArtistID,
  :strMusicBrainzID,
  :strMusicVid,
  :strMusicVidCompany,
  :strMusicVidDirector,
  :strMusicVidScreen1,
  :strMusicVidScreen2,
  :strMusicVidScreen3,
  :strStyle,
  :strTheme,
  :strTrack,
  :strTrack3x3,
  :strTrackLyrics,
  :strTrackThumb,
  :trending,
  keyword_init: true
)

# Request payload for V1List#load.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] format
#   @return [String, nil]
#
# @!attribute [rw] i
#   @return [String, nil]
#
# @!attribute [rw] s
#   @return [String, nil]
V1ListLoadMatch = Struct.new(
  :api_key,
  :format,
  :i,
  :s,
  keyword_init: true
)

# Request payload for V1List#list.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] country
#   @return [String, nil]
#
# @!attribute [rw] format
#   @return [String, nil]
#
# @!attribute [rw] type
#   @return [String, nil]
#
# @!attribute [rw] i
#   @return [Integer, nil]
#
# @!attribute [rw] s
#   @return [String, nil]
V1ListListMatch = Struct.new(
  :api_key,
  :country,
  :format,
  :type,
  :i,
  :s,
  keyword_init: true
)

# V1Lookup entity data model.
#
# @!attribute [rw] idAlbum
#   @return [String, nil]
#
# @!attribute [rw] idArtist
#   @return [String, nil]
#
# @!attribute [rw] idIMVDB
#   @return [String, nil]
#
# @!attribute [rw] idLabel
#   @return [String, nil]
#
# @!attribute [rw] idLyric
#   @return [String, nil]
#
# @!attribute [rw] idTrack
#   @return [String, nil]
#
# @!attribute [rw] intBornYear
#   @return [String, nil]
#
# @!attribute [rw] intCD
#   @return [String, nil]
#
# @!attribute [rw] intCharted
#   @return [String, nil]
#
# @!attribute [rw] intDiedYear
#   @return [String, nil]
#
# @!attribute [rw] intDuration
#   @return [String, nil]
#
# @!attribute [rw] intFormedYear
#   @return [String, nil]
#
# @!attribute [rw] intLoved
#   @return [String, nil]
#
# @!attribute [rw] intMembers
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidComments
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidDislikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidFavorites
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidLikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidViews
#   @return [String, nil]
#
# @!attribute [rw] intSales
#   @return [String, nil]
#
# @!attribute [rw] intScore
#   @return [String, nil]
#
# @!attribute [rw] intScoreVotes
#   @return [String, nil]
#
# @!attribute [rw] intTotalListeners
#   @return [String, nil]
#
# @!attribute [rw] intTotalPlays
#   @return [String, nil]
#
# @!attribute [rw] intTrackNumber
#   @return [String, nil]
#
# @!attribute [rw] intYearReleased
#   @return [String, nil]
#
# @!attribute [rw] strAlbum
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DCase
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DFace
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DFlat
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DThumb
#   @return [String, nil]
#
# @!attribute [rw] strAlbumCDart
#   @return [String, nil]
#
# @!attribute [rw] strAlbumSpine
#   @return [String, nil]
#
# @!attribute [rw] strAlbumStripped
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumb
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumbBack
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumbHQ
#   @return [String, nil]
#
# @!attribute [rw] strAllMusicID
#   @return [String, nil]
#
# @!attribute [rw] strAmazonID
#   @return [String, nil]
#
# @!attribute [rw] strArtist
#   @return [String, nil]
#
# @!attribute [rw] strArtistAlternate
#   @return [String, nil]
#
# @!attribute [rw] strArtistBanner
#   @return [String, nil]
#
# @!attribute [rw] strArtistClearart
#   @return [String, nil]
#
# @!attribute [rw] strArtistCutout
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart2
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart3
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart4
#   @return [String, nil]
#
# @!attribute [rw] strArtistLogo
#   @return [String, nil]
#
# @!attribute [rw] strArtistStripped
#   @return [String, nil]
#
# @!attribute [rw] strArtistThumb
#   @return [String, nil]
#
# @!attribute [rw] strArtistWideThumb
#   @return [String, nil]
#
# @!attribute [rw] strBBCReviewID
#   @return [String, nil]
#
# @!attribute [rw] strBiographyEN
#   @return [String, nil]
#
# @!attribute [rw] strCountry
#   @return [String, nil]
#
# @!attribute [rw] strCountryCode
#   @return [String, nil]
#
# @!attribute [rw] strDescriptionEN
#   @return [String, nil]
#
# @!attribute [rw] strDisbanded
#   @return [String, nil]
#
# @!attribute [rw] strDiscogsID
#   @return [String, nil]
#
# @!attribute [rw] strFacebook
#   @return [String, nil]
#
# @!attribute [rw] strGender
#   @return [String, nil]
#
# @!attribute [rw] strGeniusID
#   @return [String, nil]
#
# @!attribute [rw] strGenre
#   @return [String, nil]
#
# @!attribute [rw] strISNIcode
#   @return [String, nil]
#
# @!attribute [rw] strItunesID
#   @return [String, nil]
#
# @!attribute [rw] strLabel
#   @return [String, nil]
#
# @!attribute [rw] strLastFMChart
#   @return [String, nil]
#
# @!attribute [rw] strLocation
#   @return [String, nil]
#
# @!attribute [rw] strLocked
#   @return [String, nil]
#
# @!attribute [rw] strLyricWikiID
#   @return [String, nil]
#
# @!attribute [rw] strMood
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzAlbumID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzArtistID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzID
#   @return [String, nil]
#
# @!attribute [rw] strMusicMozID
#   @return [String, nil]
#
# @!attribute [rw] strMusicVid
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidCompany
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidDirector
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen1
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen2
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen3
#   @return [String, nil]
#
# @!attribute [rw] strRateYourMusicID
#   @return [String, nil]
#
# @!attribute [rw] strReleaseFormat
#   @return [String, nil]
#
# @!attribute [rw] strReview
#   @return [String, nil]
#
# @!attribute [rw] strSpeed
#   @return [String, nil]
#
# @!attribute [rw] strStyle
#   @return [String, nil]
#
# @!attribute [rw] strTheme
#   @return [String, nil]
#
# @!attribute [rw] strTrack
#   @return [String, nil]
#
# @!attribute [rw] strTrack3x3
#   @return [String, nil]
#
# @!attribute [rw] strTrackLyrics
#   @return [String, nil]
#
# @!attribute [rw] strTrackThumb
#   @return [String, nil]
#
# @!attribute [rw] strTwitter
#   @return [String, nil]
#
# @!attribute [rw] strWebsite
#   @return [String, nil]
#
# @!attribute [rw] strWikidataID
#   @return [String, nil]
#
# @!attribute [rw] strWikipediaID
#   @return [String, nil]
V1Lookup = Struct.new(
  :idAlbum,
  :idArtist,
  :idIMVDB,
  :idLabel,
  :idLyric,
  :idTrack,
  :intBornYear,
  :intCD,
  :intCharted,
  :intDiedYear,
  :intDuration,
  :intFormedYear,
  :intLoved,
  :intMembers,
  :intMusicVidComments,
  :intMusicVidDislikes,
  :intMusicVidFavorites,
  :intMusicVidLikes,
  :intMusicVidViews,
  :intSales,
  :intScore,
  :intScoreVotes,
  :intTotalListeners,
  :intTotalPlays,
  :intTrackNumber,
  :intYearReleased,
  :strAlbum,
  :strAlbum3DCase,
  :strAlbum3DFace,
  :strAlbum3DFlat,
  :strAlbum3DThumb,
  :strAlbumCDart,
  :strAlbumSpine,
  :strAlbumStripped,
  :strAlbumThumb,
  :strAlbumThumbBack,
  :strAlbumThumbHQ,
  :strAllMusicID,
  :strAmazonID,
  :strArtist,
  :strArtistAlternate,
  :strArtistBanner,
  :strArtistClearart,
  :strArtistCutout,
  :strArtistFanart,
  :strArtistFanart2,
  :strArtistFanart3,
  :strArtistFanart4,
  :strArtistLogo,
  :strArtistStripped,
  :strArtistThumb,
  :strArtistWideThumb,
  :strBBCReviewID,
  :strBiographyEN,
  :strCountry,
  :strCountryCode,
  :strDescriptionEN,
  :strDisbanded,
  :strDiscogsID,
  :strFacebook,
  :strGender,
  :strGeniusID,
  :strGenre,
  :strISNIcode,
  :strItunesID,
  :strLabel,
  :strLastFMChart,
  :strLocation,
  :strLocked,
  :strLyricWikiID,
  :strMood,
  :strMusicBrainzAlbumID,
  :strMusicBrainzArtistID,
  :strMusicBrainzID,
  :strMusicMozID,
  :strMusicVid,
  :strMusicVidCompany,
  :strMusicVidDirector,
  :strMusicVidScreen1,
  :strMusicVidScreen2,
  :strMusicVidScreen3,
  :strRateYourMusicID,
  :strReleaseFormat,
  :strReview,
  :strSpeed,
  :strStyle,
  :strTheme,
  :strTrack,
  :strTrack3x3,
  :strTrackLyrics,
  :strTrackThumb,
  :strTwitter,
  :strWebsite,
  :strWikidataID,
  :strWikipediaID,
  keyword_init: true
)

# Request payload for V1Lookup#load.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] i
#   @return [String]
V1LookupLoadMatch = Struct.new(
  :api_key,
  :i,
  keyword_init: true
)

# Request payload for V1Lookup#list.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] h
#   @return [Integer, nil]
#
# @!attribute [rw] m
#   @return [Integer, nil]
#
# @!attribute [rw] i
#   @return [Integer, nil]
V1LookupListMatch = Struct.new(
  :api_key,
  :h,
  :m,
  :i,
  keyword_init: true
)

# V1Search entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
#
# @!attribute [rw] idAlbum
#   @return [String, nil]
#
# @!attribute [rw] idArtist
#   @return [String, nil]
#
# @!attribute [rw] idIMVDB
#   @return [String, nil]
#
# @!attribute [rw] idLabel
#   @return [String, nil]
#
# @!attribute [rw] idLyric
#   @return [String, nil]
#
# @!attribute [rw] idTrack
#   @return [String, nil]
#
# @!attribute [rw] intBornYear
#   @return [String, nil]
#
# @!attribute [rw] intCD
#   @return [String, nil]
#
# @!attribute [rw] intCharted
#   @return [String, nil]
#
# @!attribute [rw] intDiedYear
#   @return [String, nil]
#
# @!attribute [rw] intDuration
#   @return [String, nil]
#
# @!attribute [rw] intFormedYear
#   @return [String, nil]
#
# @!attribute [rw] intLoved
#   @return [String, nil]
#
# @!attribute [rw] intMembers
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidComments
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidDislikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidFavorites
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidLikes
#   @return [String, nil]
#
# @!attribute [rw] intMusicVidViews
#   @return [String, nil]
#
# @!attribute [rw] intSales
#   @return [String, nil]
#
# @!attribute [rw] intScore
#   @return [String, nil]
#
# @!attribute [rw] intScoreVotes
#   @return [String, nil]
#
# @!attribute [rw] intTotalListeners
#   @return [String, nil]
#
# @!attribute [rw] intTotalPlays
#   @return [String, nil]
#
# @!attribute [rw] intTrackNumber
#   @return [String, nil]
#
# @!attribute [rw] intYearReleased
#   @return [String, nil]
#
# @!attribute [rw] strAlbum
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DCase
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DFace
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DFlat
#   @return [String, nil]
#
# @!attribute [rw] strAlbum3DThumb
#   @return [String, nil]
#
# @!attribute [rw] strAlbumCDart
#   @return [String, nil]
#
# @!attribute [rw] strAlbumSpine
#   @return [String, nil]
#
# @!attribute [rw] strAlbumStripped
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumb
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumbBack
#   @return [String, nil]
#
# @!attribute [rw] strAlbumThumbHQ
#   @return [String, nil]
#
# @!attribute [rw] strAllMusicID
#   @return [String, nil]
#
# @!attribute [rw] strAmazonID
#   @return [String, nil]
#
# @!attribute [rw] strArtist
#   @return [String, nil]
#
# @!attribute [rw] strArtistAlternate
#   @return [String, nil]
#
# @!attribute [rw] strArtistBanner
#   @return [String, nil]
#
# @!attribute [rw] strArtistClearart
#   @return [String, nil]
#
# @!attribute [rw] strArtistCutout
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart2
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart3
#   @return [String, nil]
#
# @!attribute [rw] strArtistFanart4
#   @return [String, nil]
#
# @!attribute [rw] strArtistLogo
#   @return [String, nil]
#
# @!attribute [rw] strArtistStripped
#   @return [String, nil]
#
# @!attribute [rw] strArtistThumb
#   @return [String, nil]
#
# @!attribute [rw] strArtistWideThumb
#   @return [String, nil]
#
# @!attribute [rw] strBBCReviewID
#   @return [String, nil]
#
# @!attribute [rw] strBiographyEN
#   @return [String, nil]
#
# @!attribute [rw] strCountry
#   @return [String, nil]
#
# @!attribute [rw] strCountryCode
#   @return [String, nil]
#
# @!attribute [rw] strDescriptionEN
#   @return [String, nil]
#
# @!attribute [rw] strDisbanded
#   @return [String, nil]
#
# @!attribute [rw] strDiscogsID
#   @return [String, nil]
#
# @!attribute [rw] strFacebook
#   @return [String, nil]
#
# @!attribute [rw] strGender
#   @return [String, nil]
#
# @!attribute [rw] strGeniusID
#   @return [String, nil]
#
# @!attribute [rw] strGenre
#   @return [String, nil]
#
# @!attribute [rw] strISNIcode
#   @return [String, nil]
#
# @!attribute [rw] strItunesID
#   @return [String, nil]
#
# @!attribute [rw] strLabel
#   @return [String, nil]
#
# @!attribute [rw] strLastFMChart
#   @return [String, nil]
#
# @!attribute [rw] strLocation
#   @return [String, nil]
#
# @!attribute [rw] strLocked
#   @return [String, nil]
#
# @!attribute [rw] strLyricWikiID
#   @return [String, nil]
#
# @!attribute [rw] strMood
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzAlbumID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzArtistID
#   @return [String, nil]
#
# @!attribute [rw] strMusicBrainzID
#   @return [String, nil]
#
# @!attribute [rw] strMusicMozID
#   @return [String, nil]
#
# @!attribute [rw] strMusicVid
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidCompany
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidDirector
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen1
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen2
#   @return [String, nil]
#
# @!attribute [rw] strMusicVidScreen3
#   @return [String, nil]
#
# @!attribute [rw] strRateYourMusicID
#   @return [String, nil]
#
# @!attribute [rw] strReleaseFormat
#   @return [String, nil]
#
# @!attribute [rw] strReview
#   @return [String, nil]
#
# @!attribute [rw] strSpeed
#   @return [String, nil]
#
# @!attribute [rw] strStyle
#   @return [String, nil]
#
# @!attribute [rw] strTheme
#   @return [String, nil]
#
# @!attribute [rw] strTrack
#   @return [String, nil]
#
# @!attribute [rw] strTrack3x3
#   @return [String, nil]
#
# @!attribute [rw] strTrackLyrics
#   @return [String, nil]
#
# @!attribute [rw] strTrackThumb
#   @return [String, nil]
#
# @!attribute [rw] strTwitter
#   @return [String, nil]
#
# @!attribute [rw] strWebsite
#   @return [String, nil]
#
# @!attribute [rw] strWikidataID
#   @return [String, nil]
#
# @!attribute [rw] strWikipediaID
#   @return [String, nil]
V1Search = Struct.new(
  :album,
  :idAlbum,
  :idArtist,
  :idIMVDB,
  :idLabel,
  :idLyric,
  :idTrack,
  :intBornYear,
  :intCD,
  :intCharted,
  :intDiedYear,
  :intDuration,
  :intFormedYear,
  :intLoved,
  :intMembers,
  :intMusicVidComments,
  :intMusicVidDislikes,
  :intMusicVidFavorites,
  :intMusicVidLikes,
  :intMusicVidViews,
  :intSales,
  :intScore,
  :intScoreVotes,
  :intTotalListeners,
  :intTotalPlays,
  :intTrackNumber,
  :intYearReleased,
  :strAlbum,
  :strAlbum3DCase,
  :strAlbum3DFace,
  :strAlbum3DFlat,
  :strAlbum3DThumb,
  :strAlbumCDart,
  :strAlbumSpine,
  :strAlbumStripped,
  :strAlbumThumb,
  :strAlbumThumbBack,
  :strAlbumThumbHQ,
  :strAllMusicID,
  :strAmazonID,
  :strArtist,
  :strArtistAlternate,
  :strArtistBanner,
  :strArtistClearart,
  :strArtistCutout,
  :strArtistFanart,
  :strArtistFanart2,
  :strArtistFanart3,
  :strArtistFanart4,
  :strArtistLogo,
  :strArtistStripped,
  :strArtistThumb,
  :strArtistWideThumb,
  :strBBCReviewID,
  :strBiographyEN,
  :strCountry,
  :strCountryCode,
  :strDescriptionEN,
  :strDisbanded,
  :strDiscogsID,
  :strFacebook,
  :strGender,
  :strGeniusID,
  :strGenre,
  :strISNIcode,
  :strItunesID,
  :strLabel,
  :strLastFMChart,
  :strLocation,
  :strLocked,
  :strLyricWikiID,
  :strMood,
  :strMusicBrainzAlbumID,
  :strMusicBrainzArtistID,
  :strMusicBrainzID,
  :strMusicMozID,
  :strMusicVid,
  :strMusicVidCompany,
  :strMusicVidDirector,
  :strMusicVidScreen1,
  :strMusicVidScreen2,
  :strMusicVidScreen3,
  :strRateYourMusicID,
  :strReleaseFormat,
  :strReview,
  :strSpeed,
  :strStyle,
  :strTheme,
  :strTrack,
  :strTrack3x3,
  :strTrackLyrics,
  :strTrackThumb,
  :strTwitter,
  :strWebsite,
  :strWikidataID,
  :strWikipediaID,
  keyword_init: true
)

# Request payload for V1Search#load.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] s
#   @return [String]
V1SearchLoadMatch = Struct.new(
  :api_key,
  :s,
  keyword_init: true
)

# Request payload for V1Search#list.
#
# @!attribute [rw] api_key
#   @return [String]
#
# @!attribute [rw] a
#   @return [String, nil]
#
# @!attribute [rw] s
#   @return [String]
#
# @!attribute [rw] t
#   @return [String, nil]
V1SearchListMatch = Struct.new(
  :api_key,
  :a,
  :s,
  :t,
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
# @!attribute [rw] artists
#   @return [Array, nil]
#
# @!attribute [rw] track
#   @return [Array, nil]
V2Lookup = Struct.new(
  :album,
  :artists,
  :track,
  keyword_init: true
)

# Request payload for V2Lookup#load.
#
# @!attribute [rw] id_album
#   @return [Integer]
V2LookupLoadMatch = Struct.new(
  :id_album,
  keyword_init: true
)

# V2Search entity data model.
#
# @!attribute [rw] album
#   @return [Array, nil]
#
# @!attribute [rw] artists
#   @return [Array, nil]
#
# @!attribute [rw] track
#   @return [Array, nil]
V2Search = Struct.new(
  :album,
  :artists,
  :track,
  keyword_init: true
)

# Request payload for V2Search#load.
#
# @!attribute [rw] album_name
#   @return [String]
V2SearchLoadMatch = Struct.new(
  :album_name,
  keyword_init: true
)

