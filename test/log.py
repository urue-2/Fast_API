import requests
import json
user = {"用户名":"战斗白","密码":"321","ty":"aa"}
data = json.dumps(user)
url = "http://127.0.0.1:7000/login/"
#to replace login with :  register login/change to test for other function
# data format for user please see app.py
r = requests.post(url,data)
print(r.text)
