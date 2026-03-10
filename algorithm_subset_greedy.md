# 조합적 문제  
## 부분 집합

순서 X 
```py
arr = [True, False]
name = ['MIN', 'CO', 'TIM']
def subset_recur(n, path):
    if n == 3:
        print(*path)
        return
    for i in range(2):
        if arr[i]:
            subset_recur(n+1, path+[name[n]])
        else:
            subset_recur(n+1, path)

for i in range(2):
    if arr[i]:
        subset_recur(0, [])
```
부분집합 구하기 
```py
def get_subset():
    for i in range(1 << n):
        for j in range(n):
            if i &(1 << j):
                print(arr[j], end=' ')
        print()
get_subset1()
```
부분집합 세기 따로 함수로 빼기
```py
def get_sub(tar):
    for i in range(n):
        if tar & 0x1:  # 1, True등 써도 되지만 부분집합 계산시 16진수로 쓰는게 약속
            print(arr[i], end=' ')
        tar >>= 1

for tar in range(1 <<n):
    print()
    get_sub(tar)
```

5명 중 N명을 뽑을 것이다.
```py
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []
# 깊이 3
# 자식 5
def recur(idx, prev):
    if idx == 3:
        print(*path)
        return
    # 이전에 선택한 것을 고르지 않는다.
    for i in range(prev+1, len(arr)):
        if visited[i]:
            continue
        
        path.append(arr[i])
        recur(idx+1, i)
        path.pop()
recur(0, -1)
```

# 탐욕 알고리즘
## Greedy 
결정이 필요할 때, 현재 기준으로 가장 좋아 보이는 선택지로 결정하여 답을 도출하는 알고리즘  
그리디가 맞는지 어떻게 아는가?    
**증명을 해야한다!!**    
어떤 문제가 그리디인가?     
1. 규칙성을 찾아야 한다  
   - 규칙성을 못 찾으면 못 푼다.  

2. 규칙을 찾았다!  
   - 그리디로 풀 수 있는 지 검증한다.   
   1. 탐욕적 선택 조건(Greedy CHoice Property)  
        - 각 단계의 최적해 선택이 이후 단계의 선택에 영향을 주지 않는다.   
        - 즉, 각 단계 규칙이 변경되면 안된다.   
        - ex) 동전 문제
          - 첫 번째 단계: 가장 큰 동전(500원)으로 가능한 만큼 준다.
          - 두 번째 단계: 가장 큰 동전(100원)으로 가능한 만큼 준다.
          - 세 번째 단계: 가장 큰 동전(50원)으로 가능한 만큼 준다.
          -  -> 각 단계의 규칙이 유지되고, 이전에 구했던 최적해 선택이 각 단계에 영향 X

   2. 최적 부분 구조(Optimal Substructure)   
        - 각 단계의 최적해 선택을 합하면, 전체 문제의 최적해가 되어야 한다. 
            - 증명을 통해 해결
        - 동전 문제 예시
          - [명제] 가장 큰 동전부터 순서대로 고르면 최소 동전 수가 나온다.
          - [간접증명] 최적해보다 더 작은 수의 동전으로 표현 가능하다 (가정)
          - -> N원을 더 작은 수의 동전으로 표현할 수 있다. 
          - --> 동전이 배수로 있기 때문에 숫자가 더 작으면 무조건 더 큰 수의 동전 
          - --> 수학적으로 말이 안된다(더 작은 수로 나누었는데 몫이 작다)
          - --> 모순 발생(원래 명제가 참)

   3. 반례가 없는가?  
   4. 
  