# 웹
World Wide Web   
## HTML
1. HyperText Markup Languange   
웹 페이지의 의미가 구조를 정의하는 언어   
2. HyperText    
웹 페이지를 다른 페이지로 연결하는 링크    
3. Markup Language  
태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어   
ex)HTML, Markdown  

## structure of HTML (HTML의 구조)
```html
<head></head>
```
-  HTML 문서에 관련된 설정, 설명 등 컴퓨터가 식별하는 **메타데이터**
-  사용자에게 보이지 않음  
! 하고 엔터시 기본 틀이 완성되어 제공된다.  
전체적인 틀 및 주요 태그
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset = "UTF-8"> # 메타 태그 처럼 닫힘이 없는 것도 있다.
    <title> 싸피페이지</title>
</head>
<body>
    <p>웹페이지 입니다.</p> # 문단이라 자동으로 줄바뀜이 일어난다
    <a href="이동 페이지 주소 입력"> Google</a> # 하이퍼링크
    <img src="이미지 경로" 
    alt="대체 텍스트(이미지 경로에 문제 발생 시 출력 테스트)">
    <img src="/web/01_fundamentals_of_html_css/images/sample.png" alt="샘플 이미지">
</body>
</html>
```
## Text Structure 
- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것  
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것  
대표적인 HTML Text Structure  
- Heading & Paragraphs
  - h1~6, p
- Lists
  - ol, ul, li
- Emphasis & Importance
  - em, strong

```html
<h1> 메인 대제목</h1>
<h2>중제목</h2>
<p>안녕<strong>볼드처리</strong><em>기울이기</em>입니다.</p>
<p>반갑습니다.<b>볼드처리</b></p>
# strong과 b는 둘다 볼드 처리 이지만 html은 의미가 중요하다
# strong은 강조표시. 중요하다는 뜻이다.
<ol>
    # 1 2 3 순서 태그
    <li>1.</li>
    <li>2.</li>
    <li>3.</li>
</ol>
<ul>
    <li>순서</li>
    <li>없이</li>
    <li>md의 -와 같다.</li>
</ul>
```
## 웹 스타일링
## CSS
Cascading Style Sheet  
웹 페이지의 디자인과 레이아웃을 구성하는 언어
1. 인라인 스타일
    - HTML 요소 안에 style 속성 값으로 작성
    - 가장 권장하지 않는 요소
```html
    <h1 style="color: blue; background-color: yellow">Inline Style</h1>  
    <!-- 외부   -->
```
2. 내부 스타일
```
    <style>
    
    h2{ # 내부
      color: red
    }
  </style>
```
3. 외부 스타일
    - 가장 권장하는 형태
```
<link rel ="stylesheet" herf="style.css">
```
## CSS 구문 및 선택자
선택자  
- 기본 선택자
  - '누구'를 꾸밀지 지정하는 부분  
  - *: 전체 선택자
  - h1, h2 등 ...: 요소 선택자
  - .클래스이름: 해당 클래스명 사용자 선택 - 재사용성 염두
  - #id이름:  id 선택자 - 하나만 있어야 함
- 결합자
  - .클래스 li : 자손 결합자. 하위레벨 모두 선택
  - /> : 자식 결합자 - 직계 자식만 선택  

명시도가 높은 순
1. !important : 권장하지는 않는 키워드.
2. Inline 스타일
3. 선택자
    - id선택자 > class 선택자 > 요소 선택자. : 좁게 선택할수록 강하다.
4. 소스 코드 선언 순서

선언
- 어떻게 꾸밀지에 대한 한줄의 명령  
- 속성과 값이 한 쌍으로 이루어지며, 세미콜론(;)으로 끝남
- 속성: 값;

속성
- 바꾸고 싶은 스타일의 종류를 나타냄  
- CSS가 미리 정의해 둔 키워드 사용
- font-size, background-color 등등

값
- 속성에 적용할 구체적인 설정
- 단위가 중요하다. ex) px, %, 색깔(rgb, red, blue), rem 등등  
- 절대 단위: px, pt, cm 등 다른 요소의 영향을 받지 않는다
- 상대 단위: %. em, rem, vh 등 다른 요소의 크기에 따라 상대적으로 결정  

## CSS Box Model
웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델  
내용(content), 안쪽 여백(padding), 테두리(border), 외부간격(margin)으로 구성되어 요소의 크기와 배치를 결정  
## shorthand  


## box- sizing 속성 (박스의 크기 계산법)  
1. 개발자 도구의 크기는 content 기준으로 계산한다. 
2. borderbox가 아닌 content box의 크기로 지정
3. * {box-sizing: content-box} or * {box-sizing: border-box}
4. 기본값이 content box이므로 따로 border-box 지정