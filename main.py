import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# .env 파일 불러오기
load_dotenv()

# 사용자 아이디와 비밀번호 가져오기
username = os.getenv("INHA_USERNAME")
password = os.getenv("INHA_PASSWORD")

# 로그인 정보
payload = {
    'userid': username,
    'password': password,
    'loginDomain': 'inha.ac.kr',
}

# 로그인 URL
login_url = 'https://cloud.inha.ac.kr/auth/login'

# 세션 생성
with requests.Session() as session:
    # 로그인 페이지 요청
    res = session.get(login_url)

    # 로그인 요청
    res = session.post(login_url, data=payload)

    # 로그인 실패시 예외처리
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"로그인에 실패하였습니다. 오류코드: {res.status_code}")
        print(e)
        exit()

    # 포털 페이지 요청
    res = session.get('https://cloud.inha.ac.kr')

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(res.content, 'html.parser')

    # 로그인 사용자 정보 출력
    try:
        login_header = soup.select_one('.loginHeader')
        name = login_header.string.strip().split()[0]
        student_id = login_header['data-userid']
        print(f"이름: {name}, 학번: {student_id}")
    except Exception as e:
        print("사용자 정보를 찾는 중 오류가 발생했습니다.")
        print(e)
        print("로그인에 실패하였습니다.")
