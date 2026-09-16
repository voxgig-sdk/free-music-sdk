

import Path from 'node:path'
import * as Fs from 'node:fs'

import { test, describe, afterEach } from 'node:test'
import assert from 'node:assert'
import { createLiveTransport } from '../../live-runner'
import { runLiveEntity } from '../../live-entity'


import { FreeMusicSDK, BaseFeature, stdutil } from '../../..'

import {
  envOverride,
  liveClientOptions,
  liveDelay,
  loadEnvLocal,
  makeCtrl,
  makeMatch,
  makeReqdata,
  makeStepData,
  makeValid,
  maybeSkipControl,
} from '../../utility'


// AFTER the imports on purpose: TypeScript hoists `import` above any
// statement in the emitted CommonJS, so a loader placed above them would
// run only after every imported module had already been evaluated - and
// anything reading process.env at module scope would miss these values.
loadEnvLocal(__dirname + '/../../../.env.local')


describe('V1ListEntity', async () => {

  // Per-test live pacing. Delay is read from sdk-test-control.json's
  // `test.live.delayMs`; only sleeps when FREE_MUSIC_TEST_LIVE=TRUE.
  afterEach(liveDelay('FREE_MUSIC_TEST_LIVE'))

  test('instance', async () => {
    const testsdk = FreeMusicSDK.test()
    const ent = testsdk.V1List()
    assert(null != ent)
  })


  test('basic', async (t) => {

    const live = 'TRUE' === process.env.FREE_MUSIC_TEST_LIVE
    for (const op of ['list', 'load']) {
      if (!live && maybeSkipControl(t, 'entityOp', 'v1_list.' + op, live)) return
    }

    
    const setup = basicSetup()
    if (setup.live) {
      return runLiveEntity(setup, {"active":true,"alias":{"field":{}},"fields":[{"active":true,"name":"idAlbum","req":false,"short":"Album ID","type":"`$STRING`","index$":0},{"active":true,"name":"idArtist","req":false,"short":"Artist ID","type":"`$STRING`","index$":1},{"active":true,"name":"idIMVDB","req":false,"short":"IMVDB ID","type":"`$STRING`","index$":2},{"active":true,"name":"idLyric","req":false,"short":"Lyrics ID","type":"`$STRING`","index$":3},{"active":true,"name":"idTrack","req":false,"short":"Unique track ID","type":"`$STRING`","index$":4},{"active":true,"name":"intCD","req":false,"short":"CD number","type":"`$STRING`","index$":5},{"active":true,"name":"intDuration","req":false,"short":"Track duration in milliseconds","type":"`$STRING`","index$":6},{"active":true,"name":"intLoved","req":false,"short":"Number of loves/likes","type":"`$STRING`","index$":7},{"active":true,"name":"intMusicVidComments","req":false,"short":"Music video comment count","type":"`$STRING`","index$":8},{"active":true,"name":"intMusicVidDislikes","req":false,"short":"Music video dislike count","type":"`$STRING`","index$":9},{"active":true,"name":"intMusicVidFavorites","req":false,"short":"Music video favorite count","type":"`$STRING`","index$":10},{"active":true,"name":"intMusicVidLikes","req":false,"short":"Music video like count","type":"`$STRING`","index$":11},{"active":true,"name":"intMusicVidViews","req":false,"short":"Music video view count","type":"`$STRING`","index$":12},{"active":true,"name":"intScore","req":false,"short":"Track score/rating","type":"`$STRING`","index$":13},{"active":true,"name":"intScoreVotes","req":false,"short":"Number of score votes","type":"`$STRING`","index$":14},{"active":true,"name":"intTotalListeners","req":false,"short":"Total listener count","type":"`$STRING`","index$":15},{"active":true,"name":"intTotalPlays","req":false,"short":"Total play count","type":"`$STRING`","index$":16},{"active":true,"name":"intTrackNumber","req":false,"short":"Track number on album","type":"`$STRING`","index$":17},{"active":true,"name":"strAlbum","req":false,"short":"Album name","type":"`$STRING`","index$":18},{"active":true,"name":"strArtist","req":false,"short":"Artist name","type":"`$STRING`","index$":19},{"active":true,"name":"strArtistAlternate","req":false,"short":"Alternative artist name","type":"`$STRING`","index$":20},{"active":true,"name":"strDescriptionEN","req":false,"short":"Track description in English","type":"`$STRING`","index$":21},{"active":true,"name":"strGenre","req":false,"short":"Musical genre","type":"`$STRING`","index$":22},{"active":true,"name":"strLocked","req":false,"short":"Lock status","type":"`$STRING`","index$":23},{"active":true,"name":"strMood","req":false,"short":"Track mood","type":"`$STRING`","index$":24},{"active":true,"name":"strMusicBrainzAlbumID","req":false,"short":"MusicBrainz Album ID","type":"`$STRING`","index$":25},{"active":true,"name":"strMusicBrainzArtistID","req":false,"short":"MusicBrainz Artist ID","type":"`$STRING`","index$":26},{"active":true,"name":"strMusicBrainzID","req":false,"short":"MusicBrainz Recording ID","type":"`$STRING`","index$":27},{"active":true,"name":"strMusicVid","req":false,"short":"Music video URL","type":"`$STRING`","index$":28},{"active":true,"name":"strMusicVidCompany","req":false,"short":"Music video production company","type":"`$STRING`","index$":29},{"active":true,"name":"strMusicVidDirector","req":false,"short":"Music video director","type":"`$STRING`","index$":30},{"active":true,"name":"strMusicVidScreen1","req":false,"short":"Music video screenshot 1","type":"`$STRING`","index$":31},{"active":true,"name":"strMusicVidScreen2","req":false,"short":"Music video screenshot 2","type":"`$STRING`","index$":32},{"active":true,"name":"strMusicVidScreen3","req":false,"short":"Music video screenshot 3","type":"`$STRING`","index$":33},{"active":true,"name":"strStyle","req":false,"short":"Musical style","type":"`$STRING`","index$":34},{"active":true,"name":"strTheme","req":false,"short":"Track theme","type":"`$STRING`","index$":35},{"active":true,"name":"strTrack","req":false,"short":"Track name","type":"`$STRING`","index$":36},{"active":true,"name":"strTrack3x3","req":false,"short":"3x3 track image URL","type":"`$STRING`","index$":37},{"active":true,"name":"strTrackLyrics","req":false,"short":"Track lyrics","type":"`$STRING`","index$":38},{"active":true,"name":"strTrackThumb","req":false,"short":"Track thumbnail URL","type":"`$STRING`","index$":39},{"active":true,"name":"trending","req":false,"type":"`$ARRAY`","index$":40}],"name":"v1_list","op":{"list":{"input":"data","name":"list","points":[{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"example":"us","kind":"query","name":"country","orig":"country","reqd":true,"type":"`$STRING`","index$":0},{"active":true,"kind":"query","name":"format","orig":"format","reqd":true,"type":"`$STRING`","index$":1},{"active":true,"kind":"query","name":"type","orig":"type","reqd":true,"type":"`$STRING`","index$":2}]},"contract":{"id":"GET /{apiKey}/trending.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"Country code\",\"example\":\"us\",\"in\":\"query\",\"name\":\"country\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"Chart type\",\"in\":\"query\",\"name\":\"type\",\"required\":true,\"schema\":{\"enum\":[\"itunes\"],\"type\":\"string\"}},{\"description\":\"Format type\",\"in\":\"query\",\"name\":\"format\",\"required\":true,\"schema\":{\"enum\":[\"albums\",\"singles\"],\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"trending\":{\"items\":{\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/trending.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"trending.php"}],"select":{"exist":["api_key","country","format","type"]},"transform":{"req":"`reqdata`","res":"`body.trending`"},"index$":0},{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"kind":"query","name":"i","orig":"i","reqd":true,"type":"`$INTEGER`","index$":0}]},"contract":{"id":"GET /{apiKey}/mvid.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"Artist ID\",\"in\":\"query\",\"name\":\"i\",\"required\":true,\"schema\":{\"type\":\"integer\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"mvids\":{\"items\":{\"properties\":{\"idAlbum\":{\"type\":\"string\"},\"idArtist\":{\"type\":\"string\"},\"idTrack\":{\"type\":\"string\"},\"strDescriptionEN\":{\"type\":\"string\"},\"strMusicVid\":{\"type\":\"string\"},\"strTrack\":{\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/mvid.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"mvid.php"}],"select":{"exist":["api_key","i"]},"transform":{"req":"`reqdata`","res":"`body.mvids`"},"index$":1},{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"example":"coldplay","kind":"query","name":"s","orig":"s","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /{apiKey}/track-top10.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"Artist name\",\"example\":\"coldplay\",\"in\":\"query\",\"name\":\"s\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"track\":{\"items\":{\"properties\":{\"idAlbum\":{\"description\":\"Album ID\",\"type\":\"string\"},\"idArtist\":{\"description\":\"Artist ID\",\"type\":\"string\"},\"idIMVDB\":{\"description\":\"IMVDB ID\",\"type\":\"string\"},\"idLyric\":{\"description\":\"Lyrics ID\",\"type\":\"string\"},\"idTrack\":{\"description\":\"Unique track ID\",\"type\":\"string\"},\"intCD\":{\"description\":\"CD number\",\"type\":\"string\"},\"intDuration\":{\"description\":\"Track duration in milliseconds\",\"type\":\"string\"},\"intLoved\":{\"description\":\"Number of loves/likes\",\"type\":\"string\"},\"intMusicVidComments\":{\"description\":\"Music video comment count\",\"type\":\"string\"},\"intMusicVidDislikes\":{\"description\":\"Music video dislike count\",\"type\":\"string\"},\"intMusicVidFavorites\":{\"description\":\"Music video favorite count\",\"type\":\"string\"},\"intMusicVidLikes\":{\"description\":\"Music video like count\",\"type\":\"string\"},\"intMusicVidViews\":{\"description\":\"Music video view count\",\"type\":\"string\"},\"intScore\":{\"description\":\"Track score/rating\",\"type\":\"string\"},\"intScoreVotes\":{\"description\":\"Number of score votes\",\"type\":\"string\"},\"intTotalListeners\":{\"description\":\"Total listener count\",\"type\":\"string\"},\"intTotalPlays\":{\"description\":\"Total play count\",\"type\":\"string\"},\"intTrackNumber\":{\"description\":\"Track number on album\",\"type\":\"string\"},\"strAlbum\":{\"description\":\"Album name\",\"type\":\"string\"},\"strArtist\":{\"description\":\"Artist name\",\"type\":\"string\"},\"strArtistAlternate\":{\"description\":\"Alternative artist name\",\"type\":\"string\"},\"strDescriptionEN\":{\"description\":\"Track description in English\",\"type\":\"string\"},\"strGenre\":{\"description\":\"Musical genre\",\"type\":\"string\"},\"strLocked\":{\"description\":\"Lock status\",\"type\":\"string\"},\"strMood\":{\"description\":\"Track mood\",\"type\":\"string\"},\"strMusicBrainzAlbumID\":{\"description\":\"MusicBrainz Album ID\",\"type\":\"string\"},\"strMusicBrainzArtistID\":{\"description\":\"MusicBrainz Artist ID\",\"type\":\"string\"},\"strMusicBrainzID\":{\"description\":\"MusicBrainz Recording ID\",\"type\":\"string\"},\"strMusicVid\":{\"description\":\"Music video URL\",\"type\":\"string\"},\"strMusicVidCompany\":{\"description\":\"Music video production company\",\"type\":\"string\"},\"strMusicVidDirector\":{\"description\":\"Music video director\",\"type\":\"string\"},\"strMusicVidScreen1\":{\"description\":\"Music video screenshot 1\",\"type\":\"string\"},\"strMusicVidScreen2\":{\"description\":\"Music video screenshot 2\",\"type\":\"string\"},\"strMusicVidScreen3\":{\"description\":\"Music video screenshot 3\",\"type\":\"string\"},\"strStyle\":{\"description\":\"Musical style\",\"type\":\"string\"},\"strTheme\":{\"description\":\"Track theme\",\"type\":\"string\"},\"strTrack\":{\"description\":\"Track name\",\"type\":\"string\"},\"strTrack3x3\":{\"description\":\"3x3 track image URL\",\"type\":\"string\"},\"strTrackLyrics\":{\"description\":\"Track lyrics\",\"type\":\"string\"},\"strTrackThumb\":{\"description\":\"Track thumbnail URL\",\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/track-top10.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"track-top10.php"}],"select":{"exist":["api_key","s"]},"transform":{"req":"`reqdata`","res":"`body.track`"},"index$":2}],"key$":"list"},"load":{"input":"data","name":"load","points":[{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"kind":"query","name":"format","orig":"format","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /{apiKey}/mostloved.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"Format type (track or album)\",\"in\":\"query\",\"name\":\"format\",\"required\":true,\"schema\":{\"enum\":[\"track\",\"album\"],\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/mostloved.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"mostloved.php"}],"select":{"exist":["api_key","format"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":0},{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"kind":"query","name":"i","orig":"i","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /{apiKey}/mvid-mb.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"MusicBrainz Artist ID\",\"in\":\"query\",\"name\":\"i\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/mvid-mb.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"mvid-mb.php"}],"select":{"exist":["api_key","i"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":1},{"active":true,"args":{"params":[{"active":true,"kind":"param","name":"api_key","orig":"api_key","reqd":true,"type":"`$STRING`","index$":0}],"query":[{"active":true,"kind":"query","name":"s","orig":"s","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /{apiKey}/track-top10-mb.php","json":"{\"parameters\":[{\"in\":\"path\",\"name\":\"apiKey\",\"required\":true,\"schema\":{\"type\":\"string\"}},{\"description\":\"MusicBrainz Artist ID\",\"in\":\"query\",\"name\":\"s\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"}},\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"unspecified\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/{apiKey}/track-top10-mb.php","rename":{"param":{"apiKey":"api_key"}},"segments":[{"var":"api_key"},{"lit":"track-top10-mb.php"}],"select":{"exist":["api_key","s"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":2}],"key$":"load"}},"relations":{"ancestors":[]},"key$":"v1_list","name__orig":"v1_list","Name":"V1List","name_":"v1_list","name-":"v1-list","NAME":"V1_LIST","index$":0}, {"active":true,"entity":"v1_list","key$":"BasicV1ListFlow","kind":"basic","name":"BasicV1ListFlow","param":{},"step":[{"active":true,"data":{},"input":{},"match":{"api_key":"api_key01"},"op":"list","spec":[],"valid":[{"apply":"ItemExists","def":{"ref":"v1_list_ref01"}}],"index$":0},{"active":true,"data":{},"input":{"ref":"v1_list_ref01","srcdatavar":"v1_list_ref01_data","suffix":"_dt0"},"match":{"id":"v1_list01"},"op":"load","spec":[],"valid":[{"apply":"TextFieldMark","def":{"mark":"Mark01-v1_list_ref01"}}],"index$":1}]}, 'V1List')
    }
    const client = setup.client
    const struct = setup.struct

    const isempty = struct.isempty
    const select = struct.select

    let v1_list_ref01_data = Object.values(setup.data.existing.v1_list)[0] as any

    // LIST
    const v1_list_ref01_ent = client.V1List()
    const v1_list_ref01_match: any = {}
    v1_list_ref01_match['api_key'] = setup.idmap['api_key01']

    const v1_list_ref01_list = (await v1_list_ref01_ent.list(v1_list_ref01_match)).map((e: any) => e.data())



  })
})



function basicSetup(extra?: any) {
  // TODO: fix test def options
  const options: any = {} // null

  // TODO: needs test utility to resolve path
  const entityDataFile =
    Path.resolve(__dirname, 
      '../../../../.sdk/test/entity/v1_list/V1ListTestData.json')

  // TODO: file ready util needed?
  const entityDataSource = Fs.readFileSync(entityDataFile).toString('utf8')

  // TODO: need a xlang JSON parse utility in voxgig/struct with better error msgs
  const entityData = JSON.parse(entityDataSource)

  options.entity = entityData.existing

  let client = FreeMusicSDK.test(options, extra)
  const struct = client.utility().struct
  const merge = struct.merge
  const transform = struct.transform

  let idmap = transform(
    ['v1_list01','v1_list02','v1_list03'],
    {
      '`$PACK`': ['', {
        '`$KEY`': '`$COPY`',
        '`$VAL`': ['`$FORMAT`', 'upper', '`$COPY`']
      }]
    })

  const env = envOverride({
    'FREE_MUSIC_TEST_V1_LIST_ENTID': idmap,
    'FREE_MUSIC_TEST_LIVE': 'FALSE',
    'FREE_MUSIC_TEST_EXPLAIN': 'FALSE',
    'FREE_MUSIC_APIKEY': '',
  })

  idmap = env['FREE_MUSIC_TEST_V1_LIST_ENTID']

  const live = 'TRUE' === env.FREE_MUSIC_TEST_LIVE

  const transport = createLiveTransport()
  if (live) {
    const rawIds = process.env['FREE_MUSIC_TEST_V1_LIST_ENTID']
    idmap = rawIds && rawIds.trim() ? JSON.parse(rawIds) : {}
    if (!idmap || Array.isArray(idmap) || typeof idmap !== 'object') {
      throw new Error('Live ENTID must be a JSON object')
    }
    client = new FreeMusicSDK(merge([
      // FIRST, so the generated fields below win: sdk-test-control.json's
      // test.client.options adds to the live client, it does not redirect it.
      liveClientOptions(),
      {
        apikey: env.FREE_MUSIC_APIKEY,
      },
      // 'extra || {}', not a bare 'extra': struct.merge returns UNDEFINED when the
      // last entry is undefined, and basicSetup is normally called with no
      // argument at all - so a bare 'extra' silently discarded the apikey
      // and server values above and handed the SDK undefined. Harmless
      // while there was nothing in that object; not harmless now.
      extra || {},
      { system: { fetch: transport.fetch } }
    ]))
  }

  const setup = {
    idmap,
    env,
    options,
    client,
    struct,
    data: entityData,
    explain: 'TRUE' === env.FREE_MUSIC_TEST_EXPLAIN,
    live,
    transport,
    now: Date.now(),
  }

  return setup
}
  
