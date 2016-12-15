__author__ = 'Mitsui'

import mechanize
import cookielib
import urllib2
import json

cookie = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cookie)
resp = br.open("http://www.nike.com/cn/zh_cn/")

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

data = {
    'client_id': "HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH",
    'grant_type': "password",
    'keepMeLoggedIn': True,
    'password': "Xjn04551",
    'username': "stillotherguy@qq.com",
    'ux_id': "com.nike.commerce.nikedotcom.web"
}

req = urllib2.Request(
    'https://unite.nike.com/loginWithSetCookie?appVersion=209&experienceVersion=176&uxid=com.nike.commerce.nikedotcom.web&locale=zh_CN&backendEnvironment=default&browser=Google%20Inc.&os=undefined&mobile=false&native=false'
    , json.dumps(data))
req.add_header('Content-Type', 'text/plain')
req.add_header('User-Agent',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36')
req.add_header('Host', 'unite.nike.com')
req.add_header('Origin', 'http://store.nike.com')
req.add_header('Referer', 'http://www.nike.com/cn/zh_cn')

resp = opener.open(req)
print req.get_header('Cookie')
# resp = opener.open('http://store.nike.com/cn/zh_cn/?cp=cnns_sz_022516_a_ALNUL_bz01&utm_source=Bd&utm_medium=Pcbz&utm_content=title')
print resp.read()
opener.close()
