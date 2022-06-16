# hodlhodl
## RoBERTa활용 감성분석 모델 및 Adaboost 시계열 예측기법, 변동성 돌파전략을 활용한 코인자동트레이딩 사이트

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
DB_PW="admin의 password입력"
access="upbit-api access-key입력"
secret="upbit-api secret-key입력"
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
## 2. 설계
<img width="1163" alt="DBschema" src="https://user-images.githubusercontent.com/74058047/174061960-cb915d33-532b-4769-a909-3d025264c95f.png">
## 3. 구현현황
- 홈페이지
<img width="1512" alt="홈페이지" src="https://user-images.githubusercontent.com/74058047/174060848-4cb009c2-36fb-4ea0-8e16-bb8ca1c5874f.gif">
- 회원관리페이지
<img width="1512" alt="회원관리페이지" src="https://user-images.githubusercontent.com/74058047/174061657-1e48f65e-49da-4182-a02d-a9b12c0c266c.gif">
- 주요기능
1. 비트코인 현황
<img width="1512" alt="스크린샷 2022-06-16 오후 8 26 14" src="https://user-images.githubusercontent.com/74058047/174060337-b1295c17-745d-4d72-9fa8-88e0b030a181.png">
2. 감성분석 현황
<img width="1512" alt="스크린샷 2022-06-16 오후 8 26 26" src="https://user-images.githubusercontent.com/74058047/174060347-ea2ec246-2bc2-4408-8faf-dfbf092bf376.png">
3. 시계열예측 현황
<img width="1512" alt="스크린샷 2022-06-16 오후 8 26 33" src="https://user-images.githubusercontent.com/74058047/174060356-69a31eb2-17cd-4c20-a200-9bd41a50b825.png">
4. 성능분석
<img width="1512" alt="스크린샷 2022-06-16 오후 8 26 45" src="https://user-images.githubusercontent.com/74058047/174060369-86f84264-7e52-4a2d-a3a6-71d5acc7dfdb.png">
5. 자동매매 현황
<img width="1512" alt="스크린샷 2022-06-16 오후 8 26 55" src="https://user-images.githubusercontent.com/74058047/174060323-ce5b1048-0e8a-4b47-bf77-585ff69c7e23.png">
