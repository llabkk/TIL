### 비시퀀스 데이터 구조
#### 딕셔너리
dictionary : 키와 값을 짝지어 저장하는 자료구조
- 딕셔너리는 내부적으로 해시 테이블을 사용하여 키-값 쌍을 관리
- 키를 통한 값의 삽입, 삭제, 검색이 데이터의 크기와 관계없이 매우 빠름
- 키는 hashable한 고유 값이어야 하지만, 값은 중복이 가능하고 어떤 자료형도 저장할 수 있음

딕셔너리 메서드
메서드|설명
|---|---|
***D.get(k)***|키 k에 연결된 값을 반환(키가 없으면 None을 반환)
***D.get(k, v)***|키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환
***D.keys()***|딕셔너리 D의 키를 모은 객체를 반환, 만들어진 객체는 실시간으로 반영됨(key가 추가되거나 삭제되면 실시간 반영)
***D.values()***|딕셔너리 D의 값을 모은 객체를 반환, 만들어진 객체는 실시간으로 반영됨(value가 추가되거나 삭제되면 실시간 반영)
***D.items()***|딕셔너리 D의 키/값 쌍을 모은 객체를 반환, 만들어진 객체는 실시간으로 반영됨(key/value 쌍이 추가되거나 삭제되면 실시간 반영)
***D.pop(k)***|딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 오류)
***D.pop(k,v)***|딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 v를 반환)
D.clear()|딕셔너리 D의 모든 키/값 쌍을 제거
D.setdefault(k)|딕셔너리 D에서 키 k와 연경된 값을 반환
D.setdefault(k,v)|딕셔너리 D에서 키 k와 연결된 값을 반환, k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환, v미입력 시 값으로 None 사용
D.update(other), ohter은 딕셔너리|other 내 각 키에 대해 D에 있는 키면 그 키의 값을 other에 있는 값으로 대체, other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가

#### 세트
set : 고유한 항목들의 정렬되지 않은 컬렉션
- set은 내부적으로 해시 테이블을 사용하여 데이터를 저장함
- 이로 인해 항목의 고유성을 효율적으로 보장하며, 항목의 추가, 삭제, 존재 여부 확인(in 연산)이 데이터의 크기에 관계없이 매우 빠름
- 또한, 합집합(union), 교집합(intersection), 차집합(difference) 등 수학적인 집합 연산을 간편하게 수행할 수 있는 것이 가장 큰 특징

세트 메서드
메서드|설명
|---|---|
***s.add(x)***|세트 s에 항목 x를 추가, 이미 x가 있다면 변화 없음
s.update(iterable)|세트 s에 다른 iterable 요소를 추가
s.clear()|세트 s의 모든 항목을 제거
***s.remove(x)***|세트 s에서 항목 x를 제거, 항목 x가 없을 경우 key error
s.pop()|세트 s에서 임의의 항목을 반환하고, 해당 항목을 제거(무작위는 아님)
s.discard(x)|세트 s에서 항목 x를 제거

세트의 집합 메서드
메서드|설명
|---|---|
set1.difference(set2)|set1과 set2의 합집합 (set1- set2)
set1.intersection(set2)|set1과 set2의 교집합 (set1 and set2)
set.issubset(set2)|
set.issuperset(set2)|
set1.union(set2)|set1과 set2의 합집합 (set1 + set2)

### 참고
#### 해시 테이블
hash table : 해시 테이블은 키와 값을 짝지어 저장하는 자료구조

해시 테이블의 원리
1. 키를 해시 함수를 통해서 해시 값으로 변환
2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
3. 이로 인해 검색, 삽입, 삭제를 매우 빠르게 수행

해시 : 임의의 크기를 가진 데이터를 고정도니 크기의 고유한 값으로 변환하는 것
- 생성된 해시 값(고유한 정수)은 해당 데이터를 식별하는 '지문'역할
- 파이썬에서는 이 해시 값을 이용해 해시 테이블에 데이터를 저장
- 이 변환을 수행하는 것이 해시 함수

해시 함수 : 임의의 길이 데이터를 입력 받아 고정 길이(정수)로 변환해 주는 함수. 이 '정수'가 바로 해시 값
- 주로 해시 테이블을 구현할 때, 매우 빠른 검색 및 데이터 저장 위치 결정을 위해 사용
- '해시 알고리즘'이라고도 부름
- 입력 값이 정수인 경우 해시값이 자신과 동일하거나 단순 계산으로 고정됨
- 입력 값이 문자열인 경우 해시 난수화가 적용되어 실행마다 순서가 달라질 수 있음

set의 요소 & dict의 키와 해시 테이블의 관계
- set
  - 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷에 위치시킴
  - 그래서 '순서'라기보다 '버킷위치(인덱스)'가 요소의 위치를 결정
  - 따라서 set는 순서를 보장하지 않음

- dict
  - 키->해시 함수->해시 값->해시 테이블에 저장
  - 단 set와 달리 '삽입 순서'는 유지한다는 것이 언어 사양에 따라 보장됨
    - 즉, 키를 추가한 순서대로 반복문 순회할 때 나오게 됨
    - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된 것

파이썬에서의 해시 함수
- 정수
  - 같은 정수는 항상 같은 해시 값을 가짐
- 문자열
 - 문자열 해시 시, 파이썬 인터프리터 시작 때 설정되는 난수 시드(seed)가 달라질 수 있음
 - 보안상 이유로 해시 난수화 도입
 - 각 실행마다 달라질 수 있어 'a'의 해시 값도 매번 바뀔 수 있음

hashable
- hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미
- 대부분의 불변 타입은 해시 가능(int, float, str, tuple(안에 불변값만 존재할 때))
- 가변형 객체(list, dict, set)는 기본적으로 해시 불가능

hashable과 불변성 간의 관계
- 해시 테이블에는 hashable만 저장 가능
- 불변 객체는 생성 후 값 변경이 불가능 하므로, 항상 같은 해시 값을 유지

#### 파이썬 문법 규격
EBNF : BNF를 확장한 표기법, 메타기호를 추가하여 더 간결하고 표현력이 강해진 형태

메타기호|의미
|---|---|
[]|선택적 요소
{}|0번 이상 반복
()|그룹화