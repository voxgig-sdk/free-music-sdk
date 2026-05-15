# ProjectName SDK exists test

import pytest
from freemusic_sdk import FreeMusicSDK


class TestExists:

    def test_should_create_test_sdk(self):
        testsdk = FreeMusicSDK.test(None, None)
        assert testsdk is not None
