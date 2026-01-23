# 데이터 수집

## 서버와 클라이언트
- 서버
  - 부탁을 받으면 처리해줍니다.
  - 부탁대로 원하는 값을 돌려주는 역할
- 클라이언트
  - 부탁하는 역할
  - ex) 브라우저: 크롬
### 날씨 정보 필요
날씨 정보를 가지고 있는 서버에 클라이언트를 통해 정보를 달라고 요청한다.
### HOW? 클라이언트는 어떻게 요청을 보낼까요?
1. 웹 브라우저(크롬)를 켜서 주소창에 주소(URL)를 입력한다.
2. 서버에 정보를 요청하는 파이썬 코드를 작성한다.  
- **python**
  - pip install requests
```python
import requests
from pprint import pprint

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data) # 데이터 출력 pprint 사용시 데이터가 이쁘게 출력됨
response = requests.get(url)
print(reponse) # 200 출력시 정상, 404 잘못된 주소
```

가상환경 만들기 
- git 창: python -m venv venv
- 해당 파일 안에서는 가상환경이 만들어진다.
- 여러개의 프로젝트를 진행할 때 패키지를 분리하기 위해 사용한다.

## 서버는 어떻게 요청을 해석할까?
서버에 요청을 보내는 클라이언트는 매우 다양합니다.
### API
- 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
- 기능 예시: 데이터 저장, 조회, 수정, 삭제
- 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둡니다.
- JSON()
  - JavaScript Object Notaion의 약자 자바스크립트 객체 표기법
  - 데이터를 전송하거나 저장할때 많이 쓰는 경량의 텍스트 기반 데이터 형식
  - 특징
    - 데이터는 중괄호({})로 둘러싸인 키-값 쌍의 집합으로 표현됨
    - 키 = 문자열 / 값 = 다양한 데이터 유형을 가질 수 있다
    - 값은 쉼표(,)로 구분됨
## JSON -python 예제
파싱(Parsing)
- 데이터를 의미있는 구조로 분석하고 해석하는 과정
json.loads()
- JSON 형식의 문자열을 파싱하여 python Dictionary로 변환 


파이썬 open API 가져오기 예시
```python
import requests
from pprint import pprint # 딕셔너리 이쁘게 출력하는 함수 패키지
API_key = '6b5cf3ae2e12467d3064cb524439d2ef' #api key
lat = 37.56 #날씨 api 에서의 위도
lon = 126.97 # 경도
url = f'https://api.openweathermap.org/data/2.5/weather?lat={37.56}&lon={126.97}&appid={API_key}' # 주소 및 api
# esponse = requests.get(url) 200 출력시 정상, 404 출력시 주소 에러
response = requests.get(url).json() # 요청 구문 및 json()변환
pprint(response) # 출력
city_name = 'Busan,KR'

url_2 = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
response_2 = requests.get(url_2).json()
pprint(response_2)
```

## 주의사항
1. 생성형 AI한테 파이썬 코드 줘 >>> 금지
- 정답 자체를 바로 요구하는 행동 금지!!!
- 생성형 AI의 실력이다.
- 내 실력이 늘지 않는다!
2. 학습하는 과정
- 피드백/ 검증 시에만 사용
- 개념에 대한 설명
3. 취업 후 개발할때 사용
- 정답 자체를 바로 요구하는 행동 + 반드시 검증하는 과정을 포함한다!
- 생성형 AI는 옛날버전 코드를 준다. >>if 보안 이슈가 있었던 코드라면? <span style="color:red;">**대참사**</span>

## 제출시
나의 프로젝트에 제출 혹은 내 반 그룹에 제출 >> 강사님 말씀 잘 듣기 GOOD!
이름: 01_PJT