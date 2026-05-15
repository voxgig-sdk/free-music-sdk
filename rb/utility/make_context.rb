# FreeMusic SDK utility: make_context
require_relative '../core/context'
module FreeMusicUtilities
  MakeContext = ->(ctxmap, basectx) {
    FreeMusicContext.new(ctxmap, basectx)
  }
end
