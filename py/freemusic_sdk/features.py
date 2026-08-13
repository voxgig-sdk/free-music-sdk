# FreeMusic SDK feature factory

from freemusic_sdk.feature.base_feature import FreeMusicBaseFeature
from freemusic_sdk.feature.test_feature import FreeMusicTestFeature


def _make_feature(name):
    features = {
        "base": lambda: FreeMusicBaseFeature(),
        "test": lambda: FreeMusicTestFeature(),
    }
    factory = features.get(name)
    if factory is not None:
        return factory()
    return features["base"]()
