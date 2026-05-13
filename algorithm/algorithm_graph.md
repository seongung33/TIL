# 그래프
아이템(사물 또는 추상적 개년)들과 이들 사이의 연결 관계를 표현    


## 그래프 유형
- 무향  
- 유향
- 가중치
- 사이클 없는 그래프
- 완전 그래프: 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프: 원래 그래프에서 일부 정점이나 간선을 제외한 그래프

## 그래프 경로
- 간선들을 순서대로 나열 한 것
- ex) 정점 0에서 정점 6으로 가는 경로 
  - 간선들로 표현: (0, 2), (2, 4), (4, 6)
  - 정점들로 표현: 0 - 2 - 4 - 6
- 단순경로 한 정점을 한번만 지나는 경로
- 사이클 - 시작과 끝이 같음: 1 - 3 - 5 - 1

## 그래프 표현

## 인접 행렬 vs 인접 리스트
인접 행렬
- 단점
  - 메모리 낭비
- 장점
  - 특정 노드간 연결 정보를 바로 구할 수 있다.  

인접 행렬 코드
```py
V, E = map(int, input().split())

# 인접 행렬(0, 1 로 연결 유무를 모두 저장)
# V+1인지 V 인지 생각
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start][end] = 1
    # 무향일경우
    graph[end][start] = 1
```
인접 리스트 
- 장점
  - 메모리 절약
- 단점
  - 특정 노드간 연결 정보를 바로 알 수 없다.

인접 리스트 코드(연결된 정보만 저장)
```py
V, E = map(int, input().split())
graph = [[]for _ in range(V)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    #무향이면
    graph[end].append(start)
```

## DFS 깊이우선탐색


## Union-Find (Disjoint Set)
Disjoint Set: 서로소 집합    

### 서로소 집합 연산 
- make-set(x)
- find-set(x)
- union(x, y)

```py
# 유니온파인드 코드

def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

def find_set():
    
    # 자기 == 부모 ->
    if x == parents[x]:
        return x
    # 부모가 대표자인지 검색

    # 경로압축 코드
    parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = finde_set(y)

    if ref_x == ref_y:
        return
    # 둘 중 하나를 바꿔준다.
    # 반대로 해도 상관없다.
    parents[ref_y] = ref_x
    # parents[ref_x] = ref_y

    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x
        ranks[ref_x] += 1

N = 6
parents = make_set(N)
```
어디에 쓰이는가?    
집합 관련 문제   

```py
N = 10

p = [0] * (N+1)

#자기 자신이 대표인 집합 만들기
def make(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    
    return find_set(p[x])

# 경로 압축
def find_set2(x):
    if x != p[x]:
        p[x] = find_set2(p[x])

    return p[x]

def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    if king_x == king_y:
        return
    
    p[king_y] = king_x

p = [i for i in range(N+1)]
```