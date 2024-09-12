from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver 설정
chrome_driver_path = r'C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
options = Options()
options.add_argument("--headless")  # 필요시 headless 모드를 사용

# 브라우저 열기
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://statiz.sporki.com/team/?m=team&t_code=7002&year=2024')

while True:
    try:
        # A 버튼 클릭
        a_button = driver.find_element(By.CLASS_NAME, 'score01')  # A 버튼의 텍스트로 찾기
        a_button.click()
        time.sleep(2)  # 페이지가 로드될 때까지 대기

        # B 버튼 클릭
        b_button = driver.find_element(By.LINK_TEXT, '경기로그')  # B 버튼의 텍스트로 찾기
        b_button.click()
        time.sleep(2)  # 페이지가 로드될 때까지 대기

        # 데이터 수집 (예: <div class="table_type03"> 태그의 내용 수집)
        items = driver.find_elements(By.CLASS_NAME, 'table_type03')
        for item in items:
            print(item.text)

        # 뒤로가기 2번
        driver.back()  # 첫 번째 뒤로가기
        time.sleep(2)  # 페이지가 로드될 때까지 대기
        driver.back()  # 두 번째 뒤로가기
        time.sleep(2)  # 페이지가 로드될 때까지 대기

    except Exception as e:
        # 에러 발생 시 종료 또는 로그 출력
        print(f"에러 발생: {e}")
        break

# 브라우저 닫기
driver.quit()