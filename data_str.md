# Data Structure
데이터 구조: str, list, dict  
메서드: 문자열, 리스트, 딕셔너리 등 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기
## 메서드
**객체**에 속한 **함수**
- class 내부에 정의되는 함수  
- 클래스는 파이썬에서 타입을 표현하는 방법
```python
'hello'.capitalize() # Hello
number = [1, 2, 3]
number.append(4) # 1, 2, 3, 4
```
## 공통 시퀀스 메서드 
s.index(x) : 시퀀스에서 첫 번째로 일치하는 항목 x의 인덱스를 반환  
s.count(x) : 시권스 s에서 등장하는 항목  x의 개수를 반환

무조건 있어야 되면 index / 없어도 코드를 실행시키고 싶으면 find
## 불변 시퀀스 메서드(문자열 전용)
s.find(x): x의 첫번쨰 위치를 반환 없으면, -1을 반환  
s.isupper(): 문자열 내의 모든 케이스 문자가 대문자인지 확인  
s.islower(): 문자열 내의 모든 케이스 문자가 소문자인지 확인  
s.isalpha(): 문자열의 모든 문자가 알파벳이고 하나 이상의 문자가 포함되어 있으면 True를 반환

## 문자열 조작
**새로운 문자열 반환** >> 문자열은 불변이기 때문  
`str.replace(old, new[, count]):` 기존 문자열에서 'old'라는 부분 문자열을 'new'로 모두 변경
```python
text = 'Hello, world! world world'
text.replace('world', 'Python') # Hello Python Python Python
text.replace('world', 'Python', 1) # Hello Python world world
```
`str.strip([char])`: 선행과 후행 문자가 제거된 문자열의 복사본을 돌려줌  
집합으로도 제거 가능 char 중 하나라도 있으면 계속 제거
```python
text = '   Hello     world    '
text.strip() # 아무것도 지정하지 않을시 공백 제거
# Hello     world 중간의 공백은 제거되지 않는다.
text = '!!!hello world!!!'
text.strip('!') # Hello world
```
`str.split(sep = None, maxsplit = -1)`: sep을 구분자 문자열로 사용하여 문자열에 있는 단어를 리스트화
```python
text = 'Hello world'
text.split() # ['Hello', 'world']
text ='1, 2, 3, 4'
text.split(',') # ['1', '2', '3', '4']
text.split(maxsplit = 1) # 한번만 자름
```
`str.join(iterable)`: 구분자로 iterable의 문자열을 연결한 문자열을 반환  
반복 가능한 문자열을 연결하여 출력
```python
words = ['python', 'is', 'awesome']
' '.join(words)# python is awesome
'_'.join(words)# python_is_awesome
```

## 가변 시퀀스 메서드(리스트 전용)
L.append(x): 리스트 마지막에 항목 x를 추가  
append는 반환값이 없다 > print(L.append(x)) # None이 출력  
L.extend(iterable): iterable의 모든 항목들을 리스트 끝에 추가  

.pip() 또는 .pop(i): 지정한 항목의 인덱스를 제거하고 반환  
제거한 데이터를 다른 변수에 저장하는 것, 미 작성시 마지막 항목 제거
```python
list = [1, 2, 3, 4]
item = list.pop() # 4
item1 = list.pop(0) # 1
list # [2, 3]
```
l.reverse(): 리스트의 순서를 역순으로 변경  
l.sort(): 리스트 정렬. 기본값은 오름차순 # 내림차순: reverse=True

## 객체와 참조
가변/불변의 객체의 개념  
가변객체
- 생성 후에도 그 내용을 수정할 수 있음
- 객체의 내용이 변경되어도 같은 메모리 주소 유지
- 크기가 큰 데이터를 효율적으로 수정
불변객체
- 생성 후 그 값을 변경할 수 없음
- 여러 변수가 동일한 객체를 안전하게 공유할 수 있음
- 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨
- 메모리 사용을 최소화
### 가변 객체
```python
a = [1, 2, 3, 4]
b = a # a의 주소를 b에 할당한 것이다.
b[0] = 100
print(a) # 100, 2, 3, 4
print(b) # 100, 2, 3, 4
print (a is b) # True

a = 10
b = a
b = 20 # 불변이므로 a의 값은 바뀌지 않는다
print(a)# 10
print(b)# 20
print(a is b)# False
```
id()함수를 통해 객체의 메모리 주소 확인가능

## 얕은 복사
객체의 최상위 요소만 새로운 메모리에 복사하는 방법  
내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨  
얕은 복사 구현 방법
1. 리스트 슬라이싱
2. copy() 메서드
3. list() 함수
```python
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]] 
# 최상위 리스트는 복사되고 내부 리스트는 참조한다.
b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]
# 내부 리스트는 원래 객체를 참조한다.
```
## 깊은 복사
객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법  
중첩된 객체까지 모두 새로운 객체로 생성됨

```python
import copy
b = copy.deepcopy(a)
```
## List Comprehension
list comprehension을 사용하는 것이 파이썬 내부적으로 성능이 조금 더 좋다
```python
numb = []
for num in numbers:
    numb.append(num**2)
# OR
numb = [num**2 for num in numbers]
```
위 두 식은 출력 값이 같다.
```python
data1 = [[0] * (5) for _ in range(5)]
# OR
data2 = [[0 for _ in range(5)] for _ in range(5)]
```
코드의 가독성은 기존이 더 좋으니 COmprehension을 남용하지 말자
**"Simple is better than complex"**  
**"Keep it simple. stupid"**

## 리스트를 생성하는 3가지 방법
loop(반복문), list comprehension, map  
성능비교
1. list comprehension
   - 가장 Pythonic 하고 대부분의 경우 우수한 성능을 보임
2. map
   - 특정상황(int, ster 등 내장함수와 함께 사용)에서 가장 빠름
  - 사용자가 직접 만든 함수가 lambda와 함께 사용될 때는 list comprehension과 성능이 비슷하거나 살짝 느릴 수 있음
3. for loop
   - 일반적으로 가장 느리다고 알려졌지만 python 버전이 오라가면서 비슷하거나 더 나은 결과
   - but 여러 줄에 걸친 복잡한 조건문이나 예외 처리 등에는 유일한 선택지이며 그 자체로 매우 유용하다.
- 결론
  - 성능 차이는 마이크로초 단위로 매우 미미하므로 코드의 가독성과 유지보수성을 최우선으로 고려하여 상황에 맞는 가장 명확한 방법을 선택하는 것을 권장

## 메서드 체이닝
여러 메서드를 연속해서 호출하는 방식
```python
text.swapcase().replace('z', 'l') # 대소문자 변경 후 z -> l로 변경
```
메서드 체이닝에서의 실수
```python
result = number.copy().sort()
print(result) # None sort의 반환값이 없기 떄문

number.append(7).extend([8, 9]) 
# append는 None을 반환하기 떄문에 NOne에 extend를 하는 꼴이기 때문에 불가능
```
주의사항
- 모든 메서드가 체이닝을 지원하는 것이 아님
- None을 반환하는 메서드는 메서드 체이닝이 불가 ex) append(), sort()
- 메서드 체이닝을 사용할 떄는 각 메서드의 반환 값을 잘 이해해야 함