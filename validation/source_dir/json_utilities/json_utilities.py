import json


def save_json_to_file(indata, outfile):
    """Save json data to the file"""
    if indata is not None:
        try:
            instr = json.dumps(indata, indent=2) # default=json_util.default)
            with open(outfile, 'w') as jsonwrite:
                jsonwrite.write(instr)
        except:
            pass


def json_from_string(json_str):
    """Get json from the string."""
    try:
        jsondata = json.loads(json_str)
        return jsondata
    except Exception as err:
        print(err)
        # logger.debug('Failed to load json data: %s', json_str)
    return None


def valid_json(json_input):
    """ Checks validity of the json """
    try:
        _ = json.loads(json_input)
        return True
    except Exception as err:
        print(err)
        # logger.debug('Not a valid json: %s', json_input)
    return False