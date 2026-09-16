

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


describe('V2ListEntity', async () => {

  // Per-test live pacing. Delay is read from sdk-test-control.json's
  // `test.live.delayMs`; only sleeps when FREE_MUSIC_TEST_LIVE=TRUE.
  afterEach(liveDelay('FREE_MUSIC_TEST_LIVE'))

  test('instance', async () => {
    const testsdk = FreeMusicSDK.test()
    const ent = testsdk.V2List()
    assert(null != ent)
  })


  test('basic', async (t) => {

    const live = 'TRUE' === process.env.FREE_MUSIC_TEST_LIVE
    for (const op of ['load']) {
      if (!live && maybeSkipControl(t, 'entityOp', 'v2_list.' + op, live)) return
    }

    
    const setup = basicSetup()
    if (setup.live) {
      return runLiveEntity(setup, {"active":true,"alias":{"field":{}},"fields":[{"active":true,"name":"album","req":false,"type":"`$ARRAY`","index$":0}],"name":"v2_list","op":{"load":{"input":"data","name":"load","points":[{"active":true,"args":{"params":[{"active":true,"example":111239,"kind":"param","name":"id_artist","orig":"id_artist","reqd":true,"type":"`$INTEGER`","index$":0}]},"contract":{"id":"GET /list/discography/{idArtist}","json":"{\"parameters\":[{\"description\":\"Artist ID\",\"example\":111239,\"in\":\"path\",\"name\":\"idArtist\",\"required\":true,\"schema\":{\"type\":\"integer\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"album\":{\"items\":{\"properties\":{\"idAlbum\":{\"description\":\"Unique album ID\",\"type\":\"string\"},\"idArtist\":{\"description\":\"Artist ID\",\"type\":\"string\"},\"idLabel\":{\"description\":\"Label ID\",\"type\":\"string\"},\"intLoved\":{\"description\":\"Number of loves/likes\",\"type\":\"string\"},\"intSales\":{\"description\":\"Sales figures\",\"type\":\"string\"},\"intScore\":{\"description\":\"Album score/rating\",\"type\":\"string\"},\"intScoreVotes\":{\"description\":\"Number of score votes\",\"type\":\"string\"},\"intYearReleased\":{\"description\":\"Release year\",\"type\":\"string\"},\"strAlbum\":{\"description\":\"Album name\",\"type\":\"string\"},\"strAlbum3DCase\":{\"description\":\"3D case image URL\",\"type\":\"string\"},\"strAlbum3DFace\":{\"description\":\"3D face image URL\",\"type\":\"string\"},\"strAlbum3DFlat\":{\"description\":\"3D flat image URL\",\"type\":\"string\"},\"strAlbum3DThumb\":{\"description\":\"3D thumbnail URL\",\"type\":\"string\"},\"strAlbumCDart\":{\"description\":\"CD art URL\",\"type\":\"string\"},\"strAlbumSpine\":{\"description\":\"Album spine image URL\",\"type\":\"string\"},\"strAlbumStripped\":{\"description\":\"Album name stripped of special characters\",\"type\":\"string\"},\"strAlbumThumb\":{\"description\":\"Album thumbnail URL\",\"type\":\"string\"},\"strAlbumThumbBack\":{\"description\":\"Album back cover URL\",\"type\":\"string\"},\"strAlbumThumbHQ\":{\"description\":\"High quality album thumbnail URL\",\"type\":\"string\"},\"strAllMusicID\":{\"description\":\"AllMusic ID\",\"type\":\"string\"},\"strAmazonID\":{\"description\":\"Amazon ID\",\"type\":\"string\"},\"strArtist\":{\"description\":\"Artist name\",\"type\":\"string\"},\"strArtistStripped\":{\"description\":\"Artist name stripped\",\"type\":\"string\"},\"strBBCReviewID\":{\"description\":\"BBC Review ID\",\"type\":\"string\"},\"strDescriptionEN\":{\"description\":\"Album description in English\",\"type\":\"string\"},\"strDiscogsID\":{\"description\":\"Discogs ID\",\"type\":\"string\"},\"strGeniusID\":{\"description\":\"Genius ID\",\"type\":\"string\"},\"strGenre\":{\"description\":\"Musical genre\",\"type\":\"string\"},\"strItunesID\":{\"description\":\"iTunes ID\",\"type\":\"string\"},\"strLabel\":{\"description\":\"Record label\",\"type\":\"string\"},\"strLocation\":{\"description\":\"Recording location\",\"type\":\"string\"},\"strLocked\":{\"description\":\"Lock status\",\"type\":\"string\"},\"strLyricWikiID\":{\"description\":\"LyricWiki ID\",\"type\":\"string\"},\"strMood\":{\"description\":\"Album mood\",\"type\":\"string\"},\"strMusicBrainzArtistID\":{\"description\":\"MusicBrainz Artist ID\",\"type\":\"string\"},\"strMusicBrainzID\":{\"description\":\"MusicBrainz Release Group ID\",\"type\":\"string\"},\"strMusicMozID\":{\"description\":\"MusicMoz ID\",\"type\":\"string\"},\"strRateYourMusicID\":{\"description\":\"Rate Your Music ID\",\"type\":\"string\"},\"strReleaseFormat\":{\"description\":\"Release format (CD, Vinyl, etc.)\",\"type\":\"string\"},\"strReview\":{\"description\":\"Album review\",\"type\":\"string\"},\"strSpeed\":{\"description\":\"Album speed/tempo\",\"type\":\"string\"},\"strStyle\":{\"description\":\"Musical style\",\"type\":\"string\"},\"strTheme\":{\"description\":\"Album theme\",\"type\":\"string\"},\"strWikidataID\":{\"description\":\"Wikidata ID\",\"type\":\"string\"},\"strWikipediaID\":{\"description\":\"Wikipedia ID\",\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/list/discography/{idArtist}","rename":{"param":{"idArtist":"id_artist"}},"segments":[{"lit":"list"},{"lit":"discography"},{"var":"id_artist"}],"select":{"exist":["id_artist"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":0}],"key$":"load"}},"relations":{"ancestors":[["discography"]]},"key$":"v2_list","name__orig":"v2_list","Name":"V2List","name_":"v2_list","name-":"v2-list","NAME":"V2_LIST","index$":3}, {"active":true,"entity":"v2_list","key$":"BasicV2ListFlow","kind":"basic","name":"BasicV2ListFlow","param":{},"step":[{"active":true,"data":{},"input":{"ref":"v2_list_ref01","srcdatavar":"v2_list_ref01_data","suffix":"_dt0"},"match":{"id":"v2_list01"},"op":"load","spec":[],"valid":[{"apply":"TextFieldMark","def":{"mark":"Mark01-v2_list_ref01"}}],"index$":0}]}, 'V2List')
    }
    const client = setup.client
    const struct = setup.struct

    const isempty = struct.isempty
    const select = struct.select

    let v2_list_ref01_data = Object.values(setup.data.existing.v2_list)[0] as any

    // LOAD: skipped — no entity id field and load requires path params.
    // Entity-var is declared here so later flow steps still compile.
    const v2_list_ref01_ent = client.V2List()


  })
})



function basicSetup(extra?: any) {
  // TODO: fix test def options
  const options: any = {} // null

  // TODO: needs test utility to resolve path
  const entityDataFile =
    Path.resolve(__dirname, 
      '../../../../.sdk/test/entity/v2_list/V2ListTestData.json')

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
    ['v2_list01','v2_list02','v2_list03','discography01','discography02','discography03'],
    {
      '`$PACK`': ['', {
        '`$KEY`': '`$COPY`',
        '`$VAL`': ['`$FORMAT`', 'upper', '`$COPY`']
      }]
    })

  const env = envOverride({
    'FREE_MUSIC_TEST_V2_LIST_ENTID': idmap,
    'FREE_MUSIC_TEST_LIVE': 'FALSE',
    'FREE_MUSIC_TEST_EXPLAIN': 'FALSE',
    'FREE_MUSIC_APIKEY': '',
  })

  idmap = env['FREE_MUSIC_TEST_V2_LIST_ENTID']

  const live = 'TRUE' === env.FREE_MUSIC_TEST_LIVE

  const transport = createLiveTransport()
  if (live) {
    const rawIds = process.env['FREE_MUSIC_TEST_V2_LIST_ENTID']
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
  
