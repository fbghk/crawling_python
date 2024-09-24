from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
import json
import sqlite3

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

# CSV 파일 생성 및 헤더 작성
csv_file = open('data.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['페이지', '데이터'])  # 헤더 작성

# JSON 파일에 데이터를 저장할 리스트
json_data = []

# SQLite 데이터베이스 연결
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    페이지 TEXT,
    데이터 TEXT
)
''')

while True:
    try:
        # A 버튼의 href URL을 동적으로 생성하여 페이지로 이동
        url = f"https://statiz.sporki.com/schedule/?m=gamelogs&s_no={s_no}"
        driver.get(url)
        print(f"현재 페이지: {url}")
        time.sleep(2)

        # 데이터 수집 (예: <div class="table_type03"> 태그의 내용 수집)
        items = driver.find_elements(By.CLASS_NAME, 'table_type03')
        page_data = ""
        for item in items:
            page_data += item.text + "\n"
            print(item.text)

        # 데이터를 CSV 파일에 저장
        csv_writer.writerow([url, page_data])

        # 데이터를 JSON 파일용 리스트에 저장
        json_data.append({'페이지': url, '데이터': page_data})

        # 데이터를 SQLite에 저장
        cursor.execute('INSERT INTO data (페이지, 데이터) VALUES (?, ?)', (url, page_data))

        # s_no 값을 1 증가시켜 다음 페이지로 이동
        s_no += 1
        time.sleep(2)

    except Exception as e:
        # 에러 발생 시 종료 또는 로그 출력
        print(f"에러 발생: {e}")
        break

# 브라우저 닫기
driver.quit()

# CSV 파일 닫기
csv_file.close()

# JSON 파일로 저장
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

# SQLite 데이터베이스 저장 및 닫기
conn.commit()
conn.close()

print("데이터 저장 완료")