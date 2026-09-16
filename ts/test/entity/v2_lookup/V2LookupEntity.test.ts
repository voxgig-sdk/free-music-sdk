

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


describe('V2LookupEntity', async () => {

  // Per-test live pacing. Delay is read from sdk-test-control.json's
  // `test.live.delayMs`; only sleeps when FREE_MUSIC_TEST_LIVE=TRUE.
  afterEach(liveDelay('FREE_MUSIC_TEST_LIVE'))

  test('instance', async () => {
    const testsdk = FreeMusicSDK.test()
    const ent = testsdk.V2Lookup()
    assert(null != ent)
  })


  test('basic', async (t) => {

    const live = 'TRUE' === process.env.FREE_MUSIC_TEST_LIVE
    for (const op of ['load']) {
      if (!live && maybeSkipControl(t, 'entityOp', 'v2_lookup.' + op, live)) return
    }

    
    const setup = basicSetup()
    if (setup.live) {
      return runLiveEntity(setup, {"active":true,"alias":{"field":{}},"fields":[{"active":true,"name":"album","req":false,"type":"`$ARRAY`","index$":0},{"active":true,"name":"artists","req":false,"type":"`$ARRAY`","index$":1},{"active":true,"name":"track","req":false,"type":"`$ARRAY`","index$":2}],"name":"v2_lookup","op":{"load":{"input":"data","name":"load","points":[{"active":true,"args":{"params":[{"active":true,"example":2109615,"kind":"param","name":"id_album","orig":"id_album","reqd":true,"type":"`$INTEGER`","index$":0}]},"contract":{"id":"GET /lookup/album/{idAlbum}","json":"{\"parameters\":[{\"description\":\"Album ID\",\"example\":2109615,\"in\":\"path\",\"name\":\"idAlbum\",\"required\":true,\"schema\":{\"type\":\"integer\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"album\":{\"items\":{\"properties\":{\"idAlbum\":{\"description\":\"Unique album ID\",\"type\":\"string\"},\"idArtist\":{\"description\":\"Artist ID\",\"type\":\"string\"},\"idLabel\":{\"description\":\"Label ID\",\"type\":\"string\"},\"intLoved\":{\"description\":\"Number of loves/likes\",\"type\":\"string\"},\"intSales\":{\"description\":\"Sales figures\",\"type\":\"string\"},\"intScore\":{\"description\":\"Album score/rating\",\"type\":\"string\"},\"intScoreVotes\":{\"description\":\"Number of score votes\",\"type\":\"string\"},\"intYearReleased\":{\"description\":\"Release year\",\"type\":\"string\"},\"strAlbum\":{\"description\":\"Album name\",\"type\":\"string\"},\"strAlbum3DCase\":{\"description\":\"3D case image URL\",\"type\":\"string\"},\"strAlbum3DFace\":{\"description\":\"3D face image URL\",\"type\":\"string\"},\"strAlbum3DFlat\":{\"description\":\"3D flat image URL\",\"type\":\"string\"},\"strAlbum3DThumb\":{\"description\":\"3D thumbnail URL\",\"type\":\"string\"},\"strAlbumCDart\":{\"description\":\"CD art URL\",\"type\":\"string\"},\"strAlbumSpine\":{\"description\":\"Album spine image URL\",\"type\":\"string\"},\"strAlbumStripped\":{\"description\":\"Album name stripped of special characters\",\"type\":\"string\"},\"strAlbumThumb\":{\"description\":\"Album thumbnail URL\",\"type\":\"string\"},\"strAlbumThumbBack\":{\"description\":\"Album back cover URL\",\"type\":\"string\"},\"strAlbumThumbHQ\":{\"description\":\"High quality album thumbnail URL\",\"type\":\"string\"},\"strAllMusicID\":{\"description\":\"AllMusic ID\",\"type\":\"string\"},\"strAmazonID\":{\"description\":\"Amazon ID\",\"type\":\"string\"},\"strArtist\":{\"description\":\"Artist name\",\"type\":\"string\"},\"strArtistStripped\":{\"description\":\"Artist name stripped\",\"type\":\"string\"},\"strBBCReviewID\":{\"description\":\"BBC Review ID\",\"type\":\"string\"},\"strDescriptionEN\":{\"description\":\"Album description in English\",\"type\":\"string\"},\"strDiscogsID\":{\"description\":\"Discogs ID\",\"type\":\"string\"},\"strGeniusID\":{\"description\":\"Genius ID\",\"type\":\"string\"},\"strGenre\":{\"description\":\"Musical genre\",\"type\":\"string\"},\"strItunesID\":{\"description\":\"iTunes ID\",\"type\":\"string\"},\"strLabel\":{\"description\":\"Record label\",\"type\":\"string\"},\"strLocation\":{\"description\":\"Recording location\",\"type\":\"string\"},\"strLocked\":{\"description\":\"Lock status\",\"type\":\"string\"},\"strLyricWikiID\":{\"description\":\"LyricWiki ID\",\"type\":\"string\"},\"strMood\":{\"description\":\"Album mood\",\"type\":\"string\"},\"strMusicBrainzArtistID\":{\"description\":\"MusicBrainz Artist ID\",\"type\":\"string\"},\"strMusicBrainzID\":{\"description\":\"MusicBrainz Release Group ID\",\"type\":\"string\"},\"strMusicMozID\":{\"description\":\"MusicMoz ID\",\"type\":\"string\"},\"strRateYourMusicID\":{\"description\":\"Rate Your Music ID\",\"type\":\"string\"},\"strReleaseFormat\":{\"description\":\"Release format (CD, Vinyl, etc.)\",\"type\":\"string\"},\"strReview\":{\"description\":\"Album review\",\"type\":\"string\"},\"strSpeed\":{\"description\":\"Album speed/tempo\",\"type\":\"string\"},\"strStyle\":{\"description\":\"Musical style\",\"type\":\"string\"},\"strTheme\":{\"description\":\"Album theme\",\"type\":\"string\"},\"strWikidataID\":{\"description\":\"Wikidata ID\",\"type\":\"string\"},\"strWikipediaID\":{\"description\":\"Wikipedia ID\",\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/album/{idAlbum}","rename":{"param":{"idAlbum":"id_album"}},"segments":[{"lit":"lookup"},{"lit":"album"},{"var":"id_album"}],"select":{"exist":["id_album"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":0},{"active":true,"args":{"params":[{"active":true,"example":111239,"kind":"param","name":"id_artist","orig":"id_artist","reqd":true,"type":"`$INTEGER`","index$":0}]},"contract":{"id":"GET /lookup/artist/{idArtist}","json":"{\"parameters\":[{\"description\":\"Artist ID\",\"example\":111239,\"in\":\"path\",\"name\":\"idArtist\",\"required\":true,\"schema\":{\"type\":\"integer\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"artists\":{\"items\":{\"properties\":{\"idArtist\":{\"description\":\"Unique artist ID\",\"type\":\"string\"},\"idLabel\":{\"description\":\"Label ID\",\"type\":\"string\"},\"intBornYear\":{\"description\":\"Birth year (for solo artists)\",\"type\":\"string\"},\"intCharted\":{\"description\":\"Chart position\",\"type\":\"string\"},\"intDiedYear\":{\"description\":\"Death year (if applicable)\",\"type\":\"string\"},\"intFormedYear\":{\"description\":\"Year the artist was formed\",\"type\":\"string\"},\"intMembers\":{\"description\":\"Number of band members\",\"type\":\"string\"},\"strArtist\":{\"description\":\"Artist name\",\"type\":\"string\"},\"strArtistAlternate\":{\"description\":\"Alternative artist name\",\"type\":\"string\"},\"strArtistBanner\":{\"description\":\"Banner image URL\",\"type\":\"string\"},\"strArtistClearart\":{\"description\":\"Clear art image URL\",\"type\":\"string\"},\"strArtistCutout\":{\"description\":\"Cutout image URL\",\"type\":\"string\"},\"strArtistFanart\":{\"description\":\"Fan art image URL\",\"type\":\"string\"},\"strArtistFanart2\":{\"description\":\"Additional fan art image URL\",\"type\":\"string\"},\"strArtistFanart3\":{\"description\":\"Additional fan art image URL\",\"type\":\"string\"},\"strArtistFanart4\":{\"description\":\"Additional fan art image URL\",\"type\":\"string\"},\"strArtistLogo\":{\"description\":\"Logo image URL\",\"type\":\"string\"},\"strArtistStripped\":{\"description\":\"Artist name stripped of special characters\",\"type\":\"string\"},\"strArtistThumb\":{\"description\":\"Thumbnail image URL\",\"type\":\"string\"},\"strArtistWideThumb\":{\"description\":\"Wide thumbnail image URL\",\"type\":\"string\"},\"strBiographyEN\":{\"description\":\"Biography in English\",\"type\":\"string\"},\"strCountry\":{\"description\":\"Country of origin\",\"type\":\"string\"},\"strCountryCode\":{\"description\":\"Country code\",\"type\":\"string\"},\"strDisbanded\":{\"description\":\"Disbandment status\",\"type\":\"string\"},\"strFacebook\":{\"description\":\"Facebook URL\",\"type\":\"string\"},\"strGender\":{\"description\":\"Gender\",\"type\":\"string\"},\"strGenre\":{\"description\":\"Musical genre\",\"type\":\"string\"},\"strISNIcode\":{\"description\":\"ISNI code\",\"type\":\"string\"},\"strLabel\":{\"description\":\"Record label\",\"type\":\"string\"},\"strLastFMChart\":{\"description\":\"Last.fm chart URL\",\"type\":\"string\"},\"strLocked\":{\"description\":\"Lock status\",\"type\":\"string\"},\"strMood\":{\"description\":\"Musical mood\",\"type\":\"string\"},\"strMusicBrainzID\":{\"description\":\"MusicBrainz ID\",\"type\":\"string\"},\"strStyle\":{\"description\":\"Musical style\",\"type\":\"string\"},\"strTwitter\":{\"description\":\"Twitter handle\",\"type\":\"string\"},\"strWebsite\":{\"description\":\"Official website URL\",\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/artist/{idArtist}","rename":{"param":{"idArtist":"id_artist"}},"segments":[{"lit":"lookup"},{"lit":"artist"},{"var":"id_artist"}],"select":{"exist":["id_artist"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":1},{"active":true,"args":{"params":[{"active":true,"example":32724183,"kind":"param","name":"id_track","orig":"id_track","reqd":true,"type":"`$INTEGER`","index$":0}]},"contract":{"id":"GET /lookup/track/{idTrack}","json":"{\"parameters\":[{\"description\":\"Track ID\",\"example\":32724183,\"in\":\"path\",\"name\":\"idTrack\",\"required\":true,\"schema\":{\"type\":\"integer\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"properties\":{\"track\":{\"items\":{\"properties\":{\"idAlbum\":{\"description\":\"Album ID\",\"type\":\"string\"},\"idArtist\":{\"description\":\"Artist ID\",\"type\":\"string\"},\"idIMVDB\":{\"description\":\"IMVDB ID\",\"type\":\"string\"},\"idLyric\":{\"description\":\"Lyrics ID\",\"type\":\"string\"},\"idTrack\":{\"description\":\"Unique track ID\",\"type\":\"string\"},\"intCD\":{\"description\":\"CD number\",\"type\":\"string\"},\"intDuration\":{\"description\":\"Track duration in milliseconds\",\"type\":\"string\"},\"intLoved\":{\"description\":\"Number of loves/likes\",\"type\":\"string\"},\"intMusicVidComments\":{\"description\":\"Music video comment count\",\"type\":\"string\"},\"intMusicVidDislikes\":{\"description\":\"Music video dislike count\",\"type\":\"string\"},\"intMusicVidFavorites\":{\"description\":\"Music video favorite count\",\"type\":\"string\"},\"intMusicVidLikes\":{\"description\":\"Music video like count\",\"type\":\"string\"},\"intMusicVidViews\":{\"description\":\"Music video view count\",\"type\":\"string\"},\"intScore\":{\"description\":\"Track score/rating\",\"type\":\"string\"},\"intScoreVotes\":{\"description\":\"Number of score votes\",\"type\":\"string\"},\"intTotalListeners\":{\"description\":\"Total listener count\",\"type\":\"string\"},\"intTotalPlays\":{\"description\":\"Total play count\",\"type\":\"string\"},\"intTrackNumber\":{\"description\":\"Track number on album\",\"type\":\"string\"},\"strAlbum\":{\"description\":\"Album name\",\"type\":\"string\"},\"strArtist\":{\"description\":\"Artist name\",\"type\":\"string\"},\"strArtistAlternate\":{\"description\":\"Alternative artist name\",\"type\":\"string\"},\"strDescriptionEN\":{\"description\":\"Track description in English\",\"type\":\"string\"},\"strGenre\":{\"description\":\"Musical genre\",\"type\":\"string\"},\"strLocked\":{\"description\":\"Lock status\",\"type\":\"string\"},\"strMood\":{\"description\":\"Track mood\",\"type\":\"string\"},\"strMusicBrainzAlbumID\":{\"description\":\"MusicBrainz Album ID\",\"type\":\"string\"},\"strMusicBrainzArtistID\":{\"description\":\"MusicBrainz Artist ID\",\"type\":\"string\"},\"strMusicBrainzID\":{\"description\":\"MusicBrainz Recording ID\",\"type\":\"string\"},\"strMusicVid\":{\"description\":\"Music video URL\",\"type\":\"string\"},\"strMusicVidCompany\":{\"description\":\"Music video production company\",\"type\":\"string\"},\"strMusicVidDirector\":{\"description\":\"Music video director\",\"type\":\"string\"},\"strMusicVidScreen1\":{\"description\":\"Music video screenshot 1\",\"type\":\"string\"},\"strMusicVidScreen2\":{\"description\":\"Music video screenshot 2\",\"type\":\"string\"},\"strMusicVidScreen3\":{\"description\":\"Music video screenshot 3\",\"type\":\"string\"},\"strStyle\":{\"description\":\"Musical style\",\"type\":\"string\"},\"strTheme\":{\"description\":\"Track theme\",\"type\":\"string\"},\"strTrack\":{\"description\":\"Track name\",\"type\":\"string\"},\"strTrack3x3\":{\"description\":\"3x3 track image URL\",\"type\":\"string\"},\"strTrackLyrics\":{\"description\":\"Track lyrics\",\"type\":\"string\"},\"strTrackThumb\":{\"description\":\"Track thumbnail URL\",\"type\":\"string\"}},\"type\":\"object\"},\"type\":\"array\"}},\"type\":\"object\"}}},\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/track/{idTrack}","rename":{"param":{"idTrack":"id_track"}},"segments":[{"lit":"lookup"},{"lit":"track"},{"var":"id_track"}],"select":{"exist":["id_track"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":2},{"active":true,"args":{"params":[{"active":true,"example":"1dc4c347-a1db-32aa-b14f-bc9cc507b843","kind":"param","name":"music_brainz_id","orig":"music_brainz_id","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /lookup/album_mb/{musicBrainzId}","json":"{\"parameters\":[{\"description\":\"MusicBrainz Release Group ID\",\"example\":\"1dc4c347-a1db-32aa-b14f-bc9cc507b843\",\"in\":\"path\",\"name\":\"musicBrainzId\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/album_mb/{musicBrainzId}","rename":{"param":{"musicBrainzId":"music_brainz_id"}},"segments":[{"lit":"lookup"},{"lit":"album_mb"},{"var":"music_brainz_id"}],"select":{"exist":["music_brainz_id"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":3},{"active":true,"args":{"params":[{"active":true,"example":"cc197bad-dc9c-440d-a5b5-d52ba2e14234","kind":"param","name":"music_brainz_id","orig":"music_brainz_id","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /lookup/artist_mb/{musicBrainzId}","json":"{\"parameters\":[{\"description\":\"MusicBrainz Artist ID\",\"example\":\"cc197bad-dc9c-440d-a5b5-d52ba2e14234\",\"in\":\"path\",\"name\":\"musicBrainzId\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/artist_mb/{musicBrainzId}","rename":{"param":{"musicBrainzId":"music_brainz_id"}},"segments":[{"lit":"lookup"},{"lit":"artist_mb"},{"var":"music_brainz_id"}],"select":{"exist":["music_brainz_id"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":4},{"active":true,"args":{"params":[{"active":true,"example":"50369905-68ca-48d2-912d-b37330ff7dc3","kind":"param","name":"music_brainz_id","orig":"music_brainz_id","reqd":true,"type":"`$STRING`","index$":0}]},"contract":{"id":"GET /lookup/track_mb/{musicBrainzId}","json":"{\"parameters\":[{\"description\":\"MusicBrainz Recording ID\",\"example\":\"50369905-68ca-48d2-912d-b37330ff7dc3\",\"in\":\"path\",\"name\":\"musicBrainzId\",\"required\":true,\"schema\":{\"type\":\"string\"}}],\"protocol\":\"http\",\"responses\":{\"200\":{\"description\":\"Successful response\"},\"401\":{\"description\":\"Unauthorized\"}},\"security\":[{\"ApiKeyAuth\":[]}],\"securitySchemes\":{\"ApiKeyAuth\":{\"description\":\"API key for V2 endpoints (Premium only)\",\"in\":\"header\",\"name\":\"X-API-KEY\",\"type\":\"apiKey\"}},\"securitySource\":\"operation\"}","source":"openapi3","version":1},"kind":"http","method":"GET","orig":"/lookup/track_mb/{musicBrainzId}","rename":{"param":{"musicBrainzId":"music_brainz_id"}},"segments":[{"lit":"lookup"},{"lit":"track_mb"},{"var":"music_brainz_id"}],"select":{"exist":["music_brainz_id"]},"transform":{"req":"`reqdata`","res":"`body`"},"index$":5}],"key$":"load"}},"relations":{"ancestors":[["album"],["album_mb"],["artist"],["artist_mb"],["track"],["track_mb"]]},"key$":"v2_lookup","name__orig":"v2_lookup","Name":"V2Lookup","name_":"v2_lookup","name-":"v2-lookup","NAME":"V2_LOOKUP","index$":4}, {"active":true,"entity":"v2_lookup","key$":"BasicV2LookupFlow","kind":"basic","name":"BasicV2LookupFlow","param":{},"step":[{"active":true,"data":{},"input":{"ref":"v2_lookup_ref01","srcdatavar":"v2_lookup_ref01_data","suffix":"_dt0"},"match":{"id":"v2_lookup01"},"op":"load","spec":[],"valid":[{"apply":"TextFieldMark","def":{"mark":"Mark01-v2_lookup_ref01"}}],"index$":0}]}, 'V2Lookup')
    }
    const client = setup.client
    const struct = setup.struct

    const isempty = struct.isempty
    const select = struct.select

    let v2_lookup_ref01_data = Object.values(setup.data.existing.v2_lookup)[0] as any

    // LOAD: skipped — no entity id field and load requires path params.
    // Entity-var is declared here so later flow steps still compile.
    const v2_lookup_ref01_ent = client.V2Lookup()


  })
})



function basicSetup(extra?: any) {
  // TODO: fix test def options
  const options: any = {} // null

  // TODO: needs test utility to resolve path
  const entityDataFile =
    Path.resolve(__dirname, 
      '../../../../.sdk/test/entity/v2_lookup/V2LookupTestData.json')

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
    ['v2_lookup01','v2_lookup02','v2_lookup03','album01','album02','album03','album_mb01','album_mb02','album_mb03','artist01','artist02','artist03','artist_mb01','artist_mb02','artist_mb03','track01','track02','track03','track_mb01','track_mb02','track_mb03'],
    {
      '`$PACK`': ['', {
        '`$KEY`': '`$COPY`',
        '`$VAL`': ['`$FORMAT`', 'upper', '`$COPY`']
      }]
    })

  const env = envOverride({
    'FREE_MUSIC_TEST_V2_LOOKUP_ENTID': idmap,
    'FREE_MUSIC_TEST_LIVE': 'FALSE',
    'FREE_MUSIC_TEST_EXPLAIN': 'FALSE',
    'FREE_MUSIC_APIKEY': '',
  })

  idmap = env['FREE_MUSIC_TEST_V2_LOOKUP_ENTID']

  const live = 'TRUE' === env.FREE_MUSIC_TEST_LIVE

  const transport = createLiveTransport()
  if (live) {
    const rawIds = process.env['FREE_MUSIC_TEST_V2_LOOKUP_ENTID']
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
  
