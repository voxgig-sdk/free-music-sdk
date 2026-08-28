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
    public ?string $idAlbum = null;
    public ?string $idArtist = null;
    public ?string $idIMVDB = null;
    public ?string $idLyric = null;
    public ?string $idTrack = null;
    public ?string $intCD = null;
    public ?string $intDuration = null;
    public ?string $intLoved = null;
    public ?string $intMusicVidComments = null;
    public ?string $intMusicVidDislikes = null;
    public ?string $intMusicVidFavorites = null;
    public ?string $intMusicVidLikes = null;
    public ?string $intMusicVidViews = null;
    public ?string $intScore = null;
    public ?string $intScoreVotes = null;
    public ?string $intTotalListeners = null;
    public ?string $intTotalPlays = null;
    public ?string $intTrackNumber = null;
    public ?string $strAlbum = null;
    public ?string $strArtist = null;
    public ?string $strArtistAlternate = null;
    public ?string $strDescriptionEN = null;
    public ?string $strGenre = null;
    public ?string $strLocked = null;
    public ?string $strMood = null;
    public ?string $strMusicBrainzAlbumID = null;
    public ?string $strMusicBrainzArtistID = null;
    public ?string $strMusicBrainzID = null;
    public ?string $strMusicVid = null;
    public ?string $strMusicVidCompany = null;
    public ?string $strMusicVidDirector = null;
    public ?string $strMusicVidScreen1 = null;
    public ?string $strMusicVidScreen2 = null;
    public ?string $strMusicVidScreen3 = null;
    public ?string $strStyle = null;
    public ?string $strTheme = null;
    public ?string $strTrack = null;
    public ?string $strTrack3x3 = null;
    public ?string $strTrackLyrics = null;
    public ?string $strTrackThumb = null;
    public ?array $trending = null;
}

/** Request payload for V1List#load. */
class V1ListLoadMatch
{
    public string $api_key;
    public ?string $format = null;
    public ?string $i = null;
    public ?string $s = null;
}

/** Request payload for V1List#list. */
class V1ListListMatch
{
    public string $api_key;
    public ?string $country = null;
    public ?string $format = null;
    public ?string $type = null;
    public ?int $i = null;
    public ?string $s = null;
}

/** V1Lookup entity data model. */
class V1Lookup
{
    public ?string $idAlbum = null;
    public ?string $idArtist = null;
    public ?string $idIMVDB = null;
    public ?string $idLabel = null;
    public ?string $idLyric = null;
    public ?string $idTrack = null;
    public ?string $intBornYear = null;
    public ?string $intCD = null;
    public ?string $intCharted = null;
    public ?string $intDiedYear = null;
    public ?string $intDuration = null;
    public ?string $intFormedYear = null;
    public ?string $intLoved = null;
    public ?string $intMembers = null;
    public ?string $intMusicVidComments = null;
    public ?string $intMusicVidDislikes = null;
    public ?string $intMusicVidFavorites = null;
    public ?string $intMusicVidLikes = null;
    public ?string $intMusicVidViews = null;
    public ?string $intSales = null;
    public ?string $intScore = null;
    public ?string $intScoreVotes = null;
    public ?string $intTotalListeners = null;
    public ?string $intTotalPlays = null;
    public ?string $intTrackNumber = null;
    public ?string $intYearReleased = null;
    public ?string $strAlbum = null;
    public ?string $strAlbum3DCase = null;
    public ?string $strAlbum3DFace = null;
    public ?string $strAlbum3DFlat = null;
    public ?string $strAlbum3DThumb = null;
    public ?string $strAlbumCDart = null;
    public ?string $strAlbumSpine = null;
    public ?string $strAlbumStripped = null;
    public ?string $strAlbumThumb = null;
    public ?string $strAlbumThumbBack = null;
    public ?string $strAlbumThumbHQ = null;
    public ?string $strAllMusicID = null;
    public ?string $strAmazonID = null;
    public ?string $strArtist = null;
    public ?string $strArtistAlternate = null;
    public ?string $strArtistBanner = null;
    public ?string $strArtistClearart = null;
    public ?string $strArtistCutout = null;
    public ?string $strArtistFanart = null;
    public ?string $strArtistFanart2 = null;
    public ?string $strArtistFanart3 = null;
    public ?string $strArtistFanart4 = null;
    public ?string $strArtistLogo = null;
    public ?string $strArtistStripped = null;
    public ?string $strArtistThumb = null;
    public ?string $strArtistWideThumb = null;
    public ?string $strBBCReviewID = null;
    public ?string $strBiographyEN = null;
    public ?string $strCountry = null;
    public ?string $strCountryCode = null;
    public ?string $strDescriptionEN = null;
    public ?string $strDisbanded = null;
    public ?string $strDiscogsID = null;
    public ?string $strFacebook = null;
    public ?string $strGender = null;
    public ?string $strGeniusID = null;
    public ?string $strGenre = null;
    public ?string $strISNIcode = null;
    public ?string $strItunesID = null;
    public ?string $strLabel = null;
    public ?string $strLastFMChart = null;
    public ?string $strLocation = null;
    public ?string $strLocked = null;
    public ?string $strLyricWikiID = null;
    public ?string $strMood = null;
    public ?string $strMusicBrainzAlbumID = null;
    public ?string $strMusicBrainzArtistID = null;
    public ?string $strMusicBrainzID = null;
    public ?string $strMusicMozID = null;
    public ?string $strMusicVid = null;
    public ?string $strMusicVidCompany = null;
    public ?string $strMusicVidDirector = null;
    public ?string $strMusicVidScreen1 = null;
    public ?string $strMusicVidScreen2 = null;
    public ?string $strMusicVidScreen3 = null;
    public ?string $strRateYourMusicID = null;
    public ?string $strReleaseFormat = null;
    public ?string $strReview = null;
    public ?string $strSpeed = null;
    public ?string $strStyle = null;
    public ?string $strTheme = null;
    public ?string $strTrack = null;
    public ?string $strTrack3x3 = null;
    public ?string $strTrackLyrics = null;
    public ?string $strTrackThumb = null;
    public ?string $strTwitter = null;
    public ?string $strWebsite = null;
    public ?string $strWikidataID = null;
    public ?string $strWikipediaID = null;
}

/** Request payload for V1Lookup#load. */
class V1LookupLoadMatch
{
    public string $api_key;
    public string $i;
}

/** Request payload for V1Lookup#list. */
class V1LookupListMatch
{
    public string $api_key;
    public ?int $h = null;
    public ?int $m = null;
    public ?int $i = null;
}

/** V1Search entity data model. */
class V1Search
{
    public ?array $album = null;
    public ?string $idAlbum = null;
    public ?string $idArtist = null;
    public ?string $idIMVDB = null;
    public ?string $idLabel = null;
    public ?string $idLyric = null;
    public ?string $idTrack = null;
    public ?string $intBornYear = null;
    public ?string $intCD = null;
    public ?string $intCharted = null;
    public ?string $intDiedYear = null;
    public ?string $intDuration = null;
    public ?string $intFormedYear = null;
    public ?string $intLoved = null;
    public ?string $intMembers = null;
    public ?string $intMusicVidComments = null;
    public ?string $intMusicVidDislikes = null;
    public ?string $intMusicVidFavorites = null;
    public ?string $intMusicVidLikes = null;
    public ?string $intMusicVidViews = null;
    public ?string $intSales = null;
    public ?string $intScore = null;
    public ?string $intScoreVotes = null;
    public ?string $intTotalListeners = null;
    public ?string $intTotalPlays = null;
    public ?string $intTrackNumber = null;
    public ?string $intYearReleased = null;
    public ?string $strAlbum = null;
    public ?string $strAlbum3DCase = null;
    public ?string $strAlbum3DFace = null;
    public ?string $strAlbum3DFlat = null;
    public ?string $strAlbum3DThumb = null;
    public ?string $strAlbumCDart = null;
    public ?string $strAlbumSpine = null;
    public ?string $strAlbumStripped = null;
    public ?string $strAlbumThumb = null;
    public ?string $strAlbumThumbBack = null;
    public ?string $strAlbumThumbHQ = null;
    public ?string $strAllMusicID = null;
    public ?string $strAmazonID = null;
    public ?string $strArtist = null;
    public ?string $strArtistAlternate = null;
    public ?string $strArtistBanner = null;
    public ?string $strArtistClearart = null;
    public ?string $strArtistCutout = null;
    public ?string $strArtistFanart = null;
    public ?string $strArtistFanart2 = null;
    public ?string $strArtistFanart3 = null;
    public ?string $strArtistFanart4 = null;
    public ?string $strArtistLogo = null;
    public ?string $strArtistStripped = null;
    public ?string $strArtistThumb = null;
    public ?string $strArtistWideThumb = null;
    public ?string $strBBCReviewID = null;
    public ?string $strBiographyEN = null;
    public ?string $strCountry = null;
    public ?string $strCountryCode = null;
    public ?string $strDescriptionEN = null;
    public ?string $strDisbanded = null;
    public ?string $strDiscogsID = null;
    public ?string $strFacebook = null;
    public ?string $strGender = null;
    public ?string $strGeniusID = null;
    public ?string $strGenre = null;
    public ?string $strISNIcode = null;
    public ?string $strItunesID = null;
    public ?string $strLabel = null;
    public ?string $strLastFMChart = null;
    public ?string $strLocation = null;
    public ?string $strLocked = null;
    public ?string $strLyricWikiID = null;
    public ?string $strMood = null;
    public ?string $strMusicBrainzAlbumID = null;
    public ?string $strMusicBrainzArtistID = null;
    public ?string $strMusicBrainzID = null;
    public ?string $strMusicMozID = null;
    public ?string $strMusicVid = null;
    public ?string $strMusicVidCompany = null;
    public ?string $strMusicVidDirector = null;
    public ?string $strMusicVidScreen1 = null;
    public ?string $strMusicVidScreen2 = null;
    public ?string $strMusicVidScreen3 = null;
    public ?string $strRateYourMusicID = null;
    public ?string $strReleaseFormat = null;
    public ?string $strReview = null;
    public ?string $strSpeed = null;
    public ?string $strStyle = null;
    public ?string $strTheme = null;
    public ?string $strTrack = null;
    public ?string $strTrack3x3 = null;
    public ?string $strTrackLyrics = null;
    public ?string $strTrackThumb = null;
    public ?string $strTwitter = null;
    public ?string $strWebsite = null;
    public ?string $strWikidataID = null;
    public ?string $strWikipediaID = null;
}

/** Request payload for V1Search#load. */
class V1SearchLoadMatch
{
    public string $api_key;
    public string $s;
}

/** Request payload for V1Search#list. */
class V1SearchListMatch
{
    public string $api_key;
    public ?string $a = null;
    public string $s;
    public ?string $t = null;
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
    public ?array $artists = null;
    public ?array $track = null;
}

/** Request payload for V2Lookup#load. */
class V2LookupLoadMatch
{
    public int $id_album;
}

/** V2Search entity data model. */
class V2Search
{
    public ?array $album = null;
    public ?array $artists = null;
    public ?array $track = null;
}

/** Request payload for V2Search#load. */
class V2SearchLoadMatch
{
    public string $album_name;
}

