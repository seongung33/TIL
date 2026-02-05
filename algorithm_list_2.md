# 2차원 배얄
```python
N = int(input())
arr = [list(map(int, input().split()))  for _ in range(N)] #matrix 모양
```
0으로 채워진 배열  
```python
# 3 X 4 행렬
arr = [list([0]* 4) for _ in range(3)]
#얕은 복사로 인해 불가능
# arr =[[0]* 4] * 3
len(arr) # 행의 크기
len(arr[0]) # 열의 크기
```
행 우선 순회
```python
# i 행
# j 열
for i in range(n): 
    for j in range(m):
        arr[i][j]
```
열 우선 순회
```python
for i in range(m):
    for j in range(n):
        arr[j][i]
```
지그재그 순회
```python
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j) * (i%2)] 
        # i%2 은 홀수일때만 작동하게 하기 위함
        # 홀수일 때 반대로 출력하려면 m - 1- j 가 되어야 한다. 하지만 짝수일때를 위해 j를 더했으므로
        # m - 1이 된다. 따라서 m - 1- 2*j로 하여 최종적으로 m-1- j가 된다.

    if i % 2 : # 0과 1로 boolean값이 됨
        for j in range(m-1, -1, -1)
```
j값이 커지고 작아지고 반복하는법: (m - j - 1) * (i % 2)

## 델타 
델타를 활용한 2차원 배열 탐색  
세로이동 i, 가로이동 j  
- 아래는 탐색순서 오른쪽, 아래, 왼쪽, 위 순서
- di[] <- [0, 1, 0, -1]  # 방향별로 더할 값
- dj[] <- [1, 0, -1, 0] 
for k : 0 -> 3
    ni <- i + di[k]
    nj <- j + dj[k]

인접 배열 요소 탐색
for i : 0-> N -1
    for j : 0 -> N-1
        for d in range(4) :
            ni <- i + di[d]
            nj <- j + dj[d]
            if - <= ni < N and 0 <= nj < N #유효한 인덱스 검사
                arr[ni][nj]

```python
arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
N = 3
M = 4
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        # for d in range(4):
        #     ni = i + di[d]
        #     nj = j + dj[d]
        #     if 0 <=ni < N and 0 <= nj < M:
        #         print(arr[ni][nj])  

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                print(arr[ni][nj])
```

### 델타 응용
N x N 배열에서 각 원소를 중심으로 상하좌우 k칸의 합계 중 최댓값 

## 전치 행렬
대각 행렬을 기준으로 행과 열을 바꾼다
zip을 사용하여 할 수도 있다.
```python
for i in range(N):
    for j in range(M): # for j in range(i) 사용시 if문 필요없음
        if i < j: # 대각 행렬 떄문이 아니라 두 번 바꾸는 문제가 발생하여 전치 행렬을 두 번 하게 된다
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
대각행렬 사용시 i == j   
for i in range(N):  
    arr[i][i]  

반대 대각행렬 N-1-i == j

## 부분집합 합 문제
유한 개의 정수로 이루어진 집합이 있을 때 이 집합의 부분집합 중에서 조건에 맞는 문제  
부분집합의 수 2**n 개 -> 공집합 포함 수

### 부분집합의 원소를 표현하는 법
arr[i] 원소가 부분집합에 없을 시 bit[i] == 0
arr[i] 원소가 부분집합에 있을 시 bit[i] == 1
```python
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit) # 존재하는 값만 출력되게? 잘 모르겠음
```
### 비트 연산자
& : 비트 단위로 AND 연산    
해당 값들을 bit 즉 0과 1인 2진법으로 만든 후 비교한다.  
ex) 1101 & 1001 출력시 두 값 모두 1인 1001으로 나온다.  
| : 비트 단위로 OR 연산  
\<< : 피연산자의 비트 열을 왼쪽으로 이동  
ex) 1 << 3 일경우 1을 비트로 변형 후 3비트 이동하는 것  
즉 ob1 << 3 결과: 0b1000 = 8 이다.
\>> : 피연산자의 비트열을 오른쪽으로 이동

1<< n : 2**n 즉 원소가 n개일 경우의 모든 부분집합의 수를 의미  
i & (1<<j) : 1을 왼쪽으로 j번 이동 즉 j번 비트가 0인지 아닌지 검사.   
i의 값에 상관없이 j번 비트 뺴고는 모두 0이 된다.   
j번 비트가 1이면 != 0 이다.  
이를 if에 넣으면 i의 j번 비트가 1이라면 True 이다.

### 비트 연산으로 부분집합 생성하기
```python
arr= [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n): # 2**n 부분집합의 개수
    for j in range(n): # 원소의 수만큼 비트가 비교
        if i & (1<<j): # i의 j번 비트가 1인경우
            print(arr[j], end=', ')
    print()
print()
```

# 검색과 정렬
## 순차검색
### 검색
저장되어 있는 자료 중에서 원하는 항목을 찾는 작업  
탐색 키: 자료를 구별하여 인식할 수 있는 키  
- 순차검색
  - 일렬로 되어 있는 자료를 순서대로 검색하는 방법
    - 간단하고 직관적
    - 검색 대상의 수가 많다면 수행시간이 급격히 증가합니다.
    - 순차 구조로 구현된 자료구조에서 유용하다.
  - 정렬 여부에 따라
    - 순차 검색 대상이 정렬되어 있지 않은 경우
    - 순차 검색 대상이 정렬되어 있는 경우  

### 정렬되어 있지 않은 경우
1. 첫번쨰 원소부터 순서대로 검색, 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스 반환
3. 검색 대상을 찾지 못하면 검색 실패  

검색 성공시: (1/n)*(1+2+...+n) = (n+1)/2    
검색 실패시: n  
시간 복잡도: O(n)
```py
for i in range(n):
    if a[i] == key:
        return i
```
### 정렬되어 있는 경우
1. 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다.
2. 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없는 것.  
정렬이 되었으므로 / 정렬시간 + 검색시간 (n + 1)/ 2  
시간 복잡도 : O(n)      
```py
for i in range(n):
    if a[i] == key:
        retrun i
    elif a[i] > key:
        return -1
```
## 이진 검색(Binary Search)  
자료 가운데에 있는 항목의 키 값과 비교하여 다음 검색 위치를 선정한다.  
자료가 정렬되어 있어야 한다.  
1. 자료의 중앙 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 작으면 자료의 왼쪽에서, 크면 자료의 오른쪽에서 새로 검색을 수행한다.
4. 값을 찾을때까지 이를 반복한다.
```py
def binary_search(a, N, key):
    start = 0
    end = N - 1
    while start < = end:
        median = (start + end)// 2
        if a[median] == key: # 키 값 찾음
            return median
        elif a[median] > key: # 중앙값이 더 크면
            end = median - 1 # 왼쪽 구간 탐색
        else:                # 아니면 
            start = median + 1  # 오른쪽 구간 탐색
    return -1
```
재귀함수를 통한 이진 검색 
이진 탐색은 주로 반복문으로 만든다.  
```py
def binary_search2(a, low, high, key):
    if low > high:
        return False

```
### 인덱스 
원본 데이터 인덱스와 별개로 배열 인덱스를 추가할 수 있다.  
원본 데이터의 각 데이터를 쪼개서 원본 데이터의 인덱스 값과 함께 가져와 새로운 데이터셋을 만든다.  
그럼 새로운 데이터 셋에는 인덱스, 데이터, 원본 데이터의 인덱스를 가지게 된다.  
여기서 인덱스를 통해 데이터를 확인하고 원복 데이터의 인덱스 값을 이용하여 원본 데이터에서 찾는다.  

## 선택 정렬(select sort)  
오름차순: 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환한다.  
1. 주어진 리스트에서 최솟값 찾기
2. 그 값을 리스트 맨 앞에 위차한 값과 교환
3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복  

시간 복잡도 : O(n**2)
```py
def selection_sort(arr, N):
    # arr: 정렬하고 싶은 배열
    # N: 원소의 개수

    #오름차순
    # arr 안에서 제일 작은 원소를 0번 인덱스로
    # 그 다음으로 작은 원소를 1번으로
    for i in range(N-1): #자리를 안 정해줘도 됨
        #i번 자리의 주인은 arr 안에서 i번쨰로 작은 원소
        min_idx = i
        for j in range(i, N):
            if arr[min_idx] > arr[j]: #오름차순이므로 최솟값 찾기
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
```

## 셀렉션 알고리즘  
k번째로 작은 알고리즘  
선택 정렬을 k번째까지 한다.
```py
def slection_(arr, k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if a[min_idx] > a[j]:
                min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
```