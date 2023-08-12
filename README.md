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
<img width="1000" alt="DBschema" src="https://user-images.githubusercontent.com/74058047/174061960-cb915d33-532b-4769-a909-3d025264c95f.png">

## 3. 구현현황
- 홈페이지
<img width="1000" alt="홈페이지" src="https://user-images.githubusercontent.com/74058047/174060848-4cb009c2-36fb-4ea0-8e16-bb8ca1c5874f.gif">
- 회원관리페이지
<img width="1000" alt="회원관리페이지" src="https://user-images.githubusercontent.com/74058047/174061657-1e48f65e-49da-4182-a02d-a9b12c0c266c.gif">
- 주요기능
1. 비트코인 현황
<img width="1000" alt="스크린샷 2022-06-16 오후 8 26 14" src="https://user-images.githubusercontent.com/74058047/174060337-b1295c17-745d-4d72-9fa8-88e0b030a181.png">
2. 감성분석 현황
<img width="1000" alt="스크린샷 2022-06-16 오후 8 26 26" src="https://user-images.githubusercontent.com/74058047/174060347-ea2ec246-2bc2-4408-8faf-dfbf092bf376.png">
3. 시계열예측 현황
<img width="1000" alt="스크린샷 2022-06-16 오후 8 26 33" src="https://user-images.githubusercontent.com/74058047/174060356-69a31eb2-17cd-4c20-a200-9bd41a50b825.png">
4. 성능분석
<img width="1000" alt="스크린샷 2022-06-16 오후 8 26 45" src="https://user-images.githubusercontent.com/74058047/174060369-86f84264-7e52-4a2d-a3a6-71d5acc7dfdb.png">
5. 자동매매 현황
<img width="1000" alt="스크린샷 2022-06-16 오후 8 26 55" src="https://user-images.githubusercontent.com/74058047/174060323-ce5b1048-0e8a-4b47-bf77-585ff69c7e23.png">
6. 매도 시점 이메일 경고 서비스

![image](https://github.com/baeksoojin/hodlhodl/assets/74058047/22c984d9-1057-4f38-90fa-c285ef1d87e4)




## 4. 프로젝트 관리

### [Trello](https://trello.com/b/FNAZGMEb/%EB%8F%99%EA%B5%AD%EB%8C%80%ED%95%99%EA%B5%90%EC%BA%A1%EC%8A%A4%ED%86%A4%EB%94%94%EC%9E%90%EC%9D%B81)

### 5. 실행영상

### [시연영상](https://www.youtube.com/watch?v=bDz04ImLko4)

### 6. 역할

|김윤지|백수진|윤수림|이건우|
|-------|---|---|---|
|![image](https://github.com/baeksoojin/hodlhodl/assets/74058047/1f0129b2-dfc0-4678-8c70-616df3d92e49)|![image](https://github.com/baeksoojin/hodlhodl/assets/74058047/d9cb2693-e884-4de2-b1bb-7556d03d013a)|![image](https://github.com/baeksoojin/hodlhodl/assets/74058047/2b9e4a98-a7fb-4b61-bfc6-5979dbb2bd88)|![image](https://github.com/baeksoojin/hodlhodl/assets/74058047/32b3307f-c22f-4737-9b1f-4095897f3876)|
|- ReBERTa 감성분석 모델 학습<br> - EC2에서 스케줄링화하여 table 저장|- 웹 풀스택 개발<br> - RDS 활용 DB 구축 및 table 설계 & 팀원에게 저장예제 코드 제공<br> - EC2 활용 사용자 이메일 경고 자동화 프로세스 구축 & 자동매매 프로세스 스케줄링화|- LSTM 및 Adaboost 모델 비교 후 Adaboost 적용<br> - EC2에서 스케줄링화하여 table 저장| - 변동성 돌파전략 활용 자동매매 알고리즘 작성<br> - AutoEncoder활용 이상값탐지모델 개발||

- Together :  변동성 돌파전략 알고리즘의 매매 척도 K값 설정 로직 
