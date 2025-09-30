### Cookie & Session
#### HTTP
HTTP(HyperText Transfer Protocol): HTML문서와 같은 리소스들을 가져올 수 있도록 해주는 규약(웹에서의 모든 데이터 교환의 기초)

HTTP 특징
1. 비 연결 지향(connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 클라이언트는 서버와 서로 연결되어 있는 상태가 아님
2. 무상태(stateless)
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  - 무상태의 의미
    - 장바구니에 담은 상품을 유지할 수 없음
    - 로그인 상태를 유지할 수 없음

#### 쿠키
쿠키(Cookie): 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

쿠키 특징
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
- key-value 형식의 데이터

쿠키 사용 예시
- 로그인 유지(세션 관리)
- 장바구니
- 언어, 테마 등 사용자 설정 기억

쿠키의 작동 원리와 활용
1. 쿠키 저장 방식
  - 브라우저(클라이언트)는 쿠키를 key-value의 데이터 형식으로 저장
  - 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등의 추가 속성이 포함 됨
2. 쿠키 전송 과정
  - 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송
  - 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청 시 HTTP 요청 Header의 Cookie 필드에 저장된 쿠키를 함께 전송
3. 쿠키의 주요 용도
  - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할

쿠키 사용 목적
1. 세션 관리(Session management)
  - 로그인, 아이디 자동 완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화(Personalization)
  - 사용자 선호 설정(언어 설정, 테마 등) 저장
3. 추적, 수집(Tracking)
  - 사용자 행동을 기록 및 분석

#### 세션
세션(session): 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지, 상태 정보를 저장하는 데이터 저장 방식

세션 특징
- 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지
  - 서버의 메모리나 데이터베이스에 저장되므로, 서버 리소스를 사용(효율적 관리 필요)
- 상태 정보를 저장하는 데이터 저장 방식
- 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄
- 세션은 영구적으로 유지되지 않음

세션 정리
1. 서버 측에서는 세션 데이터를 생성 후 저장하고, 이 데이터에 접근할 수 잇는 세션 ID를 생성
2. 이 ID를 클라이언트 측으로 전달하고, 클라이언트는 쿠키에 이 ID를 저장
3. 이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송
  - 로그인 상태 유지를 위해 로그인 되어있다는 사실을 입증하는 데이터를 매 요청마다 계속해서 보내는 것

쿠키와 세션의 목적
- 클라이언트와 서버 간의 상태 정보를 유지하고 사용자를 식별하기 위해 사용

### Django Authentication System
인증의 필요성
- 클라이언트와 서버 간의 상태 정보를 유지하기 위해서 쿠키와 세션을 사용
- 클라이언트와 서버는 각기 다른 사용자를 식별해야 하는 상태
- 그래서 사용자를 식별하기 위해서 필요한 과정이 바로 '인증(Authentication)'
- 다양한 인증이 존재
  - 아이디와 비밀번호
  - 소셜 로그인(OAuth)
  - 생체인증

Django Authentication System
- Django에서 사용자 인증과 관련된 기능을 모아 놓은 시스템
- 인증에 중요한 기본적인 기능을 제공
  - User Model: 사용자 인증 후 연결될 User Model 관리
  - Session 관리: 로그인 상태를 유지하고 서버에 저장하는 방식을 관리
  - 기본 인증(Id/Password): 로그인/로그아웃 등 다양한 기능을 제공

기본 User Model의 한계
- 인증 후 사용되는 User Model은 별도의 User 클래스 정의 없이 내장된 auth 앱에 작성된 User 클래스를 사용했음
- 하지만 Django의 기본 User 모델은 username, password 등 제공되는 필드가 매우 제한적
- 추가적인 사용자 정보(예: 생년월일, 주소, 나이 등)가 필요하다면 이를 위해 기본 User Model을 변경하기 어려움
  - 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정하기 어려움

### Custom User model
#### User model 대체하기
사전 준비
- app accounts 생성 및 등록
- auth와 관련된 경로나 키워드들을 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 'account'로 지정하는 것을 권장

AUTH_USER_MODEL: Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정하는 속성
- 주의! Django는 프로젝트 중간에 AUTH_USER_MODEL을 변경하는 것을 강력하게 권장하지 않음

프로젝트를 시작하며 반드시 User 모델을 대체해야 함
- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더하도 커스텀 User 모델을 설정하는 것을 강력하게 권장하고 있음
- 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 나중에 맞춤 설정 할 수 있음
- User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

```python
# accounts/urls.py
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = []

# crud/urls.py
urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls')),
]

# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass

# settings.py
AUTH_USER_MODEL = 'accounts.User'

# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
admin.site.register(User, UserAdmin)
```

### Login
Login
- 클라이언트와 서버 간의 상태 정보를 유지하기 위해서 쿠키와 세션을 사용
- 클라이언트와 서버는 각기 다른 사용자를 식별해야 하는 상태
- 서버에 "나"임을 인증하는 과정

login(request, user)
- AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수
- request
  - 현재 사용자의 세션 정보에 접근하기 위해 사용
- user
  - 어떤 사용자가 로그인 되었는지를 기록하기 위해 사용

get_user()
- AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우, 로그인 한 사용자 객체를 반환

```python
# accounts/urls.py
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

### Template with Authentication data
Template with Authentication data
- 템플릿에서 인증 관련 데이터를 출력하는 방법

현재 로그인 되어있는 유저 정보 출력하기
- user라는 context 데이터를 사용할 수 있는 이유
  - django가 미리 준비한 context 데이터가 존재하기 때문(context pocessors)

context pocessors
- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
- django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

### 참고
#### 쿠키의 수명
쿠키 종류별 Lifetime(수명)
1. Session cookie
  - 현재 세션(current session)이 종료되면 삭제됨
  - 브라우저 종료와 함께 세션이 삭제됨
2. Persistent cookies
  - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

#### 쿠키와 보안
쿠키의 보안 장치
1. 제한된 정보
  - 쿠키에는 보통 중요하지 않은 정보만 저장. (사용자 ID나 세션 번호 같은 것)
2. 암호화
  - 중요한 정보는 서버에서 암호화해서 쿠키에 저장
3. 만료 시간
  - 쿠키에는 만료 시간을 설정, 시간이 지나면 자동으로 삭제
4. 도메인 제한
  - 쿠키는 특정 웹사이트에서만 사용할 수 있도록 설정할 수 있음

#### Django에서의 세션 관리
세션 in Django
- Django는 'database-backed sessions' 저장 방식을 기본 값으로 사용
- session 정보는 DB의 django_session 테이블에 저장
- Django는 요청안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄

#### User 모델 대체하기 Tip
User 모델을 대체하는 순서를 숙지하기 어려울 경우 해당 공식문서를 보며 순서대로 진행하는 것을 권장