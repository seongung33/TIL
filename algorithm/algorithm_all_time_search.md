# 완전탐색

## 반복과 재귀
반복과 재귀는 유사하다.   
1. 시작과 끝 지점이 필요하다.
2. 누적된 값

```py
# 0~10을 출력
# 0 부터 시작 -> 10에서 종료(10보다 커지면 종료)
def recur(num):
    if num > 10:
        return

    print(num)
    recur(num+1)
# 0 1 2 3 4 5 6 7 8 9 10 9 8 7 
# 이렇게 다시 10~ 0으로 돌아가고 싶으면 아래와 같이 씁니다.
        print(num)
recur(0)
```
재귀의 형태: 상태공간 트리라 부른다.    
높이: 기저조건이 결정한다.  == 재귀호출의 깊이    
가지의 수: 재귀호출 수   
깊이: 1부터 기저조건 까지 깊이로 생각한다 보통 시작이 1이다. (0은 생각 x)    

## 순열 
### 중복순열    
[0, 1, 2] 3개의 카드가 존재(2개를 뽑는 모든 경우)  

기저조건: 2개의 카드를 모두 뽑았을 경우  
시작: 0개의 카드를 고른 상태에서 시작  
```py
path = []

def recur(cut):
    if cut == 2:
        print(path)
        return

    for i in range(3):
        path.append(i)
        recur(cut+1)
        path.pop()
    # # 0을 선택
    # path.append(0)
    # recur(cut+1)
    # path.pop()
    # #1을 선택
    # path.append(1)
    # recur(cut+1)
    # path.pop()
    # # 2를 선택
    # path.append(2)
    # recur(cut+1)
    # path.pop()
recur(0)
```
전역변수 안 쓰고 하기  
```py
def recur(cut, a):
    if cut == 2:
        print(*a)
        return
    for i in range(3):
        recur(cut+1, a +[i])
recur(0, [])
```

```py
def recur(cut, a):
    if cut == 3:
        print(*a)
        return

    for i in range(1, 7):
        recur(cut + 1, a + [i])
recur(0, [])
```

### 중복 없는 순열

```py
N = 3
visited = [False]*N

def recur(cut, a):
    global visited
    if cut == 2:
        print(*a)
        return

    for i in range(3):

        if visited[i]:
            continue
        visited[i] = True

        # if i in a: # 시간복잡도 O(N) 개구림 방문으로 대체
        #     continue

        recur(cut+1, a +[i])
        visited[i] = False
recur(0, [])
```
주사위 3개의 합이 10 이하인 케이스의 수
```py
N = 7
def recur(cut, total, cnt):

    if cut == 3:
        if total <= 10:
            cnt += 1
        return cnt
        
    if total >= 10:
        return cnt

    for i in range(1, N):
        cnt = recur(cut+1, total+i, cnt)
    return cnt
cnt = recur(0, 0, 0)
print(cnt)
```