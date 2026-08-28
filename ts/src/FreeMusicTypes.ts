// Typed models for the FreeMusic SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.

export interface V1List {
  idAlbum?: string
  idArtist?: string
  idIMVDB?: string
  idLyric?: string
  idTrack?: string
  intCD?: string
  intDuration?: string
  intLoved?: string
  intMusicVidComments?: string
  intMusicVidDislikes?: string
  intMusicVidFavorites?: string
  intMusicVidLikes?: string
  intMusicVidViews?: string
  intScore?: string
  intScoreVotes?: string
  intTotalListeners?: string
  intTotalPlays?: string
  intTrackNumber?: string
  strAlbum?: string
  strArtist?: string
  strArtistAlternate?: string
  strDescriptionEN?: string
  strGenre?: string
  strLocked?: string
  strMood?: string
  strMusicBrainzAlbumID?: string
  strMusicBrainzArtistID?: string
  strMusicBrainzID?: string
  strMusicVid?: string
  strMusicVidCompany?: string
  strMusicVidDirector?: string
  strMusicVidScreen1?: string
  strMusicVidScreen2?: string
  strMusicVidScreen3?: string
  strStyle?: string
  strTheme?: string
  strTrack?: string
  strTrack3x3?: string
  strTrackLyrics?: string
  strTrackThumb?: string
  trending?: any[]
}

export interface V1ListLoadMatch {
  api_key: string
  format?: string
  i?: string
  s?: string
}

export interface V1ListListMatch {
  api_key: string
  country?: string
  format?: string
  type?: string
  i?: number
  s?: string
}

export interface V1Lookup {
  idAlbum?: string
  idArtist?: string
  idIMVDB?: string
  idLabel?: string
  idLyric?: string
  idTrack?: string
  intBornYear?: string
  intCD?: string
  intCharted?: string
  intDiedYear?: string
  intDuration?: string
  intFormedYear?: string
  intLoved?: string
  intMembers?: string
  intMusicVidComments?: string
  intMusicVidDislikes?: string
  intMusicVidFavorites?: string
  intMusicVidLikes?: string
  intMusicVidViews?: string
  intSales?: string
  intScore?: string
  intScoreVotes?: string
  intTotalListeners?: string
  intTotalPlays?: string
  intTrackNumber?: string
  intYearReleased?: string
  strAlbum?: string
  strAlbum3DCase?: string
  strAlbum3DFace?: string
  strAlbum3DFlat?: string
  strAlbum3DThumb?: string
  strAlbumCDart?: string
  strAlbumSpine?: string
  strAlbumStripped?: string
  strAlbumThumb?: string
  strAlbumThumbBack?: string
  strAlbumThumbHQ?: string
  strAllMusicID?: string
  strAmazonID?: string
  strArtist?: string
  strArtistAlternate?: string
  strArtistBanner?: string
  strArtistClearart?: string
  strArtistCutout?: string
  strArtistFanart?: string
  strArtistFanart2?: string
  strArtistFanart3?: string
  strArtistFanart4?: string
  strArtistLogo?: string
  strArtistStripped?: string
  strArtistThumb?: string
  strArtistWideThumb?: string
  strBBCReviewID?: string
  strBiographyEN?: string
  strCountry?: string
  strCountryCode?: string
  strDescriptionEN?: string
  strDisbanded?: string
  strDiscogsID?: string
  strFacebook?: string
  strGender?: string
  strGeniusID?: string
  strGenre?: string
  strISNIcode?: string
  strItunesID?: string
  strLabel?: string
  strLastFMChart?: string
  strLocation?: string
  strLocked?: string
  strLyricWikiID?: string
  strMood?: string
  strMusicBrainzAlbumID?: string
  strMusicBrainzArtistID?: string
  strMusicBrainzID?: string
  strMusicMozID?: string
  strMusicVid?: string
  strMusicVidCompany?: string
  strMusicVidDirector?: string
  strMusicVidScreen1?: string
  strMusicVidScreen2?: string
  strMusicVidScreen3?: string
  strRateYourMusicID?: string
  strReleaseFormat?: string
  strReview?: string
  strSpeed?: string
  strStyle?: string
  strTheme?: string
  strTrack?: string
  strTrack3x3?: string
  strTrackLyrics?: string
  strTrackThumb?: string
  strTwitter?: string
  strWebsite?: string
  strWikidataID?: string
  strWikipediaID?: string
}

export interface V1LookupLoadMatch {
  api_key: string
  i: string
}

export interface V1LookupListMatch {
  api_key: string
  h?: number
  m?: number
  i?: number
}

export interface V1Search {
  album?: any[]
  idAlbum?: string
  idArtist?: string
  idIMVDB?: string
  idLabel?: string
  idLyric?: string
  idTrack?: string
  intBornYear?: string
  intCD?: string
  intCharted?: string
  intDiedYear?: string
  intDuration?: string
  intFormedYear?: string
  intLoved?: string
  intMembers?: string
  intMusicVidComments?: string
  intMusicVidDislikes?: string
  intMusicVidFavorites?: string
  intMusicVidLikes?: string
  intMusicVidViews?: string
  intSales?: string
  intScore?: string
  intScoreVotes?: string
  intTotalListeners?: string
  intTotalPlays?: string
  intTrackNumber?: string
  intYearReleased?: string
  strAlbum?: string
  strAlbum3DCase?: string
  strAlbum3DFace?: string
  strAlbum3DFlat?: string
  strAlbum3DThumb?: string
  strAlbumCDart?: string
  strAlbumSpine?: string
  strAlbumStripped?: string
  strAlbumThumb?: string
  strAlbumThumbBack?: string
  strAlbumThumbHQ?: string
  strAllMusicID?: string
  strAmazonID?: string
  strArtist?: string
  strArtistAlternate?: string
  strArtistBanner?: string
  strArtistClearart?: string
  strArtistCutout?: string
  strArtistFanart?: string
  strArtistFanart2?: string
  strArtistFanart3?: string
  strArtistFanart4?: string
  strArtistLogo?: string
  strArtistStripped?: string
  strArtistThumb?: string
  strArtistWideThumb?: string
  strBBCReviewID?: string
  strBiographyEN?: string
  strCountry?: string
  strCountryCode?: string
  strDescriptionEN?: string
  strDisbanded?: string
  strDiscogsID?: string
  strFacebook?: string
  strGender?: string
  strGeniusID?: string
  strGenre?: string
  strISNIcode?: string
  strItunesID?: string
  strLabel?: string
  strLastFMChart?: string
  strLocation?: string
  strLocked?: string
  strLyricWikiID?: string
  strMood?: string
  strMusicBrainzAlbumID?: string
  strMusicBrainzArtistID?: string
  strMusicBrainzID?: string
  strMusicMozID?: string
  strMusicVid?: string
  strMusicVidCompany?: string
  strMusicVidDirector?: string
  strMusicVidScreen1?: string
  strMusicVidScreen2?: string
  strMusicVidScreen3?: string
  strRateYourMusicID?: string
  strReleaseFormat?: string
  strReview?: string
  strSpeed?: string
  strStyle?: string
  strTheme?: string
  strTrack?: string
  strTrack3x3?: string
  strTrackLyrics?: string
  strTrackThumb?: string
  strTwitter?: string
  strWebsite?: string
  strWikidataID?: string
  strWikipediaID?: string
}

export interface V1SearchLoadMatch {
  api_key: string
  s: string
}

export interface V1SearchListMatch {
  api_key: string
  a?: string
  s: string
  t?: string
}

export interface V2List {
  album?: any[]
}

export interface V2ListLoadMatch {
  id_artist: number
}

export interface V2Lookup {
  album?: any[]
  artists?: any[]
  track?: any[]
}

export interface V2LookupLoadMatch {
  id_album: number
}

export interface V2Search {
  album?: any[]
  artists?: any[]
  track?: any[]
}

export interface V2SearchLoadMatch {
  album_name: string
}

