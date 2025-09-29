### Django Form
HTML 'form'의 한계: 지금까지 사용자로부터 데이터를 제출 받기위해 활용한 방법, 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음

유효성 검사: 수집한 데이터가 정확하고 유효한지 확인하는 과정

유효성 검사의 어려움
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

#### Form class
Django Form: 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

#### Widegts
Widgets: HTML 'input' element의 표현을 담당

### Django ModelForm
Form vs ModelForm
- Form: 사용자 입력 데이터를 DB에 저장하지 않을 때(검색, 로그인)
- ModelForm: 사용자 입력 데이터를 DB에 저장애햐 할 때(게시글 작성, 회원가입)

ModelForm: Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
- ModelForm은 Form 클래스와 Model 클래스를 결합한 상태로, 모델 필드를 기반으로 입력 폼을 자동 생성해줍니다.
- 데이터 수집과 저장 과정을 동시에 처리할 수 있도록 도와줍니다.

#### Meta class
Meta class: ModelForm의 정보를 작성하는 곳
- Meta class는 ModelForm 내부에서 어떤 모델과 연결할지, 어떤 필드를 사용할지 등을 정의하는 설정 공간입니다.
- 폼의 동작 방식을 제어하는 핵심 역할을 합니다.

'fields' 및 'exclude' 속성
- exclude 속성을 사용하여 모델에서 포함하지 않도록 필드를 지정할 수도 있음

```django
# 모든 입력값을 포함
fields = '__all__'
# title만 포함
fields = ('title',)
# title만 제외
exclude = ('title',)
```

Meta class 주의사항
- Django에서 ModelForm에 대한 추가 정보나 속성을 작성하는 클래스 구조를 Meta 클래스로 작성했을 뿐이며, 파이썬의 inner class와 같은 문법적인 관점으로 접근하지 말 것

#### ModelForm 적용
is_valid(): 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

공백 데이터가 유효하지 않은 이유
- 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정 되어있음(blank, null)

#### save 메서드
save(): 데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드
- 폼 데이터가 유효한 경우, save() 메서드를 호출하면 모델 인스턴스를 생성하고 데이터베이스에 저장됩니다.
- instance 인자를 통해 새 객체 생성과 기존 객체 수정도 구분할 수 있습니다.
- 이 과정을 통해 코드 없이 손쉽게 DB 연동이 가능합니다.

save() 메서드가 생성과 수정을 구분하는 법
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정

Django Form 정리
- 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

### HTTP 요청 다루기
#### View 함수 구조 변화
new & create 함수간 공통점과 차이점
- 공통점: 데이터 생성을 구현하기 위함
- 차이점: new는 GET 메서드 요청만 처리, create는 POST 메서드 요청만 처리

view 함수 구조화의 목적
- HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 구조화

#### new & create 함수 결합
new
```python
def new(request):
    """새로운 게시글을 작성할 수 있는 new.html 페이지를 렌더링"""
    # 사용자가 데이터를 입력할 수 있는 빈 form 페이지를 보여주는 역할만 함

    form = ArticleForm()
    context = {
        "form": form
    }
    return render(request, 'articles/new.html', context)
```

create
```python
def create(request):
    """사용자가 form을 통해 제출한 데이터를 DB에 저장"""
    # 1. 사용자 입력 데이터를 통째로 Form 클래스의 인자로 넣어서 인스턴스를 생성
    form = ArticleForm(request.POST)

    # 2. 유효성 검사
    if form.is_valid():
        # 2.1. 유효성 검사가 통과하면 저장
        article = form.save()
        return redirect('articles:detail', article.pk)
    
    # 2.2. 유효성 검사를 통과하지 못하면 해당 페이지를 다시 응답(+에러 메시지를 포함)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

new & create 함수 결합
```python
def create(request):
    # 요청 메서드가 POST라면 (과거 create 함수의 역할)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 요청 메서드가 POST가 아니라면 (과거 new 함수의 역할)
    else:
        form = ArticleForm()
    context = {
        "form": form
    }
    return render(request, 'articles/create.html', context)
```


#### edit & update 함수 결합
edit
```python
def edit(request, pk):
    """기존 게시글을 수정할 수 있는 edit.html 페이지를 렌더링"""
    # 1. 수정할 게시글의 기존 데이터를 pk를 이용해 조회
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)

    # 2. 조회된 데이터를 form에 미리 채워넣기 위해 context에 담아 템플릿에 전달
    context = {
        'article': article,
        'form': form,
    }
    # 3. edit.html 템플릿을 렌더링
    return render(request, 'articles/edit.html', context)
```

update
```python
def update(request, pk):
    """사용자가 form을 통해 제출한 수정 데이터를 DB에 반영(UPDATE)"""
    # 1. 수정할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. 사용자가 입력한(수정한) 데이터를 통째로 받음 + 기존 데이터
    form = ArticleForm(request.POST, instance=article)

    # 3. 유효성 검사
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
        # 3.1. 검사 통과 했을 때

    # 3.2. 검사 통과 못했을 때
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

edit & update 함수 결합
```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

### 참고
#### ModelForm의 키워드 인자 구성
ModelForm 키워드 인자 data와 instance 살펴보기
- data는 첫번째에 위치한 키워드 인자이기 때문에 생략 가능
- instance는 9번째에 위치한 키워드 인자이기 때문에 생략할 수 없음(앞의 8개를 모두 적지 않는 한)

#### Widgets 응용
```python
widget=forms.TextInput(
    attrs={
        'class': 'my-title',
        'placeholder': 'enter the title',
        'maxlength': 10,
    }
)
widget=forms.Textarea(
    attrs={
        'class': 'my-content',
        'placeholder': 'enter the content',
        'rows': 5,
        'cols': 30,
    }
)
```

#### 필드를 수동으로 렌더링