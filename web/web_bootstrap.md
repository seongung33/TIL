# Bootstrap 
CSS 프론트엔드 프레임워크 (Toolkit)  
다양한 기기 환경에서 웹 페이지가 적절하게 표시될 수 있도록 반응형 웹 디자인을 지원하는 도구  

## 주소를 넣은 이유 CDN (content Delivery Network)
CDN - 콘텐츠를 더 빠르게, 사용자와 더 가깝게    

## Bootstrap 사용가이드
특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음   
Bootstrap에서 클래스 이름으로 spacing을 표현하는 방법이 정해져있다.  

## Reset CSS 
모든 HTML 요소 스타일을 일관된 기준으로 재설정 하는 간결하고 압축된 규칙 시트    
모든 브라우저는 User agent stylesheet 를 가지고 있다.  
모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하기 때문  

### Normalize CSS 
웹 표준 기준으로 브라우저가 일치하지 않다면 차이가 있는 브라우저를 수정한다.  
Bootstrap에서의 Reset CSS: bootstrap-reboot.css라는 파일명으로 normalize.css를 자체적으로 커스텀해서 사용한다.  

## Bootstrap 활용 
### Typography 
제목, 본문 텍스트, 목록 등  
기존 Heading보다 더 눈에 띄는 제목이 필요할 경우  
HTML inline 요소에 대한 스타일  
HTML list 요소에 대한 스타일  

### Color 
bootstrap color system  
text, border, background 등 다양한 요소 키워드  

## Component 
재사용 가능한 독립적인 부품, 더 크고 복잡한 시스템을 구축하기 위해 사용되는 소프트웨어 기본 단위   
대표 컴포넌트: Alerts, Badges, Cards, Navbar, Carousel, Modal 

Alerts: 팝업, 알림 창..? 

Badges: 창에 숫자 같은거    

button: 이동 버튼    

cards: 사진, 설명, 버튼  

Navbar: 상단 혹은 하단에 있는 네비게이션 바  

Carousel: 움직임이 있고 사용자와 상호작용하는 컨텐츠. 커머스 상품 광고 창, 게임 홈페이지 이벤트 안내 창/ 캐루젤을 여러개 할 경우 버튼을 다르게 지정해줘야 한다.  

modal: 특정 행동 시 배경이 흐릿해지며 뜨는 창/ modal 코드가 다른 중첩된 코드 안에 위치할 경우 modal이 활성화 되었을 때 modal이 검은 화면 뒤로 이동해 클릭이 안 될 수 있습니다. 따라서 modal 코드는 body 태그가 닫히는 곳 바로 직전에 모아두는 것이 일반적
ex) 현재 저장되지 않은 상태입니다. 새로고침 하시겠습니까?  

## Semantic Web  
웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식  

### Semantic in HTML 
외형보다는 요소 자체의 의미에 집중하는 것  
head, nav, main  
## OOCSS (Objdect Orienterd SSS)
객체 지향적 접근법   
구조와 스킨을 분리하였다.  
컨테이너와 컨텐츠 분리