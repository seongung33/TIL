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