# 상속

## 클래스 상속

상속 없이 구현   


상속을 사용한 계층 구조  

## 메서드 오버라이딩
부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의  
- 부모 클래스의 메서드를 이용하면서 일부 동작을 맞춤형으로 이용할 수 있음  

``` python
class Person:
    def __init__(self, name, age): # 매직 메서드, 인스턴스 메서드
        self.anme = name
        self.age = age

        def talk(self):
            print(f"반갑습니다. {self.name}입니다.")

        def eat(self):
            print("냠냠쩝쩝")
        
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):
        print(f"반갑네. 나는 {self.name}이라고 하네. 담당은 {self.department}라네.")
p1 = Professor("박교수", 49, "컴퓨터공학과")
p1.talk() # 반갑네. 나는 박교수이라고 하네. 담당은 컴퓨터공학과라네.
p1.eat() # 냠냠쩝쩝
```

## 다중 상속
- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정됩니다.**
- 둘 이상의 상위 클래스로부터 상속받을 수 있습니다.
```python
# 22, 23 페이지 코드 작성
```
### "다이아몬드 문제"
파이썬에서의 해결책
1. 자식 클래스 우선: 부모 클래스보다 자식 클래스를 먼저 탐색
2. 왼쪽 부모 우선: 다중 상속 시, 리스트에 나열된 순서(왼쪽에서 오른쪽)대로 탐색  
3. 중복 방문 방지: 공통 부모 클래스는 모든 자식 클래스의 탐색이 끝난 뒤에 단 한 번만 탐색  
탐색 흐름 예시  
클래스 D가 B와 C를 상속받고, B와 C가 A를 상속받는 경우
```python
class A:
    v = 'A'
    vvv = 'AA'

class B(A):
    v = 'B'

class C(A):
    vv = 'C'

class D(B, C): # 왼쪽부터 상속
    pass
d = D() # 왼쪽부터 상속찾기 v를 찾았으므로 찾기 중단.
print(d.v) # B
print(d.vv) # B -> A 출력값 C
print(d.vvv) # AA  
```
### super()
super()
- 현재 클래스의 부모 클래스의 메서드나 속성에 접근할 수 있게 해주는 내장 함수  
- 다중 상속에서 super() 호출 시 상속 순서에 맞춰 여러 부모 클래스의 메서드를 순차적으로 실행할 수 있다.  

단일 상속시    
- super().__init__(): 부모 클래스에 __init 된 객체들은 가져온다. 이 외에 없는 객체값 추가 가능
```python

class parent:
    def __init__(self):
        self.value_1 = 'parent'
 
class Child(parent):
    def __init__(self):
        super().__init__()
        self.value_2 = 'child' # value_1 값을 적지 않아도 된다
```
다이아몬드 다중상속 super().__init__() 구문
```python
class A:
    def __init__(self):
        super().__init__()
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(A):
    def __init__(self):
        super().__init__()
        print('C')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')
```

## 디버깅
버그: 소프트웨어에서 발생하는 오류 또는 결함, 프로그램의 예상된 동작과 실제 동작 사이의 불일치  
**디버깅 방법**
1. print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
2. 개발환경 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
    - 라인에 빨간 점 클릭 후(여러 개 가능) 파이썬 디버그 실행
3. python tutor 활용
4. 뇌 검파일 눈 디버깅 등

## 예외 처리
```python
try:
    #예외 발생 코드
except:
    # 예외 발생 시 실행할 코드
else:
    # 예외가 발생하지 않았을 때 실행할 코드 작성
finally:
    #예외 발생 여부와 상관없이 항상 실행할 코드
```