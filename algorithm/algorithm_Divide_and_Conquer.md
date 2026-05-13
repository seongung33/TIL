# 분할정복
문제를 작은 하위 문제로 나누고 각각 해결한 뒤  
그 결과를 결합하여 원래 문제를 해결하는 알고리즘 기법   

- 분할(Divide): 해결할 문제를 여러개의 작은 부분으로 나눔  
- 정복(Conquer): 나눈 작은 문제를 각각 해결  
- 통합(Combine): 해결된 해답을 모음  

구조: Top-down approach   
- 분할: 절반씩 하는 것이 편하다. 
- 정복: 더 이상 쪼갤 수 없을 때 까지, 혹은 해결 가능할 때 까지

필요하지 않은건 버린다.   
메모이제이션을 이용하여 효율적으로 사용할 수 있다.  

## 병합 정렬
1. 여러 개의 정렬된 자료의 집합을 
2. 병합하여 한 개의 정렬된 집합으로 만드는 방식    

O(nlogn)    
쪼갤 때: logn  --> N개를 절반으로 쪼개면서 1로 만드는 횟수   
N개 모두 1개 단위로 쪼개야 하므로 NlogN 이 나온다.   

```py 
arr = [69, 10, 30 ,2, 16, 8, 31, 22] 

# 1. 분할하는 과정
# - depth: 리스트의 길이가 1이 되면 끝
# - branch: 왼쪽과 오른쪽으로 리스트 분할
def merge_sort(li):

    if len(li) == 1:
        return li

    mid = len(li)//2
    left_list = merge_sort(li[:mid])
    right_list = merge_sort(li[mid:])

    merge_list = merge(left_list, right_list)
    return merge_list
# 2. 병합하는 과정(정렬하며 병합)
def merge(left, right):
    left_idx = 0
    right_idx = 0

    result = [0]*(len(left) + len(right))
    while left_idx < len(left) and right_idx < len(right)

    if left[left_idx] > right[right_idx]:
        result[left_idx + right_idx] = right[right_idx]
        r += 1
    else:
        result[left_idx + right_idx] = left[left_idx]
        l += 1

    while left_idx < len(left):
        result[left_idx + right_idx] = left[left_idx]

    while right_idx < len(right):
        result[left_idx + right_idx] = left[right_idx]

    return result

sorted_arr = merge_sort(arr)

print(sorted_arr)
```
슬라이싱 없이 구현하기
```py
arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

def merge_sort(start, end):
    if start  == end - 1:
        return start, end
    mid = (start + end) // 2
    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    merge(left_s, left_e, right_s, right_e)
    return start, end

def merge(left_s, left_e, right_s, right_e):

    l = left_s
    r = right_s

    N = right_e - left_s
    result = [0] * N

    idx = 0

    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
    
    for i in range(N):
        arr[left_s + i] = result[i]
    print(result)
merge_sort(0, N)
```


## 퀵 정렬 
기준값(Pivot)을 중심으로 주어진 배열을 두 개로 분할하고 각각을 정렬하여 전체 배열을 정렬하는 방식   
기준 아이템을 중심으로 기준보다 작은 것을 왼편, 큰 것을 오른편에 위치 시킴  
별도의 병합 과정 불필요  

시간 복잡도:  pivot의 설정에 따라서 달라진다. (데이터의 분포에 따라 달라진다.)
평균: O(nlogn): 
    - 실제 연산 시간이 효율적이다. 
    - 데이터가 많을수록 효율적이다.
최악: O(N^2)
    - 반대로 정렬될수록 최악의 시간 복잡도
    - pivot을 처음에 설정하고 pivot의 위치가 인덱스 끝 부분에서 결정될때

**파티셔닝** 
1. 작업영역 지정
2. 작업 영역 중 가장 왼쪽에 있는 수를 Pivot이라고 하자
3. Pivot을 기준으로 
    - 왼쪽에는 Pivot 보다 작은 수를 배치한다
    - 오른쪽에는 Pivot 보다 큰 수를 배치한다

### hoare_partition 호어 파티션
피벗 + 1 = i    
인덱스의 끝 = j     
i는 피벗보다 큰 값  
j는 피벗보다 작은 값을 찾는다.   
둘 다 찾으면 두 값을 교환한다.  
만약 두 값이 교차하기 직전이라면 i와 피벗을 교환하고 종료한다.  
```py
arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

def quick_sort(A, l, r):
    if l < r:
        p = hoare_partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)
    
def hoare_partition(A, l, r):
    p = A[l]
    i = l
    j = r
    
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    # 기존 피벗의 위치가 맨 앞 이었으므로 해당 위치에는 작은 값이 와야한다.
    # i와 j가 엇갈려 끝났으므로 j는 작은 영역 i는 큰 영역에 위치해 있다.
    # 이를 위해서 피벗 위치의 값은 j 즉 작은 영역에 위치한 값과 
    # 자리를 바꿔야 피벗의 위치 맨 앞에는 작은 값이 들어온다.
    A[l], A[j] = A[j], A[l]
    return j
quick_sort(arr, 0, N-1)
print(arr)
```


### Lomuto Partition  로무토 파티션  
논리는 같지만 i, j를 앞에서부터 이동한다.  


## 이진 검색  
Binary Search  
1. 자료 중앙원소 선정
2. 중앙원소와 목표 값 비교
3. 목표값이 더 크면 중앙원소부터 오른쪽만 탐색 더 작으면 왼쪽만 탐색

```py
arr = [7, 4, 2, 9, 11, 23, 19]
arr.sort()


def binary_search_while(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)// 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
ans = binary_search_while(11)
print(ans)
```

### 현재 이진 검색으로 풀 수 없는 문제 
현재 이진 검색은 배열에서 숫자 하나를 검색   

중복된 숫자가 존재하는 문제를 풀 수 없다.  
    - 범위 값 검색
      - N이상인 개수
      - A~B 사이의 값을 가진 데이터 수 

- A가 첫 번째 시작하는 위치 
- A를 초과하는 값이 시작하는 위치 구하기
- Lower bound, upper bound 공부하기  
- 검색 키워드 : parametric search