### 문자열
#### 코드체계
코드체계 : 문자에 대응되는 숫자를 정한 것

코드체계의 문제
- 네트워크가 발전되기 전 미국의 각 지역 별로 코드체계를 정해놓고 사용
- 네트워크가 발전하면서 서로 정보를 주고 받을 때 정보를 달리 해석한다는 문제가 생김

코드체계의 개선
- 혼동을 피하기 위해 표준안을 만듦
- 1967년, 미국에서 ASCII(American Standard Code Information Interchange)라는 문자 인코딩 표준이 제정됨
- ASCII는 7-bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 문자들로 이루어짐

![출력가능한 아스키 문자(32~126)](/c/Users/SSAFY/Desktop/ksc/TIL/ssafy/algorithm/2025-08-08/"출력가능아스키.png")

확장 아스키(Extended ASCII)
- 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가
- 표준 아스키는 7-bit를 사용하여 문자를 표현, 확장 아스키는 1Byte 내의 8-bit를 모두 사용함으로써 추가적인 문자를 표현할 수 있음
- 컴퓨터 생산자와 소프트웨어 개발자가 여러 가지 다양한 문자에 할당할 수 있도록 하고 있고, 이렇게 할당된 확장 부호는 표준 아스키와 같이 서로 다른 프로그램이나 컴퓨터 사이에 교환되지 못함
- 표준 아스키는 마이크로컴퓨터 하드웨어 및 소프트웨어 사이에서 세계적으로 통용되는 데 비해, 확장 아스키는 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독될 수 있음

유니코드 : 다국어 처리를 위한 표준 코드체계
- 컴퓨터가 발전하면서 미국 뿐 아니라 각 나라에서 컴퓨터가 발전함
- 각 국가들은 자국의 문자를 표현하기 위하여 코드체계를 만들어서 사용하게 됨
  - 우리나라도 한글 코드체계를 만들어 사용했고 조합형, 완성형 두 종류를 가지고 있었음
- 인터넷이 전 세계로 발전하면서 ASCII를 만들기 전과 같은 문제가 국가 사이에 정보를 주고 받을 때 발생함.
- 자국의 코드체계를 타국가가 가지고 있지 않으면 정보를 잘못 해석 할 수 밖에 없음
- 다국어 처리를 위해 표준인 유니코드를 만듦
  - 비영리 단체인 유니코드 컨소시엄에서 관리
  - 이모지도 유니코드 문자

유니코드 Character Set
- 유니코드도 다시 Character Set으로 분류됨
- UCS-2(Universal Character Set 2)
- UCS-4(Universal Character Set 4)
- 유니코드를 저장하는 변수의 크기를 정의함
  - 그러나, 바이트 순서에 대해서는 표준화 하지 못했음
- 파일을 읽을 때 UCS-2, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야 하는 문제가 발생.
  - 그래서 유니코드의 적당한 외부 인코딩이 필요하게 됨

바이트 단위 저장 순서
- 바이트 단위 저장 순서가 정해지지 않은 경우 잘못된 해석 가능성
  - 여러 바이트로 이루어진 데이터를 저장하는 방식을 Endian이라고 함
  - Big-endian은 상위 바이트(MSB, Most Significant Byte)를 가장 낮은 주소에 저장
  - Little-endian은 하위 바이트(LSB, Least Significant Byte)를 가장 낮은 주소에 저장

유니코드 인코딩(UTF : Unocode Transformation Format)
- UTF-8 (in web)
  - MIN : 8-bit, MAX : 32-bit(1Byte*4)
  - 필요한 크기에 따른 저장 방법 예
    - 0xxxxxxx
    - 110xxxxx 10xxxxxx
    - 1110xxxx 10xxxxxx 10xxxxxx
    - 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
- UTF-16 (in windows, java)
  - MIN : 16-bit, MAX : 32-bit(2Byte*2)
- UTF-32 (in unix)
  - MIN : 32-bit, MAX : 32-bit(4Byte*1)

줄바꿈 코드
- 윈도우는 CR(13)LF(10) 두글자 사용
- Unix와 macOS는 LF(10) 한글자 사용

Python 인코딩
- UTF-8
  - 2.x 버전은 기본 인코딩 방식이 ASCII로 UTF-8 사용시 코드 첫 줄에 다음 문장을 추가해야 함
    - #-*-coding:utf-8-*-
    - 3.x 버전은 UTF-8 방식이 기본이므로 표시 생략
- 다른 인코딩 방식으로 처리시 첫 줄에 작성하는 항목에 원하는 인코딩 방식을 지정해주면 됨

코드체계의 핵심 : 전 세계의 모든 문자를 컴퓨터가 일관되게 표현하고 처리하는 것

#### 문자열
문자열(String) : 문자들이 순서대로 나열된 데이터

문자열의 분류
- Length-Controlled 문자열
  - 문자열의 길이 정보를 함께 저장해서, 그 길이만큼 문자 데이터를 읽는 방식
  - java, Python, 네트워크 패킷에 사용
- Delimited 문자열
  - 문자열의 끝을 나타내는 특정한 구분자(Delimiter)가 있어서, 구분자가 나올 때까지 문자열로 인식
  - C언어는 널문자(null, '\0')를 사용

파이썬 str 클래스 구조
- 길이 외에 다른 정보도 저장
  - PyObject_HEAD : 모든 Python 객체가 상속하는 공통 구조
  - length : 문자열의 길이
  - hash : 문자열의 해시값, 딕셔너리 키로 쓸 때 사용
  - interned : 같은 문자열을 관히라는 플래그
  - kind : 문자열의 인코딩 크기
  - data : 문자열이 저장된 실제 메모리 주소를 가리키는 포인터

C언어에서 문자열
- 문자열은 문자들의 배열 형태로 구현된 응용 자료형
- 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자('\0') 필요
  - char ary[]-"abc"; // char ary[] = {'a', 'b', 'c', '\0'};
- 문자열 처리에 필요한 연산을 함수 형태로 제공
  - strlen(), strcpy(), strcmp(),...

Java에서의 문자열
- 문자열 데이터를 저장, 처리해주는 클래스를 제공함
- String 클래스
  - String str = "abc"; // 또는 String str = new String("abc")
- 문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공함
  - +, lebgth(), replace(), split(), substring(),...

Python3에서의 문자열
- 텍스트 데이터의 취급방법이 통일되어 있음
  - python2와 달리 바이트 문자열과 unicode 구분이 없음
  - 유니코드 기반이라 어떤 언어나 기호도 동일한 방식으로 처리
- 문자열 기호
  - '(홑따옴표), "(쌍따옴표), '''(홑따옴표 3개), """(쌍따옴표 3개)
- 연산
  - +연결
    - 문자열 + 문자열 : 이어 붙여주는 역할
    - 예 : 'ab' + 'c' -> 'abc'
  - *반복
    - 문자열 * 수 : 수만큼 문자열이 반복
    - 예 : 'ab'*3 -> 'ababab'
- 문자열은 데이터의 순서가 구분되는 시퀀스 자료형으로 분류됨
  - 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
- 문자열 클래스에서 제공되는 메소드
  - replace(), split(), isalpha(), find(),...
- 문자열은 튜플과 같이 요소값을 변경 할 수 없음(immutable)

C, Java, Python3 문자열의 차이
- c는 아스키 코드로 저장
  - 한글을 출력할 수 있으나 콘솔의 도움을 받아야 함
- Java는 유니코드(UTF=16, 2-Byte)로 저장
- Python3는 유니코드(UTF-8)로 저장

Python에서의 문자열 입력
- input() 함수로 읽기
```python
text = input()
```
  - Hello python을 입력하면 빈칸을 포함해 한 행을 읽어들입니다.

#### 연습문제
Python에서의 문자열 입력
- 두 개의 문자열 s1과 s2. s1의 각 글자가 s2에 모두 존재하는가?
```python
# XYPV
# EOGGXYPVSY

s1 = input()
s2 = input()

s1 = list(input())
s2 = list(input())
```

- 첫 줄에 N, 다음에 NxN 문자열. 'Z'가 존재하는가?
```python
# 5
# GOFFA
# OYECR
# UJAJQ
# JAEZN
# WJAKC

N = int(input())
text = [input() for _ in range(N)]

N = int(input())
text = [list(input()) for _ in range(N)]
```

- 첫 줄에 N, 다음에 NxN 지도, # 집중호우 피해구역. 피해구역 수는?
```python
# 5
# 000#0
# 00###
# 000#0
# 00#00
# 000#0

N = int(input())
text = [input() for _ in range(N)]

N = int(input())
text = [list(input()) for _ in range(N)]
```
-                            AB
- 첫 줄에 N, 다음에 NxN 문자열. CD 패턴이 존재하는가?
```python
# 5
# GOFFA
# OYECR
# UJAJQ
# JAEZN
# WJAKC

N = int(input())
text = [input() for _ in range(N)]

N = int(input())
text = [list(input()) for _ in range(N)]

delta = [[0, 1], [1, 1], [1, 0]]
answer = 0
for i in range(4):
    for j in range(4):
        if text[i][j] == 'A':
            for d in rnage(3):
                di, dj = delta[d]
                ni = i + di
                nj = j + dj
                if (d == 0) and text[ni][nj] != 'B':
                    break
                elif (d == 1) and text[ni][nj] != 'D':
                    break
                elif (d == 2) and text[ni][nj] == 'C':
                    answer = 1
if answer == 1:
    print("패턴은 실존한다!")
else:
    print("아직도 패턴같은 것을 믿는 바보가 있다니")
```

#### 연산


### 패턴매칭
#### 고지식한 패턴 검색


#### KMP 알고리즘



#### 보이어-무어 알고리즘


#### 문자열 암호화