import pytest

conn = 1

@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass

@pytest.mark.skipif(conn < 3, reason='not supported until v3')
def test_api():
    pass