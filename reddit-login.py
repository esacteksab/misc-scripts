     import requests
     import json
     
     uname = 'UserABC123'
     upasswd = 'Itsasecret!'
     
     login_url = 'http://www.reddit.com/api/login/+uname'
     self_info_url = 'http://www.reddit.com/api/me.json'
     
     params = {
         'api_type': 'json',
         'passwd': upasswd,
         'user': uname
     }
     
     rlogin=requests.post(login_url, params)

