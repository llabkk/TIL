## 2025-07-23
### 함수
함수 : 특정 작업을 수행하기 위한 **재사용 가능**한 코드 묶음
- 함수를 사용하는 이유 : 재사용성이 높아지고 코드의 가독성과 유지보수성 향상

함수 호출 : 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는것

```
# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수를 호출하여 결과를 출력
num1 = 1
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)
```

함수 구조
```
def make_sum(pram1, pram2): # input
    '''docstring
    (함수 body 앞에 선택적으로 작성 가능한 함수 설명서)
    '''
    return pram1 + pram2 # output
```

함수 정의
```
def 함수이름(매개변수):
    '''함수설명(생략가능)
    '''
    함수 동작
    return(필요한 경우 결과를 반환, return이 없으면 None을 반환)
```
함수의 반환 값

print()함수 : 화면에 값을 출력하기만 할 뿐, 반환 값이 없음(None 반환)
```
# 1을 터미널에 출력, return_print에 None값을 할당
return_print = print(1)

# None을 터미널에 출력
print(return_print)
```

### 매개변수와 인자
매개변수(parameter) : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

인자(argument) : 함수를 호출할 때, 실제로 전달되는 값

다양한 인자의 종류
1. 위치인자(positional arguments)
- 함수 호출시 인자의 위치에 따라 전달되는 인자
- 위치 인자는 함수 호출 시 반드시 값을 전달해야 함
```
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('alice', 25) # 안녕하세요, alice님! 25살이시군요.
greet(25, 'alice') # 안녕하세요, 25님! alice살이시군요.
greet('alice') # error(인자가 부족함)
```

2. 기본 인자 값()
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('bob') # 안녕하세요, bob님! 30살이시군요.
greet('alice', 25) # 안녕하세요, alice님! 25살이시군요.
```

3. 키워드 인자()
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야함
```
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='dave', age=35) # 안녕하세요, dave님! 35살이시군요.
greet(age=35, name='dave') # 안녕하세요, dave님! 35살이시군요.

greet(age=35,'dave') # error(위치인자는 키워드 인자 뒤에 올 수 없음)
```

4. 임의의 인자 목록(arbitrary argument lists)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용
- 여러개의 인자를 tuple로 처리
```
def calculate_sum(*args):
    print(args) # (1, 100, 5000, 30)
    print(type(args)) # <class 'tuple'>

calculate_sum(1, 100, 5000, 30)
```

5. 임의의 키워드 인자 목록(arbitrary keyword argument lists)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용
- 여러 개의 인자를 dictionary로 묶어 처리
```
def print_info(**kwargs):
    print(kwargs)

print_info(name='eve', age=30) # {'name' : 'eve', 'age' : 30}
```

함수 인자 권장 작성 순서 : 위치 -> 기본 -> 가변 -> 가변키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- 단 모든 상황에 적용되는 규칙은 아님

### 재귀 함수
재귀 함수 : 함수 내부에서 자기 자신을 호출하는 함수

예시: 팩토리얼
```
def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n-1)

# 팩토리얼 계산 예시
print(factorial(5)) # 120
```

재귀 함수의 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- 재귀함수는 메모리 사용량이 많고 느릴 수 있음
- 종료 조건이 잘못되면 스택 오버플로우 에러가 발생할 수 있음
(스택 오버플로우: 작업 공간에 일이 너무 많이 쌓여 프로그램이 멈추는 오류)

재귀함수를 사용하는 이유
- 문제의 자연스러운 표현
- 코드 간결성
- 수학적 문제 해결

### 내장 함수
내장함수(built-in) : 파이썬이 기본적으로 제공하는 함수
(별도의 import없이 바로 사용 가능)

*파이썬 공식 문서에서 보면 좋은것 : 자습서, 라이브러리 레퍼런스, 언어 레퍼런스*

### 함수와 scope
python의 범위
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

scope
- global scope : 코드 어디에서든 참조할 수 있는 공간
- local scope : 함수가 만든 scope

variable
- global variable(전역 변수) : global scope에 정의된 변수
- local variable(지역 변수) : locla scope에 정의된 변수

변수 수명 주기
1. built-in scope : 파이썬이 실행된 이후부터 영원히 유지
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

이름 검색 규칙
아래와 같은 순서로 이름을 찾아 나가며, legb rulr이라고 부름
1. local scope : 지역범위
2. enclosed scope : 지역범위 한 단계 위 범위
3. global scope : 최상단에 위치한 범위
4. built-in scope : 모든 것을 담고 있는 범위

함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 불가
```
# LEGB Rule 예시 문제
x = 'G'
Y = 'G'

def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # EPL

    inner_func('P')
    print(x, y) # EE

outer_func()
print(x, y) # GG
```


global 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우 사용

```
num = 0 # 전역 변수

def increment():
    global num # num을 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1
```

주의사항
1. global 키워드 선언 전에 참조 불가(=참조 후에 선언하지 말것)
```
num = 0
def increment():
    print(num) # 전역변수(수정불가) 참조
    global num # 전역변수를 수정가능 선언(error)
    num += 1
```

2. 매개변수에는 global 키워드 사용 불가
```
num = 0
def increment(num): # global에 num이 있으므로 매개변수로 사용 불가
    global num
    num += 1
```

### 함수 스타일 가이드
기본규칙
- 소문자와 언더 스코어(_) 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양
- T/F를 반환하는 함수의 경우 is로 시작하는 경우가 많음

단일책임 원칙 : 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

함수 설계 원칙
1. 명확한 목적
  - 함수는 한 가지 작업만 수행
  - 함수 이름으로 목적을 명확히 표현
2. 책임 분리
  - 데이터 검증, 처리, 저장 등을 별도 함수로 분리
  - 각 함수는 독립적으로 동작 가능하도록 설계
3. 유지보수성
  - 작은 단위의 함수로 나누어 관리
  - 코드 수정 시 영향 범위를 최소화

### packing & unpacking
패킹 : 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정

기본원리
- 여러 개의 값을 하나의 튜플로 묶는 파이썬의 기본 동작
- 한 변수에 콤마(,)로 구분된 값을 넣으면 자동으로 튜플로 처리

'\*'를 활용한 패킹(함수 매개변수 작성 시)
- 남는 위치의 인자들을 튜플로 묶기
- '\*'를 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듦
```
def my_func(*args):
    print(args) # (1, 2, 3, 4, 5)
    print(type(args)) # <class 'tiple'>

my_func(1, 2, 3, 4, 5)
```

'**'을 활용한 패킹(함수 매개변수 작성 시)
- 남는 키워드 인자들을 딕셔너리로 묶기
- '**'룰 붙인 매개변수가 남는 키워드 인자들을 모두 모아 하나의 딕셔너리로 만듦
```
def my_func(**kwargs):
    print(kwargs) # {'a' : 1, 'b' : 2, 'c' : 3}
    print(type(kwargs)) # <class 'dict'>

    my_func(a=1, b=2, c=3)
```

언패킹 : 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓는 과정

기본원리




'\*'를 활용한 패킹(함수 인자 전달)
리스트나 튜플 앞에 '*'를 붙여 각 요소를 함수의 개별 위치 인자로 전달
```
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names) # alice jane peter
```

**를 활용한 언패킹(딕셔너리->함수 키워드 인자)
딕셔너리 앞에 **를 붙여 {키:값}쌍을 키=값 형태의 키워드 인자로 전달
```
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
my_function(**my_dict) # 1 2 3
```

packing & unpacking, \* & ** 정리
|구분|상황|\* 연산자|** 연산자|
|:---|:---:|:---|:---|
|패킹|함수 **정의** 시|여러 위치의 인자를 하나의 **튜플**로 받음|여러 키워드 인자를 하나의 **딕셔너리**로 받음|
|언패킹|함수 **호출** 시|리스트/튜플을 개별 **위치 인자**로 전달|딕셔너리를 개별 **키워드 인자**로 전달|



### 참고
함수와 반환
- 파이썬 함수는 언제나 단 하나의 값(객체)만 반환할 수 있음
- 여러 값을 반환하는 경우에도 하나의 튜플로 패킹하여 반환
```
def get_user_info():
    name = 'alice'
    age = 30
    # 콤마(,)로 여러 값을 반환하는 것처럼 보임
    return name, age

# 반환된 값을 user_data 변수에 담아 확인하면
user_data = get_user_info()

# 단 하나의 튜플을 반환하는 것
print(user_data) # ('alice', 30)
```

람다 표현식
- 익명 함수를 만드는 데 사용되는 표현식
- 한 줄로 간단한 함수를 정의

```
# 람다 표현식 활용(with map 함수)
numbers = [1, 2, 3, 4, 5]

# 람다 미사용
def square(x):
    return x**2

squared1 = list(map(square, numbers))
print(squared1) # [1, 4, 9, 16, 25]

# 람다 사용
squared2 = list(map(lamda x: x**2, numbers))
print(squared2) # [1, 4, 9, 16, 25]
```

```
# 람다 표현식 활용(with sorted 함수)
students = [(23, 90), (19, 95), (25, 85)]

# 람다 미사용
def get_age(student_data):
    return student_data[0]

sorted_students = sorted(students, key=get_age)
print(sorted_students) # [(19, 95), (21, 90), (25, 85)]

# 람다 사용
sorted_students = sorted(students, key=lamda student_data: student_data[0])
print(sorted_students) # [(19, 95), (21, 90), (25, 85)]
```