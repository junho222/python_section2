import sys
import io
import requests as r
from bs4 import BeautifulSoup



#Rest : POST, GET, PUT-업데이트, 대체하는 성격(FETCH: 업데이트 수정), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://user.ruliweb.com/member/login_proc"
data = {'user_id': 'rulliho' , 'user_pw': 'wnsgh135!!'}


with r.Session() as s:
    p = s.post('https://user.ruliweb.com/member/login_proc', data = data)
    if p.status_code is 200 and p.ok :
        target = s.get("https://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4685113&find=&ftext=")
        target.raise_for_status()
        soup = BeautifulSoup(target.text, 'html.parser')
        print(soup.selectAll('#mypiRead > tbody > tr:nth-child(1) > td > p:nth-child(5)'))
