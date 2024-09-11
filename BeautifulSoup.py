import requests
from bs4 import BeautifulSoup

# 웹사이트에 요청을 보내고 응답을 받는다
url = 'https://statiz.sporki.com/schedule/?m=gamelogs&s_no=20241459'
response = requests.get(url)

# BeautifulSoup으로 HTML을 파싱한다
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 데이터를 추출한다 (예: <h1> 태그의 내용)
box_head_text = soup.find('div', class_='box_head').text
print(box_head_text)