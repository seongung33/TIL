# 스택  
## 후위 표기법 변환  

### 문자열로 된 계산식

#### 중위 표기법의 후위 표기법 변환 방법
1. 우선순위에 따라 괄호 사용
2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
3. 괄호를 제거한다.
4. ex) A*B-C/D -> AB\*CD/-  

두번째 방법.  **stack**  
1. 입력받는 주우이 표기법에서 **토큰**을 읽는다. /토큰이란? 데이터를 처리하는 기본 단위  
2. 토큰이 피연산자(+, - 등)면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때
   - 이 토큰이 스택의 TOP에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,
   - 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때 까지 
   - 스택에서 pop 한 후 토큰의 연산자를 push한다. top에 연산자가 없으면 push 한다.
4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼쪽 괄호를 찾을 때 까지 pop을 수행한다. 
5. 중위 표기법에 더 읽을것이 없다면 중지하고 더 읽을 것이 있다면 1부터 다시 반복한다.
6. 스택에 남아 있는 연산자를 모두 pop 하여 출력한다.   

토큰의 우선순위를 알아야 한다.   
isp: 스택안에 들어 갔을 경우의 우선순위  
icp: 스택 밖에서의 우선순위   
스택 안의 우선순위가 스택 밖의 우선순위보다 낮으면 push 한다.   
우선순위가 동일하면 스택 안의 우선 순위가 더 낮지 않으므로 pop 한다.  
스택 밖 > 스택 안 : push  
동일 순위 : pop  
```py
stack = [0] * 10
top = -1
# 우선순위
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}# 스택 밖에서의 우선순위  
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}# 스택 안에서의 우선순위    

infix = '(6+5*(2-8)/2)' # 중위식 문자열  
postfix = '' # 후위식 문자열  
for token in infix:
    # 피연산자
    if token not in '(/*-+)': # 피연산자면 후위식에 추가
        postfix += token

    elif token in ')': # 닫는 괄호면 여는 괄호 만날떄까지 pop
        while top > -1 and stack[top] !='(':
            top -= 1
            postfix += stack[top+1]
        # 열린 괄호 따로 제거
        if top != -1:
            top -= 1

    elif token in '(/*-+': # else:
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token 
        # 안에 있는 것이 더 크다면
        elif isp[stack[top]] >= icp[token]:
            # 스택 안에 더 낮은 우선순위가 있을때까지 꺼내라
            while top > -1 and isp[stack[top]] >= icp[token]:
                top -= 1
                postfix += stack[top + 1]
            # 꺼냈으면 다시 푸쉬 하기
            top += 1
            stack[top] = token

while top > - 1:
    top -= 1
    postfix += stack[top + 1]
```
함수화 (위는 top 아래는 append)
```python
#우선순위 표
icp = {'(':3, '+':1, '-':1, '/':2, '*':2} # 바깥
isp = {'(':0, '+':1, '-':1, '/':2, '*':2} # 스택 안

#infix ->중위표기식
# n: 식의 길이
def get_postfix(infix, n):
    postfix = ''
    stack = []
    for i in infix:
        if i not in '/*-+()':
            postfix += i
        elif i ==')':
            while stack:
                op = stack.pop()
                if op == '(':
                    break # while stack
                postfix += op

        elif i in '(/*-+':
            # 스택이 비어있거나 바깥의 연산자 우선순위가 더 크면
            if not stack or isp[stack[-1]] < icp[i]:
                stack.append(i)
            else:
                while stack and isp[stack[-1]] >= icp[i]:
                    op = stack.pop()
                    postfix += op
                stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix
infix = '(6+5*(2-8)/2)'
n = len(infix)
print(get_postfix(infix, n)) # 6528-*2/+
```

## 후위표기법 연산  
후위 표기법 식을 stack을 이용하여 계산   
1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여(연산자 하나면 두개) 연산하고 연산 결과를 다시 스택에 push한다.
   - 먼저 꺼낸게 오른쪽위치 두번째가 왼쪽 위치
3. 수식이 끝나면 마지막으로 스택을 pop하여 출력한다.  
```py
stack = []
for token in postfix:
    if token not in '/*-+':
        stack.append(int(token)) # 기존 형태는 str이므로 int로 변환
    else:
        right = stack.pop() # 오른쪽 피연산자
        op1 = stack.pop() # 왼쪽 피연산자
        if token == '*': # 곱셈
            stack.append(op1*op2)
        elif token == '/': # 나눗셈
            stack.append(op1/op2)
        elif token == '+':
            stack.append(op1+op2)
        elif token == '-':
            stack.append(op1 - op2)
answer = stack.pop()
print(f"{answer:.0f}")

print(f"{9.5:.0f}") # 10, 반올림 한다..? 실수의 뒷자리 값 기준
print(f"{int(9.5)}") # 9, 버림한다. 내림이 아닌 소수점을 "절삭" 하는 것

```
연산 2
```py
stack = []
def postfix_cal(postfix):
    for i in postfix:
        if i not in '/*-+':
            stack.append(int(i))
        else:
            if i == '/':
                right = stack.pop()
                left = stack.pop()
                result = left / right # 정수로 하고 싶으면 int() or //
                
            elif i == '*':
                right = stack.pop()
                left = stack.pop()
                result = left * right
                
            elif i == '-':
                right = stack.pop()
                left = stack.pop()
                result = left - right
                
            elif i == '+':
                right = stack.pop()
                left = stack.pop()
                result = left + right
            
            stack.append(result)
    # 최종 결과는 stack에 한개 저장되어있다.
    return stack.pop()
postfix = get_postfix(infix, n)
print(postfix_cal(postfix))


```
## Backtracking 백트래킹
후보해를 구성해 나가다가, 더 이상 해가 될 수 없다고 판단되면 되돌아가서 다른 후보를 찾는다.  
- 재귀 기반
- 완전 탐색을 효율적으로 구현  
- 가능성이 있는 해를 추가해가며 완전한 해인지 검사
- 추가한 해가 가능성이 없는 경우 이를 취소하고 다시 검색한다.
- 최적화 문제와 결정 문제에 적용
- ex) N-Queen, 미로, 순열/조합, 부분집합, 스도쿠, map-coloring  

### Backtring과 DFS의 차이
- DFS는 그래프의 모든 노드에 대한 탐색, Backtracking은 완전 탐색 문제에 대한 접근 방법
  -  Backtracking은 상태공간 트리
  -  상태 공간 트리를 DFS로 탐색하는것과 같다.
- **Pruning(가지치기)**
  -  Backtracking은 선택한 부분 후보 해가 가능성이 없다면 더 이상 그 경로를 따라가지 않는다.  
- 경우의 수가 많은 문제인 경우
  -  N!인 경우의 수를 가졌다면 모든 수를 탐색할 수 없다.
  -  Backtracking을 적용하면 일반적으로 경우의 수가 줄어든다. 
  -  단, 최악의 경우에는 지수함수 시간을 요하므로 처리가 **불가능**하다.  
  -  
### Backtracking 기법
- 유망하지 않은 노드로 결정되면 그 노드의 부모로 되돌아가 다음 자식노드로 이동한다.
- 방문한 노드가 해답이 될 수 없으면 유망하지 않다고 하며, 해답의 가능성이 있으면 유망하다.
- 가지치기(pruning): 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않는다.  
- for 문 안의 if visited가 가지치기 중 하나.
- 단 목적지에 도달해도 for문 안에서 다른 방향으로 진입한다. 
- 이를 방지하기 위한 조건도 필요. 이게 없으면 dfs와 반복횟수가 같다.


### 미로찾기  
1.
stack에 현재위치를 push하기. stack을 이용하여 지나온 경로를 역으로 돌아감    
돌아갈때도 한칸씩 돌아간다.  
2. 
현재 위치에서 갈 수 있는 모든칸을 push 하고 하나를 pop해서 이동  
갈림길에서 여러 경로를 저장함. 한쪽 길이 막다른 길이면 다음 pop시 다른 갈림길로 바로 이동한다.  

### N-Queen 문제
체스판에서 N개의 퀸을 놓을 수 있는가? 또는 경우의 수는?
- 상하좌우, 대각 방향에 다른 퀸이 없어야 한다.
```py
def place_queen(i, n):
    if i == n: # 이미 모든 퀸을 놓은 경우
        write_the_solution() # 답 기록하기
    else:
        for j in range(n): # 모든 열에 대해
            if promising(i, j): # 놓을 수 있는가?
                place_queen(i+1, n) # 놓을 수 있으면 다음행 시도
```
### 부분집합 
어떤 집합의 공집합과 자기자신을 포함한 모든 부분  
첫번째 원소부터 0 or 1을 골라가며 진행 다 고르면 백트래킹 하여 다른 값 넣으면서 돌기
### 순열
백트래킹하며 순열 구하기
```py
lst = [1,2,3,4,5]
N = 5
selected = [0]*N # 사용한 원소 표기
result = []
def make_perm(idx, selected, result):
    if idx == N:
        print(result)
        return
    for j in range(N):
        if not selected[j]:
            selected[j] = 1
            result.append(lst[j])
            make_perm(idx+1, selected, result)
            selected[j] = 0
            result.pop()
make_perm(0, selected, result)
```
## 가지치기

### 부분집합의 합 
각 원소에 대해 포함 여부를 트리로 구현   
i 원소의 포함 여부를 결정하면 부분집합의 합 Si를 결정할 수 있음   
- 가지치기 
    1. Si-1이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요가 없음(Backtraking)   
    2. 현재 원소의 합과 남은 원소의 합이 찾고자 하는 합보다 작을 경우
    3. 이 외의 추가 조건 적기 ex) 1을 제외시킬래 등
이전 원소의 합으로 계산: 간결한 코드, 누적합으로 계산
```py
# s = i-1 원소까지의 합, t: 찾으려는 합
def f():
    if s == t: # i-1의 합이 찾는 값인 경우

    elif i == N: # 끝난경우
        return
    elif s > t: # 목표값보다 큰 경우. 1. 번 가지치기 이다.
        return
    elif S + RS < T: #(고려한 원소의 합) + 앞으로 더해질 수 있는 원소의 합 < 목표 값
    else: # 남은원소가 있고 s < t 인 경우
        for:
            f(i+1)
```
ver 2  
가지치기 사용시 가능한 조건인지 잘 생각하고 사용하자
```py
def make_set(idx, selected):
    # 답이 될 가능성이 없으면 더이상 진행하지 않는다.
    # 가지치기
    if s > S:
        return
    if idx == N:
        subset = []
        for i in range(N):


```


### 순열 2 
경우의 수 : n!   
자리 교환으로 순열 생성  
각 도시간의 이동시 비용이 다를경우 모든 순서를 나열해본다.  
최소비용 찾기, 
```py
# 자리 교환 방식
#자리 주인을 정하는 방식의 순열.
lst = [1, 2, 3, 4, 5]
def f(idx, N):
    if idx == N:
        print(p)
    else:
        # 인덱스 원소와 다른 위치에 있는 원소를 하나 정하고 자리를 바꾼다.
        # 다른위치의 idx보다 작으면 안된다.
        for j in range(idx, N):
            lst[idx], lst[j] = lst[j], lst[idx]  # 자리바꾸기
            f(idx+1, N)
            lst[idx], lst[j] = lst[j], lst[idx] # 원상복구
f(0, len(lst))
```

## 분할정복  
분할: 해결할 문제를 여러 개의 작은 부분으로 나눈다.  
정복: 나눈 작은 문제를 각각 해결한다.  
통합: (필요하다면)해결된 해답을 모은다.  

거듭제곱 
O(n)  
### 분할정복 기반의 알고리즘: O(logn)
시간 복잡도를 O(logn) 까지 줄일 수 있다.
C**8 = 
C\*\*n = C\*\*(n/2) x C\**(n/2) : n이 짝수
        C\*\*(n/2) x C\**(n/2) x C : n이 홀수
```py
 def power(base, exponent):
    if exponent == 0:
        return 1
    
    if exponent % 2 == 0:
        new_base = power(base, exponent//2)
        return new_base * new_base

    else:
        new_base = power(base, (exponent-1)//2)
        return (new_base * new_base) * base
```