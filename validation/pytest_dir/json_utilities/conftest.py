import tempfile
import pytest
import json

data_dict = {'a': 'b', 'c': {'d': 'e'}, 'f': {'g': {'h': 1}}}

@pytest.fixture
def create_temp_dir():
    newpath = tempfile.mkdtemp()
    return newpath

@pytest.fixture
def create_json_string():

    def create_test_json_string(string):
        return string

    return create_test_json_string

@pytest.fixture
def create_temp_json():

    def create_test_temp_json(path, data=data_dict, fname='a1.json'):
        # fname = 'a1.json'
        fullname = '%s/%s' % (path, fname)
        with open(fullname, 'w') as f:
            f.write(json.dumps(data, indent=2))
        return fname

    return create_test_temp_json

# @pytest.fixture
# def valid_json_2():
#     return '{"a": "b"}'
#
# @pytest.fixture
# def invalid_json_1():
#     return '{"a": "b"}}'

# @pytest.fixture
# def

