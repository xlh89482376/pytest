import time

def test_tmpdir(tmpdir):
    a_dir = tmpdir.mkdir('mytempdir')
    a_file = a_dir.join('tempfile.txt')

    a_file.write('hello,pytest')
    assert a_file.read() == 'hello,pytest'