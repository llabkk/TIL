### Static files
Static files(정적 파일): 서버 측에서 변경되지 않고 고정적으로 제공되는 파일

#### 웹 서버와 정적 파일
- URL의 필요성 : 정적 파일이 사용자에게 보이려면, 그 파일에 접근할 수 있는 고유한 주소(URL)가 반드시 필요

처리 과정 요약(이미지 확인 시)
1. 사용자: 브라우저에 url 주소 입력하며 이미지를 요청
2. 웹서버: url 주소를 확인하고, 서버에 미리 약속된 폴더에서 파일을 찾음
3. 웹서버: 찾은 이미지 파일을 HTTP 응답에 담아 사용자에게 전송
4. 사용자: 브라우저가 응답 받은 이미지 파일을 화면에 보여줌

Static files 경로의 종류
1. 기본 경로
2. 추가 경로

#### static files 기본 경로
Static files 기본 경로 : app폴더/static/

기본 경로 css 스타일 제공하기
- articles/static/stylesheets/ 경로에 css파일 배치하기
```style.css
h1 {
  color: crimson;
}
```

- 메인 페이지에서 css 파일 불러오기
```index.html
{% load static %}
<link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
```

- {% load %}
  - 특정 라이브러리의 태그와 필터를 현재 템플릿에서 사용할 수 있도록 불러오는 역할
  - {% load static %}은 {% static %} 태그를 사용하기 위해, Django 템플릿 시스템에 이제부터 static 관련 태그를 사용하겠다 고 알려주는 선언문
  - load 태그는 템플릿 파일의 가장 상단에 한 번만 작성하면 된다. 단, extends 아래에

- {% static '경로' %}
  - settings.py 파일의 STATIC_URL 값을 기준으로, 해당 정적 파일의 전체 URL 경로를 계산하여 생성
  - 예를 들어, STATIC_URL = 'static/'이고 CSS파일이 static/css/style.css에 위치한다면, 경로가 필요한 위치에 {% static 'css/style.css' %}로 작성

STATIC_URL: 정적 파일의 '웹 주소'

기본 경로 이미지 파일 제공하기
- articles/static/images/ 경로에 이미지 파일 배치하기
- DTL의 static tag를 사용해 이미지 경로 작성하기
```
<img src="{% static "images/python.png" %}" alt="sample">
```

정적파일 URL이 만들어지기까지
URL + STATIC_URL + 정적파일 경로

#### static files 추가 경로
static files 추가 경로: STATICFILES_DIRS에 문자열로 추가 경로를 설정

STATICFILES_DIRS: 기본 경로 외에 추가적으로 탐색할 경로의 목록을 지정하는 리스트

정적 파일의 핵심 원리: 주소(url)가 있어야 찾아갈 수 있다.
- 컴퓨터에 파일이 존재하는 것만으로는 웹 페이지에 보일 수 없음
- 외부의 손님(브라우저)이 파일을 찾아올 수 있도록 반드시 '웹 주소(url)'라는 문패를 달아줘야 함

구분|개념|비유
---|---|---
서버(내 컴퓨터)|실제 파일 경로|내 방 책상 위 세 번째 서랍
웹(인터넷 세상)|URL(웹 주소)|서울시 강남구 테헤란로 999

### Media files
Media files(미디어 파일): 사용자가 웹사이트를 통해 직접 업로드하는 파일

#### 이미지 업로드
ImageField()
- 이미지 파일을 업로드하기 위해 사용하는 Django 모델 필드
- 데이터베이스 저장 방식
  - 가장 중요한 특징은 이미지 파일 자체가 데이터베이스에 저장되는 것이 아니라는 점
  - 데이터베이스에는 upload_to 경로를 기준으로 한 이미지 파일의 경로(문자열)만 저장되고, 실제 파일은 서버의 특정 폴더(MEDIA_ROOT)에 저장
```models.py
class Article(models.Model):
  image = models.ImageField(upload_to='images/')
```

미디어 파일을 제공하기 전 준비사항
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

MEDIA_ROOT: 미디어 파일의 실제 창고 주소(업로드된 미디어 파일들이 저장된 서버 컴퓨터의 절대 경로)
```
MEDIA_ROOT = BASE_DIR / 'media'
```

MEDIA_URL: 미디어 파일의 웹 주소 별명
```
MEDIA_URL = 'media/'
```

```urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

이미지 업로드 구현
1. 모델 클래스에 image 필드 작성
```models.py
class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
```
2. pillow 설치 후 migrations
```git bash
pip install pillow
```
3. form 요소의 enctype 속성 추가
```create.html
<form action="{% url "articles:create" %}" method="POST" enctype='multipart/form-data'>
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```
4. ModelForm의 2번째 인자로 요청 받은 파일 데이터 작성
```
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        ...
```

#### 업로드 이미지 제공
게시글 상세 페이지에 업로드 한 이미지 제공하기
- ImageField의 .url 속성
  - 업로드 파일의 웹 주소
  - ImageField나 FileField에 저장된 파일 객체에서 .url 속성을 사용하면, 해당 파일을 웹에서 접근할 수 있는 전체 URL 주소를 얻을 수 있음
```detail.html
{% if article.image %}
  <img src="{{article.image.url}}" alt="media.image">
{% endif %}
```

#### 업로드 이미지 수정
- 수정 페이지 form 요소에 enctype 속성 추가
```update.html
<form action="{% url "articles:update" article.pk %}" method="POST" enctype='multipart/form-data'>
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```

- update view 함수에서 업로드 파일에 대한 추가 코드 작성
```views.py
def update(request, pk):
    article = Article.object.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        ...
```

### 참고
#### upload_to 활용
- 단순한 문자열 경로 외에도, 업로드 경로를 동적으로 생성하는 두 가지 유용한 방법을 제공
1. 날짜를 이용한 경로 구성
- strftime()의 형식 코드를 사용하여 파일이 업로드된 날짜를 기준으로 폴더를 자동으로 생성할 수 있음
  - %Y: 4자리 연도
  - %m: 2자리 월
  - %d: 2자리 일
```
class Photo(models.Model):
    # 2100년 1월 1일 에 업로드하면 '2100/01/01/' 폴더에 저장됨
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
```

2. 함수를 이용한 동적 경로 생성
- 더 복잡한 로직으로 경로를 만들고 싶을 때는, upload_to에 함수를 직접 전달할 수 있음
- 이 함수는 두 가지 인자를 받음
  - instance: 파일이 첨부된 모델의 인스턴스(해당 게시글 객체 등)
  - filename: 업로드 된 파일의 원본 이름
```
def article_image_path(instance, filename):
    # instance.user.username을 통해 게시글 작성자의 이름을 가져옴
    # 예: 'images/ssafy_user/my_photo.jpg' 와 같은 경로를 반환
    return f'images/{instance.user.username}/{filename}'

class Article(models.Model):
    user = ...
    image = models.ImageField(blank=True, upload_to=article_image_path)
```

#### AWS 인프라 이해하기
AWS(Amazon Web Services)
- 아마존이 제공하는 클라우드 컴퓨팅 플랫폼
- 서버, 스토리지, 데이터베이스 같은 IT 인프라를 직접 구매하지 않고, 인터넷을 통해 필요한 만큼 빌려쓰는 서비스

AWS 핵심 서비스 3가지
서비스|역할|설명
:---:|:---:|:---:
EC2|가상 서버|클라우드에 생성하는 고성능 컴퓨터
S3|파일 저장소|이미지, 동영상 등 모든 파일을 보관하는 객체 스토리지
RDS|데이터베이스|데이터를 체계적으로 관리하는 관계형 데이터베이스

EC2, S3, RDS를 활용한 웹 서비스 구축
- EC2(서버)
  - 웹 애플리케이션(Django)이 실행되는 컴퓨터의 역할
- S3(파일 저장소)
  - 사용자가 올린 이미지나 사이트의 로고 등 정적 파일을 보관하는 외부 창고 역할
- RDS(데이터베이스)
  - 회원 정보, 게시글 등 중요한 데이터를 기록하고 관리하는 장부 역할

![데이터 흐름도 요약](데이터흐름도요약.png)

클라우드 컴퓨팅 플랫폼을 사용하는 이유
- 비용 절감
  - 물리 장비를 직접 구매할 필요 없이, 사용한 만큼만 비용을 지불
- 유연성과 확장성
  - 필요에 따라 서버 사양이나 저장 공간 용량을 몇 번의 클릭만으로 자유롭게 조절할 수 있음
- 글로벌 서비스
  - 전 세계에 위치한 데이터 센터를 통해 어떤 국가의 사용자에게도 빠르고 안정적인 서비스를 제공할 수 있음

#### BaseModelForm
- BaseModelForm의 생성자 함수 키워드 인자 순서 참고
![BaseModelForm의 인자 순서](Basemodelform.png)