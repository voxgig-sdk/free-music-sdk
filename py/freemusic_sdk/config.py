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
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
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
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "type": "`$STRING`",
          },
          {
            "name": "idLabel",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "type": "`$STRING`",
          },
          {
            "name": "intBornYear",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "type": "`$STRING`",
          },
          {
            "name": "intCharted",
            "type": "`$STRING`",
          },
          {
            "name": "intDiedYear",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "type": "`$STRING`",
          },
          {
            "name": "intFormedYear",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "type": "`$STRING`",
          },
          {
            "name": "intMembers",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "type": "`$STRING`",
          },
          {
            "name": "intSales",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "type": "`$STRING`",
          },
          {
            "name": "intYearReleased",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DCase",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFace",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFlat",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumCDart",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumSpine",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumStripped",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbBack",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbHQ",
            "type": "`$STRING`",
          },
          {
            "name": "strAllMusicID",
            "type": "`$STRING`",
          },
          {
            "name": "strAmazonID",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistBanner",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistClearart",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistCutout",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart2",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart3",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart4",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistLogo",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistStripped",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistWideThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strBBCReviewID",
            "type": "`$STRING`",
          },
          {
            "name": "strBiographyEN",
            "type": "`$STRING`",
          },
          {
            "name": "strCountry",
            "type": "`$STRING`",
          },
          {
            "name": "strCountryCode",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "type": "`$STRING`",
          },
          {
            "name": "strDisbanded",
            "type": "`$STRING`",
          },
          {
            "name": "strDiscogsID",
            "type": "`$STRING`",
          },
          {
            "name": "strFacebook",
            "type": "`$STRING`",
          },
          {
            "name": "strGender",
            "type": "`$STRING`",
          },
          {
            "name": "strGeniusID",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "type": "`$STRING`",
          },
          {
            "name": "strISNIcode",
            "type": "`$STRING`",
          },
          {
            "name": "strItunesID",
            "type": "`$STRING`",
          },
          {
            "name": "strLabel",
            "type": "`$STRING`",
          },
          {
            "name": "strLastFMChart",
            "type": "`$STRING`",
          },
          {
            "name": "strLocation",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "type": "`$STRING`",
          },
          {
            "name": "strLyricWikiID",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicMozID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "type": "`$STRING`",
          },
          {
            "name": "strRateYourMusicID",
            "type": "`$STRING`",
          },
          {
            "name": "strReleaseFormat",
            "type": "`$STRING`",
          },
          {
            "name": "strReview",
            "type": "`$STRING`",
          },
          {
            "name": "strSpeed",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strTwitter",
            "type": "`$STRING`",
          },
          {
            "name": "strWebsite",
            "type": "`$STRING`",
          },
          {
            "name": "strWikidataID",
            "type": "`$STRING`",
          },
          {
            "name": "strWikipediaID",
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
            "type": "`$STRING`",
          },
          {
            "name": "idArtist",
            "type": "`$STRING`",
          },
          {
            "name": "idIMVDB",
            "type": "`$STRING`",
          },
          {
            "name": "idLabel",
            "type": "`$STRING`",
          },
          {
            "name": "idLyric",
            "type": "`$STRING`",
          },
          {
            "name": "idTrack",
            "type": "`$STRING`",
          },
          {
            "name": "intBornYear",
            "type": "`$STRING`",
          },
          {
            "name": "intCD",
            "type": "`$STRING`",
          },
          {
            "name": "intCharted",
            "type": "`$STRING`",
          },
          {
            "name": "intDiedYear",
            "type": "`$STRING`",
          },
          {
            "name": "intDuration",
            "type": "`$STRING`",
          },
          {
            "name": "intFormedYear",
            "type": "`$STRING`",
          },
          {
            "name": "intLoved",
            "type": "`$STRING`",
          },
          {
            "name": "intMembers",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidComments",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidDislikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidFavorites",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidLikes",
            "type": "`$STRING`",
          },
          {
            "name": "intMusicVidViews",
            "type": "`$STRING`",
          },
          {
            "name": "intSales",
            "type": "`$STRING`",
          },
          {
            "name": "intScore",
            "type": "`$STRING`",
          },
          {
            "name": "intScoreVotes",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalListeners",
            "type": "`$STRING`",
          },
          {
            "name": "intTotalPlays",
            "type": "`$STRING`",
          },
          {
            "name": "intTrackNumber",
            "type": "`$STRING`",
          },
          {
            "name": "intYearReleased",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DCase",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFace",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DFlat",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbum3DThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumCDart",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumSpine",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumStripped",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbBack",
            "type": "`$STRING`",
          },
          {
            "name": "strAlbumThumbHQ",
            "type": "`$STRING`",
          },
          {
            "name": "strAllMusicID",
            "type": "`$STRING`",
          },
          {
            "name": "strAmazonID",
            "type": "`$STRING`",
          },
          {
            "name": "strArtist",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistAlternate",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistBanner",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistClearart",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistCutout",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart2",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart3",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistFanart4",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistLogo",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistStripped",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strArtistWideThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strBBCReviewID",
            "type": "`$STRING`",
          },
          {
            "name": "strBiographyEN",
            "type": "`$STRING`",
          },
          {
            "name": "strCountry",
            "type": "`$STRING`",
          },
          {
            "name": "strCountryCode",
            "type": "`$STRING`",
          },
          {
            "name": "strDescriptionEN",
            "type": "`$STRING`",
          },
          {
            "name": "strDisbanded",
            "type": "`$STRING`",
          },
          {
            "name": "strDiscogsID",
            "type": "`$STRING`",
          },
          {
            "name": "strFacebook",
            "type": "`$STRING`",
          },
          {
            "name": "strGender",
            "type": "`$STRING`",
          },
          {
            "name": "strGeniusID",
            "type": "`$STRING`",
          },
          {
            "name": "strGenre",
            "type": "`$STRING`",
          },
          {
            "name": "strISNIcode",
            "type": "`$STRING`",
          },
          {
            "name": "strItunesID",
            "type": "`$STRING`",
          },
          {
            "name": "strLabel",
            "type": "`$STRING`",
          },
          {
            "name": "strLastFMChart",
            "type": "`$STRING`",
          },
          {
            "name": "strLocation",
            "type": "`$STRING`",
          },
          {
            "name": "strLocked",
            "type": "`$STRING`",
          },
          {
            "name": "strLyricWikiID",
            "type": "`$STRING`",
          },
          {
            "name": "strMood",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzAlbumID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzArtistID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicBrainzID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicMozID",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVid",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidCompany",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidDirector",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen1",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen2",
            "type": "`$STRING`",
          },
          {
            "name": "strMusicVidScreen3",
            "type": "`$STRING`",
          },
          {
            "name": "strRateYourMusicID",
            "type": "`$STRING`",
          },
          {
            "name": "strReleaseFormat",
            "type": "`$STRING`",
          },
          {
            "name": "strReview",
            "type": "`$STRING`",
          },
          {
            "name": "strSpeed",
            "type": "`$STRING`",
          },
          {
            "name": "strStyle",
            "type": "`$STRING`",
          },
          {
            "name": "strTheme",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack",
            "type": "`$STRING`",
          },
          {
            "name": "strTrack3x3",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackLyrics",
            "type": "`$STRING`",
          },
          {
            "name": "strTrackThumb",
            "type": "`$STRING`",
          },
          {
            "name": "strTwitter",
            "type": "`$STRING`",
          },
          {
            "name": "strWebsite",
            "type": "`$STRING`",
          },
          {
            "name": "strWikidataID",
            "type": "`$STRING`",
          },
          {
            "name": "strWikipediaID",
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
