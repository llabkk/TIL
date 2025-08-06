### 배열
#### 배열의 이해
배열
- 동일한 데이터 타입의 값(0개 이상)들을 저장하기 위한 자료구조
- 인덱스를 이용하여 각 요소에 접근할 수 있음
- 고정된 크기 (생성된 배열의 크기를 바꿀 수 없음)
- 메모리에 연속적으로 저장이 됨

배열 선언
- 데이터타입[] 배열이름 (주로 사용하는 방법)
- 데이터타입 배열이름[]

자료형|배열이름(변수명)|배열 선언문
---|---|---
int|intArray|int[] intArray;
char|charArray|char[] charArray;
boolean|boolArray|boolean[] boolArray;
String|strArray|String[] strArray;
float|floatArray|float[] floatArray;

배열의 생성과 초기화
- 자료형[] 배열이름 = new 자료형[길이];   // 배열 생성(자료형의 초기값으로 초기화)
- 자료형[] 배열이름 = new 자료형[] {값1, 값2, 값3, 값4};  // 배열 생성 및 값 초기화
- 자료형[] 배열이름 = {값1, 값2, 값3, 값4};   // 선언과 동시에 초기화, 선언과 동시에 이루어질때만 가능
```java
int[] arr1 = new int[5];

String[] arr2 = new String[] {"김승철", "자바"};

int[] arr3 = {1, 2, 3, 4}

arr4 = new int[] {5, 6, 7, 8}

arr5 = {5, 6, 7, 8} // 오류
```

자료형|기본값|비고
---|---|---
boolean|false|
char|'\u0000'|공백 문자(널 문자)
byte, short, int|0|
long|0L|
float|0.0f|
double|0.0|
참조형 변수|null|아무것도 참조하지 않음


#### 다차원 배열
