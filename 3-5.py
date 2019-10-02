import sys
import io
import requests , json
from bs4 import BeautifulSoup
import urllib
from fake_useragent import UserAgent


#Rest : POST, GET, PUT-업데이트, 대체하는 성격(FETCH: 업데이트 수정), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.wishket.com/accounts/login/"

#Fake UserAgent 생성:
ua = UserAgent()


with requests.Session() as s:
    s.get(url)

    LOGIN_INFO = {
    'identification': 'znchoi59',
    'password': 'wnsgh135!!',
    'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }

    response = s.post(url, data=LOGIN_INFO, headers ={'User-Agent':str(ua.chrome),  'Referer' : 'https://www.wishket.com/accounts/login/'})
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectlist = soup.select('div.client-history-body > div')
        for i in projectlist:
            print(i.find('div').text)
