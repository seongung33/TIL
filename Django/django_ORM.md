1. Django ORM은 파이썬과 데이터베이스 사이의 통역사 역할을 하며, 선언적 코드만으로 데이터 저장, 조회 명령을 실행한다.
2. QuerySet API로 게시글을 생성, 조회, 수정, 삭제 하면서 데이터베이스 명령어를 직접 작성하지 않아도 된다.    
# ORM
객체 지향 프로그래밍 언어의 객체와 데이터베이스의 데이터를 매핑하는 기술     
ORM은 Django 개발자를 위해 QuerySet API라는 특별한 도구를 제공함      


## QuerySet API  
QuerySet API: 객체지향적이고 직관적인 방식으로 DB를 조작할 수 있도록 제공하는 인터페이스       
개발자는 SQL을 직접 작성하지 않고 .filter()와 같은 파이썬 코드로 다룰 수 있도록 함    

### 동작방식
1. Django -> DB: QuerySet API에서 ORM을 통해 데이터베이스로 요청
    - SQL 쿼리로 변환되어 데이터베이스로 전달
2. DB -> Django: 데이터베이스가 요청에 의한 응답을 보낼 떄
    - ORM은 SQL 결과를 다시 파이썬이 이해할 수 있는 python object로 변환    

Article.objects.all()     
Article: model class         
objects: manager       
all(): Queryset API      

## QuerySet  
QuerySet: ORM을 통해 만들어진 자료형    
순회 가능한 데이터로 1개 이상 데이터를 불러와 사용 가능함    


DB가 단일객체 반환시 모델의 인스턴스로 반환      
여러 객체를 반환하면 QuerySet으로 반환함    

## CRUD  
QuerySet API를 통해 python 코드(sql 없이)로 CRUD 작업을 직관적으로 수행  

Create: 생성
Read: 조회
Update: 수정(갱신)
Delete: 삭제   

pip install ipython: 셸이 이뻐진다네요     

python manage.py shell: 터미널에서 셸 환경 진입     
python manage.py shell -v 2: 필요한 라이브러리 불러서 셸 환경 바로 진입    

###  Create 생성 - 3가지 방법
1. 빈 객체 생성 후 값 할당 및 저장  
    - article = Article() -< 모델 클래스 이름
    - article.title = 'first' -> 값 할당 
    - article.content = 'django!' -> 값 할당
    - article.save() -> 저장 

2. 초기 값과 함께 객체 생성 및 저장   
       - article = Aritcle(title='second', content='django!') -> 초기값을 생성하여 객체 생성
       - aricle.save() -> 저장

3. create() 메서드로 한번에 생성 및 저장       
    - Article.objects.create(title='third', content='django!')
    - 이는 저장까지 자동이다


### Read  읽기
QuerySet 반환 메서드: all(), filter()    
QuerySet을 반환하지 않는 메서드: get()    

- all() 
    - Article.objects.all()
- filter()
  - content로 조회 Article.objects.filter(content='django!') - 3개
  - title로 조회 Article.objects.filter(title='abc') - 빈 QuerySet 반환
  - 얘는 QuerySet에 담겨서 반환
- get()
  - 일치하는 데이터가 하나여야 한다. Article.objects.get(pk=1) - 1개
  - 일치하는 데이터가 여러개이므로 사용 불가 Article.objects.get(content='django!') - 여러개라 안됨
  - get은 무조건 1개가 반환되므로 본인 클래스의 인스턴스로 반환된다.

### Updated 수정  
수정할 인스턴스 조회    
article = Article.objects.get(pk=1)    
데이터 수정    
article.title = 'byebye'     
지금은  DB변경 X 쟝고에서만 변경됨      
저장    
article.save()    
저장을 통해 DB 저장   

### Delete 삭제  
불러오기     
article = Article.objects.get(pk=1)     
삭제  - 호출 시 즉시 DB 삭제    
article.delete()   

## ORM with view  
