# Stack
## 스택
물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조  
후입선출(LIFO) : 가장 마지막에 넣은 자료가 가장 먼저 나오는 것  
1, 2, 3 으로 넣으면 3, 2, 1로 나온다.  

### 스택의 기본 연산
스택 구현
    - 배열을 사용해 구현할 수 있다.(파이썬은 list)
    - 저장소 자체를 스택이라 부르기도 한다. 
    - 스택에서 마지막 삽입된 원소의 위치: 스택 포인터, top이다.   
스택의 연산
    - 삽입(push)
      - 저장소에 자료를 저장하는 연산, 보통 push라 부름
    - 삭제(pop)
      - 저장소에서 삽입한 자료의 역순으로 꺼내는 연산, 보통 pop이라 부름
    - 공백 확인(isEmpty)
      - 비어 있으면 True 아니면 False
    - 스택의 top 원소(item) 반환(peek)
      - 삭제 X

## 스택 구현 실습
### push 연산  
- append 메소드를 통해 리스트의 마지막에 데이터를 삽입
- 인덱스 연산을 활용한 구현
```python 
# append
# 성능이 좋지 않다.
stack = []
def my_push(item):
    s.append(item) # append, pop: top 지정 없이 사용가능. 실제로 해당 값을 리스트에서 제거한다.
# index
# 크기를 예측해야 한다.

#스택 포인터
top = -1
#스택의 크기
N = 10
stack = [0]* N
# 스택 삽입
for i in range(1, 11):
    top += 1
    stack[top] = i
#스택이 꽉 찼나 확인해야 한다.
if top < N -1:
    top += 1
    stack[top] = 11
else:
    print('overflow')

def my_push(item, size):
    global top
    top += 1
    # 스택이 가득 차 있는가 확인해야 한다.
    if top = size: # 스택이 꽉 차면 저장 X
        print('Overflow') # 디버깅용
    else:
        stack[top] = item #저장

# 크기가 정해진 리스트와 인덱스 연산 활용
size = 10
stack[0] * size
top = -1
my_push(10, size)
top += 1        # push 20
stack[top] = 20
```
### pop 연산  
- 남은 데이터 중 가장 늦게 저장 된 데이터를 삭제하는 연산
- 값을 꺼낸다는 것이 해당 값을 지운다는 것이 아니다.
- 다시 push를 한다면 top의 위치에 따라 해당 데이터의 값이 변경되기 때문에 상관이 없다.
- 크기가 정해진 리스틍 인덱스 활용
```python
# pop 함수 사용
stack.pop()

# stack안에 모든걸 꺼내고 싶다.
stack = [i for i in range(10)]
while stack: # list내에 무언가가 존재하면 True, 아무것도 없으면 False 이다.
    element = stack.pop()
    print(element, end = ',') # 9 8 7 6 5 4 3 2 1 0
print()
print(stack) # []

#스택에서 자료 삭제
for i in range(10):
    element = stack[top]
    top -= 1
    print(element, end=',')
print()
print(stack, top) #실제로 stack에는 그대로 남아있다. 하지만 top을 기준으로 생각하여야 한다.
# 남아있는 데이터들은 의미 없는 더미 데이터로 볼 수 있다.

# 크기가 정해진 리스트 인덱스 활용

def my_pop():
    if len(s) == 0:  # 아무것도 없다면꺼낼 수 없다.
        print('Underflow') # 디버깅 용
        return 0
    else:
        top -= 1
        return stack[top+1]
print(my_pop())

if top > -1:
    top -= 1
    print(stack[top+1])
```
### 고려 사항
1차원 배열을 사용하여 구현할 경우
   - 장점: 구현이 용이하다.
   - 단점: 스택의 크기를 변경하기가 어렵다.
해결방법: 저장소를 동적으로 할당하여 스택을 구현한다.(동적 연결리스트)
- 장점: 메모리를 효율적으로 사용합니다. 
- 단점: 구현이 복잡하다.

## 스택 구현 코드
```python
top = -1
stack = [0] * 10
# push 1
top += 1
stack[top] = 1
# push 2
top += 1
stack[top] = 2
# push 3
top += 1
stack[top] = 3
# pop
top -= 1
print(stack[top+1]) # pop 3

st = []
st.append(1) # push 1
st.append(2) # push 2
st.append(3) # push 3
print(st.pop()) # pop 3
```
## stack의 응용  
괄호 검사   
여는 괄호는 push 하여 스택에 넣는다.  
닫힌 괄호가 나온다면 pop 하여 비교한다.
```python
data = '({[f{[a]b}b]})'
n = len(data)
top = -1
stack = [0] * 100
for i in range(n):
    # print(top)
    if data[i] in '{[(':
        top += 1
        stack[top] = data[i]

    elif data[i] in ')}]':
        if top == -1:
            ans = 'Error'
            break # for i
        else:
            top -= 1
            # 괄호 종류 비교
            if stack[top+1] == '(' and data[i] == ')':
                continue
            elif stack[top+1] == '{' and data[i] == '}':
                continue
            elif stack[top+1] == '[' and data[i] == ']':
                continue
            else:
                ans = 'Error'
                break # for i
if  top != -1:
    ans = 'Error'
else:
    ans = 'yes'
print(ans)
print(stack)
```

## Function Call  
프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리  
가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조  
**시스템 스택**  
  - 함수 수행에 필요한 지역변수 매개변수 및 수행 후 복귀할 주소 등의 정보를 저장
  - 함수 호출이 발생하면 스택 프레임에 저장하여 시스템 스택에 삽입  

함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제(pop)하면서 프레임에 저장된 복귀 주소를 확인하고 복귀합니다.  
함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시트템 스택은 공백이 됩니다.

## 재귀호출
n에 대한 factorial
n! = n * (n - 1)!
         (n - 1)! = (n - 1) * (n-2)!
              ...
2! = 2* 1!
        1! = 1
