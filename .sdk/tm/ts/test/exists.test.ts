
import { test, describe } from 'node:test'
import { equal } from 'node:assert'


import { FreeMusicSDK } from '..'


describe('exists', async () => {

  test('test-mode', async () => {
    const testsdk = await FreeMusicSDK.test()
    equal(null !== testsdk, true)
  })

})
