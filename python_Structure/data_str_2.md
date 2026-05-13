# 비 시퀀스 데이터 구조
## 딕셔너리
D.get(key[, default]): 키와 연결된 값을 반환하거나 키가 없으면 None 혹은 지정한 값을 반환
```python
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown
```
D.keys(): 딕셔너리 키를 모은 객체를 반환
map, range 같이 평가를 미룬다.
```python
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age']) 평가를 미룸
for item in person.keys():
    print(item)
```
D.values(): 딕셔너리 값만 출력  

D.items(): 딕셔너리 키/값 쌍을 모은 객체를 반환
```python
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items(): # 키와 밸류 값 지정으로 튜플로 나옴
    print(key, value)
```
.pop(key[, default]): 키를 제거하고 연결된 값을 반환한다.  
값이 없으면 에러나 default를 반환한다.
```python
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
print(person.pop('country')) # Error
```
.clear(): 딕셔너리의 모든 키/값 쌍을 제거한다.

.setdefault(key[, default]): 키와 연결된 값을 반환한다.  
키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환  
get은 단순 반환 setdefault는 값 추가까지
```python
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country', 'KOREA'}
# 키가 없으면 해당 키와 값을 추가한다.
```
.update([other]): other가 제공하는 키/값 쌍으로 딕셔너리를 갱신한다.  
기존 키와 겹친다면 추가된 키/값 으로 교체한다.
```python
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}
print(person) # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}
# Alice 가 Jane으로 교체되었다.
person.update(age =100, adderss = 'SEOUL') #키 = 값으로 표현 가능하다.
```
## 세트
set
- set은 내부적으로 해시테이블을 사용하여 저장합니다.
- 항목의 고유성을 효율적으로 보장, 항목의 추가, 삭제, 존재 여부 확인이 매우 빠릅니다.
- 합집합, 교집합, 차집합 등 수학적인 집합 연산을 간편하게 수행할 수 있습니다.
- 가변데이터, 중복 불가

.add(x): 세트에 x를 추가  

.update(iterable)

.clear() : 모든 항목 제거, 세트의 경우 set()으로 표기된다 중괄호는 딕셔너리가 가져갔기 때문

.remove(x): 세트에서 항목 x를 제거, x가 없을경우 keyError

.pop: **임의의** 요소를 제거하고 **반환**  
순서가 없기 때문에 임의로 제거된다. (무작위와는 다르다.)

.discard(x): 세트에서 항목 x를 제거. remove와 달리 에러가 없음

### 집합 메서드
아래 두개 모두 같이 작동한다.
- set1.difference(set2)  set1 - set2
- set1.intersection(set2)  set1 & set2
- set1.issubset(set2) set1 <= set2
- set1.issuperset(set2) set1 >= set2
- set1.union(set2) set1 | set2

## 비 시퀀스 데이터 구조에서의 이해해야할 내용

### 딕셔너리의 확장: defaultdict
defaultdict: 파이썬 내장 모듈 collections에서 제공하는 딕셔너리의 확장판  
defaultdict(자료형)
- 숫자세기 defaultdict(int), 키가 없으면 0
- 그룹핑/리스트 모으기: defaultdict(list) 키가 없으면 빈 리스트 []
- 조회만 해도 key가 생성된다. 키가 있는지 확인할 때는 get
- setdefault는 호출할 때마다 기본값을 넣어야 하지만 defaultdict는 한 번만 설정하면 된다.
```python
from collections import defaultdict

fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
fruit_by_color = defaultdict(list)

for color, fruit in fruits:
    # color 키가 없으면 빈 리스트 생성 -> append 바로 가능
    print(fruit_by_color)
    fruit_by_color[color].append(fruit)
    pass

print(fruit_by_color)  
# defaultdict(<class 'list'>, {'red': ['apple', 'cherry'], 'yellow': ['banana']})
print(dict(fruit_by_color))  
# {'red': ['apple', 'cherry'], 'yellow': ['banana']}
```
### 파이썬 문법 규격
BNF: 프로그래밍 언어의 문법을 표현하기 위한 표기법  
서로 다른 프로그래밍 언어, 데티어 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함  
메타기호
- [] 선택적 요소
- {} 0번 이상 반복
- () 그룹화

## 해시테이블
해시테이블은 키와 값을 짝지어 저장하는 자료구조   
원리
1. 키를 해시함수를 통해 해시 값으로 변환
2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
3. 이로 인해 검색, 삽입, 삭제를 매우 빠르게 수행

**해시**: 임의의 크기를 가진 데이터를 고정된 고유한 값으로 변환

**해시 함수**: 임의 길이 데이터를 입력받아 고정 길이(정수)로 변환해 주는 함수. 이 **정수가 해시 값** 이다.  

set
- 요소를 해시함수를 통해 버킷(정수값)으로 변환하고 출력한다. 
- 버킷에 따라 위치가 변한다.  
- 해시 함수는 매 실행마다 변하기 때문에 set는 매번 버킷 값이 달라지며 위치가 달라진다.   

dict 는 set 와 달리 삽입 순서를 유지해 준다.  

#### set의 pop 메서드 예시 - 정수  
- 정수 값은 해시 값이 자기 자신으로 그대로 쓴다.
- 단, 같은 값은 아니다. 
- 정수만으로 이루어진 set를 pop 한다면 매번 똑같은 순서로 pop이 진행된다. 
- 하지만 set은 순서가 없으므로 pop 되는 순서를 예측할 수는 없다. 
#### 문자열
- 문자열은 해시 계산 시 해시 난수화(Hash Randomization)가 적용되므로 실행순서가 매번 다르다.
### 파이썬에서의 해시 함수
같은 정수는 항상 같은 해시 값을 가진다.  

문자열 해시 시 파이썬 인터프리터 시작때 설정되는 난수 시드가 달라질 수 있음
```python
print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행 단위 마다 다르다.
print(hash('a')) # 위와 같은 값이 나온다.
```
**hashable**  
- hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미
- 대부분의 불변 타입은 해시 가능
- 가변 데이터는 hashable 하지 않다.
- 동일 키 -> 동일 위치로 가정하고 빠른 수행을 하는데 키가 바뀐다면 이 규칙이 깨짐  

필요한 이유
1. 해시 테이블 기반 자료 구조 사용
   - set의 요소, dict의 키
   - 중복 방지 & 빠른 검색, 조회
2. 불변성을 통한 일관된 해시 값
   - 한 번 해시값이 정해지면 바뀌지 않아야 해서 테이블 무결성이 유지
3. 안정성과 예측 가능성 유지
    - 동일한 데이터는 항상 동일한 해시 값을 반환 -> 로직을 단순화