<?php
declare(strict_types=1);

// FreeMusic SDK configuration

class FreeMusicConfig
{
    public static function make_config(): array
    {
        return [
            "main" => [
                "name" => "FreeMusic",
            ],
            "feature" => [
                "test" => [
          'options' => [
            'active' => false,
          ],
        ],
            ],
            "options" => [
                "base" => "https://www.theaudiodb.com/api/v1/json",
                "auth" => [
                    "prefix" => "",
                ],
                "headers" => [
          'content-type' => 'application/json',
        ],
                "entity" => [
                    "v1_list" => [],
                    "v1_lookup" => [],
                    "v1_search" => [],
                    "v2_list" => [],
                    "v2_lookup" => [],
                    "v2_search" => [],
                ],
            ],
            "entity" => [
        'v1_list' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'idAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 0,
            ],
            [
              'active' => true,
              'name' => 'idArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 1,
            ],
            [
              'active' => true,
              'name' => 'idIMVDB',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 2,
            ],
            [
              'active' => true,
              'name' => 'idLyric',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 3,
            ],
            [
              'active' => true,
              'name' => 'idTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 4,
            ],
            [
              'active' => true,
              'name' => 'intCD',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 5,
            ],
            [
              'active' => true,
              'name' => 'intDuration',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 6,
            ],
            [
              'active' => true,
              'name' => 'intLoved',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 7,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidComments',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 8,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidDislikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 9,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidFavorites',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 10,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidLikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 11,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidViews',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 12,
            ],
            [
              'active' => true,
              'name' => 'intScore',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 13,
            ],
            [
              'active' => true,
              'name' => 'intScoreVotes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 14,
            ],
            [
              'active' => true,
              'name' => 'intTotalListeners',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 15,
            ],
            [
              'active' => true,
              'name' => 'intTotalPlays',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 16,
            ],
            [
              'active' => true,
              'name' => 'intTrackNumber',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 17,
            ],
            [
              'active' => true,
              'name' => 'strAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 18,
            ],
            [
              'active' => true,
              'name' => 'strArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 19,
            ],
            [
              'active' => true,
              'name' => 'strArtistAlternate',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 20,
            ],
            [
              'active' => true,
              'name' => 'strDescriptionEN',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 21,
            ],
            [
              'active' => true,
              'name' => 'strGenre',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 22,
            ],
            [
              'active' => true,
              'name' => 'strLocked',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 23,
            ],
            [
              'active' => true,
              'name' => 'strMood',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 24,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzAlbumID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 25,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzArtistID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 26,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 27,
            ],
            [
              'active' => true,
              'name' => 'strMusicVid',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 28,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidCompany',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 29,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidDirector',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 30,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen1',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 31,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen2',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 32,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 33,
            ],
            [
              'active' => true,
              'name' => 'strStyle',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 34,
            ],
            [
              'active' => true,
              'name' => 'strTheme',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 35,
            ],
            [
              'active' => true,
              'name' => 'strTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 36,
            ],
            [
              'active' => true,
              'name' => 'strTrack3x3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 37,
            ],
            [
              'active' => true,
              'name' => 'strTrackLyrics',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 38,
            ],
            [
              'active' => true,
              'name' => 'strTrackThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 39,
            ],
            [
              'active' => true,
              'name' => 'trending',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 40,
            ],
          ],
          'name' => 'v1_list',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'us',
                        'kind' => 'query',
                        'name' => 'country',
                        'orig' => 'country',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'format',
                        'orig' => 'format',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'type',
                        'orig' => 'type',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/trending.php',
                  'parts' => [
                    '{api_key}',
                    'trending.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'country',
                      'format',
                      'type',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.trending`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/mvid.php',
                  'parts' => [
                    '{api_key}',
                    'mvid.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.mvids`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'coldplay',
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/track-top10.php',
                  'parts' => [
                    '{api_key}',
                    'track-top10.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.track`',
                  ],
                  'index$' => 2,
                ],
              ],
              'key$' => 'list',
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'format',
                        'orig' => 'format',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/mostloved.php',
                  'parts' => [
                    '{api_key}',
                    'mostloved.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'format',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/mvid-mb.php',
                  'parts' => [
                    '{api_key}',
                    'mvid-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/track-top10-mb.php',
                  'parts' => [
                    '{api_key}',
                    'track-top10-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 2,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
        'v1_lookup' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'idAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 0,
            ],
            [
              'active' => true,
              'name' => 'idArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 1,
            ],
            [
              'active' => true,
              'name' => 'idIMVDB',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 2,
            ],
            [
              'active' => true,
              'name' => 'idLabel',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 3,
            ],
            [
              'active' => true,
              'name' => 'idLyric',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 4,
            ],
            [
              'active' => true,
              'name' => 'idTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 5,
            ],
            [
              'active' => true,
              'name' => 'intBornYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 6,
            ],
            [
              'active' => true,
              'name' => 'intCD',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 7,
            ],
            [
              'active' => true,
              'name' => 'intCharted',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 8,
            ],
            [
              'active' => true,
              'name' => 'intDiedYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 9,
            ],
            [
              'active' => true,
              'name' => 'intDuration',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 10,
            ],
            [
              'active' => true,
              'name' => 'intFormedYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 11,
            ],
            [
              'active' => true,
              'name' => 'intLoved',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 12,
            ],
            [
              'active' => true,
              'name' => 'intMembers',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 13,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidComments',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 14,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidDislikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 15,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidFavorites',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 16,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidLikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 17,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidViews',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 18,
            ],
            [
              'active' => true,
              'name' => 'intSales',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 19,
            ],
            [
              'active' => true,
              'name' => 'intScore',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 20,
            ],
            [
              'active' => true,
              'name' => 'intScoreVotes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 21,
            ],
            [
              'active' => true,
              'name' => 'intTotalListeners',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 22,
            ],
            [
              'active' => true,
              'name' => 'intTotalPlays',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 23,
            ],
            [
              'active' => true,
              'name' => 'intTrackNumber',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 24,
            ],
            [
              'active' => true,
              'name' => 'intYearReleased',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 25,
            ],
            [
              'active' => true,
              'name' => 'strAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 26,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DCase',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 27,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DFace',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 28,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DFlat',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 29,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 30,
            ],
            [
              'active' => true,
              'name' => 'strAlbumCDart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 31,
            ],
            [
              'active' => true,
              'name' => 'strAlbumSpine',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 32,
            ],
            [
              'active' => true,
              'name' => 'strAlbumStripped',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 33,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 34,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumbBack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 35,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumbHQ',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 36,
            ],
            [
              'active' => true,
              'name' => 'strAllMusicID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 37,
            ],
            [
              'active' => true,
              'name' => 'strAmazonID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 38,
            ],
            [
              'active' => true,
              'name' => 'strArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 39,
            ],
            [
              'active' => true,
              'name' => 'strArtistAlternate',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 40,
            ],
            [
              'active' => true,
              'name' => 'strArtistBanner',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 41,
            ],
            [
              'active' => true,
              'name' => 'strArtistClearart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 42,
            ],
            [
              'active' => true,
              'name' => 'strArtistCutout',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 43,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 44,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart2',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 45,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 46,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart4',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 47,
            ],
            [
              'active' => true,
              'name' => 'strArtistLogo',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 48,
            ],
            [
              'active' => true,
              'name' => 'strArtistStripped',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 49,
            ],
            [
              'active' => true,
              'name' => 'strArtistThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 50,
            ],
            [
              'active' => true,
              'name' => 'strArtistWideThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 51,
            ],
            [
              'active' => true,
              'name' => 'strBBCReviewID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 52,
            ],
            [
              'active' => true,
              'name' => 'strBiographyEN',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 53,
            ],
            [
              'active' => true,
              'name' => 'strCountry',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 54,
            ],
            [
              'active' => true,
              'name' => 'strCountryCode',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 55,
            ],
            [
              'active' => true,
              'name' => 'strDescriptionEN',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 56,
            ],
            [
              'active' => true,
              'name' => 'strDisbanded',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 57,
            ],
            [
              'active' => true,
              'name' => 'strDiscogsID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 58,
            ],
            [
              'active' => true,
              'name' => 'strFacebook',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 59,
            ],
            [
              'active' => true,
              'name' => 'strGender',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 60,
            ],
            [
              'active' => true,
              'name' => 'strGeniusID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 61,
            ],
            [
              'active' => true,
              'name' => 'strGenre',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 62,
            ],
            [
              'active' => true,
              'name' => 'strISNIcode',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 63,
            ],
            [
              'active' => true,
              'name' => 'strItunesID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 64,
            ],
            [
              'active' => true,
              'name' => 'strLabel',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 65,
            ],
            [
              'active' => true,
              'name' => 'strLastFMChart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 66,
            ],
            [
              'active' => true,
              'name' => 'strLocation',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 67,
            ],
            [
              'active' => true,
              'name' => 'strLocked',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 68,
            ],
            [
              'active' => true,
              'name' => 'strLyricWikiID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 69,
            ],
            [
              'active' => true,
              'name' => 'strMood',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 70,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzAlbumID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 71,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzArtistID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 72,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 73,
            ],
            [
              'active' => true,
              'name' => 'strMusicMozID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 74,
            ],
            [
              'active' => true,
              'name' => 'strMusicVid',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 75,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidCompany',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 76,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidDirector',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 77,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen1',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 78,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen2',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 79,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 80,
            ],
            [
              'active' => true,
              'name' => 'strRateYourMusicID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 81,
            ],
            [
              'active' => true,
              'name' => 'strReleaseFormat',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 82,
            ],
            [
              'active' => true,
              'name' => 'strReview',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 83,
            ],
            [
              'active' => true,
              'name' => 'strSpeed',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 84,
            ],
            [
              'active' => true,
              'name' => 'strStyle',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 85,
            ],
            [
              'active' => true,
              'name' => 'strTheme',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 86,
            ],
            [
              'active' => true,
              'name' => 'strTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 87,
            ],
            [
              'active' => true,
              'name' => 'strTrack3x3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 88,
            ],
            [
              'active' => true,
              'name' => 'strTrackLyrics',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 89,
            ],
            [
              'active' => true,
              'name' => 'strTrackThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 90,
            ],
            [
              'active' => true,
              'name' => 'strTwitter',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 91,
            ],
            [
              'active' => true,
              'name' => 'strWebsite',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 92,
            ],
            [
              'active' => true,
              'name' => 'strWikidataID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 93,
            ],
            [
              'active' => true,
              'name' => 'strWikipediaID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 94,
            ],
          ],
          'name' => 'v1_lookup',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'h',
                        'orig' => 'h',
                        'reqd' => false,
                        'type' => '`$INTEGER`',
                      ],
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'm',
                        'orig' => 'm',
                        'reqd' => false,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/track.php',
                  'parts' => [
                    '{api_key}',
                    'track.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'h',
                      'm',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.track`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => false,
                        'type' => '`$INTEGER`',
                      ],
                      [
                        'active' => true,
                        'example' => 2115888,
                        'kind' => 'query',
                        'name' => 'm',
                        'orig' => 'm',
                        'reqd' => false,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/album.php',
                  'parts' => [
                    '{api_key}',
                    'album.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                      'm',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.album`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 112024,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/artist.php',
                  'parts' => [
                    '{api_key}',
                    'artist.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.artists`',
                  ],
                  'index$' => 2,
                ],
              ],
              'key$' => 'list',
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/album-mb.php',
                  'parts' => [
                    '{api_key}',
                    'album-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'cc197bad-dc9c-440d-a5b5-d52ba2e14234',
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/artist-mb.php',
                  'parts' => [
                    '{api_key}',
                    'artist-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/artist-social.php',
                  'parts' => [
                    '{api_key}',
                    'artist-social.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 2,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 'i',
                        'orig' => 'i',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/track-mb.php',
                  'parts' => [
                    '{api_key}',
                    'track-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      'i',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 3,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
        'v1_search' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'album',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 0,
            ],
            [
              'active' => true,
              'name' => 'idAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 1,
            ],
            [
              'active' => true,
              'name' => 'idArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 2,
            ],
            [
              'active' => true,
              'name' => 'idIMVDB',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 3,
            ],
            [
              'active' => true,
              'name' => 'idLabel',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 4,
            ],
            [
              'active' => true,
              'name' => 'idLyric',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 5,
            ],
            [
              'active' => true,
              'name' => 'idTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 6,
            ],
            [
              'active' => true,
              'name' => 'intBornYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 7,
            ],
            [
              'active' => true,
              'name' => 'intCD',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 8,
            ],
            [
              'active' => true,
              'name' => 'intCharted',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 9,
            ],
            [
              'active' => true,
              'name' => 'intDiedYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 10,
            ],
            [
              'active' => true,
              'name' => 'intDuration',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 11,
            ],
            [
              'active' => true,
              'name' => 'intFormedYear',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 12,
            ],
            [
              'active' => true,
              'name' => 'intLoved',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 13,
            ],
            [
              'active' => true,
              'name' => 'intMembers',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 14,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidComments',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 15,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidDislikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 16,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidFavorites',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 17,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidLikes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 18,
            ],
            [
              'active' => true,
              'name' => 'intMusicVidViews',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 19,
            ],
            [
              'active' => true,
              'name' => 'intSales',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 20,
            ],
            [
              'active' => true,
              'name' => 'intScore',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 21,
            ],
            [
              'active' => true,
              'name' => 'intScoreVotes',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 22,
            ],
            [
              'active' => true,
              'name' => 'intTotalListeners',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 23,
            ],
            [
              'active' => true,
              'name' => 'intTotalPlays',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 24,
            ],
            [
              'active' => true,
              'name' => 'intTrackNumber',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 25,
            ],
            [
              'active' => true,
              'name' => 'intYearReleased',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 26,
            ],
            [
              'active' => true,
              'name' => 'strAlbum',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 27,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DCase',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 28,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DFace',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 29,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DFlat',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 30,
            ],
            [
              'active' => true,
              'name' => 'strAlbum3DThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 31,
            ],
            [
              'active' => true,
              'name' => 'strAlbumCDart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 32,
            ],
            [
              'active' => true,
              'name' => 'strAlbumSpine',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 33,
            ],
            [
              'active' => true,
              'name' => 'strAlbumStripped',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 34,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 35,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumbBack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 36,
            ],
            [
              'active' => true,
              'name' => 'strAlbumThumbHQ',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 37,
            ],
            [
              'active' => true,
              'name' => 'strAllMusicID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 38,
            ],
            [
              'active' => true,
              'name' => 'strAmazonID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 39,
            ],
            [
              'active' => true,
              'name' => 'strArtist',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 40,
            ],
            [
              'active' => true,
              'name' => 'strArtistAlternate',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 41,
            ],
            [
              'active' => true,
              'name' => 'strArtistBanner',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 42,
            ],
            [
              'active' => true,
              'name' => 'strArtistClearart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 43,
            ],
            [
              'active' => true,
              'name' => 'strArtistCutout',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 44,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 45,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart2',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 46,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 47,
            ],
            [
              'active' => true,
              'name' => 'strArtistFanart4',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 48,
            ],
            [
              'active' => true,
              'name' => 'strArtistLogo',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 49,
            ],
            [
              'active' => true,
              'name' => 'strArtistStripped',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 50,
            ],
            [
              'active' => true,
              'name' => 'strArtistThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 51,
            ],
            [
              'active' => true,
              'name' => 'strArtistWideThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 52,
            ],
            [
              'active' => true,
              'name' => 'strBBCReviewID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 53,
            ],
            [
              'active' => true,
              'name' => 'strBiographyEN',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 54,
            ],
            [
              'active' => true,
              'name' => 'strCountry',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 55,
            ],
            [
              'active' => true,
              'name' => 'strCountryCode',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 56,
            ],
            [
              'active' => true,
              'name' => 'strDescriptionEN',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 57,
            ],
            [
              'active' => true,
              'name' => 'strDisbanded',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 58,
            ],
            [
              'active' => true,
              'name' => 'strDiscogsID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 59,
            ],
            [
              'active' => true,
              'name' => 'strFacebook',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 60,
            ],
            [
              'active' => true,
              'name' => 'strGender',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 61,
            ],
            [
              'active' => true,
              'name' => 'strGeniusID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 62,
            ],
            [
              'active' => true,
              'name' => 'strGenre',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 63,
            ],
            [
              'active' => true,
              'name' => 'strISNIcode',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 64,
            ],
            [
              'active' => true,
              'name' => 'strItunesID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 65,
            ],
            [
              'active' => true,
              'name' => 'strLabel',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 66,
            ],
            [
              'active' => true,
              'name' => 'strLastFMChart',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 67,
            ],
            [
              'active' => true,
              'name' => 'strLocation',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 68,
            ],
            [
              'active' => true,
              'name' => 'strLocked',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 69,
            ],
            [
              'active' => true,
              'name' => 'strLyricWikiID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 70,
            ],
            [
              'active' => true,
              'name' => 'strMood',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 71,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzAlbumID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 72,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzArtistID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 73,
            ],
            [
              'active' => true,
              'name' => 'strMusicBrainzID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 74,
            ],
            [
              'active' => true,
              'name' => 'strMusicMozID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 75,
            ],
            [
              'active' => true,
              'name' => 'strMusicVid',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 76,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidCompany',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 77,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidDirector',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 78,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen1',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 79,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen2',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 80,
            ],
            [
              'active' => true,
              'name' => 'strMusicVidScreen3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 81,
            ],
            [
              'active' => true,
              'name' => 'strRateYourMusicID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 82,
            ],
            [
              'active' => true,
              'name' => 'strReleaseFormat',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 83,
            ],
            [
              'active' => true,
              'name' => 'strReview',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 84,
            ],
            [
              'active' => true,
              'name' => 'strSpeed',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 85,
            ],
            [
              'active' => true,
              'name' => 'strStyle',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 86,
            ],
            [
              'active' => true,
              'name' => 'strTheme',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 87,
            ],
            [
              'active' => true,
              'name' => 'strTrack',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 88,
            ],
            [
              'active' => true,
              'name' => 'strTrack3x3',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 89,
            ],
            [
              'active' => true,
              'name' => 'strTrackLyrics',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 90,
            ],
            [
              'active' => true,
              'name' => 'strTrackThumb',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 91,
            ],
            [
              'active' => true,
              'name' => 'strTwitter',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 92,
            ],
            [
              'active' => true,
              'name' => 'strWebsite',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 93,
            ],
            [
              'active' => true,
              'name' => 'strWikidataID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 94,
            ],
            [
              'active' => true,
              'name' => 'strWikipediaID',
              'req' => false,
              'type' => '`$STRING`',
              'index$' => 95,
            ],
          ],
          'name' => 'v1_search',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'Homework',
                        'kind' => 'query',
                        'name' => 'a',
                        'orig' => 'a',
                        'reqd' => false,
                        'type' => '`$STRING`',
                      ],
                      [
                        'active' => true,
                        'example' => 'daft_punk',
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/searchalbum.php',
                  'parts' => [
                    '{api_key}',
                    'searchalbum.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'a',
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.album`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'coldplay',
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                      [
                        'active' => true,
                        'example' => 'yellow',
                        'kind' => 'query',
                        'name' => 't',
                        'orig' => 't',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/searchtrack.php',
                  'parts' => [
                    '{api_key}',
                    'searchtrack.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                      't',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.track`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/discography.php',
                  'parts' => [
                    '{api_key}',
                    'discography.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.album`',
                  ],
                  'index$' => 2,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => '123',
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'example' => 'coldplay',
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/search.php',
                  'parts' => [
                    '{api_key}',
                    'search.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.artists`',
                  ],
                  'index$' => 3,
                ],
              ],
              'key$' => 'list',
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'kind' => 'param',
                        'name' => 'api_key',
                        'orig' => 'api_key',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                    'query' => [
                      [
                        'active' => true,
                        'kind' => 'query',
                        'name' => 's',
                        'orig' => 's',
                        'reqd' => true,
                        'type' => '`$STRING`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/{apiKey}/discography-mb.php',
                  'parts' => [
                    '{api_key}',
                    'discography-mb.php',
                  ],
                  'rename' => [
                    'param' => [
                      'apiKey' => 'api_key',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'api_key',
                      's',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
        'v2_list' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'album',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 0,
            ],
          ],
          'name' => 'v2_list',
          'op' => [
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 111239,
                        'kind' => 'param',
                        'name' => 'id_artist',
                        'orig' => 'id_artist',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/list/discography/{idArtist}',
                  'parts' => [
                    'list',
                    'discography',
                    '{id_artist}',
                  ],
                  'rename' => [
                    'param' => [
                      'idArtist' => 'id_artist',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'id_artist',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [
              [
                'discography',
              ],
            ],
          ],
        ],
        'v2_lookup' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'album',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 0,
            ],
            [
              'active' => true,
              'name' => 'artists',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 1,
            ],
            [
              'active' => true,
              'name' => 'track',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 2,
            ],
          ],
          'name' => 'v2_lookup',
          'op' => [
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 2109615,
                        'kind' => 'param',
                        'name' => 'id_album',
                        'orig' => 'id_album',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/album/{idAlbum}',
                  'parts' => [
                    'lookup',
                    'album',
                    '{id_album}',
                  ],
                  'rename' => [
                    'param' => [
                      'idAlbum' => 'id_album',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'id_album',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 111239,
                        'kind' => 'param',
                        'name' => 'id_artist',
                        'orig' => 'id_artist',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/artist/{idArtist}',
                  'parts' => [
                    'lookup',
                    'artist',
                    '{id_artist}',
                  ],
                  'rename' => [
                    'param' => [
                      'idArtist' => 'id_artist',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'id_artist',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 32724183,
                        'kind' => 'param',
                        'name' => 'id_track',
                        'orig' => 'id_track',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/track/{idTrack}',
                  'parts' => [
                    'lookup',
                    'track',
                    '{id_track}',
                  ],
                  'rename' => [
                    'param' => [
                      'idTrack' => 'id_track',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'id_track',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 2,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => '1dc4c347-a1db-32aa-b14f-bc9cc507b843',
                        'kind' => 'param',
                        'name' => 'music_brainz_id',
                        'orig' => 'music_brainz_id',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/album_mb/{musicBrainzId}',
                  'parts' => [
                    'lookup',
                    'album_mb',
                    '{music_brainz_id}',
                  ],
                  'rename' => [
                    'param' => [
                      'musicBrainzId' => 'music_brainz_id',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'music_brainz_id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 3,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 'cc197bad-dc9c-440d-a5b5-d52ba2e14234',
                        'kind' => 'param',
                        'name' => 'music_brainz_id',
                        'orig' => 'music_brainz_id',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/artist_mb/{musicBrainzId}',
                  'parts' => [
                    'lookup',
                    'artist_mb',
                    '{music_brainz_id}',
                  ],
                  'rename' => [
                    'param' => [
                      'musicBrainzId' => 'music_brainz_id',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'music_brainz_id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 4,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => '50369905-68ca-48d2-912d-b37330ff7dc3',
                        'kind' => 'param',
                        'name' => 'music_brainz_id',
                        'orig' => 'music_brainz_id',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/lookup/track_mb/{musicBrainzId}',
                  'parts' => [
                    'lookup',
                    'track_mb',
                    '{music_brainz_id}',
                  ],
                  'rename' => [
                    'param' => [
                      'musicBrainzId' => 'music_brainz_id',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'music_brainz_id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 5,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [
              [
                'album',
              ],
              [
                'album_mb',
              ],
              [
                'artist',
              ],
              [
                'artist_mb',
              ],
              [
                'track',
              ],
              [
                'track_mb',
              ],
            ],
          ],
        ],
        'v2_search' => [
          'fields' => [
            [
              'active' => true,
              'name' => 'album',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 0,
            ],
            [
              'active' => true,
              'name' => 'artists',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 1,
            ],
            [
              'active' => true,
              'name' => 'track',
              'req' => false,
              'type' => '`$ARRAY`',
              'index$' => 2,
            ],
          ],
          'name' => 'v2_search',
          'op' => [
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 'parachutes',
                        'kind' => 'param',
                        'name' => 'album_name',
                        'orig' => 'album_name',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/search/album/{albumName}',
                  'parts' => [
                    'search',
                    'album',
                    '{album_name}',
                  ],
                  'rename' => [
                    'param' => [
                      'albumName' => 'album_name',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'album_name',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 0,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 'coldplay',
                        'kind' => 'param',
                        'name' => 'artist_name',
                        'orig' => 'artist_name',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/search/artist/{artistName}',
                  'parts' => [
                    'search',
                    'artist',
                    '{artist_name}',
                  ],
                  'rename' => [
                    'param' => [
                      'artistName' => 'artist_name',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'artist_name',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 1,
                ],
                [
                  'active' => true,
                  'args' => [
                    'params' => [
                      [
                        'active' => true,
                        'example' => 'yellow',
                        'kind' => 'param',
                        'name' => 'track_name',
                        'orig' => 'track_name',
                        'reqd' => true,
                        'type' => '`$STRING`',
                        'index$' => 0,
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/search/track/{trackName}',
                  'parts' => [
                    'search',
                    'track',
                    '{track_name}',
                  ],
                  'rename' => [
                    'param' => [
                      'trackName' => 'track_name',
                    ],
                  ],
                  'select' => [
                    'exist' => [
                      'track_name',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                  'index$' => 2,
                ],
              ],
              'key$' => 'load',
            ],
          ],
          'relations' => [
            'ancestors' => [
              [
                'album',
              ],
              [
                'artist',
              ],
              [
                'track',
              ],
            ],
          ],
        ],
      ],
        ];
    }


    public static function make_feature(string $name)
    {
        require_once __DIR__ . '/features.php';
        return FreeMusicFeatures::make_feature($name);
    }
}
