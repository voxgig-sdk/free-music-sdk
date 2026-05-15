
import { Context } from './Context'


class FreeMusicError extends Error {

  isFreeMusicError = true

  sdk = 'FreeMusic'

  code: string
  ctx: Context

  constructor(code: string, msg: string, ctx: Context) {
    super(msg)
    this.code = code
    this.ctx = ctx
  }

}

export {
  FreeMusicError
}

