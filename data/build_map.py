import json
import urllib
import struct
import csv
import requests


response = requests.get('http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP949.TXT', stream=True)

map = {}
for line in csv.reader(response.raw, delimiter='\t'):
    if len(line) != 3:
        continue

    cp949_str, utf8_str, comment = line

    if cp949_str.strip() and utf8_str.strip():
        utf8 = unichr(int(utf8_str, 0)).encode('utf8')
        cp949_int = int(cp949_str, 0)
        cp949 = urllib.quote(struct.pack('>H', cp949_int)) if cp949_int > 255 else chr(cp949_int)
        map[utf8] = cp949


charTable = 'var charTable = %s;' % json.dumps(map)
commonScript = open('src.js').read()

open('build.js', 'w+').write(charTable + commonScript)
