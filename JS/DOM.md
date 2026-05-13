ES6 이후의 기준으로 설명

# JS


## const
const x = 1  
- 재할당 불가
- 재선언 불가

## let  
let x = 1 
- 재할당 가능
- 재선언 불가  

재할당: num = 10  --> 가능
재선언: let num = 10 --> 불가능

## 블록 스코프 
if, for 안에서 선언한 것은 해당 블록 밖에서 사용불가  
- 파이썬의 함수 느낌임
- 지역변수로 갇힘

## DOM (The Document Object Model)
Document를 객체로  
- Document.title = "바꾸기"  
- document.queryselector(selector) - selector 에는 class= "asdf" 즉 .asdf를 쓰면 된다. 
- document.queryselectorAll(.content)
- document.queryselectorAll(ul > li) 와 같이 실제 style 쓰는것처럼 가능  
- All은 값 여러개, 없으면 selector는 하나
- console.log(h1Tag.classList) -> h1 태그 클래스 불러오기
- h1Tag.classList.add("red") -> 클래스 추가    


요소 선택하기 진행
const box = document.querySelector("#box")   
아래는 조작 메서드(클래스 속성)
1. box.classList.add("red")
2. box.classList.remove()
3. box.classList.toggle()  

일반속성 조작 메서드
- element.getAttribute() - 조회
- setAttribute(name, value) - name의 속성 값 설정
- removeAttribute() - 속성 제거  

DOM 요소 조작   
요소 조작 메서드    
1. document.createElement(tagName)
2. Node.appendChild() -> 해당 Node의 자식으로 감
3. Node.removeChild()  
1번은 태그를 생성하는 것이고 2 번으로 종속시켜 만든다.