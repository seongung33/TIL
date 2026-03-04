# 시작하기 
## SW 문제해결
1. 문제를 읽고 이해한다.
2. 나만의 언어로 문제를 재정의 한다.
3. 어떻게 해결할지 계획을 세운다.
4. 계획을 검증한다. 
5. 프로그램으로 구현한다. 
6. 어떻게 풀었는지 돌아보고 개선할 방법이 있는지 찾아본다.  

**자료구조와 알고리즘을 선정해야 한다.**  

## 복잡도 분석  
O(big-O): 최악의 케이스
Ω(Big-Omega): 최선, 평균
Θ(Big-Theta):    

파이썬 기준 1초당 3천만번   
C언어 기준 1초당 1억번 정도   

이를 기준으로 시간복잡도 계산하기  

공간복잡도: python의 경우 명확한 계산이 어렵다.  
 - 변수 하나도 많은 메모리를 차지
 - 동적 메모리는 어느순간 2배로 계산

- append 사용을 최대한 피하자.  

pypy vs python3
 - pypy: 시간 - 빠름 / 메모리 - 비효율
   - 재귀 사용 X -> python3으로 제출하기
 - python3: 시간 - 느림 / 메모리 - 효율


## 표준 입출력 방법
```py
import sys
# 입력
sys.stdin = open("주소/파일명", "r") # read 모드

# 출력
sys.stdout = opne('파일명', "w") # 쓰기 write
```
사용이유   
1. 테스트케이스를 바꾸면서 테스트가 가능하다.  
2. 복붙하기 귀찮다. ㅠ  

## 진법과 연산   
10진수: 0~9, 사람이 사용하는 진수  
2진수: 컴퓨터가 사용하는 진수, 수 하나를 0, 1로 표현   
8진수: 2진수를 더 가독성 있게 사용   
16진수: 2진수를 더 가독성 있게 사용, 0~9, A~F 로 표현  


10진수를 2진수로 변환 2로 계속 나누기 마지막부터 숫자 읽어 나가기  
```py
decimal = 149
binary = 0
a= 1
while decimal != 0: # d
    binary += (decimal % 2)*a
    a *= 10
    decimal //= 2 # 1// 2 는 0 이된다.
print(binary)

# 비트연산자
def bit_print(dec):
    output = ""
    for i in range(7, -1, -1):
        if dec & (1 << i):
            output += "1"
        else:
            output += "0"
    return output
print(bit_print(149))

# 동시 계산. dec 값 보다 8의 자릿수가 더 커야함. 
def bit_print(dec):
    output = dec & 2**8-1
    return output
print(bit_print(149))

# 이진수를 7칸씩 쪼개서 쪼갠 것들 각각 십진수로 바꾸기  
bit = "0000000010110"
N = len(bit)
for i in range(0, N, 7):
    ith_bit = bit[i:i+7]
    decimal = 0
    i = 0
    for j in range(6, -1, -1):
        decimal += int(ith_bit[j]) * 2 ** (6-j)
        i += 1

    print(decimal)
```