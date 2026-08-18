package core

import (
	"sync"
)

// MakeConfig builds a fresh, fully materialised config map. Every call
// rebuilds the whole structure, so prefer SharedConfig unless you need a
// private copy you intend to mutate.
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
				"prefix": "",
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
						"name": "idAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "trending",
						"type": "`$ARRAY`",
					},
				},
				"name": "v1_list",
				"op": map[string]any{
					"list": map[string]any{
						"input": "data",
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
										},
										map[string]any{
											"kind": "query",
											"name": "format",
											"orig": "format",
											"reqd": true,
											"type": "`$STRING`",
										},
										map[string]any{
											"kind": "query",
											"name": "type",
											"orig": "type",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.trending`",
								},
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$INTEGER`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.mvids`",
								},
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
										},
									},
								},
								"kind": "http",
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
									"res": "`body.track`",
								},
							},
						},
					},
					"load": map[string]any{
						"input": "data",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "format",
											"orig": "format",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
							},
						},
					},
				},
				"relations": map[string]any{
					"ancestors": []any{},
				},
			},
			"v1_lookup": map[string]any{
				"fields": []any{
					map[string]any{
						"name": "idAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLabel",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intBornYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCharted",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDiedYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intFormedYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMembers",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intSales",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intYearReleased",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DCase",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFace",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFlat",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumCDart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumSpine",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumStripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbBack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbHQ",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAllMusicID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAmazonID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistBanner",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistClearart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistCutout",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart4",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistLogo",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistStripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistWideThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBBCReviewID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBiographyEN",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountry",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountryCode",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDisbanded",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDiscogsID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strFacebook",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGender",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGeniusID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strISNIcode",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strItunesID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLabel",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLastFMChart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocation",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLyricWikiID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicMozID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strRateYourMusicID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReleaseFormat",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReview",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strSpeed",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTwitter",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWebsite",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikidataID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikipediaID",
						"type": "`$STRING`",
					},
				},
				"name": "v1_lookup",
				"op": map[string]any{
					"list": map[string]any{
						"input": "data",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "h",
											"orig": "h",
											"type": "`$INTEGER`",
										},
										map[string]any{
											"kind": "query",
											"name": "m",
											"orig": "m",
											"type": "`$INTEGER`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.track`",
								},
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"type": "`$INTEGER`",
										},
										map[string]any{
											"example": 2115888,
											"kind": "query",
											"name": "m",
											"orig": "m",
											"type": "`$INTEGER`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.album`",
								},
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
										},
									},
								},
								"kind": "http",
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
									"res": "`body.artists`",
								},
							},
						},
					},
					"load": map[string]any{
						"input": "data",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$INTEGER`",
										},
									},
								},
								"kind": "http",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "i",
											"orig": "i",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
							},
						},
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
						"type": "`$ARRAY`",
					},
					map[string]any{
						"name": "idAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLabel",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intBornYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCharted",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDiedYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intFormedYear",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMembers",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intSales",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intYearReleased",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DCase",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFace",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFlat",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumCDart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumSpine",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumStripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbBack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbHQ",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAllMusicID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAmazonID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistBanner",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistClearart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistCutout",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart4",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistLogo",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistStripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistWideThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBBCReviewID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBiographyEN",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountry",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountryCode",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDisbanded",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDiscogsID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strFacebook",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGender",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGeniusID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strISNIcode",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strItunesID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLabel",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLastFMChart",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocation",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLyricWikiID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicMozID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strRateYourMusicID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReleaseFormat",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReview",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strSpeed",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTwitter",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWebsite",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikidataID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikipediaID",
						"type": "`$STRING`",
					},
				},
				"name": "v1_search",
				"op": map[string]any{
					"list": map[string]any{
						"input": "data",
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
										},
									},
									"query": []any{
										map[string]any{
											"example": "Homework",
											"kind": "query",
											"name": "a",
											"orig": "a",
											"type": "`$STRING`",
										},
										map[string]any{
											"example": "daft_punk",
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.album`",
								},
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
										},
										map[string]any{
											"example": "yellow",
											"kind": "query",
											"name": "t",
											"orig": "t",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.track`",
								},
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
									"res": "`body.album`",
								},
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
										},
									},
								},
								"kind": "http",
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
									"res": "`body.artists`",
								},
							},
						},
					},
					"load": map[string]any{
						"input": "data",
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
										},
									},
									"query": []any{
										map[string]any{
											"kind": "query",
											"name": "s",
											"orig": "s",
											"reqd": true,
											"type": "`$STRING`",
										},
									},
								},
								"kind": "http",
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
							},
						},
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
						"type": "`$ARRAY`",
					},
				},
				"name": "v2_list",
				"op": map[string]any{
					"load": map[string]any{
						"input": "data",
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
										},
									},
								},
								"kind": "http",
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
							},
						},
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
						"type": "`$ARRAY`",
					},
					map[string]any{
						"name": "artists",
						"type": "`$ARRAY`",
					},
					map[string]any{
						"name": "track",
						"type": "`$ARRAY`",
					},
				},
				"name": "v2_lookup",
				"op": map[string]any{
					"load": map[string]any{
						"input": "data",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
							},
						},
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
						"type": "`$ARRAY`",
					},
					map[string]any{
						"name": "artists",
						"type": "`$ARRAY`",
					},
					map[string]any{
						"name": "track",
						"type": "`$ARRAY`",
					},
				},
				"name": "v2_search",
				"op": map[string]any{
					"load": map[string]any{
						"input": "data",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
										},
									},
								},
								"kind": "http",
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
							},
						},
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

var (
	sharedConfigOnce sync.Once
	sharedConfigVal  map[string]any
)

// SharedConfig returns the process-wide config, built once on first use.
// The SDK reads the config on every request and never writes to it, so one
// instance is shared by every client rather than rebuilt per client.
//
// The returned map is shared: treat it as read-only. Callers that need to
// mutate should use MakeConfig, which always returns a fresh copy.
func SharedConfig() map[string]any {
	sharedConfigOnce.Do(func() {
		sharedConfigVal = MakeConfig()
	})
	return sharedConfigVal
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
