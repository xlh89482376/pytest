# import pytest
#
# @pytest.fixture()
# def postcode():
#     return '010'

def test_postcode(postcode):
    code = '0'
    assert code != postcode