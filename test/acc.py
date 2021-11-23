import requests
import json
user = {"用户名":"小谭","密码":"123"}
acc = {"用户名":"碰碰车","加速度":100,"时间":202110111609}

data = json.dumps(acc)
url = "http://127.0.0.1:7000/writeaccv/"
r = requests.post(url,data)
print(r.text)
