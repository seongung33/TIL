# MODEL  
모델을 통한 DB 관리
- urls.py: 사용자 요청의 시작점
- views.py: 요청을 처리하고 models.py르 통해 데이터를 다룸
- models.py: 데이터베이스를 정의하고, 데이터베이스와 상호작용
- templates: views.py로부터 받은 데이터를 사용자에게 보여줄 화면을 구성

## Model class 
DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공  

models.py 에 등록
```py
class Aritcle(models.Model):
    # max_length = 선택옵션이지만 
    # 제한된 길이를 저장하는 것이 목적이라 사용 권장
    title = models.CharField(max_length=10)
    # 길이 제한이 없는 대용량 텍스트 저장
    # 무한은 아니며 시스템 따라 최대치가 달라짐
    content = models.TextField()
```
- 문자열 - CharField, TextField
- 숫자 - IntegerField, FloatField
- 날짜/시간 - DataField, TimeField, DateTimeField
- 파일관련 - FileField, ImageField
## 제약조건 
- null
- blank(0)
- default


# Migrations
생성: python manage.py makemigrations     

sql에 데이터 구조 등록: python manage.py migrate     

DB 있어야함    
관리자 계정 만들기: python manage.py createsuperuser     


DataField, TimeField, DateTimeField       
여기에 인자로 사용하는거     
auto_now=True -> 데이터가 저장될 때마다 자동으로 현재시간 저장     
auto_now_add=True -> 데이터가 처음 생성될 때만 자동으로 현재 날짜시간 저장     

