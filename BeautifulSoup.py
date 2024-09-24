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

# User-Agent를 설정하여 봇으로 인식되지 않게 함
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

# 브라우저 열기
driver = webdriver.Chrome(service=service, options=options)

# s_no 값을 시작하는 숫자로 설정
s_no = 20241425  # 첫 번째 페이지의 s_no 값

while True:
    try:
        # A 버튼의 href URL을 동적으로 생성하여 페이지로 이동
        url = f"https://statiz.sporki.com/schedule/?m=gamelogs&s_no={s_no}"
        driver.get(url)
        print(f"현재 페이지: {url}")
        time.sleep(2)

        # # B 버튼 클릭
        # b_button = driver.find_element(By.LINK_TEXT, '경기로그')  # B 버튼의 텍스트로 찾기
        # b_button.click()
        # time.sleep(2)  # 페이지가 로드될 때까지 대기

        # 데이터 수집 (예: <div class="table_type03"> 태그의 내용 수집)
        items = driver.find_elements(By.CLASS_NAME, 'table_type03')
        for item in items:
            print(item.text)

        # # 뒤로가기 2번
        # driver.back()  # 첫 번째 뒤로가기
        # time.sleep(2)  # 페이지가 로드될 때까지 대기
        # driver.back()  # 두 번째 뒤로가기
        # time.sleep(2)  # 페이지가 로드될 때까지 대기

        # s_no 값을 1 증가시켜 다음 페이지로 이동
        s_no += 1
        time.sleep(2)

    except Exception as e:
        # 에러 발생 시 종료 또는 로그 출력
        print(f"에러 발생: {e}")
        break

# 브라우저 닫기
driver.quit()