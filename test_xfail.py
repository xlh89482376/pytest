import pytest

version = 1.1

@pytest.mark.xfail(version < 1.2, reason='not supported until v1.2')
def test_api():
    id_1 = 1
    id_2 = 2
    assert id_1 != id_2