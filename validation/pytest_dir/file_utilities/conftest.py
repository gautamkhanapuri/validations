import pytest
import tempfile
import os

@pytest.fixture
def create_temp_file():

    def create_test_file(fname):
        newpath = tempfile.mkdtemp()
        os.chdir(newpath)
        with open(fname, 'w') as f:
            f.write('hello')
        return '%s/%s' % (newpath, fname)

    return create_test_file


@pytest.fixture
def create_temp_dir():
    newpath = tempfile.mkdtemp()
    return newpath