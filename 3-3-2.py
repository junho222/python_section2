import sys
import io
import requests , json

#Rest : POST, GET, PUT-업데이트, 대체하는 성격(FETCH: 업데이트 수정), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1 = {'key1' : 'value1', 'key2' : 'value2'} #dictionary 많이사용하긴함
payload2 = (('key1','value1'),('key2','value2')) #튜플
payload3 = {'some':'nice'}

#r = requests.put('http://httpbin.org/put', data = payload1)
#print(r.text)

r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data = payload1)
print(r.text)
