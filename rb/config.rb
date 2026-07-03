# FreeMusic SDK configuration

module FreeMusicConfig
  def self.make_config
    {
      "main" => {
        "name" => "FreeMusic",
      },
      "feature" => {
        "test" => {
          "options" => {
            "active" => false,
          },
        },
      },
      "options" => {
        "base" => "https://www.theaudiodb.com/api/v1/json",
        "auth" => {
          "prefix" => "Bearer",
        },
        "headers" => {
          "content-type" => "application/json",
        },
        "entity" => {
          "v1_list" => {},
          "v1_lookup" => {},
          "v1_search" => {},
          "v2_list" => {},
          "v2_lookup" => {},
          "v2_search" => {},
        },
      },
      "entity" => {
        "v1_list" => {
          "fields" => [
            {
              "active" => true,
              "name" => "id_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 0,
            },
            {
              "active" => true,
              "name" => "id_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 1,
            },
            {
              "active" => true,
              "name" => "id_imvdb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 2,
            },
            {
              "active" => true,
              "name" => "id_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 3,
            },
            {
              "active" => true,
              "name" => "id_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 4,
            },
            {
              "active" => true,
              "name" => "int_cd",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 5,
            },
            {
              "active" => true,
              "name" => "int_duration",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 6,
            },
            {
              "active" => true,
              "name" => "int_loved",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 7,
            },
            {
              "active" => true,
              "name" => "int_music_vid_comment",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 8,
            },
            {
              "active" => true,
              "name" => "int_music_vid_dislike",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 9,
            },
            {
              "active" => true,
              "name" => "int_music_vid_favorite",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 10,
            },
            {
              "active" => true,
              "name" => "int_music_vid_like",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 11,
            },
            {
              "active" => true,
              "name" => "int_music_vid_view",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 12,
            },
            {
              "active" => true,
              "name" => "int_score",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 13,
            },
            {
              "active" => true,
              "name" => "int_score_vote",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 14,
            },
            {
              "active" => true,
              "name" => "int_total_listener",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 15,
            },
            {
              "active" => true,
              "name" => "int_total_play",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 16,
            },
            {
              "active" => true,
              "name" => "int_track_number",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 17,
            },
            {
              "active" => true,
              "name" => "str_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 18,
            },
            {
              "active" => true,
              "name" => "str_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 19,
            },
            {
              "active" => true,
              "name" => "str_artist_alternate",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 20,
            },
            {
              "active" => true,
              "name" => "str_description_en",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 21,
            },
            {
              "active" => true,
              "name" => "str_genre",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 22,
            },
            {
              "active" => true,
              "name" => "str_locked",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 23,
            },
            {
              "active" => true,
              "name" => "str_mood",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 24,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_album_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 25,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_artist_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 26,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 27,
            },
            {
              "active" => true,
              "name" => "str_music_vid",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 28,
            },
            {
              "active" => true,
              "name" => "str_music_vid_company",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 29,
            },
            {
              "active" => true,
              "name" => "str_music_vid_director",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 30,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen1",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 31,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen2",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 32,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 33,
            },
            {
              "active" => true,
              "name" => "str_style",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 34,
            },
            {
              "active" => true,
              "name" => "str_theme",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 35,
            },
            {
              "active" => true,
              "name" => "str_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 36,
            },
            {
              "active" => true,
              "name" => "str_track3x3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 37,
            },
            {
              "active" => true,
              "name" => "str_track_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 38,
            },
            {
              "active" => true,
              "name" => "str_track_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 39,
            },
            {
              "active" => true,
              "name" => "trending",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 40,
            },
          ],
          "name" => "v1_list",
          "op" => {
            "list" => {
              "input" => "data",
              "name" => "list",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "us",
                        "kind" => "query",
                        "name" => "country",
                        "orig" => "country",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "format",
                        "orig" => "format",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "type",
                        "orig" => "type",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/trending.php",
                  "parts" => [
                    "{api_key}",
                    "trending.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "country",
                      "format",
                      "type",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/mvid.php",
                  "parts" => [
                    "{api_key}",
                    "mvid.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "coldplay",
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/track-top10.php",
                  "parts" => [
                    "{api_key}",
                    "track-top10.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
              ],
              "key$" => "list",
            },
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "format",
                        "orig" => "format",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/mostloved.php",
                  "parts" => [
                    "{api_key}",
                    "mostloved.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "format",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/mvid-mb.php",
                  "parts" => [
                    "{api_key}",
                    "mvid-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/track-top10-mb.php",
                  "parts" => [
                    "{api_key}",
                    "track-top10-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [],
          },
        },
        "v1_lookup" => {
          "fields" => [
            {
              "active" => true,
              "name" => "id_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 0,
            },
            {
              "active" => true,
              "name" => "id_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 1,
            },
            {
              "active" => true,
              "name" => "id_imvdb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 2,
            },
            {
              "active" => true,
              "name" => "id_label",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 3,
            },
            {
              "active" => true,
              "name" => "id_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 4,
            },
            {
              "active" => true,
              "name" => "id_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 5,
            },
            {
              "active" => true,
              "name" => "int_born_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 6,
            },
            {
              "active" => true,
              "name" => "int_cd",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 7,
            },
            {
              "active" => true,
              "name" => "int_charted",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 8,
            },
            {
              "active" => true,
              "name" => "int_died_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 9,
            },
            {
              "active" => true,
              "name" => "int_duration",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 10,
            },
            {
              "active" => true,
              "name" => "int_formed_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 11,
            },
            {
              "active" => true,
              "name" => "int_loved",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 12,
            },
            {
              "active" => true,
              "name" => "int_member",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 13,
            },
            {
              "active" => true,
              "name" => "int_music_vid_comment",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 14,
            },
            {
              "active" => true,
              "name" => "int_music_vid_dislike",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 15,
            },
            {
              "active" => true,
              "name" => "int_music_vid_favorite",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 16,
            },
            {
              "active" => true,
              "name" => "int_music_vid_like",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 17,
            },
            {
              "active" => true,
              "name" => "int_music_vid_view",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 18,
            },
            {
              "active" => true,
              "name" => "int_sale",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 19,
            },
            {
              "active" => true,
              "name" => "int_score",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 20,
            },
            {
              "active" => true,
              "name" => "int_score_vote",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 21,
            },
            {
              "active" => true,
              "name" => "int_total_listener",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 22,
            },
            {
              "active" => true,
              "name" => "int_total_play",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 23,
            },
            {
              "active" => true,
              "name" => "int_track_number",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 24,
            },
            {
              "active" => true,
              "name" => "int_year_released",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 25,
            },
            {
              "active" => true,
              "name" => "str_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 26,
            },
            {
              "active" => true,
              "name" => "str_album3_d_case",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 27,
            },
            {
              "active" => true,
              "name" => "str_album3_d_face",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 28,
            },
            {
              "active" => true,
              "name" => "str_album3_d_flat",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 29,
            },
            {
              "active" => true,
              "name" => "str_album3_d_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 30,
            },
            {
              "active" => true,
              "name" => "str_album_c_dart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 31,
            },
            {
              "active" => true,
              "name" => "str_album_spine",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 32,
            },
            {
              "active" => true,
              "name" => "str_album_stripped",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 33,
            },
            {
              "active" => true,
              "name" => "str_album_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 34,
            },
            {
              "active" => true,
              "name" => "str_album_thumb_back",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 35,
            },
            {
              "active" => true,
              "name" => "str_album_thumb_hq",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 36,
            },
            {
              "active" => true,
              "name" => "str_all_music_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 37,
            },
            {
              "active" => true,
              "name" => "str_amazon_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 38,
            },
            {
              "active" => true,
              "name" => "str_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 39,
            },
            {
              "active" => true,
              "name" => "str_artist_alternate",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 40,
            },
            {
              "active" => true,
              "name" => "str_artist_banner",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 41,
            },
            {
              "active" => true,
              "name" => "str_artist_clearart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 42,
            },
            {
              "active" => true,
              "name" => "str_artist_cutout",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 43,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 44,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart2",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 45,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 46,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart4",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 47,
            },
            {
              "active" => true,
              "name" => "str_artist_logo",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 48,
            },
            {
              "active" => true,
              "name" => "str_artist_stripped",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 49,
            },
            {
              "active" => true,
              "name" => "str_artist_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 50,
            },
            {
              "active" => true,
              "name" => "str_artist_wide_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 51,
            },
            {
              "active" => true,
              "name" => "str_bbc_review_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 52,
            },
            {
              "active" => true,
              "name" => "str_biography_en",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 53,
            },
            {
              "active" => true,
              "name" => "str_country",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 54,
            },
            {
              "active" => true,
              "name" => "str_country_code",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 55,
            },
            {
              "active" => true,
              "name" => "str_description_en",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 56,
            },
            {
              "active" => true,
              "name" => "str_disbanded",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 57,
            },
            {
              "active" => true,
              "name" => "str_discogs_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 58,
            },
            {
              "active" => true,
              "name" => "str_facebook",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 59,
            },
            {
              "active" => true,
              "name" => "str_gender",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 60,
            },
            {
              "active" => true,
              "name" => "str_genius_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 61,
            },
            {
              "active" => true,
              "name" => "str_genre",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 62,
            },
            {
              "active" => true,
              "name" => "str_isn_icode",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 63,
            },
            {
              "active" => true,
              "name" => "str_itunes_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 64,
            },
            {
              "active" => true,
              "name" => "str_label",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 65,
            },
            {
              "active" => true,
              "name" => "str_last_fm_chart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 66,
            },
            {
              "active" => true,
              "name" => "str_location",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 67,
            },
            {
              "active" => true,
              "name" => "str_locked",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 68,
            },
            {
              "active" => true,
              "name" => "str_lyric_wiki_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 69,
            },
            {
              "active" => true,
              "name" => "str_mood",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 70,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_album_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 71,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_artist_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 72,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 73,
            },
            {
              "active" => true,
              "name" => "str_music_moz_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 74,
            },
            {
              "active" => true,
              "name" => "str_music_vid",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 75,
            },
            {
              "active" => true,
              "name" => "str_music_vid_company",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 76,
            },
            {
              "active" => true,
              "name" => "str_music_vid_director",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 77,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen1",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 78,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen2",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 79,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 80,
            },
            {
              "active" => true,
              "name" => "str_rate_your_music_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 81,
            },
            {
              "active" => true,
              "name" => "str_release_format",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 82,
            },
            {
              "active" => true,
              "name" => "str_review",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 83,
            },
            {
              "active" => true,
              "name" => "str_speed",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 84,
            },
            {
              "active" => true,
              "name" => "str_style",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 85,
            },
            {
              "active" => true,
              "name" => "str_theme",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 86,
            },
            {
              "active" => true,
              "name" => "str_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 87,
            },
            {
              "active" => true,
              "name" => "str_track3x3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 88,
            },
            {
              "active" => true,
              "name" => "str_track_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 89,
            },
            {
              "active" => true,
              "name" => "str_track_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 90,
            },
            {
              "active" => true,
              "name" => "str_twitter",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 91,
            },
            {
              "active" => true,
              "name" => "str_website",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 92,
            },
            {
              "active" => true,
              "name" => "str_wikidata_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 93,
            },
            {
              "active" => true,
              "name" => "str_wikipedia_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 94,
            },
          ],
          "name" => "v1_lookup",
          "op" => {
            "list" => {
              "input" => "data",
              "name" => "list",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "h",
                        "orig" => "h",
                        "reqd" => false,
                        "type" => "`$INTEGER`",
                      },
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "m",
                        "orig" => "m",
                        "reqd" => false,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/track.php",
                  "parts" => [
                    "{api_key}",
                    "track.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "h",
                      "m",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => false,
                        "type" => "`$INTEGER`",
                      },
                      {
                        "active" => true,
                        "example" => 2115888,
                        "kind" => "query",
                        "name" => "m",
                        "orig" => "m",
                        "reqd" => false,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/album.php",
                  "parts" => [
                    "{api_key}",
                    "album.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                      "m",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => 112024,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/artist.php",
                  "parts" => [
                    "{api_key}",
                    "artist.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
              ],
              "key$" => "list",
            },
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/album-mb.php",
                  "parts" => [
                    "{api_key}",
                    "album-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/artist-mb.php",
                  "parts" => [
                    "{api_key}",
                    "artist-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/artist-social.php",
                  "parts" => [
                    "{api_key}",
                    "artist-social.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "i",
                        "orig" => "i",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/track-mb.php",
                  "parts" => [
                    "{api_key}",
                    "track-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "i",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 3,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [],
          },
        },
        "v1_search" => {
          "fields" => [
            {
              "active" => true,
              "name" => "album",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 0,
            },
            {
              "active" => true,
              "name" => "id_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 1,
            },
            {
              "active" => true,
              "name" => "id_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 2,
            },
            {
              "active" => true,
              "name" => "id_imvdb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 3,
            },
            {
              "active" => true,
              "name" => "id_label",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 4,
            },
            {
              "active" => true,
              "name" => "id_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 5,
            },
            {
              "active" => true,
              "name" => "id_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 6,
            },
            {
              "active" => true,
              "name" => "int_born_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 7,
            },
            {
              "active" => true,
              "name" => "int_cd",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 8,
            },
            {
              "active" => true,
              "name" => "int_charted",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 9,
            },
            {
              "active" => true,
              "name" => "int_died_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 10,
            },
            {
              "active" => true,
              "name" => "int_duration",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 11,
            },
            {
              "active" => true,
              "name" => "int_formed_year",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 12,
            },
            {
              "active" => true,
              "name" => "int_loved",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 13,
            },
            {
              "active" => true,
              "name" => "int_member",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 14,
            },
            {
              "active" => true,
              "name" => "int_music_vid_comment",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 15,
            },
            {
              "active" => true,
              "name" => "int_music_vid_dislike",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 16,
            },
            {
              "active" => true,
              "name" => "int_music_vid_favorite",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 17,
            },
            {
              "active" => true,
              "name" => "int_music_vid_like",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 18,
            },
            {
              "active" => true,
              "name" => "int_music_vid_view",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 19,
            },
            {
              "active" => true,
              "name" => "int_sale",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 20,
            },
            {
              "active" => true,
              "name" => "int_score",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 21,
            },
            {
              "active" => true,
              "name" => "int_score_vote",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 22,
            },
            {
              "active" => true,
              "name" => "int_total_listener",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 23,
            },
            {
              "active" => true,
              "name" => "int_total_play",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 24,
            },
            {
              "active" => true,
              "name" => "int_track_number",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 25,
            },
            {
              "active" => true,
              "name" => "int_year_released",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 26,
            },
            {
              "active" => true,
              "name" => "str_album",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 27,
            },
            {
              "active" => true,
              "name" => "str_album3_d_case",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 28,
            },
            {
              "active" => true,
              "name" => "str_album3_d_face",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 29,
            },
            {
              "active" => true,
              "name" => "str_album3_d_flat",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 30,
            },
            {
              "active" => true,
              "name" => "str_album3_d_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 31,
            },
            {
              "active" => true,
              "name" => "str_album_c_dart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 32,
            },
            {
              "active" => true,
              "name" => "str_album_spine",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 33,
            },
            {
              "active" => true,
              "name" => "str_album_stripped",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 34,
            },
            {
              "active" => true,
              "name" => "str_album_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 35,
            },
            {
              "active" => true,
              "name" => "str_album_thumb_back",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 36,
            },
            {
              "active" => true,
              "name" => "str_album_thumb_hq",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 37,
            },
            {
              "active" => true,
              "name" => "str_all_music_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 38,
            },
            {
              "active" => true,
              "name" => "str_amazon_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 39,
            },
            {
              "active" => true,
              "name" => "str_artist",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 40,
            },
            {
              "active" => true,
              "name" => "str_artist_alternate",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 41,
            },
            {
              "active" => true,
              "name" => "str_artist_banner",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 42,
            },
            {
              "active" => true,
              "name" => "str_artist_clearart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 43,
            },
            {
              "active" => true,
              "name" => "str_artist_cutout",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 44,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 45,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart2",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 46,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 47,
            },
            {
              "active" => true,
              "name" => "str_artist_fanart4",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 48,
            },
            {
              "active" => true,
              "name" => "str_artist_logo",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 49,
            },
            {
              "active" => true,
              "name" => "str_artist_stripped",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 50,
            },
            {
              "active" => true,
              "name" => "str_artist_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 51,
            },
            {
              "active" => true,
              "name" => "str_artist_wide_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 52,
            },
            {
              "active" => true,
              "name" => "str_bbc_review_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 53,
            },
            {
              "active" => true,
              "name" => "str_biography_en",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 54,
            },
            {
              "active" => true,
              "name" => "str_country",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 55,
            },
            {
              "active" => true,
              "name" => "str_country_code",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 56,
            },
            {
              "active" => true,
              "name" => "str_description_en",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 57,
            },
            {
              "active" => true,
              "name" => "str_disbanded",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 58,
            },
            {
              "active" => true,
              "name" => "str_discogs_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 59,
            },
            {
              "active" => true,
              "name" => "str_facebook",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 60,
            },
            {
              "active" => true,
              "name" => "str_gender",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 61,
            },
            {
              "active" => true,
              "name" => "str_genius_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 62,
            },
            {
              "active" => true,
              "name" => "str_genre",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 63,
            },
            {
              "active" => true,
              "name" => "str_isn_icode",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 64,
            },
            {
              "active" => true,
              "name" => "str_itunes_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 65,
            },
            {
              "active" => true,
              "name" => "str_label",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 66,
            },
            {
              "active" => true,
              "name" => "str_last_fm_chart",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 67,
            },
            {
              "active" => true,
              "name" => "str_location",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 68,
            },
            {
              "active" => true,
              "name" => "str_locked",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 69,
            },
            {
              "active" => true,
              "name" => "str_lyric_wiki_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 70,
            },
            {
              "active" => true,
              "name" => "str_mood",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 71,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_album_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 72,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_artist_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 73,
            },
            {
              "active" => true,
              "name" => "str_music_brainz_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 74,
            },
            {
              "active" => true,
              "name" => "str_music_moz_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 75,
            },
            {
              "active" => true,
              "name" => "str_music_vid",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 76,
            },
            {
              "active" => true,
              "name" => "str_music_vid_company",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 77,
            },
            {
              "active" => true,
              "name" => "str_music_vid_director",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 78,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen1",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 79,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen2",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 80,
            },
            {
              "active" => true,
              "name" => "str_music_vid_screen3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 81,
            },
            {
              "active" => true,
              "name" => "str_rate_your_music_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 82,
            },
            {
              "active" => true,
              "name" => "str_release_format",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 83,
            },
            {
              "active" => true,
              "name" => "str_review",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 84,
            },
            {
              "active" => true,
              "name" => "str_speed",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 85,
            },
            {
              "active" => true,
              "name" => "str_style",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 86,
            },
            {
              "active" => true,
              "name" => "str_theme",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 87,
            },
            {
              "active" => true,
              "name" => "str_track",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 88,
            },
            {
              "active" => true,
              "name" => "str_track3x3",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 89,
            },
            {
              "active" => true,
              "name" => "str_track_lyric",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 90,
            },
            {
              "active" => true,
              "name" => "str_track_thumb",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 91,
            },
            {
              "active" => true,
              "name" => "str_twitter",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 92,
            },
            {
              "active" => true,
              "name" => "str_website",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 93,
            },
            {
              "active" => true,
              "name" => "str_wikidata_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 94,
            },
            {
              "active" => true,
              "name" => "str_wikipedia_id",
              "req" => false,
              "type" => "`$STRING`",
              "index$" => 95,
            },
          ],
          "name" => "v1_search",
          "op" => {
            "list" => {
              "input" => "data",
              "name" => "list",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "Homework",
                        "kind" => "query",
                        "name" => "a",
                        "orig" => "a",
                        "reqd" => false,
                        "type" => "`$STRING`",
                      },
                      {
                        "active" => true,
                        "example" => "daft_punk",
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/searchalbum.php",
                  "parts" => [
                    "{api_key}",
                    "searchalbum.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "a",
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "coldplay",
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                      {
                        "active" => true,
                        "example" => "yellow",
                        "kind" => "query",
                        "name" => "t",
                        "orig" => "t",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/searchtrack.php",
                  "parts" => [
                    "{api_key}",
                    "searchtrack.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                      "t",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/discography.php",
                  "parts" => [
                    "{api_key}",
                    "discography.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "123",
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "example" => "coldplay",
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/search.php",
                  "parts" => [
                    "{api_key}",
                    "search.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 3,
                },
              ],
              "key$" => "list",
            },
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "kind" => "param",
                        "name" => "api_key",
                        "orig" => "api_key",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                    "query" => [
                      {
                        "active" => true,
                        "kind" => "query",
                        "name" => "s",
                        "orig" => "s",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/{apiKey}/discography-mb.php",
                  "parts" => [
                    "{api_key}",
                    "discography-mb.php",
                  ],
                  "rename" => {
                    "param" => {
                      "apiKey" => "api_key",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "api_key",
                      "s",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [],
          },
        },
        "v2_list" => {
          "fields" => [
            {
              "active" => true,
              "name" => "album",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 0,
            },
          ],
          "name" => "v2_list",
          "op" => {
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => 111239,
                        "kind" => "param",
                        "name" => "id_artist",
                        "orig" => "id_artist",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/list/discography/{idArtist}",
                  "parts" => [
                    "list",
                    "discography",
                    "{id_artist}",
                  ],
                  "rename" => {
                    "param" => {
                      "idArtist" => "id_artist",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "id_artist",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [
              [
                "discography",
              ],
            ],
          },
        },
        "v2_lookup" => {
          "fields" => [
            {
              "active" => true,
              "name" => "album",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 0,
            },
            {
              "active" => true,
              "name" => "artist",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 1,
            },
            {
              "active" => true,
              "name" => "track",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 2,
            },
          ],
          "name" => "v2_lookup",
          "op" => {
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => 2109615,
                        "kind" => "param",
                        "name" => "id_album",
                        "orig" => "id_album",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/album/{idAlbum}",
                  "parts" => [
                    "lookup",
                    "album",
                    "{id_album}",
                  ],
                  "rename" => {
                    "param" => {
                      "idAlbum" => "id_album",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "id_album",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => 111239,
                        "kind" => "param",
                        "name" => "id_artist",
                        "orig" => "id_artist",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/artist/{idArtist}",
                  "parts" => [
                    "lookup",
                    "artist",
                    "{id_artist}",
                  ],
                  "rename" => {
                    "param" => {
                      "idArtist" => "id_artist",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "id_artist",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => 32724183,
                        "kind" => "param",
                        "name" => "id_track",
                        "orig" => "id_track",
                        "reqd" => true,
                        "type" => "`$INTEGER`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/track/{idTrack}",
                  "parts" => [
                    "lookup",
                    "track",
                    "{id_track}",
                  ],
                  "rename" => {
                    "param" => {
                      "idTrack" => "id_track",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "id_track",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "1dc4c347-a1db-32aa-b14f-bc9cc507b843",
                        "kind" => "param",
                        "name" => "music_brainz_id",
                        "orig" => "music_brainz_id",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/album_mb/{musicBrainzId}",
                  "parts" => [
                    "lookup",
                    "album_mb",
                    "{music_brainz_id}",
                  ],
                  "rename" => {
                    "param" => {
                      "musicBrainzId" => "music_brainz_id",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "music_brainz_id",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 3,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                        "kind" => "param",
                        "name" => "music_brainz_id",
                        "orig" => "music_brainz_id",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/artist_mb/{musicBrainzId}",
                  "parts" => [
                    "lookup",
                    "artist_mb",
                    "{music_brainz_id}",
                  ],
                  "rename" => {
                    "param" => {
                      "musicBrainzId" => "music_brainz_id",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "music_brainz_id",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 4,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "50369905-68ca-48d2-912d-b37330ff7dc3",
                        "kind" => "param",
                        "name" => "music_brainz_id",
                        "orig" => "music_brainz_id",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/lookup/track_mb/{musicBrainzId}",
                  "parts" => [
                    "lookup",
                    "track_mb",
                    "{music_brainz_id}",
                  ],
                  "rename" => {
                    "param" => {
                      "musicBrainzId" => "music_brainz_id",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "music_brainz_id",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 5,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [
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
        "v2_search" => {
          "fields" => [
            {
              "active" => true,
              "name" => "album",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 0,
            },
            {
              "active" => true,
              "name" => "artist",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 1,
            },
            {
              "active" => true,
              "name" => "track",
              "req" => false,
              "type" => "`$ARRAY`",
              "index$" => 2,
            },
          ],
          "name" => "v2_search",
          "op" => {
            "load" => {
              "input" => "data",
              "name" => "load",
              "points" => [
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "parachutes",
                        "kind" => "param",
                        "name" => "album_name",
                        "orig" => "album_name",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/search/album/{albumName}",
                  "parts" => [
                    "search",
                    "album",
                    "{album_name}",
                  ],
                  "rename" => {
                    "param" => {
                      "albumName" => "album_name",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "album_name",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 0,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "coldplay",
                        "kind" => "param",
                        "name" => "artist_name",
                        "orig" => "artist_name",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/search/artist/{artistName}",
                  "parts" => [
                    "search",
                    "artist",
                    "{artist_name}",
                  ],
                  "rename" => {
                    "param" => {
                      "artistName" => "artist_name",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "artist_name",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 1,
                },
                {
                  "active" => true,
                  "args" => {
                    "params" => [
                      {
                        "active" => true,
                        "example" => "yellow",
                        "kind" => "param",
                        "name" => "track_name",
                        "orig" => "track_name",
                        "reqd" => true,
                        "type" => "`$STRING`",
                      },
                    ],
                  },
                  "method" => "GET",
                  "orig" => "/search/track/{trackName}",
                  "parts" => [
                    "search",
                    "track",
                    "{track_name}",
                  ],
                  "rename" => {
                    "param" => {
                      "trackName" => "track_name",
                    },
                  },
                  "select" => {
                    "exist" => [
                      "track_name",
                    ],
                  },
                  "transform" => {
                    "req" => "`reqdata`",
                    "res" => "`body`",
                  },
                  "index$" => 2,
                },
              ],
              "key$" => "load",
            },
          },
          "relations" => {
            "ancestors" => [
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
  end


  def self.make_feature(name)
    require_relative 'features'
    FreeMusicFeatures.make_feature(name)
  end
end
