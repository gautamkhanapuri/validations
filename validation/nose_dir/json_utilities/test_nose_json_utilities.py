import os.path
from source_dir.json_utilities.json_utilities import save_json_to_file, valid_json, json_from_string
import unittest
from nose2.tools import params
import tempfile
import json
import time

def create_temp_dir():
    newpath = tempfile.mkdtemp()
    return newpath


def create_temp_json(path, data, fname='a1.json'):
    # fname = 'a1.json'
    fullname = '%s/%s' % (path, fname)
    with open(fullname, 'w') as f:
        f.write(json.dumps(data, indent=2))
    print(fullname)
    return fname

class TestJsonUtilities(unittest.TestCase):

    @params("/a1.json", "/a2.json", "/a3.json", "/a4.json", "/a5.json")
    def test_save_json_to_file(self, file_name):
        fname = '%s' % create_temp_dir() + file_name
        file_exists = os.path.exists(fname)
        assert False == file_exists
        save_json_to_file({}, fname)
        file_exists = os.path.exists(fname)
        assert True == file_exists
        os.remove(fname)

    @params("{}", '{"a": "b"}', '[{"name": "Python"}, {"a": "b"}]', "123", "123.634")
    def test_valid_json(self, isjson):
        assert True == valid_json(isjson)

    @params(({}, 'a2.json'), ([{124: "Python"}, {"a": "b"}], 'a1.json'), ({}, 'a2.json'))
    def test_json_from_string(self, data, file_name):
        newpath = create_temp_dir()
        fname = create_temp_json(newpath, data, file_name)
        fullpath = '%s/%s' % (newpath, fname)
        file_exists = os.path.exists(fullpath)
        assert True == file_exists
        with open(fullpath) as f:
            data_str = f.read()
        assert data_str is not None
        data = json_from_string(data_str)
        assert data is not None
        os.remove(fullpath)


if __name__ == '__main__':
    import nose2
    nose2.main()



#     def setUp(self):
#         print("creating temp directory")
#         new_path = tempfile.mkdtemp()
#         TestJsonFromString.temporary_directory += new_path
#
#
    # @params(('[{"name": "Python"}, {"a": "b"}]', 'a1.json'), ("{", 'a2.json'))
    # def test_json_from_string(self, data, file_name):
    #     newpath = TestJsonFromString.temporary_directory
    #     fname = create_temp_json(newpath, data, file_name)
    #     fullpath = '%s/%s' % (newpath, fname)
    #     file_exists = os.path.exists(fullpath)
    #     assert True == file_exists
    #     with open(fullpath) as f:
    #         data_str = f.read()
    #     assert data_str is not None
    #     data = json_from_string(data_str)
    #     assert data is not None
    #     os.remove(fullpath)

#
# "{", 'a2.json'

# class TestJsonFromString(unittest.TestCase):
    # def setUp(self):
    #     print("creating temp directory")
    #     new_path = tempfile.mkdtemp()
    #     TestJsonFromString.temporary_directory += new_path
    # def test_json_from_string(self):
    #     newpath = TestJsonFromString.temporary_directory
    #     fname = create_temp_json(newpath, '[{"name": "Python"}, {"a": "b"}]', 'a1.json')
    #     fullpath = '%s/%s' % (newpath, fname)
    #     file_exists = os.path.exists(fullpath)
    #     assert True == file_exists
    #     with open(fullpath) as f:
    #         data_str = f.read()
    #     assert data_str is not None
    #     data = json_from_string(data_str)
    #     assert data is not None
    #     os.remove(fullpath)
    #
    # def test_json_from_string1(self):
    #     newpath = TestJsonFromString.temporary_directory
    #     fname = create_temp_json(newpath, "{}", 'a2.json')
    #     fullpath = '%s/%s' % (newpath, fname)
    #     file_exists = os.path.exists(fullpath)
    #     assert True == file_exists
    #     with open(fullpath) as f:
    #         data_str = f.read()
    #     assert data_str is not None
    #     data = json_from_string(data_str)
    #     assert data is not None
    #     os.remove(fullpath)
    #
    # def tearDown(self):
    #     print("deleting temp directory")
    #     os.rmdir(TestJsonFromString.temporary_directory)
