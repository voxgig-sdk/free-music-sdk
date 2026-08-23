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
			"slug": "free-music",
			"version": "0.0.1",
			"target": "go",
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
						"short": "Album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"short": "Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"short": "IMVDB ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"short": "Lyrics ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"short": "Unique track ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"short": "CD number",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"short": "Track duration in milliseconds",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"short": "Number of loves/likes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"short": "Music video comment count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"short": "Music video dislike count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"short": "Music video favorite count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"short": "Music video like count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"short": "Music video view count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"short": "Track score/rating",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"short": "Number of score votes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"short": "Total listener count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"short": "Total play count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"short": "Track number on album",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"short": "Album name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"short": "Artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"short": "Alternative artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"short": "Track description in English",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"short": "Musical genre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"short": "Lock status",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"short": "Track mood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"short": "MusicBrainz Album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"short": "MusicBrainz Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"short": "MusicBrainz Recording ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"short": "Music video URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"short": "Music video production company",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"short": "Music video director",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"short": "Music video screenshot 1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"short": "Music video screenshot 2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"short": "Music video screenshot 3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"short": "Musical style",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"short": "Track theme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"short": "Track name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"short": "3x3 track image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"short": "Track lyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"short": "Track thumbnail URL",
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
						"short": "Album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"short": "Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"short": "IMVDB ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLabel",
						"short": "Label ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"short": "Lyrics ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"short": "Unique track ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intBornYear",
						"short": "Birth year (for solo artists)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"short": "CD number",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCharted",
						"short": "Chart position",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDiedYear",
						"short": "Death year (if applicable)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"short": "Track duration in milliseconds",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intFormedYear",
						"short": "Year the artist was formed",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"short": "Number of loves/likes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMembers",
						"short": "Number of band members",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"short": "Music video comment count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"short": "Music video dislike count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"short": "Music video favorite count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"short": "Music video like count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"short": "Music video view count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intSales",
						"short": "Sales figures",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"short": "Track score/rating",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"short": "Number of score votes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"short": "Total listener count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"short": "Total play count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"short": "Track number on album",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intYearReleased",
						"short": "Release year",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"short": "Album name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DCase",
						"short": "3D case image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFace",
						"short": "3D face image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFlat",
						"short": "3D flat image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DThumb",
						"short": "3D thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumCDart",
						"short": "CD art URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumSpine",
						"short": "Album spine image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumStripped",
						"short": "Album name stripped of special characters",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumb",
						"short": "Album thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbBack",
						"short": "Album back cover URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbHQ",
						"short": "High quality album thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAllMusicID",
						"short": "AllMusic ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAmazonID",
						"short": "Amazon ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"short": "Artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"short": "Alternative artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistBanner",
						"short": "Banner image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistClearart",
						"short": "Clear art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistCutout",
						"short": "Cutout image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart",
						"short": "Fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart2",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart3",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart4",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistLogo",
						"short": "Logo image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistStripped",
						"short": "Artist name stripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistThumb",
						"short": "Thumbnail image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistWideThumb",
						"short": "Wide thumbnail image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBBCReviewID",
						"short": "BBC Review ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBiographyEN",
						"short": "Biography in English",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountry",
						"short": "Country of origin",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountryCode",
						"short": "Country code",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"short": "Track description in English",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDisbanded",
						"short": "Disbandment status",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDiscogsID",
						"short": "Discogs ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strFacebook",
						"short": "Facebook URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGender",
						"short": "Gender",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGeniusID",
						"short": "Genius ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"short": "Musical genre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strISNIcode",
						"short": "ISNI code",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strItunesID",
						"short": "iTunes ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLabel",
						"short": "Record label",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLastFMChart",
						"short": "Last.fm chart URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocation",
						"short": "Recording location",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"short": "Lock status",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLyricWikiID",
						"short": "LyricWiki ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"short": "Track mood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"short": "MusicBrainz Album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"short": "MusicBrainz Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"short": "MusicBrainz Recording ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicMozID",
						"short": "MusicMoz ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"short": "Music video URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"short": "Music video production company",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"short": "Music video director",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"short": "Music video screenshot 1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"short": "Music video screenshot 2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"short": "Music video screenshot 3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strRateYourMusicID",
						"short": "Rate Your Music ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReleaseFormat",
						"short": "Release format (CD, Vinyl, etc.)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReview",
						"short": "Album review",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strSpeed",
						"short": "Album speed/tempo",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"short": "Musical style",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"short": "Track theme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"short": "Track name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"short": "3x3 track image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"short": "Track lyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"short": "Track thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTwitter",
						"short": "Twitter handle",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWebsite",
						"short": "Official website URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikidataID",
						"short": "Wikidata ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikipediaID",
						"short": "Wikipedia ID",
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
						"short": "Unique album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idArtist",
						"short": "Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idIMVDB",
						"short": "IMVDB ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLabel",
						"short": "Label ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idLyric",
						"short": "Lyrics ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "idTrack",
						"short": "Unique track ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intBornYear",
						"short": "Birth year (for solo artists)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCD",
						"short": "CD number",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intCharted",
						"short": "Chart position",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDiedYear",
						"short": "Death year (if applicable)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intDuration",
						"short": "Track duration in milliseconds",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intFormedYear",
						"short": "Year the artist was formed",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intLoved",
						"short": "Number of loves/likes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMembers",
						"short": "Number of band members",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidComments",
						"short": "Music video comment count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidDislikes",
						"short": "Music video dislike count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidFavorites",
						"short": "Music video favorite count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidLikes",
						"short": "Music video like count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intMusicVidViews",
						"short": "Music video view count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intSales",
						"short": "Sales figures",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScore",
						"short": "Album score/rating",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intScoreVotes",
						"short": "Number of score votes",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalListeners",
						"short": "Total listener count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTotalPlays",
						"short": "Total play count",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intTrackNumber",
						"short": "Track number on album",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "intYearReleased",
						"short": "Release year",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum",
						"short": "Album name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DCase",
						"short": "3D case image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFace",
						"short": "3D face image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DFlat",
						"short": "3D flat image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbum3DThumb",
						"short": "3D thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumCDart",
						"short": "CD art URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumSpine",
						"short": "Album spine image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumStripped",
						"short": "Album name stripped of special characters",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumb",
						"short": "Album thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbBack",
						"short": "Album back cover URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAlbumThumbHQ",
						"short": "High quality album thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAllMusicID",
						"short": "AllMusic ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strAmazonID",
						"short": "Amazon ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtist",
						"short": "Artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistAlternate",
						"short": "Alternative artist name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistBanner",
						"short": "Banner image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistClearart",
						"short": "Clear art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistCutout",
						"short": "Cutout image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart",
						"short": "Fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart2",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart3",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistFanart4",
						"short": "Additional fan art image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistLogo",
						"short": "Logo image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistStripped",
						"short": "Artist name stripped",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistThumb",
						"short": "Thumbnail image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strArtistWideThumb",
						"short": "Wide thumbnail image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBBCReviewID",
						"short": "BBC Review ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strBiographyEN",
						"short": "Biography in English",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountry",
						"short": "Country of origin",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strCountryCode",
						"short": "Country code",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDescriptionEN",
						"short": "Album description in English",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDisbanded",
						"short": "Disbandment status",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strDiscogsID",
						"short": "Discogs ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strFacebook",
						"short": "Facebook URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGender",
						"short": "Gender",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGeniusID",
						"short": "Genius ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strGenre",
						"short": "Musical genre",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strISNIcode",
						"short": "ISNI code",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strItunesID",
						"short": "iTunes ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLabel",
						"short": "Record label",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLastFMChart",
						"short": "Last.fm chart URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocation",
						"short": "Recording location",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLocked",
						"short": "Lock status",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strLyricWikiID",
						"short": "LyricWiki ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMood",
						"short": "Album mood",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzAlbumID",
						"short": "MusicBrainz Album ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzArtistID",
						"short": "MusicBrainz Artist ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicBrainzID",
						"short": "MusicBrainz Release Group ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicMozID",
						"short": "MusicMoz ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVid",
						"short": "Music video URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidCompany",
						"short": "Music video production company",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidDirector",
						"short": "Music video director",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen1",
						"short": "Music video screenshot 1",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen2",
						"short": "Music video screenshot 2",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strMusicVidScreen3",
						"short": "Music video screenshot 3",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strRateYourMusicID",
						"short": "Rate Your Music ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReleaseFormat",
						"short": "Release format (CD, Vinyl, etc.)",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strReview",
						"short": "Album review",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strSpeed",
						"short": "Album speed/tempo",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strStyle",
						"short": "Musical style",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTheme",
						"short": "Album theme",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack",
						"short": "Track name",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrack3x3",
						"short": "3x3 track image URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackLyrics",
						"short": "Track lyrics",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTrackThumb",
						"short": "Track thumbnail URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strTwitter",
						"short": "Twitter handle",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWebsite",
						"short": "Official website URL",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikidataID",
						"short": "Wikidata ID",
						"type": "`$STRING`",
					},
					map[string]any{
						"name": "strWikipediaID",
						"short": "Wikipedia ID",
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
