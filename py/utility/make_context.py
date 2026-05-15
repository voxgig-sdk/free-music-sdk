# FreeMusic SDK utility: make_context

from core.context import FreeMusicContext


def make_context_util(ctxmap, basectx):
    return FreeMusicContext(ctxmap, basectx)
