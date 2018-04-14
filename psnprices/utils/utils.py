import sys
import json
from pprint import pprint

version = sys.version_info[0]

# import only once
if version == 3:
    from urllib.request import urlopen
    from urllib.parse import quote
elif version == 2:
    from urllib2 import urlopen
    from urllib2 import quote
else:
    version == False


def get_json_file(filename):
    json_data = open(filename)
    data = json.load(json_data)
    json_data.close()
    return data


def get_json_response(url):

    response = urlopen(url)

    enc = response.read().decode('utf-8')
    data = json.loads(enc)

    return data


def pretty_print_json(jsonString):
    return json.dumps(
        jsonString,
        sort_keys=True,
        indent=4,
        separators=(
            ',',
            ': '))


def print_enc(s):
    print(s.decode('utf-8') if isinstance(s, type(b'')) else s)
