터미널에 cd

cd .. : 폴더 뒤로가기

cd {name} : 해당 폴더로 들어가기

python {파일명} : 해당 파일 실행 / 폴더 내에 있어야 함

```python

# 표현식

3 + 5

4 < 10

4 * 5

```

```python

# 값 : 표현식이 평가된 결과

# 모든 값은 그 자체로 단순한 표현식이지만, 모든 표현식이 값은 아니다.

103.56

"안녕하세요"

True, False

```

변수는 특정 객체를 가리키는 이름표, 변수는 메모리 주소를 가지지 않습니다.

값(Object) = 객체 이는 메모리에 저장되어 있는 객체이다.

변수는 메모리에 저장되어 있는 객체를 가리키는 이름이다.

```python

#Numeric Types

int(123)

float(103.56)

complex(1+2j) # 실수 + 복소수

#Text Sequence Type

str("Hello, World!")

#Sequence Types

list

tuple

range

#Non-Sequence Types

set

dict

#기타

bool

None

# function


```

```python

3*4 # 12 곱셈  

10/2 # 5 나눗셈

# // #몫 나눗셈

# % #나머지

# ** #거듭제곱

# - #음수

```



```python

#리스트



my_list = [1, 'a', 3, 'b', 5]

print(my_list[1]) # a



my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]

print(len(my_list)) # 5

print(my_list[4][-1]) # !!!

print(my_list[-1][1][0]) # 마지막 리스트의 두번째 문자열의 첫번쨰 w


```

```python

#인덱싱 값 수정

my_list = [1, 2, 3, 4, 5]

my_list[1] = 'two'



print(my_list)# 1, 'two', 3, 4, 5

```

```python

#튜플

mytuple_1 = ()

mytuple_2 = (1,) #단일요소 튜플 생성 시 후행 쉼표(Trailing comma) 사용

mytuple_3 = (1, 'a', 3, 'b', 5)

mytuple_4 = 1, 'hello', 3.14, True



#튜플의 불변성

mytuple = (1, 'a', 3, 'b', 5)

mytuple[1] = 'z' # TypeError



#다중할당

x, y = 10, 20

#실제 동작

(x, y) = (10, 20)

```

```python

range

range(stop)

range(start, stop)

range(start, stop, step)

range(5) # range(0, 5)

list(range(5)) # [0, 1, 2, 3, 4]

list(range(5, 0, -1)) # [5, 4, 3, 2, 1]



#반복문

for i in range(1, 10):

    print(i) #1 2 3 4 5 6 7 8 9

```

```python

#dictionary

#순서 X

my_dict_1 = {}

my_dict_2 = {'key': 'value'}

my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_3['list'])



my_dict = {'apple': 12, 'list': [1, 2, 3]}

my_dict['banana'] = 50 #값 추가

my_dict['apple'] = 100 #value 값 변경

print(my_dict)

#key의 규칙

#key는 중복이 불가함

#변경 불가능한 자료형만 사용가능 > str int float tuple



#value의 규칙 

#모든 형태가 가능

```

```python

#set

#순서와 중복이 없는 변경 가능한 자료

my_set_1 = set()     # set()

my_set_2 = {1, 2, 3} # 1 2 3

my_set_3 = {1, 1, 1} # 1



#집합

my_set_1 = {1, 2, 3}

my_set_2 = {3, 6, 9}



#합집합

print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}



#차집합 

print(my_set_1 - my_set_2) #{1, 2}



#교집합

print(my_set_1 & my_set_2) # {3}

```

```python

None

#값이 존재하지 않음

#빈 상자와 같다.



my_variable = None

print(my_variable) # None

```

```python

#Boolean

True

False

```

```python

from IPython.display import Image

Image("C:/Users/SSAFY/Desktop/문성웅/pic.png")



#str, list, tuple = 시퀀스 /나머지 비시퀀스

```

### 불변

- 변경불가, 안전성, 예측가능

- str, tuple, range



### 가변

- 변경가능, 유연성, 효율성

- list, dict, set

```python

# 형변환

# 정수와 실수의 합

print(3 + 5.0) # 8.0



# 불리언과 정수의 합 > True =1

print(True + 3) # 4



#불리언간의 합

print(True + False) # 1

```

```python

#명시적 형변환

from IPython.display import Image

Image("C:/Users/SSAFY/Desktop/문성웅/형변환.png")

```

```python

#복합 연산자

a = 5

a += 3 # 8



b =4

b *= 2 # 8



c = 20

c //=7 # 2



d =10

d /= 4 #2.5

```

```python

# == 연산자 동등성(equality)

#값이 같은가

print(1 == True) # True

print(2 == 2.0) # True



# is 연산자 식별성(identity)

print(1 is True) # False

print(2 is 2.0) # False

# is 는 메모리 주소를 비교하는 것



None, True, False # 사용시 is 권장

```



```python

a = [1, 2, 3]

b = [1, 2, 3]

# 동일한 객체가 아니기 때문

print( a == b) # True

print ( a is b) # False



#동일한 객체로 변경

b = a

print( a is b ) # True

```

단축 평가

```python

# in

# not in

word = 'hello'

numbers = [1, 2, 3, 4, 5]

print('h' in word) # True

print('z' in word) # False

```