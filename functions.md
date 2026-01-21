# 함수

## 함수 구조
간단한 함수 구조  
함수의 설명: Docstring
함수 구조: function body
```python
def make_sum(pram1, pram2):
    '''
    이것은 두 수를 받아 두수의 합을 반환하는 함수 입니다.
    make_sum(1,2)
    3
    '''
    return pram1 + pram2
```

 1. def make_sum(x, y):
    - def: 정의 
    - make_sum: 함수 이름
    - (x, y): 변수 이름
 2. result = x + y
    - 계산
 3. return result
    - 출력 
```python
result = make_sum(100, 200)
print(result) # 300
```

print 함수는 반환값이 없다.
- result2 = print(100) >>> print가 작동되면서 출력 반환값은 없으므로 result2에는 None이 된다.
- print(result2) >>> result2가 반환값을 못 받아 아무것도 없는 None 이므로 None이 출력된다
- <span  style="color:red"> **즉, print는 출력이 되지만 반환값이 있는 것은 아니다.** </span>
```python
result2 = print(100) # 100
print(result2) # NOne
```

## 매개변수

1. def add( x, y): 함수정의
-  여기서의 (x, y)는 "매개변수" 이다.

2. add(x, y): 함수 실행
- 함수 실행 시의 (x, y)는 "인자" 이다.
- 인자에는 변수명이 들어간다.

## 다양한 인자 종류
인자: 함수를 호출할 때, 실제로 전달되는 값  
1. 위치 인자(Positional Arguments)
- 함수 호출시 인자의 위치에 따라 전달되는 인자
- 위치 인자는 함수 호출 시 반드시 값을 전달해야 함
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살 이시군요.')

greet('Bob') #에러
greet('bob', 25) # 올바르게 출력 됨
```
----------
2. 기본 인자 값
- 함수 정의에서 매개변수에 기본 값을 할당한다.
- 인자를 전달하지 않으면 기본 값이 매개변수에 할당된다.
```python
def greet(name, age= 30):
    print(f'안녕하세요, {name}님! {age}살 이시군요.')

greet('Bob') # 안녕하세요, Bob님! 30살 이시군요.
greet('alice', 20) # 안녕하세요, alice님! 20살 이시군요.
```
----------
3. 키워드 인자(Keyword Arguments)
- 키워드 인자는 위치 인자 앞에 나타날 수 없다.
- 즉 키워드 인자는 위치 인자 뒤에 위치해야 함
- 위치 인자는 무조건 앞에 있어야 한다.

```python
def greet(name, age= 30):
    print(f'안녕하세요, {name}님! {age}살 이시군요.')

greet(age = 35, name ='Dave') #정상 출력
greet(age =35, 'Dave') # 오류
```
**왜 위치 인자가 앞에 와야 할까?**
순서의 모호성 때문.
- 순서 의존: 위치인자는 첫 번쨰, 두번쨰라는 순서에 따라 값이 전달됨
- 순서파괴: 키워드 인자는 순서를 무시하고 이름을 직접 지정함
------
4. 임의의 인자 목록(Arbitrary Argument Lists)
- 함수 정의시 매개변수 앞에 *을 붙여 사용
- 여러개의 인자를 tuple로 처리
- 인자가 없어도 됨.
```python
def calculate(*args): # 몇 개가 들어올지 모른다.
    print(args)
    print(type(args)) # <class 'tuple'>

```
-------
5. 임의의 키워드 인자 목록(Arbitrary Keyword Argument Lists)
- 함수 정의시 매개변수 앞에 **을 붙여 사용
- 여러개의 인자를 dictionary로 묶어 처리
```python
def print_info(**kwargs):
    print(kwargs)

print_info(name ='Eve', age = 30) # {'name': 'Eve, 'age': 30}
```

인자 권장 작성 순서  
위치 -> 기본 -> 가변 -> 가변 키워드
## 재귀함수
함수 내부에서 자기 자신을 호출하는 함수  
대표예시: 팩토리얼, 피보나치
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # 120
```
```python
# f(n) = f(n-1) + f(n-2)
# f(0) = 0 f(1) = 1
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(7)) # 13
```
- 재귀함수 특징
  - 코드의 가독성이 높아짐
  - 1개 이상의 base case(종료되는 상황)가 존재하고 수렴하도록 작성
- 재귀함수 활용 시
  - 종료 조건을 명확히 할 것
  - 반복되는 호출이 종료 조건을 향하도록 할 것
  - 종료조건을 잘못할 시 스택 오버플로우 에러가 발생할 수 있다.

## 내장함수 (Bulit-in function)
기본적으로 내장된 함수
- 이미 검증되고 최적화된 기능, 적극 활용하기
- 성능과 효율성
자주 사용되는 함수
```python
len()
max()
min()
sum()
sorted(num, reverse = True) # 5 4 3 2 1
```
파이썬 공식문서 보기.

## 함수와 스코프
함수는 내부에 local scope를 생성하며 그 외의 공간인 global scope로 구분  
- scope
  - local scope : 함수 내부만 가능
  - global scope : 코드 어디서든 참조가능

- variable
  - local variable(지역변수)
  - global variable(전역변수)  
LEGB Rule  
Bulit_in - 정의하지 않아도 사용 가능한 함수  
함수는 local > Enclosed > Global > Bulit_in 순으로 찾으러 감.
```python
sum = 5
sum(list) >> # 5(list) 가 된다 즉 오류가 남
```
![사진]("정규수업/LEGB_rule.png")

## global 키워드
- 주의사항
- global 키워드 선언 전 참조 불가
- 매개변수에는 global 키워드 사용불가
```python
num = 0 #전역변수
def inc():
    global num
    num+= 1
print(num) # 0
inc()
print(num) # 1
```
---------------------- 
- 함수 이름은 동사로, 약어 지양
- return 이 True/False 일시 is or has 로 시작하기
## 단일 책임 원칙
함수는 하나의 명확한 목적과 책임만 가져야함  
함수는 한 가지 작업만 수행

## Packing *

여러개의 데이터를 하나의 컬렉션으로 모아 담기  
*을 활용한 패킹  
을 활용한 패킹

## Unpacking
**
튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당  
**을 활용한 언패킹
- 리스트나 튜플 앞에 **을 붙여 각 요소를 함수의 개별 위치 인자로 전달

|구분|상황|*연산자|**연산자|
|------|-----|----|-----|
| 패킹 | 함수 정의 시 | 여러 위치 인자를 하나의**튜플**로 받음| 여러 키워드 인자를 하나의 **딕셔너리**로 받음|
|언패킹|함수 호출 시| 리스트/튜플을 개별 **위치 인자**로 전달| 딕셔너리를 개별 **키워드 인자**로 전달|


## 람다
lambda  
- 일회성 사용 함수
- 간단한 연산이나 함수를 한 줄로 표현 가능
- 함수를 필요로 하는 곳에서 즉석에서 로직 작성 가능