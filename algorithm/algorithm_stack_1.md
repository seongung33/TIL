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
A함수 에서 B 함수 호출 B함수에서 C 함수 호출 C -> B -> A 순으로 종료된다.
프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리  
가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조  
**시스템 스택**  
  - 함수 수행에 필요한 지역변수 매개변수 및 수행 후 복귀할 주소 등의 정보를 저장
  - 함수 호출이 발생하면 스택 프레임에 저장하여 시스템 스택에 삽입  

함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제(pop)하면서 프레임에 저장된 복귀 주소를 확인하고 복귀합니다.  
함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시트템 스택은 공백이 됩니다.

## 재귀호출
함수가 자신과 같은 반복 작업을 할때 자신을 다시 호출하는 구조    
각 함수마다 메모리의 위치가 완전히 다르다.(구분된 상태) 메모리상 완전히 다른 함수 호출  
메모리 그림 그려보기    

각 함수가 메모리 영역을 가지고 해당 영역안에 필요한 값을 저장해둔다. 이게 스택처럼 쌓이고  
한 스택처럼 함수가 종료된다.
### n에 대한 factorial
n! = n * (n - 1)!
         (n - 1)! = (n - 1) * (n-2)!
              ...
2! = 2* 1!
        1! = 1    
### 피보나치 수열  
0과 1로 시작하고 이전 두 수의 합을 다음 항으로 한다.  
F0 = 0, F1 = 1  
Fi = F(i-1)+ F(i-2), for i>= 2
```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
```
fibo(n-1)+fibo(n-2) : 메모리를 보면 fibo(n-1)이 완료된 후 fibo(n-2)가 실행되게 된다.  
이때 fibo(n-2)의 메모리는 fibo(n-1)이 사용했던 메모리를 다시 사용하게 된다.(새로운 함수로)  
### 재귀함수의 기본형 
```py
def f(i, N):
    if i == N: # 중단
        return
    else:   # 재귀호출
        f(i+1, N)
```
메모리가 처음부터 쭉 함수를 차곡차곡 쌓고 마지막부터 다시 함수가 종료된다.  
(스택처럼 처음부터 함수가 쌓이다가 top부터 함수가 return되면서 완료된다.)  

모든 배열 원소에 접근하는 재귀함수
```py
def f(i, N):
    if i == N:
        return 
    else:
        print(A[i])
        return f(i+1, N)

A = [1, 2, 3]
print(f(0, 3))
```
배열 원소 검색
```py
def f(i, N, V):
    if i == N:
        return 0
    elif A[i] == V:
        return 1
    else:
        return f(i+1, N, V)

V = 2
N = 4
A = [1,2,3,4]
ans =f(0, N, V)
print(ans)
```
2차원 배열 순회 재귀 함수  
행 우선 순회이다.
```python
N = 5
arr = [[N*j + i for i in range(1, N+1)] for j in range(N)]
def arr2(x, y, arr, N):
    if x==N-1 and y ==N-1:
        print(arr[x][y])
        return
    
    elif y == N-1:
        print(arr[x][y])
        return arr2(x+1, y-N+1, arr, N)
    # elif y == N-1:
    #     print(arr[x][y])
    #     return arr2(x-N+1, y)
    else:
        print(arr[x][y], end = ' ')
        return arr2(x, y+1, arr, N)
arr2(0,0,arr,N)
```
## Memoization (메모이제이션)
피보나치 수열의 경우 중복호출이 많다. 이를 방지하기 위해 메모이제이션을 사용한다.  
이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 실행속도를 빠르게 한다.  
**동적 계획법**의 핵심이 되는 기술이다.   
memoization을 적용한 피보나치: 계산된 값이 있는 피보나치 수는 저장된 값을 리턴  
피보나치는 O(2**n) 이지만 메모이제이션을 사용하면 O(n)으로 줄일 수 있다.
```py
def fibo1(n):
    if n>= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)# 계산된 값을 memo에 저장한다.
    return memo[n] # 계산된 값이 있으므로 해당 값을 반환한다.

n = 10
memo = [0]* (n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))
```

## DP (Dynamic Programming)
입력 크기가 작은 부분 문제들을 먼저 해결한 뒤 그 결과를 바탕으로  
더 큰 부분 문제를 차례대로 해결해 나가며 최종적으로 전체 문제의 해답을 도출한다.
- DP 적용 문제
  - 문제의 최적 해가 그 하위 문제의 최적 해로부터 쉽게 구성될 수 있는 최적 부분 구조여야 합니다.
  - 동일한 하위문제가 여러 번 반복되어 나타나는 중복 부분 문제여야 합니다.   

피보나치 수열을 DP로 구현 
```py
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
```
메모이제이션 보다는 반복구조 DP 가 더 성능 면에서 효율적이다.  
재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.  
오버헤드: 추가적인 자원 소모나 처리 시간을 발생시키는 부가적인 비용

## DFS (깊이 우선 탐색, Depth First Search)
깊이 우선 탐색: 한 방향으로 가능한 한 깊게 탐색한 후 더이상 갈 곳이 없으면 되돌아와 다른 방향을 탐색  
스택을 사용하는 이유: 마지막 갈림길로 되돌아 오기 위함이다.  
DFS 동작 원리
  - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지 깊이 탐색해 나간다.
  - 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서  
  - 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 탐색방법  

로봇이 선을 따라 모든 칸을 탐색하는 방법  
1. 시작 정점  V 결정
2. 갈림길로 진입하면 해당 지점을 스택에 넣고 한 쪽으로 진행한다.
3. 지나가는 곳도 스택에 넣는다..
4. 더이상 갈림길이 없다면 스택에서 제거하며 되돌아 간다.
5. 방문하지 않은 곳으로 동일하게 진행한다.  

DFS 알고리즘
visited[], stack[]
DFS(v):
    시작점 v 방문
    viseited[v] = True






### DFS A형 노리자! 
DFS 알고리즘
```py
visited = []
stack = []
def dfs(v, w, way):
    visited[v] = 1

    while True:
        if not visited[w]: # is False
            stack.append(v)
            w = v
            visited[w] = 1
        else:
            if not stack:
                v = stack.pop()
            else:
                break
```

인접 리스트
```python
graph = list(map)
# V번째 까지 비어있는 2차원 리스트이다.
adj_list = [[] for_ in range(V + 1)] # 인접 리스트
# i번 행: i번 정점에 인접한 정점번호
for i in range(E): # 1번 행에 인접한 정점 번호 2, 3 과 같은 식
    v, W = graph[i*2], graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v)
```
처음부터 다시  
인접 행렬 생성
```py
adj_matrix = [[[0]*N] for _ in range(N)]
# 1번 정점과 2번 정점이 인접
adj_matrix[1][2] = 1
adj_matrix[2][1] = 0 # 유향 그래프에서 A->B인 경우. 즉 B에서 A로 못 가기 때문
# 3번과 4번이 인접 하지 않음
adj_matrix[3][4] = 0
```
인접 행렬 그래프를 통한 깊이 탐색
DFS
```python
s = 정점 번호
V = 정점의 개수
def dfs(s, V):
    #dfs 깊이 우선 탐색
    #그래프의 모든 정점을 빠짐없이 한번씩 모두 탐색
    #방문한 곳 저장
    visited = [0] * V

    # 스택
    stack = []

    #시작 정점 방문
    visited[x] = 1
    # 정점에서 할 일 작성
    print(x)
    # 현재 내가 방문하고 있는 정점 번호 v
    v = s

    #그래프 탐색
    while True:
        # 현재 정점 위치
        # v와 인접한 정점(w) 확인, 있다면 방문하였는가?
        # 방문 가능하면 방문한다.
        for w in range(V):
            #v와 w가 인접하고 , w를 방문한적 없다면 방문한다.
            if adj_matrix[v][w] and not visited[w]:
                # w는 갈 수 있다.
                # 방문처리 w정점에서 필요한 작업을 한다.
                # w에서 더이상 갈 길이 없으면 v로 돌아와야 하니
                # v를 스택에 저장
                stack.append(v)
                # w 방문
                visited[w] = 1
                # 정점에서 할 일
                print(w)
                # w로 이동후 탐색 반복하기
                v = w
                # 반복 중단/ 바뀐 v로 새로운 탐색을 이어가야 한다.
                break # for w
        else:
        # 반복 중 break 한 적이 없다. -> 이동 가능한 다른 정점이 없다,
        # 이전 길로 돌아가기
            if stack:
                # 스택에서 꺼낸 위치로 돌아간다.
                v = stack.pop()
            else:
                #스택이 비어서 돌아갈 곧이 없다면 모든 정점 탐색완료
                break # while True
dfs(0, 7)
```

