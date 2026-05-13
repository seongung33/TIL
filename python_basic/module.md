# Module

## math 내장 모듈  
```python
import math
print(math.pi)_ # 3.14~~
```
- import 절 사용
  - math.pi 
  - . 연산자, 모듈간의 충돌을 방지한다
  - 단, 코드가 길어질 수 있음

```python
from math import pi, sqrt
print(pi)
print(sqrt(6))
```
- from 절 사용
  - pi
  - 코드가 짧고 간결해짐
  - 정의된 모듈의 위치를 알기 어려워 명시적이지 않음
  - 사용자가 선언한 변수 또는 함수와 겹쳐 모듈의 동작이 이뤄지지 않을 수 있음

- as 키워드
  - 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올때 발생하는 이름 충돌 해결
  - as를 통해 키워드 변경 가능
```python
from math import sqrt
from my_math import sqrt as my_sqrt
sqrt(4)
my_sqrt(4)
```
## 패키지
연관된 모듈들을 하나의 디렉토리에 모아 놓은 것  
직접 만든 패키지 사용법 > from my_package.math import my_math.py  

- 패키지 설치하는법: pip install <name>
- 설치한 패키지는 pip freeeze > requirements.txt로 버전 정보를 기록해 둡니다.
pip list : 설치된 패키지 목록


## 제어문
코드의 실행 흐름을 제어하는 데 사용되는 구문  
**조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행  
상황에 따라 다른 코드를 실행하거나 같은 코드를 여러 번 반복 할 수 있게 합니다.  

## 조건문
if / elif / else  
주어진 조건식이 참(True)인 경우 실행되거나 건너 뜀  
코드는 위에서 아래로 입력되므로 **순서** 잘 맞출 것
```python
if a == 0:
    b = 1
elif a == 1:
    b = 2
else:
    b = 4
```
## 반복문
for / while
주어진 코드 블록을 여러 번 반복해서 실행하는 구문  
### for
- for
  - 반복 가능(iterable)한 객체
  - 반복 가능한 객체의 요소 개수만큼 반복
  - 반복 횟수가 정해져 있음
```python
stu = ['alice', 'Bob', 'charlie']
for st in stu:
    print(f'Hello, {st}!') # 세 번 출력
```
iterable: 요소를 하나씩 반환할 수 있는 모든 객체  
1. stu의 리스트 내 변수가 할당되고 코드 블록이 실행됩니다.  
2. 다음 반복 시 다음 변수가 할당되고 코드 블록이 실행됩니다.  
3. 마지막 변수 요소까지 할당되고 코드 블록 실행 후 종료됩니다.
- for문이 가능한 순회
  - 문자열 ex) 'korea' 5 바퀴
  -  range() ex) range(5) 5바퀴 0~4까지
  -  딕셔너리: 기본적으로 key를 추출합니다. value 사용시 dict[key] 사용
  -  인덱스로 list 순회 for i in range(len(list))
- 중첩 반복문
  - 중첩 리스트 시 중첩 반복문을 이용할 수 있다.
```python
elements = [['a', 'b']. ['c', 'd']]
for ele in elements:
    for item in elem:
        print(item)
# 출력시
# a
# b
# c
# d

```

### while
- while
  - 조건이 참(True)인 동안 반복 == 조건이 거짓(False)이 될 때 까지 실행
  - 반복 횟수가 명확하게 정해지지 않음
```python
a = 0
while a < 3:
    print(a)
    a += 1
```
반드시 **종료 조건**이 필요하다.  
반복문 내부에서 변수 값을 변하시키는게 좋아요.
break를 이용하여 반복문을 종료 할 수도 있습니다.

## 반복 제어
break / continue/ pass
- break
  - 해당 키워드를 만나면 즉시 반복 종료
  - 반복을 끝내야 할 명확한 조건이 있을때 사용
```python
numbers = [1, 3, 5, 6, 7, 9]
found_even = False # flag 변수
for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다')
```
- continue
  - 해당 키워드를 만나면 다음 코드는 무시하고 즉시 다음 반복 수행
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
```
- pass
  - 아무 동작도 하지 않음
  - 반복 제어가 아닌 코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도
  - 코드를 비워두면 오류가 발생하기 때문에 pass 사용
  - 반복문, 함수, 조건문에도 사용가능

## 유용한 내장 함수 map & zip
### map(function, iterable)
반복 가능한 데이터구조(iterable)의 모든 요소에 fucntion을 적용하고, 그 결과 값들을 map object 로 묶어서 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result) # <map object at 0x000~>
print(list(result)) # ['1', '2', '3']
```
map은 형 변환을 해야함. 하지 않으면 덩어리로 나온다.
```python
numbers = [1, 2, 3]
list(map(lambda x:x**2, numbers))
```
### zip(*iterables)
zip 함수는 여러 개의 반복 가능한 데이터 구조를 묶어서 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 그것들을 모아 zip object로 반환하는 함수

```python
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]
for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)
#출력값
# (10, 20, 40) 0번 인덱스 값
# (20, 40, 20) 1번 인덱스 값
# (30, 50, 30) 2번 인덱스 값
# (50, 70, 50) 3번 인덱스 값
```
- 2차원 리스트의 같은 컬렴(열) 요소를 동시에 조회할 때 실행결과가 **전치 행렬**과 동일함
