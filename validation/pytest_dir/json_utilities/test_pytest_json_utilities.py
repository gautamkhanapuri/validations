import os.path
from source_dir.json_utilities.json_utilities import save_json_to_file, valid_json, json_from_string

def test_save_json_to_file(create_temp_dir):
    fname = '%s/a1.json' % create_temp_dir
    file_exists = os.path.exists(fname)
    assert False == file_exists
    save_json_to_file({}, fname)
    file_exists = os.path.exists(fname)
    assert True == file_exists
    os.remove(fname)


def test_valid_json(create_json_string):
    isjson = create_json_string('{}')
    assert True == valid_json(isjson)
    isjson = create_json_string('{"a": "b"}')
    assert True == valid_json(isjson)
    isjson = create_json_string('{"a": "b"}}')
    assert False == valid_json(isjson)

def test_json_from_string(create_json_string, create_temp_dir, create_temp_json):
    newpath = create_temp_dir
    fname = create_temp_json(newpath)
    fullpath = '%s/%s' % (newpath, fname)
    file_exists = os.path.exists(fullpath)
    assert True == file_exists
    with open(fullpath) as f:
        data_str = f.read()
    assert data_str is not None
    data = json_from_string(data_str)
    assert data is not None
    data_str = 'abcd'
    data = json_from_string(data_str)
    assert data is None
    data = json_from_string(None)
    assert data is None
    data = json_from_string(create_json_string('123'))
    assert data is 123
    data = json_from_string(create_json_string('12.64533'))
    assert data == 12.64533
    data = json_from_string(create_json_string("{'12.64533': '763'"))
    assert data is None




