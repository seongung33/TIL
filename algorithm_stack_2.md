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

### Backtracking 기법
- 유망하지 않은 노드로 결정되면 그 노드의 부모로 되돌아가 다음 자식노드로 이동한다.
- 방문한 노드가 해답이 될 수 없으면 유망하지 않다고 하며, 해답의 가능성이 있으면 유망하다.
- 가지치기(pruning): 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않는다.  

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
