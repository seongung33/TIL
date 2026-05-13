# CSS
## display 속성(박스의 화면 배치 방식) 
1. Block 타입
2. Inline 타입

### Block 타입
 - 항상 새로운 행으로 나뉨
 - width, height, margin, padding 속성을 모두 사용할 수 있음
 - padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
 - width 지정을 안 할시 inline 방향으로 모두 차지함
 - 대표 태그: h1 ~ h6, p, div, ul, li  
Block 타입의 대표: div  
헤드, 푸터, 사이드바 등 웹 페이지의 다양한 섹션을 구조화 하는데 가장 많이 쓰인다.  

### Inline 타입
 - 줄 바꿈이 일어나지 않음
 -  텍스트의 일부에만 다른 스타일을 적용할 때 사용됩니다. 
 -  수직 방향(상하)
   -  padding, margin, border가 적용되지만, 다른 요소를 밀어낼 수는 없음
 - 수평방향(좌우)
   -  padding, margin, border가 적용되어 다른 요소를 밀어낸다.
 -  대표 태그: span, a, img, strong  
inline 타입의 대표:span  
블록처럼 줄 바꿈이 일어나지 않아 문서 구조에 큰 변화가 없다.  
## Normal flow 
레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식  
block 요소는 한 줄 전체를, inline 요소는 콘텐츠의 공간만 차지하며 줄바꿈 X  
## 기타 display 속성
1. inline-block
2. none
3. flex  
사용법 display: inline-block  none 
### inline-block 
inline과 block의 특징을 모두 가진 특별한 display 속성 값  
- 줄바꿈 없음, 크기 지정 가능
- width 및 height 속성 사용가능
- paddin, margin 및 border로 인해 다른 요소가 상자에서 밀려남
- 리스트 요소 가로 정렬, span에 width 사용 등

### none 타입
요소를 화면에 표시하지 않고 공간조차 부여되지 않음   
웹 페이지가 보이지 않는다.

## CSS Position
Normal Flow에서 제거하여 **다른 위치로 배치**하는 것  
- 요소 위에 올리기
- 화면의 특정 위치에 고정시키기 등
- 상 하 좌 우 의 방향으로 이동 가능하고 겹치는 요소의 쌓이는 순서 조절 가능  
- **position: static**
### position 유형
1. static
 - Normal Flow에 따라 배치
 -  아무것도 하지 않으면 기본 설정되는 유형이다.  

2. relative
 - Normal Flow에 따라 배치: 자신의 기존 공간을 유지하는 것. 
   - 눈에 보이는 것과 자신의 영역이 다르다.
 - 자기자신(static)을 기준으로 이동
 - top, right, bottom, left 속성으로 위치를 조정할 수 있다.
 - 다른 요소의 레이아웃에 영향을 주지 않음  

3. absolute
 - 요소를 Normal Flow에서 제거
 - 가장 가까운 relative 부모 요소를 기준으로 이동
   - relative가 없다면 body를 기준으로 이동
 - 문서에서 차지하는 공간이 없다.  

4. fixed  
 - Normal Flow에서 제거
 - 현재 화면영역(viewport)을 기준으로 이동
 - 스크롤 해도 항상 같은 위치에 유지됨
 - 문서에서 차지하는 공간이 없다.  

5. sticky
 - relative와 fixex의 특성을 결합한 속성
 - 화면 안에 있으면 해당 위치에 있지만
 - 이를 벗어난다면 fixed 처럼 화면에 고정
 - 다음 sticky 요소가 나오면 sticky 교체  

## z-index
- 정수 값을 사용해 z축 순서 지정
- 값이 클수록 요소가 위에 쌓인다.
- static이 아닌 요소에만 적용
- 기본값은 auto로 부모요소의 z-index 값에 영향을 받음
- 같은 부모 내에서만 z-index 값을 비교하고, 값이 같으면 HTML 순서대로 쌓임(아래가 위로)
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 올라갈 수 없음

## CSS Flexbox
요소를 행과 열 형태로 배치하는 1차원 레이아웃
구성요소
 - main axis
 - cross axis
 - flex container
 - flex item

### main axis  (주 축)
기본 축  
방향은 수정 가능하여 가로 세로 가 아닌다. 
main start > main end  
### cross axis(교차 축)
수직 축    
cross start에서 cross end 방향으로 배치  
### flex container
flexbox 속성 값들을 사용하여 자식 요소 flex item들을 배치하는 주체

### flex item
flex container 내부에 레이아웃 되는 항목

## Flexbox 속성
display: flex;  
flex container 가로 or 세로로 변경  

flex-direction: row; 기본값. 가로로 왼쪽에서 오른쪽으로 배치  
flex-direction: column; 세로배치 위에서 아래로 item들을 배치한다.  
flex-direction: row-reverse; 시작지점 위치를 반대로  

flex-direction: wrap; 한 행에 모든 item이 안 들어갈 경우 줄을 바꾼다.  


justify-content: center 주 축을 가운데로 고정. 화면 크기 비율에 맞추어 무조건 center로 고정한다.
align-content  : 교차 축 정렬 방법을 지정  

flex-grow: 1  남는 행 비율에 따라 각 flex item에 분배  
flex-grow: 2  
flex-grow: 3    위 세개는 1:2:3 비율로 컨테이너 내에서 공간을 차지한다.    
**남은 공간을 가져가는 것**   

flex-basis: 100px flex item의 초기 크기 값을 지정  
만약 flex-basis와 width가 함께 있다면 flex-basis 적용  
## flex-wrap 응용  
반응형 레이아웃  
화면 크기가 줄어들어서 특정 넓이를 쓸 수 없다면 다른 곳으로 위치를 옮긴다.  
display: flex;  
flex-wrap: wrap;  