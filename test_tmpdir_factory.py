import time

def test_tmpdir_factory(my_tempdir_factory):
    my_tempdir_factory.write("hello,pytest")
    assert my_tempdir_factory.read() == "hello,pytest"


def test_tmpdir_factory2(my_tempdir_factory):
    assert my_tempdir_factory.read() == "hello,pytest"


