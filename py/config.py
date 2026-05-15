# FreeMusic SDK configuration


def make_config():
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
                "prefix": "Bearer",
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
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 4,
          },
          {
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 5,
          },
          {
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 6,
          },
          {
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 7,
          },
          {
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 8,
          },
          {
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 9,
          },
          {
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 10,
          },
          {
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 11,
          },
          {
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 12,
          },
          {
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 13,
          },
          {
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 14,
          },
          {
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 15,
          },
          {
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 16,
          },
          {
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 17,
          },
          {
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 18,
          },
          {
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 19,
          },
          {
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 20,
          },
          {
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 21,
          },
          {
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 22,
          },
          {
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 23,
          },
          {
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 24,
          },
          {
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 25,
          },
          {
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 26,
          },
          {
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 27,
          },
          {
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 28,
          },
          {
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 29,
          },
          {
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 30,
          },
          {
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 31,
          },
          {
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 32,
          },
          {
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 33,
          },
          {
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 34,
          },
          {
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 35,
          },
          {
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 36,
          },
          {
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 37,
          },
          {
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 38,
          },
          {
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 39,
          },
          {
            "name": "trending",
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 40,
          },
        ],
        "name": "v1_list",
        "op": {
          "list": {
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
                      "active": True,
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
                      "active": True,
                    },
                    {
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                    {
                      "kind": "query",
                      "name": "type",
                      "orig": "type",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 0,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 1,
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
                      "active": True,
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
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 2,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 1,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 2,
              },
            ],
            "input": "data",
            "key$": "load",
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "v1_lookup": {
        "fields": [
          {
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "id_label",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 4,
          },
          {
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 5,
          },
          {
            "name": "int_born_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 6,
          },
          {
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 7,
          },
          {
            "name": "int_charted",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 8,
          },
          {
            "name": "int_died_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 9,
          },
          {
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 10,
          },
          {
            "name": "int_formed_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 11,
          },
          {
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 12,
          },
          {
            "name": "int_member",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 13,
          },
          {
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 14,
          },
          {
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 15,
          },
          {
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 16,
          },
          {
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 17,
          },
          {
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 18,
          },
          {
            "name": "int_sale",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 19,
          },
          {
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 20,
          },
          {
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 21,
          },
          {
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 22,
          },
          {
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 23,
          },
          {
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 24,
          },
          {
            "name": "int_year_released",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 25,
          },
          {
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 26,
          },
          {
            "name": "str_album3_d_case",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 27,
          },
          {
            "name": "str_album3_d_face",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 28,
          },
          {
            "name": "str_album3_d_flat",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 29,
          },
          {
            "name": "str_album3_d_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 30,
          },
          {
            "name": "str_album_c_dart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 31,
          },
          {
            "name": "str_album_spine",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 32,
          },
          {
            "name": "str_album_stripped",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 33,
          },
          {
            "name": "str_album_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 34,
          },
          {
            "name": "str_album_thumb_back",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 35,
          },
          {
            "name": "str_album_thumb_hq",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 36,
          },
          {
            "name": "str_all_music_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 37,
          },
          {
            "name": "str_amazon_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 38,
          },
          {
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 39,
          },
          {
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 40,
          },
          {
            "name": "str_artist_banner",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 41,
          },
          {
            "name": "str_artist_clearart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 42,
          },
          {
            "name": "str_artist_cutout",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 43,
          },
          {
            "name": "str_artist_fanart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 44,
          },
          {
            "name": "str_artist_fanart2",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 45,
          },
          {
            "name": "str_artist_fanart3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 46,
          },
          {
            "name": "str_artist_fanart4",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 47,
          },
          {
            "name": "str_artist_logo",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 48,
          },
          {
            "name": "str_artist_stripped",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 49,
          },
          {
            "name": "str_artist_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 50,
          },
          {
            "name": "str_artist_wide_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 51,
          },
          {
            "name": "str_bbc_review_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 52,
          },
          {
            "name": "str_biography_en",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 53,
          },
          {
            "name": "str_country",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 54,
          },
          {
            "name": "str_country_code",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 55,
          },
          {
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 56,
          },
          {
            "name": "str_disbanded",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 57,
          },
          {
            "name": "str_discogs_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 58,
          },
          {
            "name": "str_facebook",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 59,
          },
          {
            "name": "str_gender",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 60,
          },
          {
            "name": "str_genius_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 61,
          },
          {
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 62,
          },
          {
            "name": "str_isn_icode",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 63,
          },
          {
            "name": "str_itunes_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 64,
          },
          {
            "name": "str_label",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 65,
          },
          {
            "name": "str_last_fm_chart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 66,
          },
          {
            "name": "str_location",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 67,
          },
          {
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 68,
          },
          {
            "name": "str_lyric_wiki_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 69,
          },
          {
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 70,
          },
          {
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 71,
          },
          {
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 72,
          },
          {
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 73,
          },
          {
            "name": "str_music_moz_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 74,
          },
          {
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 75,
          },
          {
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 76,
          },
          {
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 77,
          },
          {
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 78,
          },
          {
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 79,
          },
          {
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 80,
          },
          {
            "name": "str_rate_your_music_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 81,
          },
          {
            "name": "str_release_format",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 82,
          },
          {
            "name": "str_review",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 83,
          },
          {
            "name": "str_speed",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 84,
          },
          {
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 85,
          },
          {
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 86,
          },
          {
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 87,
          },
          {
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 88,
          },
          {
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 89,
          },
          {
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 90,
          },
          {
            "name": "str_twitter",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 91,
          },
          {
            "name": "str_website",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 92,
          },
          {
            "name": "str_wikidata_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 93,
          },
          {
            "name": "str_wikipedia_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 94,
          },
        ],
        "name": "v1_lookup",
        "op": {
          "list": {
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "h",
                      "orig": "h",
                      "reqd": False,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                    {
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "reqd": False,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 0,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": False,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                    {
                      "example": 2115888,
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "reqd": False,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 1,
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
                      "active": True,
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
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 2,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
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
                      "active": True,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 1,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 2,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 3,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "id_label",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 4,
          },
          {
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 5,
          },
          {
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 6,
          },
          {
            "name": "int_born_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 7,
          },
          {
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 8,
          },
          {
            "name": "int_charted",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 9,
          },
          {
            "name": "int_died_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 10,
          },
          {
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 11,
          },
          {
            "name": "int_formed_year",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 12,
          },
          {
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 13,
          },
          {
            "name": "int_member",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 14,
          },
          {
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 15,
          },
          {
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 16,
          },
          {
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 17,
          },
          {
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 18,
          },
          {
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 19,
          },
          {
            "name": "int_sale",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 20,
          },
          {
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 21,
          },
          {
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 22,
          },
          {
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 23,
          },
          {
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 24,
          },
          {
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 25,
          },
          {
            "name": "int_year_released",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 26,
          },
          {
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 27,
          },
          {
            "name": "str_album3_d_case",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 28,
          },
          {
            "name": "str_album3_d_face",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 29,
          },
          {
            "name": "str_album3_d_flat",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 30,
          },
          {
            "name": "str_album3_d_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 31,
          },
          {
            "name": "str_album_c_dart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 32,
          },
          {
            "name": "str_album_spine",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 33,
          },
          {
            "name": "str_album_stripped",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 34,
          },
          {
            "name": "str_album_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 35,
          },
          {
            "name": "str_album_thumb_back",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 36,
          },
          {
            "name": "str_album_thumb_hq",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 37,
          },
          {
            "name": "str_all_music_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 38,
          },
          {
            "name": "str_amazon_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 39,
          },
          {
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 40,
          },
          {
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 41,
          },
          {
            "name": "str_artist_banner",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 42,
          },
          {
            "name": "str_artist_clearart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 43,
          },
          {
            "name": "str_artist_cutout",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 44,
          },
          {
            "name": "str_artist_fanart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 45,
          },
          {
            "name": "str_artist_fanart2",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 46,
          },
          {
            "name": "str_artist_fanart3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 47,
          },
          {
            "name": "str_artist_fanart4",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 48,
          },
          {
            "name": "str_artist_logo",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 49,
          },
          {
            "name": "str_artist_stripped",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 50,
          },
          {
            "name": "str_artist_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 51,
          },
          {
            "name": "str_artist_wide_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 52,
          },
          {
            "name": "str_bbc_review_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 53,
          },
          {
            "name": "str_biography_en",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 54,
          },
          {
            "name": "str_country",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 55,
          },
          {
            "name": "str_country_code",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 56,
          },
          {
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 57,
          },
          {
            "name": "str_disbanded",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 58,
          },
          {
            "name": "str_discogs_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 59,
          },
          {
            "name": "str_facebook",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 60,
          },
          {
            "name": "str_gender",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 61,
          },
          {
            "name": "str_genius_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 62,
          },
          {
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 63,
          },
          {
            "name": "str_isn_icode",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 64,
          },
          {
            "name": "str_itunes_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 65,
          },
          {
            "name": "str_label",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 66,
          },
          {
            "name": "str_last_fm_chart",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 67,
          },
          {
            "name": "str_location",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 68,
          },
          {
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 69,
          },
          {
            "name": "str_lyric_wiki_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 70,
          },
          {
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 71,
          },
          {
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 72,
          },
          {
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 73,
          },
          {
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 74,
          },
          {
            "name": "str_music_moz_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 75,
          },
          {
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 76,
          },
          {
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 77,
          },
          {
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 78,
          },
          {
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 79,
          },
          {
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 80,
          },
          {
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 81,
          },
          {
            "name": "str_rate_your_music_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 82,
          },
          {
            "name": "str_release_format",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 83,
          },
          {
            "name": "str_review",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 84,
          },
          {
            "name": "str_speed",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 85,
          },
          {
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 86,
          },
          {
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 87,
          },
          {
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 88,
          },
          {
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 89,
          },
          {
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 90,
          },
          {
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 91,
          },
          {
            "name": "str_twitter",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 92,
          },
          {
            "name": "str_website",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 93,
          },
          {
            "name": "str_wikidata_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 94,
          },
          {
            "name": "str_wikipedia_id",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 95,
          },
        ],
        "name": "v1_search",
        "op": {
          "list": {
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "example": "Homework",
                      "kind": "query",
                      "name": "a",
                      "orig": "a",
                      "reqd": False,
                      "type": "`$STRING`",
                      "active": True,
                    },
                    {
                      "example": "daft_punk",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 0,
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
                      "active": True,
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
                      "active": True,
                    },
                    {
                      "example": "yellow",
                      "kind": "query",
                      "name": "t",
                      "orig": "t",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 1,
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 2,
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
                      "active": True,
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
                      "active": True,
                    },
                  ],
                },
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
                  "res": "`body`",
                },
                "active": True,
                "index$": 3,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                  "query": [
                    {
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 0,
          },
        ],
        "name": "v2_list",
        "op": {
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "artist",
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "track",
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 2,
          },
        ],
        "name": "v2_lookup",
        "op": {
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 1,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 2,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 3,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 4,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 5,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "artist",
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "track",
            "req": False,
            "type": "`$ARRAY`",
            "active": True,
            "index$": 2,
          },
        ],
        "name": "v2_search",
        "op": {
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 1,
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 2,
              },
            ],
            "input": "data",
            "key$": "load",
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
