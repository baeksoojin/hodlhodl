# hodlhodl
## gpt-3 감정분석 모델 및 시계열 예측기법 사용해, 코인동향 예측에 반한 후 코인자동매매 프로그램

## 0. 세팅방법

###### 가상환경 패키지 설치
- clone을 진행할 폴더에서 가상환경 설치 후 활성화
``` c
python3 -m venv venv
cd venv/bin
source ./activate
```

- venv와 동일한 위치에서 클론
```c
git clone "repository code입력"
```

- 패키지 설치
``` c
>> cd AutoTrade
pip install -r requirments.txt
```

###### .env파일 등록
- manage.py와 동일한 위치
```c
DEBUG=on
SECRET_KEY="장고 secret_key 입력"
DB_PW="mysql hodl(사용자명)의 비밀번호 입력"
```

## 1. 실행방법

###### 서버 실행방법
- manage.py와 동일한 위치에서 진행
``` c
python manage.py runserver
```

###### 데이터베이스 모델 저장 및 적용
- manage.py와 동일한 위치에서 진행
``` c
python manage.py makemigrations
python manage.py migrate
```
