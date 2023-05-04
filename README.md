# INHA Login Checker

이 프로젝트는 파이썬을 사용하여 인하대학교 사이트에 로그인을 확인하고 이름과 학번을 가져오는 스크립트입니다.

## 시작하기 전에

1. `.env` 파일을 생성하고 아래와 같이 사용자 아이디와 비밀번호를 입력하세요.

``` env
INHA_USERNAME=your_username
INHA_PASSWORD=your_password
```

`your_username` 및 `your_password`를 실제 사용자 아이디와 비밀번호로 바꿔주세요.

2. 필요한 패키지를 설치하세요. 터미널에서 다음 명령어를 실행하세요:

``` sh
pip install python-dotenv requests bs4
```

## 실행방법

프로젝트를 클론한 디렉토리에서 터미널을 열고 다음 명령어를 실행하세요:

``` python
python main.py
```

로그인이 성공하면 이름과 학번이 출력되고, 실패하면 "로그인에 실패하였습니다."가 출력됩니다.