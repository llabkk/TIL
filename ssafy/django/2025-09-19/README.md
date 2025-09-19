### Template System
#### Django Template System
Django Template System: 파이썬 데이터(context)를 HTML 문서(Template)와 결합하여, 로직과 표현을 분리한 채 동적인 웹페이지를 생성하는 도구

Django Template System의 목적
- '페이지 틀'에 '데이터'를 동적으로 결합하여 수많은 페이지를 효율적으로 만들어 내기 위함

#### Django Template Language
Django Template Language(DTL): Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

DTL Syntax
1. Variable(변수)
  - Django Template에서의 변수
  - render 함수의 세번째 인자로 딕셔너리 타입으로 전달됨
  - 해당 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  - dot(.)을 사용하여 변수 속성에 접근할 수 있음
  - {{}}의 안에 넣어서 사용
2. Filters
  - 표시할 변수를 수정할 때 사용(변수 + '|' + 필터)
  - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
  - 약 60개의 built-in template filters를 제공
3. Tag
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦
  - 일부 태그는 시작과 종료 태그가 필요
  - 약 24개의 built-in template tags를 제공
  - {% tag %}
  - if, else, endif 태그
    ```
    context = {
      'login': False,
    }
    {% if login %}
      <h1>Hello, user!!!</h1>
    {% else %}
      <h1>Please, login.</h1>
    {% endif %}
    ```
  - for 태그
    ```
    context = {
      'nums': [1, 2, 3],
    }
    <ul>
      {% for num in nums %}
        <li>{{num}}</li>
      {% endfor %}
    </ul>
    ```
4. Comments
  - 주석
    - inline
    ```
    <h1>Hello, {# name #}</h1>
    ```
    - multiline
    ```
    {% comment %}
      ...
    {% endcomment %}
    ```

### 템플릿 상속
템플릿 상속(Template inheritance)
1. 페이지의 공통요소를 포함
2.  하위 템플릿이 재정의 할 수 있는 공간을 정의
- 여러 템플릿이 공통요소를 공유할 수 있게 해주는 기능

상속 구조 만들기
- skeleton 역할을 하게 되는 상위 템플릿(base.html) 작성(파일명이 반드시 base일 필요는 없음)
  - 모든 템플릿이 공유햇으면 좋겠는 공통요소를 작성
  - 템플릿 별로 재정의할 부분은 block 태그를 활용
- 기존 하위 템플릿들이 상위 템플릿을 상속받도록 변경
  - extends 태그를 상속받을 템플릿 결정
  - block 태그를 활용해 base.html의 같은 이름으로 작성된 block 태그의 내용을 대체

#### 상속 관련 DTL 태그
'extends' tag
```
{% extends 'articles/base.html' %}
```
- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 자식 템플릿 최상단에 작성되어야 함
  - extends 태그는 2개 이상 사용이 불가능

'block' tag
```
{% block 'content' %} {% endblock 'content' %}
```
- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
- 상위 템플릿에서 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것

### 요청과 응답
#### HTML form
데이터를 보내고 가져오기
- HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

HTML 'form'
- HTTP 요청을 서버에 보내는 가장 편리한 방법

'form' element: 사용자로부터 할당된 데이터를 서버로 전송하는 HTML 요소
- 웹에서 사용자 정보를 입력하는 여러 방식: (text, password, checkbox 등)을 제공

#### HTML form 핵심 속성
action & method: form의 핵심 속성 2가지
- 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
- action
  - 입력 데이터가 전송될 URL을 지정(목적지)
  - actions을 지정하지 않으면 데이터는 현재 페이지의 URL로 설정됨
- method
  - 데이터를 어떤 방식으로 보낼 것인지 정의
  - 데이터의 HTTP request method(GET, POST)를 지정
    - GET: 조회
    - POST: 생성, 삭제, 수정

'input' element: 사용자의 데이터를 입력 받을 수 있는 HTML 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
  - 핵심 속성 - 'name'

'name' attribute
```
```
- input 요소의 핵심 속성
- 사용자가 입력한 데이터에 붙이는 이름(key)
- 데이터를 제출했을 때, 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드('&')로 연결된 key=value 쌍으로 구성되며 기본 URL과는 물음표('?')로 구분됨

#### HTML form 활용
HTTP request 객체: form으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨 있음

### Django URLs
요청과 응답에서 Django URLs의 역할
- 요청 URL에 따라 실행될 view함수가 달라진다.

URL dispatcher(운항 관리자, 분배기): URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view함수를 연결(매핑)

#### Variable Routing
Variable Routing
- URL 일부에 변수를 포함시키는 것
  - 변수는 view함수의 인자로 전달할 수 있음
```
path('articles/<int:num>', views.detail)
path('articles/<str:name>', virws.greeting)
```
- 요청 URL의 <int:num>, <str:name>의 위치에 들어있는 값이 변수처럼 취급됨
- Path Converter
  - URL 변수의 타입을 지정
  - str, int 등 5가지 타입 지원

#### App URL 정의
App URL mapping: 각 앱에 URL을 정의하는 것
- 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함

include 함수
- include('app.urls'): 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
- URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

### URL 이름 지정
#### Naming URL patterns
Naming URL patterns
- URL에 이름을 지정하는 것
  - path 함수에 name 인자를 키워드 인자로 정의해서 사용
- 해당 URL을 사용했던 곳의 링크 변경
  - a태그의 href 속성 값, form태그의 action 속성 값

#### DTL URL tag
URL tag: 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
- URL 패턴에 변수가 포함되어 있으면, url_name 이후 추가
- DTL의 for 태그에서 사용한 변수 이름 사용 가능

### URL 이름 공간
#### app_name 속성
앱들의 url 이름이 같은 경우 충돌로 인해 setting에서 먼저 정의된 앱만 사용 가능
- 문제 해결을 위해 key 사용

app_name 속성 지정
- urls.py에 app_name 변수 설정
- app_name이 추가 또는 수정되면 url태그에도 해당 내용이 반영되어야 함

### 참고
#### 추가 템플릿 경로
추가 템플릿 경로 지정
- 앱 폴더 내부 templates 폴더(기본 경로) 외에 템플릿을 위치하고 싶을 때