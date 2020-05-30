import pytest


def test_raises():
    with pytest.raises(TypeError) as e:
        exec_msg = e.value.args[0]
        assert exec_msg == 'port type must be int'