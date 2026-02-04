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
i & (i<<j) : i의 j 번째 비트가 1인지 아닌지를 검사

### 비트 연산으로 부분집합 생성하기
```python
arr= [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n): # 2**n
    for j in range(n): # 원소의 수만큼
        if i & (i<<j): # 0번 밀었다.
            print(arr[j], end=', ')
    print()
print()
```