import pytest
import os.path

from hoarder_bot.main import HoarderBot
from hoarder_bot.keyValueTable import KeyValueTable


@pytest.fixture
def app():
    return HoarderBot()


@pytest.fixture
def kvt():
    return KeyValueTable('/tmp/test_table.db')


class TestApplication(object):

    def test_versioning(self, app):
        # App version must be present
        assert len(app.version) > 1

    def test_config_mountpoint(self, app):
        # Mountpoint must point where we expect
        assert os.path.isdir('/config') is True

    def test_key_value_table(self, kvt):
        kvt['bot_token'] = '0101u72636462615517'
        assert len(kvt.items()) == 3

        assert kvt['bot_token'] == '0101u72636462615517'

        kvt.close()
