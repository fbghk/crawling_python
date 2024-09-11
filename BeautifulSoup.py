import requests
from bs4 import BeautifulSoup

# 기본 URL 설정 (page 파라미터 제외)
base_url = 'https://statiz.sporki.com/schedule/?m=gamelogs&s_no='

# 페이지 범위 설정 (1~5페이지까지 크롤링)
for page_num in range(20241457, 20241459):
    # 각 페이지의 URL 생성
    url = base_url + str(page_num)
    
    # 웹사이트에 요청을 보내고 응답을 받음
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 원하는 데이터를 추출 (예: <div class="table_type03">의 내용)
    items = soup.find_all('div', class_='table_type03')
    
    # 각 페이지에서 수집한 데이터 출력
    for item in items:
        print(item.text)

    print(f'Page {page_num} done!')