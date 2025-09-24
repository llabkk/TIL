### ORM
ORM(Object-Relational-Mapping): 객체 지향 프로그래밍 언어의 객체(Object)와 데이터베이스의 데이터를 매핑(Mapping)하는 기술

### QuerySet API
QuerySet API: 데이터베이스의 복잡한 SQL 쿼리문을, 직관적인 Python 코드로 다룰 수 있게 해주는 강력한 번역기

QuerySet API 구문 기본 구조: Article.objects.all()
- Article(Model class)
  - 역할: 데이터베이스 테이블에 대한 Python 클래스 표현
  - 테이블의 스키마(필드, 데이터 타입, 구조)를 정의하며, Django ORM이 데이터베이스와 상호작용할 때, 사용하는 기본적인 구조체
- objects(Manager)
  - 역할: 데이터베이스 조회(Query) 작업을 위한 기본 인터페이스
  - 모델 클래스가 데이터베이스 쿼리 작업을 수행할 수 있도록 하는 진입점
  - Django는 모든 모델에 objects라는 이름의 매니저를 자동으로 추가하며, 이 매니저를 통해 .all(), .filter() 등의 쿼리 메서드를 호출
- all()(Queryset API 메서드)
  - 역할: 특정 데이터베이스 작업을 수행하는 명령
  - 매니저를 통해 호출되는 메서드로, 해당 모델과 연결된 테이블의 모든 레코드(rows)를 조회하라는 SQL 쿼리를 생성하고 실행

Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다: 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.

QuerySet
- 데이터베이스에서 전달받은 객체 목록(데이터 모음)
- 순회 가능한 데이터로 1개 이상 데이터를 불러와 사용 가능함
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

### QuerySet API 실습
CRUD: 대부분의 소프트웨어가 가지는 기본적인 데이터 처리 기능인 생성, 조회, 수정, 삭제를 묶어 이르는 말

#### Create
데이터 객체를 만드는(생성하는) 3가지 방법
1. 빈 객체 생성 후 값 할당 및 저장
2. 초기 값과 함께 객체 생성 및 저장
3. create() 메서드로 한 번에 생성 및 저장

save(): 객체를 데이터베이스에 저장하는 인스턴스 메서드
- 객체를 먼저 생성한 후, 데이터베이스에 저장하기 전에 추가적인 처리

#### Read
대표적인 조회 메서드
- QuerySet 반환 메서드
  - all(): 전체 데이터 조회
  - filter(): 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
- QuerySet을 반환하지 않는 메서드
  - get(): 주어진 매개변수와 일치하는 객체를 반환, 보통 pk를 사용

#### Update
1. 수정할 인스턴스 조회
```
article = Article.objects.get(pk=1)
```
2. 인스턴스 변수를 변경
```
article.title = "byebye"
```
3. 저장
```
article.save()
```

#### Delete
1. 삭제할 인스턴스 조회
```
article = Article.objects.get(pk=1)
```
2. delete 메서드 호출(삭제 된 객체가 반환)
```
article.delete()
```
- 삭제한 데이터는 더이상 조회할 수 없음

### 참고
#### Field lookups
Field lookups: 단순 동치 비교(=)를 넘어 더 상세한 조건으로 데이터를 조회할 수 있도록 Django ORM이 제공하는 기능
- Field lookups은 모델의 필드 이름 뒤에 이중 밑줄(double underscore, __)을 붙이고, 원하는 조회 유형을 명시하는 방식으로 사용
- filter(), exclude() 및 get()에 대한 키워드 인자로 지정, 손쉽게 필터링 로직을 구성
```python
# Field lookups 예시
# 내용에 'dja'가 포함된 모든 게시글 조회
Article.objects.filter(content__contains="dja")
# 제목이 'he'로 시작하는 모든 게시글 조회
Article.objects.filter(title__startswith="he")
```

다양한 조건의 Field lookups 조회 조건
- exact / iexact
  - exact: 대소문자를 구분하여 정확히 일치하는 값을 찾음
  - iexact: 대소문자 구분 없이(대소문자 무시) 정확히 일치하는 값을 찾음
- contains / icontains
  - contains: 문자열 내에 특정 값이 포함되어 있는지(대소문자 구분)
  - icontains: 문자열 포함 여부를 대소문자 구분 없이 확인
- 비교 연산자(gt, gte, lt, lte)
  - 숫자 또는 날짜 필드에 대해 크거나 작음을 비교

#### ORM, QuerySet API를 사용하는 이유
1. 데이터베이스 추상화
  - 개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음
2. 생산성 향상
  - 복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음
3. 객체 지향적 접근
  - 데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향 프로그래밍의 이점을 활용할 수 있음