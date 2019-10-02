import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class EverytimeText:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options() #한번만 사용할거기 때문에 self 안씀
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="c:/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인 & 출석체크
    def class_evaluation(self):
        self.driver.get('https://everytime.kr/login')
        self.driver.find_element_by_name('userid').send_keys('wnshdl')
        self.driver.find_element_by_name('password').send_keys('784512')
        self.driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="menu"]/li[3]/a').click()
        self.driver.find_element_by_name('keyword').send_keys('박재홍')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="container"]/form/input[2]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/a[5]/h3/p[1]').click()
        time.sleep(3)

        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        text = soup.select('#container > div.side.article > div.articles > article')

        for i in text:
            print(i.select_one('p.text').text)

    def printTextList(self,list):
        f = open("C:/textList.txt", 'wt')
        for i in list:
            f.write(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()
    # 소멸자

    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit() #Selenium 전체 프로그램 종료
        print('removed driver object')
#실행

if __name__ == '__main__':
    #객체생성
    a = EverytimeText()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.class_evaluation()
    #종료 시간 출력

    a.printTextList(a.class_evaluation())
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
