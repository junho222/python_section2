import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options() #한번만 사용할거기 때문에 self 안씀
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="c:/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인 & 출석체크
    def writeAttendCheck(self):
        self.driver.get('https://everytime.kr/login')
        self.driver.find_element_by_name('userid').send_keys('wnshdl')
        self.driver.find_element_by_name('password').send_keys('784512')
        self.driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get("")
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main') #iframe 변환!!!!!1 name / id값기본!
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다')
        self.driver.find_element_by_xpath('#copy->xpath')click()
        time.sleep(3)

    # 소멸자

    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit() #Selenium 전체 프로그램 종료
        print('removed driver object')
#실행

if __name__ == '__main__':
    #객체생성
    a = NcafeWriteAtt()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
