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
            "active": True,
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 0,
          },
          {
            "active": True,
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 1,
          },
          {
            "active": True,
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "index$": 2,
          },
          {
            "active": True,
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 3,
          },
          {
            "active": True,
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 4,
          },
          {
            "active": True,
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "index$": 5,
          },
          {
            "active": True,
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "index$": 6,
          },
          {
            "active": True,
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "index$": 7,
          },
          {
            "active": True,
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "index$": 8,
          },
          {
            "active": True,
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "index$": 9,
          },
          {
            "active": True,
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "index$": 10,
          },
          {
            "active": True,
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "index$": 11,
          },
          {
            "active": True,
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "index$": 12,
          },
          {
            "active": True,
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "index$": 13,
          },
          {
            "active": True,
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "index$": 14,
          },
          {
            "active": True,
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "index$": 15,
          },
          {
            "active": True,
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "index$": 16,
          },
          {
            "active": True,
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "index$": 17,
          },
          {
            "active": True,
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 18,
          },
          {
            "active": True,
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 19,
          },
          {
            "active": True,
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "index$": 20,
          },
          {
            "active": True,
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "index$": 21,
          },
          {
            "active": True,
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "index$": 22,
          },
          {
            "active": True,
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "index$": 23,
          },
          {
            "active": True,
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "index$": 24,
          },
          {
            "active": True,
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 25,
          },
          {
            "active": True,
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 26,
          },
          {
            "active": True,
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 27,
          },
          {
            "active": True,
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "index$": 28,
          },
          {
            "active": True,
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "index$": 29,
          },
          {
            "active": True,
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "index$": 30,
          },
          {
            "active": True,
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "index$": 31,
          },
          {
            "active": True,
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "index$": 32,
          },
          {
            "active": True,
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "index$": 33,
          },
          {
            "active": True,
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "index$": 34,
          },
          {
            "active": True,
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "index$": 35,
          },
          {
            "active": True,
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 36,
          },
          {
            "active": True,
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "index$": 37,
          },
          {
            "active": True,
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 38,
          },
          {
            "active": True,
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 39,
          },
          {
            "active": True,
            "name": "trending",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 40,
          },
        ],
        "name": "v1_list",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": "us",
                      "kind": "query",
                      "name": "country",
                      "orig": "country",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "active": True,
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "active": True,
                      "kind": "query",
                      "name": "type",
                      "orig": "type",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 2,
              },
            ],
            "key$": "list",
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "format",
                      "orig": "format",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 2,
              },
            ],
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
            "active": True,
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 0,
          },
          {
            "active": True,
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 1,
          },
          {
            "active": True,
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "index$": 2,
          },
          {
            "active": True,
            "name": "id_label",
            "req": False,
            "type": "`$STRING`",
            "index$": 3,
          },
          {
            "active": True,
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 4,
          },
          {
            "active": True,
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 5,
          },
          {
            "active": True,
            "name": "int_born_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 6,
          },
          {
            "active": True,
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "index$": 7,
          },
          {
            "active": True,
            "name": "int_charted",
            "req": False,
            "type": "`$STRING`",
            "index$": 8,
          },
          {
            "active": True,
            "name": "int_died_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 9,
          },
          {
            "active": True,
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "index$": 10,
          },
          {
            "active": True,
            "name": "int_formed_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 11,
          },
          {
            "active": True,
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "index$": 12,
          },
          {
            "active": True,
            "name": "int_member",
            "req": False,
            "type": "`$STRING`",
            "index$": 13,
          },
          {
            "active": True,
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "index$": 14,
          },
          {
            "active": True,
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "index$": 15,
          },
          {
            "active": True,
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "index$": 16,
          },
          {
            "active": True,
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "index$": 17,
          },
          {
            "active": True,
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "index$": 18,
          },
          {
            "active": True,
            "name": "int_sale",
            "req": False,
            "type": "`$STRING`",
            "index$": 19,
          },
          {
            "active": True,
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "index$": 20,
          },
          {
            "active": True,
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "index$": 21,
          },
          {
            "active": True,
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "index$": 22,
          },
          {
            "active": True,
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "index$": 23,
          },
          {
            "active": True,
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "index$": 24,
          },
          {
            "active": True,
            "name": "int_year_released",
            "req": False,
            "type": "`$STRING`",
            "index$": 25,
          },
          {
            "active": True,
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 26,
          },
          {
            "active": True,
            "name": "str_album3_d_case",
            "req": False,
            "type": "`$STRING`",
            "index$": 27,
          },
          {
            "active": True,
            "name": "str_album3_d_face",
            "req": False,
            "type": "`$STRING`",
            "index$": 28,
          },
          {
            "active": True,
            "name": "str_album3_d_flat",
            "req": False,
            "type": "`$STRING`",
            "index$": 29,
          },
          {
            "active": True,
            "name": "str_album3_d_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 30,
          },
          {
            "active": True,
            "name": "str_album_c_dart",
            "req": False,
            "type": "`$STRING`",
            "index$": 31,
          },
          {
            "active": True,
            "name": "str_album_spine",
            "req": False,
            "type": "`$STRING`",
            "index$": 32,
          },
          {
            "active": True,
            "name": "str_album_stripped",
            "req": False,
            "type": "`$STRING`",
            "index$": 33,
          },
          {
            "active": True,
            "name": "str_album_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 34,
          },
          {
            "active": True,
            "name": "str_album_thumb_back",
            "req": False,
            "type": "`$STRING`",
            "index$": 35,
          },
          {
            "active": True,
            "name": "str_album_thumb_hq",
            "req": False,
            "type": "`$STRING`",
            "index$": 36,
          },
          {
            "active": True,
            "name": "str_all_music_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 37,
          },
          {
            "active": True,
            "name": "str_amazon_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 38,
          },
          {
            "active": True,
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 39,
          },
          {
            "active": True,
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "index$": 40,
          },
          {
            "active": True,
            "name": "str_artist_banner",
            "req": False,
            "type": "`$STRING`",
            "index$": 41,
          },
          {
            "active": True,
            "name": "str_artist_clearart",
            "req": False,
            "type": "`$STRING`",
            "index$": 42,
          },
          {
            "active": True,
            "name": "str_artist_cutout",
            "req": False,
            "type": "`$STRING`",
            "index$": 43,
          },
          {
            "active": True,
            "name": "str_artist_fanart",
            "req": False,
            "type": "`$STRING`",
            "index$": 44,
          },
          {
            "active": True,
            "name": "str_artist_fanart2",
            "req": False,
            "type": "`$STRING`",
            "index$": 45,
          },
          {
            "active": True,
            "name": "str_artist_fanart3",
            "req": False,
            "type": "`$STRING`",
            "index$": 46,
          },
          {
            "active": True,
            "name": "str_artist_fanart4",
            "req": False,
            "type": "`$STRING`",
            "index$": 47,
          },
          {
            "active": True,
            "name": "str_artist_logo",
            "req": False,
            "type": "`$STRING`",
            "index$": 48,
          },
          {
            "active": True,
            "name": "str_artist_stripped",
            "req": False,
            "type": "`$STRING`",
            "index$": 49,
          },
          {
            "active": True,
            "name": "str_artist_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 50,
          },
          {
            "active": True,
            "name": "str_artist_wide_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 51,
          },
          {
            "active": True,
            "name": "str_bbc_review_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 52,
          },
          {
            "active": True,
            "name": "str_biography_en",
            "req": False,
            "type": "`$STRING`",
            "index$": 53,
          },
          {
            "active": True,
            "name": "str_country",
            "req": False,
            "type": "`$STRING`",
            "index$": 54,
          },
          {
            "active": True,
            "name": "str_country_code",
            "req": False,
            "type": "`$STRING`",
            "index$": 55,
          },
          {
            "active": True,
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "index$": 56,
          },
          {
            "active": True,
            "name": "str_disbanded",
            "req": False,
            "type": "`$STRING`",
            "index$": 57,
          },
          {
            "active": True,
            "name": "str_discogs_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 58,
          },
          {
            "active": True,
            "name": "str_facebook",
            "req": False,
            "type": "`$STRING`",
            "index$": 59,
          },
          {
            "active": True,
            "name": "str_gender",
            "req": False,
            "type": "`$STRING`",
            "index$": 60,
          },
          {
            "active": True,
            "name": "str_genius_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 61,
          },
          {
            "active": True,
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "index$": 62,
          },
          {
            "active": True,
            "name": "str_isn_icode",
            "req": False,
            "type": "`$STRING`",
            "index$": 63,
          },
          {
            "active": True,
            "name": "str_itunes_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 64,
          },
          {
            "active": True,
            "name": "str_label",
            "req": False,
            "type": "`$STRING`",
            "index$": 65,
          },
          {
            "active": True,
            "name": "str_last_fm_chart",
            "req": False,
            "type": "`$STRING`",
            "index$": 66,
          },
          {
            "active": True,
            "name": "str_location",
            "req": False,
            "type": "`$STRING`",
            "index$": 67,
          },
          {
            "active": True,
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "index$": 68,
          },
          {
            "active": True,
            "name": "str_lyric_wiki_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 69,
          },
          {
            "active": True,
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "index$": 70,
          },
          {
            "active": True,
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 71,
          },
          {
            "active": True,
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 72,
          },
          {
            "active": True,
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 73,
          },
          {
            "active": True,
            "name": "str_music_moz_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 74,
          },
          {
            "active": True,
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "index$": 75,
          },
          {
            "active": True,
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "index$": 76,
          },
          {
            "active": True,
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "index$": 77,
          },
          {
            "active": True,
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "index$": 78,
          },
          {
            "active": True,
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "index$": 79,
          },
          {
            "active": True,
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "index$": 80,
          },
          {
            "active": True,
            "name": "str_rate_your_music_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 81,
          },
          {
            "active": True,
            "name": "str_release_format",
            "req": False,
            "type": "`$STRING`",
            "index$": 82,
          },
          {
            "active": True,
            "name": "str_review",
            "req": False,
            "type": "`$STRING`",
            "index$": 83,
          },
          {
            "active": True,
            "name": "str_speed",
            "req": False,
            "type": "`$STRING`",
            "index$": 84,
          },
          {
            "active": True,
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "index$": 85,
          },
          {
            "active": True,
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "index$": 86,
          },
          {
            "active": True,
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 87,
          },
          {
            "active": True,
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "index$": 88,
          },
          {
            "active": True,
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 89,
          },
          {
            "active": True,
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 90,
          },
          {
            "active": True,
            "name": "str_twitter",
            "req": False,
            "type": "`$STRING`",
            "index$": 91,
          },
          {
            "active": True,
            "name": "str_website",
            "req": False,
            "type": "`$STRING`",
            "index$": 92,
          },
          {
            "active": True,
            "name": "str_wikidata_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 93,
          },
          {
            "active": True,
            "name": "str_wikipedia_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 94,
          },
        ],
        "name": "v1_lookup",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "h",
                      "orig": "h",
                      "reqd": False,
                      "type": "`$INTEGER`",
                    },
                    {
                      "active": True,
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "reqd": False,
                      "type": "`$INTEGER`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": False,
                      "type": "`$INTEGER`",
                    },
                    {
                      "active": True,
                      "example": 2115888,
                      "kind": "query",
                      "name": "m",
                      "orig": "m",
                      "reqd": False,
                      "type": "`$INTEGER`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": 112024,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 2,
              },
            ],
            "key$": "list",
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 2,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "i",
                      "orig": "i",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 3,
              },
            ],
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
            "active": True,
            "name": "album",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 0,
          },
          {
            "active": True,
            "name": "id_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 1,
          },
          {
            "active": True,
            "name": "id_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 2,
          },
          {
            "active": True,
            "name": "id_imvdb",
            "req": False,
            "type": "`$STRING`",
            "index$": 3,
          },
          {
            "active": True,
            "name": "id_label",
            "req": False,
            "type": "`$STRING`",
            "index$": 4,
          },
          {
            "active": True,
            "name": "id_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 5,
          },
          {
            "active": True,
            "name": "id_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 6,
          },
          {
            "active": True,
            "name": "int_born_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 7,
          },
          {
            "active": True,
            "name": "int_cd",
            "req": False,
            "type": "`$STRING`",
            "index$": 8,
          },
          {
            "active": True,
            "name": "int_charted",
            "req": False,
            "type": "`$STRING`",
            "index$": 9,
          },
          {
            "active": True,
            "name": "int_died_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 10,
          },
          {
            "active": True,
            "name": "int_duration",
            "req": False,
            "type": "`$STRING`",
            "index$": 11,
          },
          {
            "active": True,
            "name": "int_formed_year",
            "req": False,
            "type": "`$STRING`",
            "index$": 12,
          },
          {
            "active": True,
            "name": "int_loved",
            "req": False,
            "type": "`$STRING`",
            "index$": 13,
          },
          {
            "active": True,
            "name": "int_member",
            "req": False,
            "type": "`$STRING`",
            "index$": 14,
          },
          {
            "active": True,
            "name": "int_music_vid_comment",
            "req": False,
            "type": "`$STRING`",
            "index$": 15,
          },
          {
            "active": True,
            "name": "int_music_vid_dislike",
            "req": False,
            "type": "`$STRING`",
            "index$": 16,
          },
          {
            "active": True,
            "name": "int_music_vid_favorite",
            "req": False,
            "type": "`$STRING`",
            "index$": 17,
          },
          {
            "active": True,
            "name": "int_music_vid_like",
            "req": False,
            "type": "`$STRING`",
            "index$": 18,
          },
          {
            "active": True,
            "name": "int_music_vid_view",
            "req": False,
            "type": "`$STRING`",
            "index$": 19,
          },
          {
            "active": True,
            "name": "int_sale",
            "req": False,
            "type": "`$STRING`",
            "index$": 20,
          },
          {
            "active": True,
            "name": "int_score",
            "req": False,
            "type": "`$STRING`",
            "index$": 21,
          },
          {
            "active": True,
            "name": "int_score_vote",
            "req": False,
            "type": "`$STRING`",
            "index$": 22,
          },
          {
            "active": True,
            "name": "int_total_listener",
            "req": False,
            "type": "`$STRING`",
            "index$": 23,
          },
          {
            "active": True,
            "name": "int_total_play",
            "req": False,
            "type": "`$STRING`",
            "index$": 24,
          },
          {
            "active": True,
            "name": "int_track_number",
            "req": False,
            "type": "`$STRING`",
            "index$": 25,
          },
          {
            "active": True,
            "name": "int_year_released",
            "req": False,
            "type": "`$STRING`",
            "index$": 26,
          },
          {
            "active": True,
            "name": "str_album",
            "req": False,
            "type": "`$STRING`",
            "index$": 27,
          },
          {
            "active": True,
            "name": "str_album3_d_case",
            "req": False,
            "type": "`$STRING`",
            "index$": 28,
          },
          {
            "active": True,
            "name": "str_album3_d_face",
            "req": False,
            "type": "`$STRING`",
            "index$": 29,
          },
          {
            "active": True,
            "name": "str_album3_d_flat",
            "req": False,
            "type": "`$STRING`",
            "index$": 30,
          },
          {
            "active": True,
            "name": "str_album3_d_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 31,
          },
          {
            "active": True,
            "name": "str_album_c_dart",
            "req": False,
            "type": "`$STRING`",
            "index$": 32,
          },
          {
            "active": True,
            "name": "str_album_spine",
            "req": False,
            "type": "`$STRING`",
            "index$": 33,
          },
          {
            "active": True,
            "name": "str_album_stripped",
            "req": False,
            "type": "`$STRING`",
            "index$": 34,
          },
          {
            "active": True,
            "name": "str_album_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 35,
          },
          {
            "active": True,
            "name": "str_album_thumb_back",
            "req": False,
            "type": "`$STRING`",
            "index$": 36,
          },
          {
            "active": True,
            "name": "str_album_thumb_hq",
            "req": False,
            "type": "`$STRING`",
            "index$": 37,
          },
          {
            "active": True,
            "name": "str_all_music_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 38,
          },
          {
            "active": True,
            "name": "str_amazon_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 39,
          },
          {
            "active": True,
            "name": "str_artist",
            "req": False,
            "type": "`$STRING`",
            "index$": 40,
          },
          {
            "active": True,
            "name": "str_artist_alternate",
            "req": False,
            "type": "`$STRING`",
            "index$": 41,
          },
          {
            "active": True,
            "name": "str_artist_banner",
            "req": False,
            "type": "`$STRING`",
            "index$": 42,
          },
          {
            "active": True,
            "name": "str_artist_clearart",
            "req": False,
            "type": "`$STRING`",
            "index$": 43,
          },
          {
            "active": True,
            "name": "str_artist_cutout",
            "req": False,
            "type": "`$STRING`",
            "index$": 44,
          },
          {
            "active": True,
            "name": "str_artist_fanart",
            "req": False,
            "type": "`$STRING`",
            "index$": 45,
          },
          {
            "active": True,
            "name": "str_artist_fanart2",
            "req": False,
            "type": "`$STRING`",
            "index$": 46,
          },
          {
            "active": True,
            "name": "str_artist_fanart3",
            "req": False,
            "type": "`$STRING`",
            "index$": 47,
          },
          {
            "active": True,
            "name": "str_artist_fanart4",
            "req": False,
            "type": "`$STRING`",
            "index$": 48,
          },
          {
            "active": True,
            "name": "str_artist_logo",
            "req": False,
            "type": "`$STRING`",
            "index$": 49,
          },
          {
            "active": True,
            "name": "str_artist_stripped",
            "req": False,
            "type": "`$STRING`",
            "index$": 50,
          },
          {
            "active": True,
            "name": "str_artist_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 51,
          },
          {
            "active": True,
            "name": "str_artist_wide_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 52,
          },
          {
            "active": True,
            "name": "str_bbc_review_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 53,
          },
          {
            "active": True,
            "name": "str_biography_en",
            "req": False,
            "type": "`$STRING`",
            "index$": 54,
          },
          {
            "active": True,
            "name": "str_country",
            "req": False,
            "type": "`$STRING`",
            "index$": 55,
          },
          {
            "active": True,
            "name": "str_country_code",
            "req": False,
            "type": "`$STRING`",
            "index$": 56,
          },
          {
            "active": True,
            "name": "str_description_en",
            "req": False,
            "type": "`$STRING`",
            "index$": 57,
          },
          {
            "active": True,
            "name": "str_disbanded",
            "req": False,
            "type": "`$STRING`",
            "index$": 58,
          },
          {
            "active": True,
            "name": "str_discogs_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 59,
          },
          {
            "active": True,
            "name": "str_facebook",
            "req": False,
            "type": "`$STRING`",
            "index$": 60,
          },
          {
            "active": True,
            "name": "str_gender",
            "req": False,
            "type": "`$STRING`",
            "index$": 61,
          },
          {
            "active": True,
            "name": "str_genius_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 62,
          },
          {
            "active": True,
            "name": "str_genre",
            "req": False,
            "type": "`$STRING`",
            "index$": 63,
          },
          {
            "active": True,
            "name": "str_isn_icode",
            "req": False,
            "type": "`$STRING`",
            "index$": 64,
          },
          {
            "active": True,
            "name": "str_itunes_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 65,
          },
          {
            "active": True,
            "name": "str_label",
            "req": False,
            "type": "`$STRING`",
            "index$": 66,
          },
          {
            "active": True,
            "name": "str_last_fm_chart",
            "req": False,
            "type": "`$STRING`",
            "index$": 67,
          },
          {
            "active": True,
            "name": "str_location",
            "req": False,
            "type": "`$STRING`",
            "index$": 68,
          },
          {
            "active": True,
            "name": "str_locked",
            "req": False,
            "type": "`$STRING`",
            "index$": 69,
          },
          {
            "active": True,
            "name": "str_lyric_wiki_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 70,
          },
          {
            "active": True,
            "name": "str_mood",
            "req": False,
            "type": "`$STRING`",
            "index$": 71,
          },
          {
            "active": True,
            "name": "str_music_brainz_album_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 72,
          },
          {
            "active": True,
            "name": "str_music_brainz_artist_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 73,
          },
          {
            "active": True,
            "name": "str_music_brainz_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 74,
          },
          {
            "active": True,
            "name": "str_music_moz_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 75,
          },
          {
            "active": True,
            "name": "str_music_vid",
            "req": False,
            "type": "`$STRING`",
            "index$": 76,
          },
          {
            "active": True,
            "name": "str_music_vid_company",
            "req": False,
            "type": "`$STRING`",
            "index$": 77,
          },
          {
            "active": True,
            "name": "str_music_vid_director",
            "req": False,
            "type": "`$STRING`",
            "index$": 78,
          },
          {
            "active": True,
            "name": "str_music_vid_screen1",
            "req": False,
            "type": "`$STRING`",
            "index$": 79,
          },
          {
            "active": True,
            "name": "str_music_vid_screen2",
            "req": False,
            "type": "`$STRING`",
            "index$": 80,
          },
          {
            "active": True,
            "name": "str_music_vid_screen3",
            "req": False,
            "type": "`$STRING`",
            "index$": 81,
          },
          {
            "active": True,
            "name": "str_rate_your_music_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 82,
          },
          {
            "active": True,
            "name": "str_release_format",
            "req": False,
            "type": "`$STRING`",
            "index$": 83,
          },
          {
            "active": True,
            "name": "str_review",
            "req": False,
            "type": "`$STRING`",
            "index$": 84,
          },
          {
            "active": True,
            "name": "str_speed",
            "req": False,
            "type": "`$STRING`",
            "index$": 85,
          },
          {
            "active": True,
            "name": "str_style",
            "req": False,
            "type": "`$STRING`",
            "index$": 86,
          },
          {
            "active": True,
            "name": "str_theme",
            "req": False,
            "type": "`$STRING`",
            "index$": 87,
          },
          {
            "active": True,
            "name": "str_track",
            "req": False,
            "type": "`$STRING`",
            "index$": 88,
          },
          {
            "active": True,
            "name": "str_track3x3",
            "req": False,
            "type": "`$STRING`",
            "index$": 89,
          },
          {
            "active": True,
            "name": "str_track_lyric",
            "req": False,
            "type": "`$STRING`",
            "index$": 90,
          },
          {
            "active": True,
            "name": "str_track_thumb",
            "req": False,
            "type": "`$STRING`",
            "index$": 91,
          },
          {
            "active": True,
            "name": "str_twitter",
            "req": False,
            "type": "`$STRING`",
            "index$": 92,
          },
          {
            "active": True,
            "name": "str_website",
            "req": False,
            "type": "`$STRING`",
            "index$": 93,
          },
          {
            "active": True,
            "name": "str_wikidata_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 94,
          },
          {
            "active": True,
            "name": "str_wikipedia_id",
            "req": False,
            "type": "`$STRING`",
            "index$": 95,
          },
        ],
        "name": "v1_search",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": "Homework",
                      "kind": "query",
                      "name": "a",
                      "orig": "a",
                      "reqd": False,
                      "type": "`$STRING`",
                    },
                    {
                      "active": True,
                      "example": "daft_punk",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                    {
                      "active": True,
                      "example": "yellow",
                      "kind": "query",
                      "name": "t",
                      "orig": "t",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 2,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
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
                      "active": True,
                      "example": "coldplay",
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 3,
              },
            ],
            "key$": "list",
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "kind": "param",
                      "name": "api_key",
                      "orig": "api_key",
                      "reqd": True,
                      "type": "`$STRING`",
                    },
                  ],
                  "query": [
                    {
                      "active": True,
                      "kind": "query",
                      "name": "s",
                      "orig": "s",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
            ],
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
            "active": True,
            "name": "album",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 0,
          },
        ],
        "name": "v2_list",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": 111239,
                      "kind": "param",
                      "name": "id_artist",
                      "orig": "id_artist",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 0,
              },
            ],
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
            "active": True,
            "name": "album",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 0,
          },
          {
            "active": True,
            "name": "artist",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 1,
          },
          {
            "active": True,
            "name": "track",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 2,
          },
        ],
        "name": "v2_lookup",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": 2109615,
                      "kind": "param",
                      "name": "id_album",
                      "orig": "id_album",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": 111239,
                      "kind": "param",
                      "name": "id_artist",
                      "orig": "id_artist",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": 32724183,
                      "kind": "param",
                      "name": "id_track",
                      "orig": "id_track",
                      "reqd": True,
                      "type": "`$INTEGER`",
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
                "index$": 2,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "1dc4c347-a1db-32aa-b14f-bc9cc507b843",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 3,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 4,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "50369905-68ca-48d2-912d-b37330ff7dc3",
                      "kind": "param",
                      "name": "music_brainz_id",
                      "orig": "music_brainz_id",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 5,
              },
            ],
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
            "active": True,
            "name": "album",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 0,
          },
          {
            "active": True,
            "name": "artist",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 1,
          },
          {
            "active": True,
            "name": "track",
            "req": False,
            "type": "`$ARRAY`",
            "index$": 2,
          },
        ],
        "name": "v2_search",
        "op": {
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "parachutes",
                      "kind": "param",
                      "name": "album_name",
                      "orig": "album_name",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 0,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "coldplay",
                      "kind": "param",
                      "name": "artist_name",
                      "orig": "artist_name",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 1,
              },
              {
                "active": True,
                "args": {
                  "params": [
                    {
                      "active": True,
                      "example": "yellow",
                      "kind": "param",
                      "name": "track_name",
                      "orig": "track_name",
                      "reqd": True,
                      "type": "`$STRING`",
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
                "index$": 2,
              },
            ],
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
