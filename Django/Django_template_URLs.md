# Template system 
파이썬 데이터(context)를 HTML 문서(Template)와 결합하여
로직과 표현을 분리한 채 동적인 웹 페이지를 생성하는 도구     

ex): 뉴스 사이트를 보면 기본적인 틀은 같지만 기사 헤더 광고 위치등은 고정인 것     

### 변수
- render 함수의 세번째 인자로 딕셔너리 타입으로 전달
- html에 {{ 변수명 }} 을 입력하여 사용할 수 있음
- 변수 속성 접근 시 {{ variable.attribute}} 로 사용

### 필터 
- 표시할 변수를 수정 할 때 {{변수 | 필터}} 사용
- 일부 필터는 인자를 받기도 함
- 약 60개의 빌트인 템플릿 필터가 있으니 찾아보자

### 태그 tags 
- 반복 또는 논리를 수행하여 제어 흐름을 만듦
- 일부 태그는 시작과 종료 태그가 필요 { % tag %}
- 약 24개의 빌트인 템플릿 태그가 있으니 찾아보자
- {% if %}, {% endif %}  


### Comments 주석
```html
  <h1>Hello, {# name #}</h1>
  {% comment %} 
    ... multiline 주석
  {% endcomment %}
```
DTL 예시    
Urls.py -> views.py -> html 순으로 작성하여야 한다.     
url에 이동경로 만들기, views에 입력할 값 작성, html에 시각화 구조 짜기


## 템플릿 상속
{% extends "articles/base.html" %}   
위와 같이 적어두면 어디에든 있음   
base.html 정보
```html
  <h1>네비게이션 바 </h1>
  {% block content %}
  {% endblock content %}
  <h1>하단 바 <h1>
```
맨 위에 네비게이션 바 맨 아래 하단 바 라고 글자가 나온다.    
extends 외에도 이를 사용할 파일에 block과 endblock의 위치를 적어줘야 한다.    
index.html의 구조    
```html
{% extends "articles/base.html" %}

{% block content %}
  <h1>Hello, {{ name }}!</h1>
{% endblock content %}
```
두 블럭 사이는 독자적 작성 위 아래는 base.html로부터 상속 받는 것이다.  


## 요청과 응답  
?? 안 듣고 있었는데 뭐 기억하라하고 넘어감 ㅋㅋ;

## HTML form
데이터를 보내고 가져오기  - 클라이언트 서버 구조 사용
사용자로부터 입력을 가져오는 것이다.   
ex) - 로그인, 검색 등   

기본 틀    
```html
#은 현재 페이지, action에는 목적지를 적어야 한다.
<form action='#' method='GET'>    
```
```html
<input type="text" name="query" id="message">   
<form action="https://search.naver.com/search.naver" method="GET">
    <label for="message">검색어</label>
# name이 있어야함. 변수 선언과 비슷함  
    <input type="text" name="query" id="message">
    <input type="submit" value="submit">
  </form>
```
Query String parameters  
- 사용자의 입력 데이터를 받아 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 &로 연결된 key=value 쌍
- 기본 URL과는 ? 로 구분  

### 사용자 입력 데이터를 받아 출력하는 서버 
view 함수는 두개: 입력 받을 함수(throw),  출력하는 함수(catch)     
throw의 주소는 이동할  catch 여야한다.


# Django URL  
지금까지 기능 단위 묶음 하나만 했음       
urls 에서 앱 1, 앱 2 기능을 다 호출하게 해야함       

URL dispatcher(운항 관리자, 분배기): URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결      

새로운 주소가 생기면 계속 직접 주소를 추가해야 하는가??  -> 너무 힘듦 말이 안 됨    
이를 위해 Variable Routing이 생김  

## Variable Routing  
```py
# 아무 숫자로 다 주소 생성 가능
path('articles/<int:num>/', views.detail),
# hello/jane, hello/asdfkh 등으로 주소 생성 가능
path('hello/<str:name>/', views.greeting, name='greeting'),
```

## App URL 정의  
App URL mapping: 각 앱에 URL을 정의하는 것    
프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함    

urls 에서 각 앱의 urls로 연결하여 각자 관리    
settings.py 의 INSTALLED_APPS 에 'pages' 추가    
메인
```py
# 메인, 프로젝트  
from django.urls import path, include
path('articles/', include('articles.urls')),
```

## URL 이름 공간  
같은 이름일 경우 aritlces에 있는 건지 pages에 있는 건지 알 수 없음     
app_name = 'articles' 로 지정하면  
path('index/', views.index, name='index') 에서 name에 지정 가능  
{% url 'app_name:path_name' arg1 arg2 %} 로 사용 가능

