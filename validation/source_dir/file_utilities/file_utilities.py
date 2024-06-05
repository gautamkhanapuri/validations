import os


def remove_file(fname):
    """Remove the file."""
    try:
        os.remove(fname)
        return True
    except:
        return False


def mkdir_path(dirpath):
    """Make directories recursively."""
    try:
        os.makedirs(dirpath)
        return exists_dir(dirpath)
    except:
        return False


def save_file(file_path, content):
    "write content in file and save file to specified path"
    try:
        f = open(file_path, "w")
        f.write(content)
        f.close()
        return True
    except Exception as e:
        print(e)
        # logger.error(e)
        return False