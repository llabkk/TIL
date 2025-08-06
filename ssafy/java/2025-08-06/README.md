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

arr3 = new int[] {5, 6, 7, 8} // 재할당 가능

arr3 = {5, 6, 7, 8}           // 오류, 재할당 불가능
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

배열의 인덱스
- []사이에 숫자를 넣으면 해당 위치의 요소에 접근할 수 있음
- 인덱스는 0부터 시작 → 길이가 5인 배열의 인덱스 : 0, 1, 2, 3, 4
- 음수를 사용할 수 없음
- 접근이 가능한 배열의 인덱스 범위를 벗어나면 오류 발생
- .length를 이용하여 배열의 길이를 구할 수 있음

배열의 순회
- 반복문을 이용하여 배열의 요소를 순회할 수 있음
```java
int[] intArray = {1, 3, 5, 7, 9}

for (int i = 0; i < intArray.length; i++) {
  System.out.println(intArray[i])
}
```

배열의 순회(for-each)
- 가독성이 개선된 반복문으로, 배열 및 collections에서 사용가능
- index 대신 직접 요소(elements)에 접근하는 변수를 제공
- naturally ready only(copied value)

```java
// for-each
// for(요소: 반복할 것)

int[] intArray = {1, 3, 5, 7, 9};

for(int x : intArray) {
  System.out.println(x);
}

// read only
for(int x : intArray) {
  x *= 2;
}
System.out.println(Arrays.toString(intArray));
// [1, 3, 5 ,7 ,9]
```

얕은 복사(shallow copy)
- 객체 내부의 참조형 변수는 원본 객체의 참조를 복사
- 원본 객체와 복사본이 같은 참조를 가리키므로, 하나를 수정하면 다른 객체에도 영향을 미침
```java
import java.util.Arrays;

public class ShallowCopyExample {
    public static void main(String[] args) {
        int[] original = {1, 2, 3};
        int[] shallwCopy = original; // 얕은 복사(참조 공유)

        shallowCopy[0] = 10;

        System.out.println(Arrays.toString(original)) // [10, 2, 3]
        System.out.println(Arrays.toString(shallowCopy)) // [10, 2, 3]
    }
}
```

깊은 복사(deep copy)
- 객체의 모든 필드 값을 새로 복사하여 독립적인 객체를 생성
- 원본 객체와 복사본은 완전히 별개의 메모리 공간을 가지므로, 한 객체의 변경이 다른 객체에 영향X
```java
import java.util.Arrays;

public class DeepCopyExample {
    public static void main(String[] args) {
        int[] original = {1, 2, 3};
        int[] deepCopy = Arrays.copyOf(original, original.length); // 깊은 복사

        deepCopy[0] = 10;

        System.out.println(Arrays.toString(original)) // [1, 2, 3]
        System.out.println(Arrays.toString(deepCopy)) // [10, 2, 3]


    }
}

public class DeepCopyExample2 {
    public static void main(String[] args) {
        int[] original = {1, 2, 3};
        int[] deepCopy = new int[original.length]; // 새로운 배열 생성
        
        // 새로운 배열에 값 저장하기
        for(int i = 0; i<original.length; i++>) {
            deepCopy[i] = original[i];
        }
        deepCopy[0] = 10;

        System.out.println(Arrays.toString(original)) // [1, 2, 3]
        System.out.println(Arrays.toString(deepCopy)) // [10, 2, 3]

        
    }
}
```

배열의 복사
- 배열은 고정된 크기이므로 배열의 크기를 변경하고 싶다면 새로운 배열을 생성하여 복사해야함

배열의 복사 메서드
- Arrays.copyOf() : 배열을 복사하여 새로운 배열을 생성
```java
int[] original = {10, 20, 30};
int[] copy = Arrays.copyOf(original, original.length);
System.out.println(Arrays.toString(copy)); // [10, 20, 30]
```
- Arrays.copyOfRange() : 배열의 특정 범위를 복사하여 새로운 배열을 생성
```java
int[] numbers = {10, 20, 30, 40, 50};
int[] subArray = Arrays.copyOfRange(numbers, 1, 4);
System.out.println(Arrays.toString(subArray)); // [20, 30, 40]
```
- System.arratcopy(Object src, int srcPos, Object dest, int destPos, int length)

#### 다차원 배열
