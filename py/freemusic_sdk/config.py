# FreeMusic SDK configuration


_shared_config = None


def shared_config():
    """Return the process-wide config, built once on first use.

    The SDK reads the config on every request and never writes to it, so one
    instance is shared by every client rather than rebuilt per client.

    The returned dict is shared: treat it as read-only. Callers that need to
    mutate should use make_config, which always returns a fresh copy.
    """
    global _shared_config
    if _shared_config is None:
        _shared_config = make_config()
    return _shared_config


def make_config():
    """Build a fresh, fully materialised config dict.

    Every call rebuilds the whole structure, so prefer shared_config unless
    you need a private copy you intend to mutate.
    """
    return {
        "main": {
            "name": "FreeMusic",
            "slug": "free-music",
            "version": "0.0.1",
            "target": "py",
        },
        "feature": {
            "test": {
        "options": {
          "active": False,
        },
      },
        },
        "options": {
            "base": "https://www.theaudiodb.com/api/v1/json",
            "auth": {
                "prefix": "",
            },
            "headers": {
        "content-type": "application/json",
      },
            "entity": {
                "v1_list": {},
                "v1_lookup": {},
                "v1_search": {},
                "v2_list": {},
                "v2_lookup": {},
                "v2_search": {},
            },
        },
        "entity": {
      "v1_list": {
        "fields": [
          {
            "name": "idAlbum",
            "short": "Album ID",
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "short": "Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "short": "IMVDB ID",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "short": "Lyrics ID",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "short": "Unique track ID",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "short": "CD number",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "short": "Track duration in milliseconds",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "short": "Number of loves/likes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "short": "Music video comment count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "short": "Music video dislike count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "short": "Music video favorite count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "short": "Music video like count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "short": "Music video view count",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "short": "Track score/rating",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "short": "Number of score votes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "short": "Total listener count",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "short": "Total play count",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "short": "Track number on album",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "short": "Album name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "short": "Artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "short": "Alternative artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "short": "Track description in English",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "short": "Musical genre",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "short": "Lock status",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "short": "Track mood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "short": "MusicBrainz Album ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "short": "MusicBrainz Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "short": "MusicBrainz Recording ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "short": "Music video URL",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "short": "Music video production company",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "short": "Music video director",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "short": "Music video screenshot 1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "short": "Music video screenshot 2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "short": "Music video screenshot 3",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "short": "Musical style",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "short": "Track theme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "short": "Track name",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "short": "3x3 track image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "short": "Track lyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
            "short": "Track thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "trending",
            "type": "`$ARRAY`",
          },
        ],
        "name": "v1_list",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "us",
                      "kind": "query",
                      "name": "country",
                      "orig": "country",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "kind": "query",
                      "name": "type",
                      "orig": "type",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/trending.php",
                "parts": [
                  "{api_key}",
                  "trending.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "country",
                    "format",
                    "type",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.trending`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/mvid.php",
                "parts": [
                  "{api_key}",
                  "mvid.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.mvids`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/track-top10.php",
                "parts": [
                  "{api_key}",
                  "track-top10.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.track`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/mostloved.php",
                "parts": [
                  "{api_key}",
                  "mostloved.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "format",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/mvid-mb.php",
                "parts": [
                  "{api_key}",
                  "mvid-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/track-top10-mb.php",
                "parts": [
                  "{api_key}",
                  "track-top10-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "v1_lookup": {
        "fields": [
          {
            "name": "idAlbum",
            "short": "Album ID",
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "short": "Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "short": "IMVDB ID",
            "type": "`$STRING`",
          },
          {
            "name": "idLabel",
            "short": "Label ID",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "short": "Lyrics ID",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "short": "Unique track ID",
            "type": "`$STRING`",
          },
          {
            "name": "intBornYear",
            "short": "Birth year (for solo artists)",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "short": "CD number",
            "type": "`$STRING`",
          },
          {
            "name": "intCharted",
            "short": "Chart position",
            "type": "`$STRING`",
          },
          {
            "name": "intDiedYear",
            "short": "Death year (if applicable)",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "short": "Track duration in milliseconds",
            "type": "`$STRING`",
          },
          {
            "name": "intFormedYear",
            "short": "Year the artist was formed",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "short": "Number of loves/likes",
            "type": "`$STRING`",
          },
          {
            "name": "intMembers",
            "short": "Number of band members",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "short": "Music video comment count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "short": "Music video dislike count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "short": "Music video favorite count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "short": "Music video like count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "short": "Music video view count",
            "type": "`$STRING`",
          },
          {
            "name": "intSales",
            "short": "Sales figures",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "short": "Track score/rating",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "short": "Number of score votes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "short": "Total listener count",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "short": "Total play count",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "short": "Track number on album",
            "type": "`$STRING`",
          },
          {
            "name": "intYearReleased",
            "short": "Release year",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "short": "Album name",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DCase",
            "short": "3D case image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFace",
            "short": "3D face image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFlat",
            "short": "3D flat image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DThumb",
            "short": "3D thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumCDart",
            "short": "CD art URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumSpine",
            "short": "Album spine image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumStripped",
            "short": "Album name stripped of special characters",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumb",
            "short": "Album thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbBack",
            "short": "Album back cover URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbHQ",
            "short": "High quality album thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAllMusicID",
            "short": "AllMusic ID",
            "type": "`$STRING`",
          },
          {
            "name": "strAmazonID",
            "short": "Amazon ID",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "short": "Artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "short": "Alternative artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistBanner",
            "short": "Banner image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistClearart",
            "short": "Clear art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistCutout",
            "short": "Cutout image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart",
            "short": "Fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart2",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart3",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart4",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistLogo",
            "short": "Logo image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistStripped",
            "short": "Artist name stripped",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistThumb",
            "short": "Thumbnail image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistWideThumb",
            "short": "Wide thumbnail image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strBBCReviewID",
            "short": "BBC Review ID",
            "type": "`$STRING`",
          },
          {
            "name": "strBiographyEN",
            "short": "Biography in English",
            "type": "`$STRING`",
          },
          {
            "name": "strCountry",
            "short": "Country of origin",
            "type": "`$STRING`",
          },
          {
            "name": "strCountryCode",
            "short": "Country code",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "short": "Track description in English",
            "type": "`$STRING`",
          },
          {
            "name": "strDisbanded",
            "short": "Disbandment status",
            "type": "`$STRING`",
          },
          {
            "name": "strDiscogsID",
            "short": "Discogs ID",
            "type": "`$STRING`",
          },
          {
            "name": "strFacebook",
            "short": "Facebook URL",
            "type": "`$STRING`",
          },
          {
            "name": "strGender",
            "short": "Gender",
            "type": "`$STRING`",
          },
          {
            "name": "strGeniusID",
            "short": "Genius ID",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "short": "Musical genre",
            "type": "`$STRING`",
          },
          {
            "name": "strISNIcode",
            "short": "ISNI code",
            "type": "`$STRING`",
          },
          {
            "name": "strItunesID",
            "short": "iTunes ID",
            "type": "`$STRING`",
          },
          {
            "name": "strLabel",
            "short": "Record label",
            "type": "`$STRING`",
          },
          {
            "name": "strLastFMChart",
            "short": "Last.fm chart URL",
            "type": "`$STRING`",
          },
          {
            "name": "strLocation",
            "short": "Recording location",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "short": "Lock status",
            "type": "`$STRING`",
          },
          {
            "name": "strLyricWikiID",
            "short": "LyricWiki ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "short": "Track mood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "short": "MusicBrainz Album ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "short": "MusicBrainz Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "short": "MusicBrainz Recording ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicMozID",
            "short": "MusicMoz ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "short": "Music video URL",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "short": "Music video production company",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "short": "Music video director",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "short": "Music video screenshot 1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "short": "Music video screenshot 2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "short": "Music video screenshot 3",
            "type": "`$STRING`",
          },
          {
            "name": "strRateYourMusicID",
            "short": "Rate Your Music ID",
            "type": "`$STRING`",
          },
          {
            "name": "strReleaseFormat",
            "short": "Release format (CD, Vinyl, etc.)",
            "type": "`$STRING`",
          },
          {
            "name": "strReview",
            "short": "Album review",
            "type": "`$STRING`",
          },
          {
            "name": "strSpeed",
            "short": "Album speed/tempo",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "short": "Musical style",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "short": "Track theme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "short": "Track name",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "short": "3x3 track image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "short": "Track lyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
            "short": "Track thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strTwitter",
            "short": "Twitter handle",
            "type": "`$STRING`",
          },
          {
            "name": "strWebsite",
            "short": "Official website URL",
            "type": "`$STRING`",
          },
          {
            "name": "strWikidataID",
            "short": "Wikidata ID",
            "type": "`$STRING`",
          },
          {
            "name": "strWikipediaID",
            "short": "Wikipedia ID",
            "type": "`$STRING`",
          },
        ],
        "name": "v1_lookup",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "h",
                      "orig": "h",
                      "type": "`$INTEGER`",
                    },
                    {
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/track.php",
                "parts": [
                  "{api_key}",
                  "track.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "h",
                    "m",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.track`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "type": "`$INTEGER`",
                    },
                    {
                      "example": 2115888,
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/album.php",
                "parts": [
                  "{api_key}",
                  "album.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                    "m",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.album`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": 112024,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/artist.php",
                "parts": [
                  "{api_key}",
                  "artist.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.artists`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/album-mb.php",
                "parts": [
                  "{api_key}",
                  "album-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/artist-mb.php",
                "parts": [
                  "{api_key}",
                  "artist-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/artist-social.php",
                "parts": [
                  "{api_key}",
                  "artist-social.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/track-mb.php",
                "parts": [
                  "{api_key}",
                  "track-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "i",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "v1_search": {
        "fields": [
          {
            "name": "album",
            "type": "`$ARRAY`",
          },
          {
            "name": "idAlbum",
            "short": "Unique album ID",
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "short": "Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "short": "IMVDB ID",
            "type": "`$STRING`",
          },
          {
            "name": "idLabel",
            "short": "Label ID",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "short": "Lyrics ID",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "short": "Unique track ID",
            "type": "`$STRING`",
          },
          {
            "name": "intBornYear",
            "short": "Birth year (for solo artists)",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "short": "CD number",
            "type": "`$STRING`",
          },
          {
            "name": "intCharted",
            "short": "Chart position",
            "type": "`$STRING`",
          },
          {
            "name": "intDiedYear",
            "short": "Death year (if applicable)",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "short": "Track duration in milliseconds",
            "type": "`$STRING`",
          },
          {
            "name": "intFormedYear",
            "short": "Year the artist was formed",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "short": "Number of loves/likes",
            "type": "`$STRING`",
          },
          {
            "name": "intMembers",
            "short": "Number of band members",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "short": "Music video comment count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "short": "Music video dislike count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "short": "Music video favorite count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "short": "Music video like count",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "short": "Music video view count",
            "type": "`$STRING`",
          },
          {
            "name": "intSales",
            "short": "Sales figures",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "short": "Album score/rating",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "short": "Number of score votes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "short": "Total listener count",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "short": "Total play count",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "short": "Track number on album",
            "type": "`$STRING`",
          },
          {
            "name": "intYearReleased",
            "short": "Release year",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "short": "Album name",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DCase",
            "short": "3D case image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFace",
            "short": "3D face image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFlat",
            "short": "3D flat image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DThumb",
            "short": "3D thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumCDart",
            "short": "CD art URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumSpine",
            "short": "Album spine image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumStripped",
            "short": "Album name stripped of special characters",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumb",
            "short": "Album thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbBack",
            "short": "Album back cover URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbHQ",
            "short": "High quality album thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strAllMusicID",
            "short": "AllMusic ID",
            "type": "`$STRING`",
          },
          {
            "name": "strAmazonID",
            "short": "Amazon ID",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "short": "Artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "short": "Alternative artist name",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistBanner",
            "short": "Banner image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistClearart",
            "short": "Clear art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistCutout",
            "short": "Cutout image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart",
            "short": "Fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart2",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart3",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart4",
            "short": "Additional fan art image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistLogo",
            "short": "Logo image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistStripped",
            "short": "Artist name stripped",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistThumb",
            "short": "Thumbnail image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistWideThumb",
            "short": "Wide thumbnail image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strBBCReviewID",
            "short": "BBC Review ID",
            "type": "`$STRING`",
          },
          {
            "name": "strBiographyEN",
            "short": "Biography in English",
            "type": "`$STRING`",
          },
          {
            "name": "strCountry",
            "short": "Country of origin",
            "type": "`$STRING`",
          },
          {
            "name": "strCountryCode",
            "short": "Country code",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "short": "Album description in English",
            "type": "`$STRING`",
          },
          {
            "name": "strDisbanded",
            "short": "Disbandment status",
            "type": "`$STRING`",
          },
          {
            "name": "strDiscogsID",
            "short": "Discogs ID",
            "type": "`$STRING`",
          },
          {
            "name": "strFacebook",
            "short": "Facebook URL",
            "type": "`$STRING`",
          },
          {
            "name": "strGender",
            "short": "Gender",
            "type": "`$STRING`",
          },
          {
            "name": "strGeniusID",
            "short": "Genius ID",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "short": "Musical genre",
            "type": "`$STRING`",
          },
          {
            "name": "strISNIcode",
            "short": "ISNI code",
            "type": "`$STRING`",
          },
          {
            "name": "strItunesID",
            "short": "iTunes ID",
            "type": "`$STRING`",
          },
          {
            "name": "strLabel",
            "short": "Record label",
            "type": "`$STRING`",
          },
          {
            "name": "strLastFMChart",
            "short": "Last.fm chart URL",
            "type": "`$STRING`",
          },
          {
            "name": "strLocation",
            "short": "Recording location",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "short": "Lock status",
            "type": "`$STRING`",
          },
          {
            "name": "strLyricWikiID",
            "short": "LyricWiki ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "short": "Album mood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "short": "MusicBrainz Album ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "short": "MusicBrainz Artist ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "short": "MusicBrainz Release Group ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicMozID",
            "short": "MusicMoz ID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "short": "Music video URL",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "short": "Music video production company",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "short": "Music video director",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "short": "Music video screenshot 1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "short": "Music video screenshot 2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "short": "Music video screenshot 3",
            "type": "`$STRING`",
          },
          {
            "name": "strRateYourMusicID",
            "short": "Rate Your Music ID",
            "type": "`$STRING`",
          },
          {
            "name": "strReleaseFormat",
            "short": "Release format (CD, Vinyl, etc.)",
            "type": "`$STRING`",
          },
          {
            "name": "strReview",
            "short": "Album review",
            "type": "`$STRING`",
          },
          {
            "name": "strSpeed",
            "short": "Album speed/tempo",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "short": "Musical style",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "short": "Album theme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "short": "Track name",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "short": "3x3 track image URL",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "short": "Track lyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
            "short": "Track thumbnail URL",
            "type": "`$STRING`",
          },
          {
            "name": "strTwitter",
            "short": "Twitter handle",
            "type": "`$STRING`",
          },
          {
            "name": "strWebsite",
            "short": "Official website URL",
            "type": "`$STRING`",
          },
          {
            "name": "strWikidataID",
            "short": "Wikidata ID",
            "type": "`$STRING`",
          },
          {
            "name": "strWikipediaID",
            "short": "Wikipedia ID",
            "type": "`$STRING`",
          },
        ],
        "name": "v1_search",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "Homework",
                      "kind": "query",
                      "name": "a",
                      "orig": "a",
                      "type": "`$STRING`",
                    },
                    {
                      "example": "daft_punk",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/searchalbum.php",
                "parts": [
                  "{api_key}",
                  "searchalbum.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "a",
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.album`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "example": "yellow",
                      "kind": "query",
                      "name": "t",
                      "orig": "t",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/searchtrack.php",
                "parts": [
                  "{api_key}",
                  "searchtrack.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                    "t",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.track`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/discography.php",
                "parts": [
                  "{api_key}",
                  "discography.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.album`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "123",
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/search.php",
                "parts": [
                  "{api_key}",
                  "search.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.artists`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/{apiKey}/discography-mb.php",
                "parts": [
                  "{api_key}",
                  "discography-mb.php",
                ],
                "rename": {
                  "param": {
                    "apiKey": "api_key",
                  },
                },
                "select": {
                  "exist": [
                    "api_key",
                    "s",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "v2_list": {
        "fields": [
          {
            "name": "album",
            "type": "`$ARRAY`",
          },
        ],
        "name": "v2_list",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": 111239,
                      "kind": "param",
                      "name": "id_artist",
                      "orig": "id_artist",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/list/discography/{idArtist}",
                "parts": [
                  "list",
                  "discography",
                  "{id_artist}",
                ],
                "rename": {
                  "param": {
                    "idArtist": "id_artist",
                  },
                },
                "select": {
                  "exist": [
                    "id_artist",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [
            [
              "discography",
            ],
          ],
        },
      },
      "v2_lookup": {
        "fields": [
          {
            "name": "album",
            "type": "`$ARRAY`",
          },
          {
            "name": "artists",
            "type": "`$ARRAY`",
          },
          {
            "name": "track",
            "type": "`$ARRAY`",
          },
        ],
        "name": "v2_lookup",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": 2109615,
                      "kind": "param",
                      "name": "id_album",
                      "orig": "id_album",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/album/{idAlbum}",
                "parts": [
                  "lookup",
                  "album",
                  "{id_album}",
                ],
                "rename": {
                  "param": {
                    "idAlbum": "id_album",
                  },
                },
                "select": {
                  "exist": [
                    "id_album",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": 111239,
                      "kind": "param",
                      "name": "id_artist",
                      "orig": "id_artist",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/artist/{idArtist}",
                "parts": [
                  "lookup",
                  "artist",
                  "{id_artist}",
                ],
                "rename": {
                  "param": {
                    "idArtist": "id_artist",
                  },
                },
                "select": {
                  "exist": [
                    "id_artist",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": 32724183,
                      "kind": "param",
                      "name": "id_track",
                      "orig": "id_track",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/track/{idTrack}",
                "parts": [
                  "lookup",
                  "track",
                  "{id_track}",
                ],
                "rename": {
                  "param": {
                    "idTrack": "id_track",
                  },
                },
                "select": {
                  "exist": [
                    "id_track",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "1dc4c347-a1db-32aa-b14f-bc9cc507b843",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/album_mb/{musicBrainzId}",
                "parts": [
                  "lookup",
                  "album_mb",
                  "{music_brainz_id}",
                ],
                "rename": {
                  "param": {
                    "musicBrainzId": "music_brainz_id",
                  },
                },
                "select": {
                  "exist": [
                    "music_brainz_id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/artist_mb/{musicBrainzId}",
                "parts": [
                  "lookup",
                  "artist_mb",
                  "{music_brainz_id}",
                ],
                "rename": {
                  "param": {
                    "musicBrainzId": "music_brainz_id",
                  },
                },
                "select": {
                  "exist": [
                    "music_brainz_id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "50369905-68ca-48d2-912d-b37330ff7dc3",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/lookup/track_mb/{musicBrainzId}",
                "parts": [
                  "lookup",
                  "track_mb",
                  "{music_brainz_id}",
                ],
                "rename": {
                  "param": {
                    "musicBrainzId": "music_brainz_id",
                  },
                },
                "select": {
                  "exist": [
                    "music_brainz_id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [
            [
              "album",
            ],
            [
              "album_mb",
            ],
            [
              "artist",
            ],
            [
              "artist_mb",
            ],
            [
              "track",
            ],
            [
              "track_mb",
            ],
          ],
        },
      },
      "v2_search": {
        "fields": [
          {
            "name": "album",
            "type": "`$ARRAY`",
          },
          {
            "name": "artists",
            "type": "`$ARRAY`",
          },
          {
            "name": "track",
            "type": "`$ARRAY`",
          },
        ],
        "name": "v2_search",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": "parachutes",
                      "kind": "param",
                      "name": "album_name",
                      "orig": "album_name",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/search/album/{albumName}",
                "parts": [
                  "search",
                  "album",
                  "{album_name}",
                ],
                "rename": {
                  "param": {
                    "albumName": "album_name",
                  },
                },
                "select": {
                  "exist": [
                    "album_name",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "coldplay",
                      "kind": "param",
                      "name": "artist_name",
                      "orig": "artist_name",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/search/artist/{artistName}",
                "parts": [
                  "search",
                  "artist",
                  "{artist_name}",
                ],
                "rename": {
                  "param": {
                    "artistName": "artist_name",
                  },
                },
                "select": {
                  "exist": [
                    "artist_name",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
              {
                "args": {
                  "params": [
                    {
                      "example": "yellow",
                      "kind": "param",
                      "name": "track_name",
                      "orig": "track_name",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/search/track/{trackName}",
                "parts": [
                  "search",
                  "track",
                  "{track_name}",
                ],
                "rename": {
                  "param": {
                    "trackName": "track_name",
                  },
                },
                "select": {
                  "exist": [
                    "track_name",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [
            [
              "album",
            ],
            [
              "artist",
            ],
            [
              "track",
            ],
          ],
        },
      },
    },
    }
