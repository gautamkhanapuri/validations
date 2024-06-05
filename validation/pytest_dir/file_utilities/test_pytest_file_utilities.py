from source_dir.file_utilities.file_utilities import remove_file, mkdir_path, save_file


def test_remove_file(create_temp_file):
    fname = create_temp_file('a.txt')
    assert True == remove_file(fname)
    assert False == remove_file('/tmp/acxs')


def test_mkdir_path(create_temp_dir):
    assert False == mkdir_path(create_temp_dir)
    assert True == mkdir_path(create_temp_dir + "trial_file")
    assert False == mkdir_path('/a/b/c')


def test_save_file(create_temp_file):
    fpath1 = create_temp_file('f1')
    assert True == save_file(fpath1, "Hello World. this is trial content")
    fpath2 = create_temp_file('f2')
    assert True == save_file(fpath2, "Hello World. this is trial content")


