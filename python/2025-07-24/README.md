### 모듈
모듈 : 한 파일로 묶인 변수와 함수의 모음
- 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

모듈 예시
- math 내장 모듈 : 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈

#### 모듈 활용
import 문 사용
- 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
```
import math

print(math.pi)      # 모듈명.변수명
print(math.sqrt(4)) # 모듈명.함수명
```

from 절 사용
- 코드가 짧고 간결해짐
```
from math import pi, sqrt

print(pi)       # 변수명
print(sqrt(4))  # 함수명
```

from 절 사용시 주의사항
- 서로 다른 모듈에서 import된 변수나 함수의 이름이 같은 경우 이름 충돌이 발생
- 마지막에 import된 것이 이전 것을 덮어쓰기 때문에 나중에 import된 것만 유효함
```
from math import sqrt     # math.sqrt가 먼저 import 됨
from my_math import sqrt  # my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9)  # math.sqrt가 아닌 my_math.sqrt가 사용됨
```

'as' 키워드
as 키워드를 사용하여 별칭(alias)을 부여
- 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
```
from math import sqrt
from my_math import sqrt as my_sqrt

sqrt(4)
my_sqrt(4)

--------------------------------------
# 별칭을 붙이지 않으면 길고 불편
import pandas as pd
import matplotlib.pyplot as plt

# 짧고 편리
df = pd.DataFrame()
plt.plot(x, y)
```

#### 사용자 정의 모듈
직접 정의한 모듈 사용하기

### 파이썬 표준 라이브러리
PSL(python standard library) : 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

#### 패키지
패키지 : 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

패키지의 모듈을 사용하는 방법
```
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))
print(tools.mod(1, 2))
```
tip
- 너무 많은 기능이 한 파일에 몰려 있으면 사용자가 헷갈릴 수 있음
- 비슷한 기능은 묶고, 관련 없는 것은 나누는 것이 사용하기 편함

패키지의 종류
- psi 내부 패키지
- 파이썬 외부 패키지(웹) : 사용할 패키지를 설치 할 때는 'pip'를 사용

pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

패키지 설치
최신 버전/특정 버전/최소 버전을 명시하여 설치할 수 있음
-터미널에서 사용
```
pip install somepackage         # 최신 버전
pip install somepackage==1.0.5  # 특정 버전
pip install somepackage>=1.0.4  # 최소 버전
```

request 패키지

pip를 통해 request 패키지를 설치
- terminal에서 사용
```
pip install requests 
```

request를 import하여 웹에 데이터 요청
```
import requests

url = "링크"
response = requests.get(url).hson()
print(response)
```
패키지 사용 목적
- 모듈들의 이름공간을 구분하여 충돌을 방지
- 모듈들을 효율적으로 관리하고 할 수 있도록 돕는 역할

### 제어문
- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

### 조건문
조건문 : 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

#### if statement
if 문
- 조건문의 기본 형태
- if문에 작성된 조건을 만족할 때 내부 코드 실행
- 작성되는 조건은 표현식으로 작성

elif 문
- 이전의 조건을 만족하지 못하고 추가로 다른 조건이 필요할 때 사용
- 여러 개의 elif문을 사용 가능 

else 문
- 모든 조건들을 만족하지 않으면 실행됨

조건문 예시
```
score = 100
if score > 95: # 조건(표현식)
    print('축하합니다!')
else:
    print('수고하셨습니다')
```
복수 조건문
- 조건식을 순차적으로 비교하므로 순서를 잘 정렬

중첩 조건문
- 조건문 내부에 다른 조건문 작성 가능

### 반복문
loop statement : 주어진 코드 블록을 여러 번 반복해서 실행하는 구문

#### for statement
- 반복 가능한 객체의 요소들을 반복하는데 주로 사용
- 주로 반복 가능한 객체 요소의 개수만큼 반복
- 특징 : 반복 횟수가 정해져 있음
```
```

반복가능한 객체 : 요소를 하나씩 반환할 수 있는 모든 객체
- 시퀀스 자료형(list, tuple, str), 비 시퀀스 자료형(dict, set)

for문 작동원리
- 리스트 내 첫 항목이 반복 변수(student)에 할당되고 코드블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 실행
- 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
- 더 이상 반복 변수에 할당할 값이 없으면 반복 종료

```
students = ['alice', 'bob', 'poter']

for student in students:
    print(f'{student} hi!')
```

문자열 순회
- 문자열 반복시 문자가 반복 변수에 할당되어 반복 수행
```
county = 'korea'

for char in country:
    print(char)

# 출력
# k
# o
# r
# e
# a
```

range 순회
- 특정 숫자 범위만큼 반복을 하고 싶을 때 range함수를 사용
```
for i in range(5):
    print(i)

# 출력
# 0
# 1
# 2
# 3
# 4
```

딕셔너리 순회
- dict 자료형은 비시퀀스 자료형으로 반복 순서가 보장되지 않음
```
my_dict = {
  'x': 10,
  'y': 20,
  'z': 30,
}

# key에는 dict의 키값만 저장
for key in my_dict:
    print(key)
    print(my_dict[key])

# 출력
# x
# 10
# y
# 20
# z
# 30
```

**인덱스로 리스트 순회**
- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
- 인덱스를 사용하면 리스트의 원하는 위치에 있는 값을 읽거나 변경할 수 있음
```
numbers = [4, 6, 10, -8, 5]

for i range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10]
```

중첩된 반복문
```
outers = ['a', 'b']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 출력
# a, c
# a, d
# b, c
# c, d
```

중첩 리스트 순회
- 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
```
elements = [['a', 'b'], ['c', 'd']]

for elem in elements:
    print(elem)

# 출력
# ['a', 'b']
# ['c', 'd']
```
```
elements =[['a', 'b'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)

# 출력
# a
# b
# c
# d
```

#### while statement
- while 조건이 참(True)인 동안 반복
- 반복 횟수가 정해지지 않은 경우 주로 사용
```
input_value = ''
while input_value != 'exit':
    input_value = input('enter a value: ')
    print(input_value)
```

while문의 반복 원리
- while의 조건식 확인
  - 조건식이 참이면 실행, 거짓이면 반복 종료
-코드 블록 실행이 마무리되면 다시 while 조건식 확인
```
a= 0

while a<3:
    print(a)
    a= a + 1
```

while문의 특징 : 반드시 종료 조건이 필요
- 예상치 못한 상황에 대비해 break문을 활용하면 반복문을 안전하게 종료 가능

#### 반복 제어
for문과 while문은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

반복 제어 키워드 : 반드시 반복문안에서만 사용 가능

break 키워드
- 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료
- 반복을 끝내야 할 명확한 조건이 있을 때 사용
```
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 ==0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다.')
```

continue 키워드
- 해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 수행
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# 출력
# 1
# 3
# 5
# 7
# 9
```

빈 코드 블록 키워드

pass
- 아무 동작도 하지 않음을 명시적으로 나타내는 키워드
- 반복 제어가 아닌 코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도로 사용
- 코드를 비워두면 오류가 발생하기 때문에 pass 키워드를 사용
- 반복문 뿐만 아니라 함수 조건문에서도 사용 가능

#### 유용한 내장 함수 map & zip

map(function, iterable)
- 반복가능한 데이터구조(iterable)의 모든 요소에 function을 적용하고, 그 결과 값들을 map object로 묶어서 반환
- map object : 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형, 전체 값을 확인하려면 list나 tuple로 형변환을 해줘야함

zip(*iterables)
- zip 함수는 여러개의 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 그것들을 모아 zip object로 반환하는 함수

#### 참고
for-else 문법
for 루프가 break를 만나 중단되지 않고 끝까지 정상적으로 완료되었을 때만 else블록이 실행

enumerate(iterable, start=0) : iterable 객체의 각 요소에 대해 인덱스 값을 함께 반환하는 내장함수