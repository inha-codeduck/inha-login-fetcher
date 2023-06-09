# 인하대학교 로그인 정보 가져오기

이 프로젝트는 파이썬을 사용하여 인하대학교 사이트에 로그인을 확인하고 이름과 학번을 가져오는 스크립트입니다.

## 파이썬 패키지 설치하기

이제 PyPI에서 최신 코드의 파이썬 패키지를 다운로드 받을 수 있습니다.

``` sh
$ pip install inha-cloud
```

## 시작하기 전에

1. `.env` 파일을 생성하고 아래와 같이 사용자 아이디와 비밀번호를 입력하세요.

``` env
INHA_USERNAME=your_username
INHA_PASSWORD=your_password
```

`your_username` 및 `your_password`를 실제 사용자 아이디와 비밀번호로 바꿔주세요.

2. 필요한 패키지를 설치하세요. 터미널에서 다음 명령어를 실행하세요:

``` sh
$ pip install python-dotenv requests bs4
```

``` sh
$ pip install -r requirements.txt
```

## 실행방법

프로젝트를 클론한 디렉토리에서 터미널을 열고 다음 명령어를 실행하세요:

``` sh
$ python main.py
```

로그인이 성공하면 이름과 학번이 출력되고, 실패하면 "로그인에 실패하였습니다."가 출력됩니다.

## 예제

``` python
from inha_cloud.inha_cloud import InhaCloud

def main():
    # Instantiate an InhaCloud object
    inha = InhaCloud()

    # Login to the InhaCloud with the username and password stored in the .env file
    inha.login()

    # Login to the InhaCloud with the provided username and password
    inha.login(username="your_username", password="your_password")

    # Alternatively, you can set the username and password instance variables and then login without passing them as arguments
    inha.username = "your_username"
    inha.password = "your_password"
    inha.login()

    # If login fails, exit the program
    if not inha.login():
        exit()

    # Fetch login information and print name and student ID
    login_info = inha.fetch_login_info()
    print(login_info["name"])
    print(login_info["student_id"])

if __name__ == '__main__':
    main()
```

## 라이선스

이 프로젝트는 MIT 라이선스 조건에 따라 사용이 가능합니다. 자세한 내용은 [LICENSE](/LICENSE) 파일을 확인해주세요.
