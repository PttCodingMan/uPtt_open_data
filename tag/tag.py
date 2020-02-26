

import hashlib

def sha256(s):
    s_lower = s.lower()
    hash = hashlib.sha256(s_lower.encode('utf-8')).hexdigest()
    print(f'[{s}]\n[{s_lower}]\n[{hash}]')

# sha256('QQ_id')


import urllib.request, json
with urllib.request.urlopen("https://raw.githubusercontent.com/PttCodingMan/uPtt/develop/server/tag/tag.json?token=AOHXCXHI6TM4C55DBILID3C6KXVGU") as url:
    data = json.loads(url.read().decode())
    print(data)