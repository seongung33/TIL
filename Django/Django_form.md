# FORM  

## HTML 'form'   
사용자로부터 데이터를 제출받기 위해 활용한 방법      
but, 비정상적 혹은 악의적인 요청을 필터링 할 수 없음        

## 유효성 검사
수집한 데이터가 정확하고 유효한지 확인하는 과정      

- Form은 사용자 입력 데이터를 DB에 저장하지 않을 때 사용 - 검색, 로그인 등              
- modelForm은 사용자 입력 데이터를 DB에 저장해야 할 때 - 글 작성, 회원가입 등             
    

## ModelForm  
안에는 mate 클래스가 있어야 한다.

### is_valid()
유효성 검사를 실행한다.
```py
def create(request):
    form = Article_form(request.POST)
    if form.is_valid(): # 빈 값은 is_valid에 공백이므로 False가 된다.
      # 출력
      return
    # 공백 있으니 메워라는 문구 출력하기
```
### save 
폼 데이터가 유효하면 save를 통해 인스턴스 생성과 DB 저장


## HTTP 요청 다루기
