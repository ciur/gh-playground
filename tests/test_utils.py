from packaging.version import Version

from xumper.utils import search_ver, increment_ver


def test_search_version_1():
    text = """
    version = "2.38.0"
    """
    assert search_ver(text) == "2.38.0"


def test_search_version_2():
    text = """
    version = '2.1.0b2'
    """
    assert search_ver(text) == "2.1.0b2"


def test_search_version_3():
    text = """
    __version__ = '2.1.0b2'
    """
    assert search_ver(text) == "2.1.0b2"


def test_increment_ver():
    assert increment_ver("2.1.0b1") == Version("2.1.0b2")
    assert increment_ver("2.1.1") == Version("2.1.2")
    assert increment_ver("2.1.1dev2") == Version("2.1.1dev3")
