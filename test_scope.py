import pytest

# def test_multi_scope(sess_scope, mod_scope, func_scope):
#     pass

# @pytest.mark.usefixtures('class_scope')
@pytest.mark.usefixtures('func_scope')
class TestClassScope:

    def test_1(self):
        pass

    def test_2(self):
        pass