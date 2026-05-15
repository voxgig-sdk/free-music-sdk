package core

func MakeConfig() map[string]any {
	return map[string]any{
		"main": map[string]any{
			"name": "FreeMusic",
		},
		"feature": map[string]any{
			"test": map[string]any{
				"options": map[string]any{
					"active": false,
				},
			},
		},
		"options": map[string]any{
			"base": "https://www.theaudiodb.com/api/v1/json",
			"auth": map[string]any{
				"prefix": "Bearer",
			},
			"headers": map[string]any{
				"content-type": "application/json",
			},
			"entity": map[string]any{
				"v1_list": map[string]any{},
				"v1_lookup": map[string]any{},
				"v1_search": map[string]any{},
				"v2_list": map[string]any{},
				"v2_lookup": map[string]any{},
				"v2_search": map[string]any{},
			},
		},
		"entity": map[string]any{
			"v1_list": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "id_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 0,
					},
					map[string]any{
						"name": "id_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 1,
					},
					map[string]any{
						"name": "id_imvdb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 2,
					},
					map[string]any{
						"name": "id_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 3,
					},
					map[string]any{
						"name": "id_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 4,
					},
					map[string]any{
						"name": "int_cd",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 5,
					},
					map[string]any{
						"name": "int_duration",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 6,
					},
					map[string]any{
						"name": "int_loved",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 7,
					},
					map[string]any{
						"name": "int_music_vid_comment",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 8,
					},
					map[string]any{
						"name": "int_music_vid_dislike",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 9,
					},
					map[string]any{
						"name": "int_music_vid_favorite",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 10,
					},
					map[string]any{
						"name": "int_music_vid_like",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 11,
					},
					map[string]any{
						"name": "int_music_vid_view",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 12,
					},
					map[string]any{
						"name": "int_score",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 13,
					},
					map[string]any{
						"name": "int_score_vote",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 14,
					},
					map[string]any{
						"name": "int_total_listener",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 15,
					},
					map[string]any{
						"name": "int_total_play",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 16,
					},
					map[string]any{
						"name": "int_track_number",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 17,
					},
					map[string]any{
						"name": "str_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 18,
					},
					map[string]any{
						"name": "str_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 19,
					},
					map[string]any{
						"name": "str_artist_alternate",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 20,
					},
					map[string]any{
						"name": "str_description_en",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 21,
					},
					map[string]any{
						"name": "str_genre",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 22,
					},
					map[string]any{
						"name": "str_locked",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 23,
					},
					map[string]any{
						"name": "str_mood",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 24,
					},
					map[string]any{
						"name": "str_music_brainz_album_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 25,
					},
					map[string]any{
						"name": "str_music_brainz_artist_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 26,
					},
					map[string]any{
						"name": "str_music_brainz_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 27,
					},
					map[string]any{
						"name": "str_music_vid",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 28,
					},
					map[string]any{
						"name": "str_music_vid_company",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 29,
					},
					map[string]any{
						"name": "str_music_vid_director",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 30,
					},
					map[string]any{
						"name": "str_music_vid_screen1",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 31,
					},
					map[string]any{
						"name": "str_music_vid_screen2",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 32,
					},
					map[string]any{
						"name": "str_music_vid_screen3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 33,
					},
					map[string]any{
						"name": "str_style",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 34,
					},
					map[string]any{
						"name": "str_theme",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 35,
					},
					map[string]any{
						"name": "str_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 36,
					},
					map[string]any{
						"name": "str_track3x3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 37,
					},
					map[string]any{
						"name": "str_track_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 38,
					},
					map[string]any{
						"name": "str_track_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 39,
					},
					map[string]any{
						"name": "trending",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 40,
					},
				},
				"name": "v1_list",
				"op": map[string]any{
					"list": map[string]any{
						"name": "list",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "us",
											"kind": "query",
											"name": "country",
											"orig": "country",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
										map[string]any{
											"kind": "query",
											"name": "format",
											"orig": "format",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
										map[string]any{
											"kind": "query",
											"name": "type",
											"orig": "type",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/trending.php",
								"parts": []any{
									"{api_key}",
									"trending.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"country",
										"format",
										"type",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/mvid.php",
								"parts": []any{
									"{api_key}",
									"mvid.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "coldplay",
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/track-top10.php",
								"parts": []any{
									"{api_key}",
									"track-top10.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
						},
						"input": "data",
						"key$": "list",
					},
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "format",
											"orig": "format",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/mostloved.php",
								"parts": []any{
									"{api_key}",
									"mostloved.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"format",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/mvid-mb.php",
								"parts": []any{
									"{api_key}",
									"mvid-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/track-top10-mb.php",
								"parts": []any{
									"{api_key}",
									"track-top10-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{},
				},
			},
			"v1_lookup": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "id_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 0,
					},
					map[string]any{
						"name": "id_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 1,
					},
					map[string]any{
						"name": "id_imvdb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 2,
					},
					map[string]any{
						"name": "id_label",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 3,
					},
					map[string]any{
						"name": "id_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 4,
					},
					map[string]any{
						"name": "id_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 5,
					},
					map[string]any{
						"name": "int_born_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 6,
					},
					map[string]any{
						"name": "int_cd",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 7,
					},
					map[string]any{
						"name": "int_charted",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 8,
					},
					map[string]any{
						"name": "int_died_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 9,
					},
					map[string]any{
						"name": "int_duration",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 10,
					},
					map[string]any{
						"name": "int_formed_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 11,
					},
					map[string]any{
						"name": "int_loved",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 12,
					},
					map[string]any{
						"name": "int_member",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 13,
					},
					map[string]any{
						"name": "int_music_vid_comment",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 14,
					},
					map[string]any{
						"name": "int_music_vid_dislike",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 15,
					},
					map[string]any{
						"name": "int_music_vid_favorite",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 16,
					},
					map[string]any{
						"name": "int_music_vid_like",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 17,
					},
					map[string]any{
						"name": "int_music_vid_view",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 18,
					},
					map[string]any{
						"name": "int_sale",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 19,
					},
					map[string]any{
						"name": "int_score",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 20,
					},
					map[string]any{
						"name": "int_score_vote",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 21,
					},
					map[string]any{
						"name": "int_total_listener",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 22,
					},
					map[string]any{
						"name": "int_total_play",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 23,
					},
					map[string]any{
						"name": "int_track_number",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 24,
					},
					map[string]any{
						"name": "int_year_released",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 25,
					},
					map[string]any{
						"name": "str_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 26,
					},
					map[string]any{
						"name": "str_album3_d_case",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 27,
					},
					map[string]any{
						"name": "str_album3_d_face",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 28,
					},
					map[string]any{
						"name": "str_album3_d_flat",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 29,
					},
					map[string]any{
						"name": "str_album3_d_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 30,
					},
					map[string]any{
						"name": "str_album_c_dart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 31,
					},
					map[string]any{
						"name": "str_album_spine",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 32,
					},
					map[string]any{
						"name": "str_album_stripped",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 33,
					},
					map[string]any{
						"name": "str_album_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 34,
					},
					map[string]any{
						"name": "str_album_thumb_back",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 35,
					},
					map[string]any{
						"name": "str_album_thumb_hq",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 36,
					},
					map[string]any{
						"name": "str_all_music_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 37,
					},
					map[string]any{
						"name": "str_amazon_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 38,
					},
					map[string]any{
						"name": "str_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 39,
					},
					map[string]any{
						"name": "str_artist_alternate",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 40,
					},
					map[string]any{
						"name": "str_artist_banner",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 41,
					},
					map[string]any{
						"name": "str_artist_clearart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 42,
					},
					map[string]any{
						"name": "str_artist_cutout",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 43,
					},
					map[string]any{
						"name": "str_artist_fanart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 44,
					},
					map[string]any{
						"name": "str_artist_fanart2",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 45,
					},
					map[string]any{
						"name": "str_artist_fanart3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 46,
					},
					map[string]any{
						"name": "str_artist_fanart4",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 47,
					},
					map[string]any{
						"name": "str_artist_logo",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 48,
					},
					map[string]any{
						"name": "str_artist_stripped",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 49,
					},
					map[string]any{
						"name": "str_artist_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 50,
					},
					map[string]any{
						"name": "str_artist_wide_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 51,
					},
					map[string]any{
						"name": "str_bbc_review_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 52,
					},
					map[string]any{
						"name": "str_biography_en",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 53,
					},
					map[string]any{
						"name": "str_country",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 54,
					},
					map[string]any{
						"name": "str_country_code",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 55,
					},
					map[string]any{
						"name": "str_description_en",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 56,
					},
					map[string]any{
						"name": "str_disbanded",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 57,
					},
					map[string]any{
						"name": "str_discogs_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 58,
					},
					map[string]any{
						"name": "str_facebook",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 59,
					},
					map[string]any{
						"name": "str_gender",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 60,
					},
					map[string]any{
						"name": "str_genius_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 61,
					},
					map[string]any{
						"name": "str_genre",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 62,
					},
					map[string]any{
						"name": "str_isn_icode",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 63,
					},
					map[string]any{
						"name": "str_itunes_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 64,
					},
					map[string]any{
						"name": "str_label",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 65,
					},
					map[string]any{
						"name": "str_last_fm_chart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 66,
					},
					map[string]any{
						"name": "str_location",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 67,
					},
					map[string]any{
						"name": "str_locked",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 68,
					},
					map[string]any{
						"name": "str_lyric_wiki_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 69,
					},
					map[string]any{
						"name": "str_mood",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 70,
					},
					map[string]any{
						"name": "str_music_brainz_album_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 71,
					},
					map[string]any{
						"name": "str_music_brainz_artist_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 72,
					},
					map[string]any{
						"name": "str_music_brainz_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 73,
					},
					map[string]any{
						"name": "str_music_moz_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 74,
					},
					map[string]any{
						"name": "str_music_vid",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 75,
					},
					map[string]any{
						"name": "str_music_vid_company",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 76,
					},
					map[string]any{
						"name": "str_music_vid_director",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 77,
					},
					map[string]any{
						"name": "str_music_vid_screen1",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 78,
					},
					map[string]any{
						"name": "str_music_vid_screen2",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 79,
					},
					map[string]any{
						"name": "str_music_vid_screen3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 80,
					},
					map[string]any{
						"name": "str_rate_your_music_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 81,
					},
					map[string]any{
						"name": "str_release_format",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 82,
					},
					map[string]any{
						"name": "str_review",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 83,
					},
					map[string]any{
						"name": "str_speed",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 84,
					},
					map[string]any{
						"name": "str_style",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 85,
					},
					map[string]any{
						"name": "str_theme",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 86,
					},
					map[string]any{
						"name": "str_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 87,
					},
					map[string]any{
						"name": "str_track3x3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 88,
					},
					map[string]any{
						"name": "str_track_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 89,
					},
					map[string]any{
						"name": "str_track_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 90,
					},
					map[string]any{
						"name": "str_twitter",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 91,
					},
					map[string]any{
						"name": "str_website",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 92,
					},
					map[string]any{
						"name": "str_wikidata_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 93,
					},
					map[string]any{
						"name": "str_wikipedia_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 94,
					},
				},
				"name": "v1_lookup",
				"op": map[string]any{
					"list": map[string]any{
						"name": "list",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "h",
											"orig": "h",
											"reqd": false,
											"type": "`$INTEGER`",
											"active": true,
										},
										map[string]any{
											"kind": "query",
											"name": "m",
											"orig": "m",
											"reqd": false,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/track.php",
								"parts": []any{
									"{api_key}",
									"track.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"h",
										"m",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": false,
											"type": "`$INTEGER`",
											"active": true,
										},
										map[string]any{
											"example": 2115888,
											"kind": "query",
											"name": "m",
											"orig": "m",
											"reqd": false,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/album.php",
								"parts": []any{
									"{api_key}",
									"album.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
										"m",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": 112024,
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/artist.php",
								"parts": []any{
									"{api_key}",
									"artist.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
						},
						"input": "data",
						"key$": "list",
					},
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/album-mb.php",
								"parts": []any{
									"{api_key}",
									"album-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/artist-mb.php",
								"parts": []any{
									"{api_key}",
									"artist-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/artist-social.php",
								"parts": []any{
									"{api_key}",
									"artist-social.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/track-mb.php",
								"parts": []any{
									"{api_key}",
									"track-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"i",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 3,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{},
				},
			},
			"v1_search": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "album",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 0,
					},
					map[string]any{
						"name": "id_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 1,
					},
					map[string]any{
						"name": "id_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 2,
					},
					map[string]any{
						"name": "id_imvdb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 3,
					},
					map[string]any{
						"name": "id_label",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 4,
					},
					map[string]any{
						"name": "id_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 5,
					},
					map[string]any{
						"name": "id_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 6,
					},
					map[string]any{
						"name": "int_born_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 7,
					},
					map[string]any{
						"name": "int_cd",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 8,
					},
					map[string]any{
						"name": "int_charted",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 9,
					},
					map[string]any{
						"name": "int_died_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 10,
					},
					map[string]any{
						"name": "int_duration",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 11,
					},
					map[string]any{
						"name": "int_formed_year",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 12,
					},
					map[string]any{
						"name": "int_loved",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 13,
					},
					map[string]any{
						"name": "int_member",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 14,
					},
					map[string]any{
						"name": "int_music_vid_comment",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 15,
					},
					map[string]any{
						"name": "int_music_vid_dislike",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 16,
					},
					map[string]any{
						"name": "int_music_vid_favorite",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 17,
					},
					map[string]any{
						"name": "int_music_vid_like",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 18,
					},
					map[string]any{
						"name": "int_music_vid_view",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 19,
					},
					map[string]any{
						"name": "int_sale",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 20,
					},
					map[string]any{
						"name": "int_score",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 21,
					},
					map[string]any{
						"name": "int_score_vote",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 22,
					},
					map[string]any{
						"name": "int_total_listener",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 23,
					},
					map[string]any{
						"name": "int_total_play",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 24,
					},
					map[string]any{
						"name": "int_track_number",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 25,
					},
					map[string]any{
						"name": "int_year_released",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 26,
					},
					map[string]any{
						"name": "str_album",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 27,
					},
					map[string]any{
						"name": "str_album3_d_case",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 28,
					},
					map[string]any{
						"name": "str_album3_d_face",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 29,
					},
					map[string]any{
						"name": "str_album3_d_flat",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 30,
					},
					map[string]any{
						"name": "str_album3_d_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 31,
					},
					map[string]any{
						"name": "str_album_c_dart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 32,
					},
					map[string]any{
						"name": "str_album_spine",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 33,
					},
					map[string]any{
						"name": "str_album_stripped",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 34,
					},
					map[string]any{
						"name": "str_album_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 35,
					},
					map[string]any{
						"name": "str_album_thumb_back",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 36,
					},
					map[string]any{
						"name": "str_album_thumb_hq",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 37,
					},
					map[string]any{
						"name": "str_all_music_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 38,
					},
					map[string]any{
						"name": "str_amazon_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 39,
					},
					map[string]any{
						"name": "str_artist",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 40,
					},
					map[string]any{
						"name": "str_artist_alternate",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 41,
					},
					map[string]any{
						"name": "str_artist_banner",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 42,
					},
					map[string]any{
						"name": "str_artist_clearart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 43,
					},
					map[string]any{
						"name": "str_artist_cutout",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 44,
					},
					map[string]any{
						"name": "str_artist_fanart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 45,
					},
					map[string]any{
						"name": "str_artist_fanart2",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 46,
					},
					map[string]any{
						"name": "str_artist_fanart3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 47,
					},
					map[string]any{
						"name": "str_artist_fanart4",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 48,
					},
					map[string]any{
						"name": "str_artist_logo",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 49,
					},
					map[string]any{
						"name": "str_artist_stripped",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 50,
					},
					map[string]any{
						"name": "str_artist_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 51,
					},
					map[string]any{
						"name": "str_artist_wide_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 52,
					},
					map[string]any{
						"name": "str_bbc_review_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 53,
					},
					map[string]any{
						"name": "str_biography_en",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 54,
					},
					map[string]any{
						"name": "str_country",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 55,
					},
					map[string]any{
						"name": "str_country_code",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 56,
					},
					map[string]any{
						"name": "str_description_en",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 57,
					},
					map[string]any{
						"name": "str_disbanded",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 58,
					},
					map[string]any{
						"name": "str_discogs_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 59,
					},
					map[string]any{
						"name": "str_facebook",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 60,
					},
					map[string]any{
						"name": "str_gender",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 61,
					},
					map[string]any{
						"name": "str_genius_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 62,
					},
					map[string]any{
						"name": "str_genre",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 63,
					},
					map[string]any{
						"name": "str_isn_icode",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 64,
					},
					map[string]any{
						"name": "str_itunes_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 65,
					},
					map[string]any{
						"name": "str_label",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 66,
					},
					map[string]any{
						"name": "str_last_fm_chart",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 67,
					},
					map[string]any{
						"name": "str_location",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 68,
					},
					map[string]any{
						"name": "str_locked",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 69,
					},
					map[string]any{
						"name": "str_lyric_wiki_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 70,
					},
					map[string]any{
						"name": "str_mood",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 71,
					},
					map[string]any{
						"name": "str_music_brainz_album_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 72,
					},
					map[string]any{
						"name": "str_music_brainz_artist_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 73,
					},
					map[string]any{
						"name": "str_music_brainz_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 74,
					},
					map[string]any{
						"name": "str_music_moz_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 75,
					},
					map[string]any{
						"name": "str_music_vid",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 76,
					},
					map[string]any{
						"name": "str_music_vid_company",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 77,
					},
					map[string]any{
						"name": "str_music_vid_director",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 78,
					},
					map[string]any{
						"name": "str_music_vid_screen1",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 79,
					},
					map[string]any{
						"name": "str_music_vid_screen2",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 80,
					},
					map[string]any{
						"name": "str_music_vid_screen3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 81,
					},
					map[string]any{
						"name": "str_rate_your_music_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 82,
					},
					map[string]any{
						"name": "str_release_format",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 83,
					},
					map[string]any{
						"name": "str_review",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 84,
					},
					map[string]any{
						"name": "str_speed",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 85,
					},
					map[string]any{
						"name": "str_style",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 86,
					},
					map[string]any{
						"name": "str_theme",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 87,
					},
					map[string]any{
						"name": "str_track",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 88,
					},
					map[string]any{
						"name": "str_track3x3",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 89,
					},
					map[string]any{
						"name": "str_track_lyric",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 90,
					},
					map[string]any{
						"name": "str_track_thumb",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 91,
					},
					map[string]any{
						"name": "str_twitter",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 92,
					},
					map[string]any{
						"name": "str_website",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 93,
					},
					map[string]any{
						"name": "str_wikidata_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 94,
					},
					map[string]any{
						"name": "str_wikipedia_id",
						"req": false,
						"type": "`$STRING`",
						"active": true,
						"index$": 95,
					},
				},
				"name": "v1_search",
				"op": map[string]any{
					"list": map[string]any{
						"name": "list",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "Homework",
											"kind": "query",
											"name": "a",
											"orig": "a",
											"reqd": false,
											"type": "`$STRING`",
											"active": true,
										},
										map[string]any{
											"example": "daft_punk",
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/searchalbum.php",
								"parts": []any{
									"{api_key}",
									"searchalbum.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"a",
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "coldplay",
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
										map[string]any{
											"example": "yellow",
											"kind": "query",
											"name": "t",
											"orig": "t",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/searchtrack.php",
								"parts": []any{
									"{api_key}",
									"searchtrack.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
										"t",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/discography.php",
								"parts": []any{
									"{api_key}",
									"discography.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "123",
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"example": "coldplay",
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/search.php",
								"parts": []any{
									"{api_key}",
									"search.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 3,
							},
						},
						"input": "data",
						"key$": "list",
					},
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"kind": "param",
											"name": "api_key",
											"orig": "api_key",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/{apiKey}/discography-mb.php",
								"parts": []any{
									"{api_key}",
									"discography-mb.php",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"apiKey": "api_key",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"api_key",
										"s",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{},
				},
			},
			"v2_list": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "album",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 0,
					},
				},
				"name": "v2_list",
				"op": map[string]any{
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": 111239,
											"kind": "param",
											"name": "id_artist",
											"orig": "id_artist",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/list/discography/{idArtist}",
								"parts": []any{
									"list",
									"discography",
									"{id_artist}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"idArtist": "id_artist",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"id_artist",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{
						[]any{
							"discography",
						},
					},
				},
			},
			"v2_lookup": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "album",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 0,
					},
					map[string]any{
						"name": "artist",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 1,
					},
					map[string]any{
						"name": "track",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 2,
					},
				},
				"name": "v2_lookup",
				"op": map[string]any{
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": 2109615,
											"kind": "param",
											"name": "id_album",
											"orig": "id_album",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/album/{idAlbum}",
								"parts": []any{
									"lookup",
									"album",
									"{id_album}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"idAlbum": "id_album",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"id_album",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": 111239,
											"kind": "param",
											"name": "id_artist",
											"orig": "id_artist",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/artist/{idArtist}",
								"parts": []any{
									"lookup",
									"artist",
									"{id_artist}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"idArtist": "id_artist",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"id_artist",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": 32724183,
											"kind": "param",
											"name": "id_track",
											"orig": "id_track",
											"reqd": true,
											"type": "`$INTEGER`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/track/{idTrack}",
								"parts": []any{
									"lookup",
									"track",
									"{id_track}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"idTrack": "id_track",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"id_track",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "1dc4c347-a1db-32aa-b14f-bc9cc507b843",
											"kind": "param",
											"name": "music_brainz_id",
											"orig": "music_brainz_id",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/album_mb/{musicBrainzId}",
								"parts": []any{
									"lookup",
									"album_mb",
									"{music_brainz_id}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"musicBrainzId": "music_brainz_id",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"music_brainz_id",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 3,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
											"kind": "param",
											"name": "music_brainz_id",
											"orig": "music_brainz_id",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/artist_mb/{musicBrainzId}",
								"parts": []any{
									"lookup",
									"artist_mb",
									"{music_brainz_id}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"musicBrainzId": "music_brainz_id",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"music_brainz_id",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 4,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "50369905-68ca-48d2-912d-b37330ff7dc3",
											"kind": "param",
											"name": "music_brainz_id",
											"orig": "music_brainz_id",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/lookup/track_mb/{musicBrainzId}",
								"parts": []any{
									"lookup",
									"track_mb",
									"{music_brainz_id}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"musicBrainzId": "music_brainz_id",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"music_brainz_id",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 5,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{
						[]any{
							"album",
						},
						[]any{
							"album_mb",
						},
						[]any{
							"artist",
						},
						[]any{
							"artist_mb",
						},
						[]any{
							"track",
						},
						[]any{
							"track_mb",
						},
					},
				},
			},
			"v2_search": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "album",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 0,
					},
					map[string]any{
						"name": "artist",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 1,
					},
					map[string]any{
						"name": "track",
						"req": false,
						"type": "`$ARRAY`",
						"active": true,
						"index$": 2,
					},
				},
				"name": "v2_search",
				"op": map[string]any{
					"load": map[string]any{
						"name": "load",
						"points": []any{
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "parachutes",
											"kind": "param",
											"name": "album_name",
											"orig": "album_name",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/search/album/{albumName}",
								"parts": []any{
									"search",
									"album",
									"{album_name}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"albumName": "album_name",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"album_name",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 0,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "coldplay",
											"kind": "param",
											"name": "artist_name",
											"orig": "artist_name",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/search/artist/{artistName}",
								"parts": []any{
									"search",
									"artist",
									"{artist_name}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"artistName": "artist_name",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"artist_name",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 1,
							},
							map[string]any{
								"args": map[string]any{
									"params": []any{
										map[string]any{
											"example": "yellow",
											"kind": "param",
											"name": "track_name",
											"orig": "track_name",
											"reqd": true,
											"type": "`$STRING`",
											"active": true,
										},
									},
								},
								"method": "GET",
								"orig": "/search/track/{trackName}",
								"parts": []any{
									"search",
									"track",
									"{track_name}",
								},
								"rename": map[string]any{
									"param": map[string]any{
										"trackName": "track_name",
									},
								},
								"select": map[string]any{
									"exist": []any{
										"track_name",
									},
								},
								"transform": map[string]any{
									"req": "`reqdata`",
									"res": "`body`",
								},
								"active": true,
								"index$": 2,
							},
						},
						"input": "data",
						"key$": "load",
					},
				},
				"relations": map[string]any{
					"ancestors": []any{
						[]any{
							"album",
						},
						[]any{
							"artist",
						},
						[]any{
							"track",
						},
					},
				},
			},
		},
	}
}

func makeFeature(name string) Feature {
	switch name {
	case "test":
		if NewTestFeatureFunc != nil {
			return NewTestFeatureFunc()
		}
	default:
		if NewBaseFeatureFunc != nil {
			return NewBaseFeatureFunc()
		}
	}
	return nil
}
