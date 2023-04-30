import os
import requests
from dotenv import load_dotenv

# .env 파일 불러오기
load_dotenv()

login_url = "https://learn.inha.ac.kr/login/index.php"
session = requests.Session()

# .env 파일에서 사용자 아이디와 비밀번호를 불러오기
username = os.getenv("INHA_USERNAME")
password = os.getenv("INHA_PASSWORD")

payload = {
    "username": username,
    "password": password,
    "rememberusername": "1",  # 사용자 이름 기억 여부 (1 = 기억, 0 = 기억하지 않음)
}

# POST 요청을 사용하여 로그인
response = session.post(login_url, data=payload)

# 로그인 성공 여부 확인
if response.url == login_url:
    print("로그인 실패")
else:
    print("로그인 성공")