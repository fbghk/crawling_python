from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ChromeDriver의 경로를 지정하고 Chrome 옵션을 설정
chrome_driver_path = 'C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\chromedriver.exe'  # 다운로드한 크롬드라이버 경로로 수정
service = Service(chrome_driver_path)
options = Options()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행

# 브라우저 열기
driver = webdriver.Chrome(service=service, options=options)

# 웹사이트 열기
driver.get('https://statiz.sporki.com/schedule/?m=gamelogs&s_no=20241459')

# 원하는 데이터 가져오기 (예: <div class="box_head">) <div class="box_cont">
box_cont = driver.find_element(By.CLASS_NAME, 'box_cont')
print(box_cont.text)

# 브라우저 닫기
driver.quit()