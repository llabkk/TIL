## easy
### Numpy
```python
import numpy as np
np.array([1, 3, 5, 7])
# [1 3 5 7]
# <class 'numpy.ndarray>
# 1차원 벡터

np.array([1, 2, 2], [1, 1, 5])
# [[1 2 2]
#  [1 1 5]]
# <class 'numpy.ndarray>
# 2차원 행렬
```
- 선형 변환은 행렬 곱으로 실행

- **행렬곱 (Matrix Multiplication)**: 선형대수의 행렬 곱셈 규칙을 따릅니다
  - 수학 기호: `×` 또는 `·`
  - NumPy: `@` 연산자, `np.matmul()` 함수 사용
  - 용도: 변환 합성, 선형변환 적용

- 회전 행렬
<br><br>
$
\Large
\begin{bmatrix}
cos θ & -sin θ \\
sin θ & cos θ
\end{bmatrix}
$<br><br>

- 반사 행렬(x축 기준 뒤집기)
<br><br>
$
\Large
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$<br><br>

- **원소곱 (Element-wise Multiplication)**: 같은 위치의 원소끼리만 곱합니다
  - 수학 기호: `⊙` (Hadamard product)
  - NumPy: `*` 연산자 사용
  - 용도: 배열의 각 원소를 개별적으로 스케일링

numpy method
- numpy.zeros(num): 0을 원소로 하는 벡터(행렬) 생성

```python
import numpy as np
A = np.zeros(5)
# [0. 0. 0. 0. 0.]

A = np.zeros(2, 5)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
```

- numpy.random.rand(num): 무작위 수를 원소로 하는 벡터(행렬) 생성

```python
import numpy as np
np.random.seed(42)
A = np.random.rand(5)
# [0.05808361 0.86617615 0.60111501 0.70807258 0.02058449]

A = np.random.rand(2, 5)
# [[0.37454012 0.95071431 0.73199394]
#  [0.59865848 0.15601864 0.15599452]]
```

- numpy.eyes(num): 단위 행렬 생성

```python
import numpy as np
A = np.eyes(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

- nimpy로 가능한 수학 계산
```python
import numpy as np

A = np.array([4, 16, 25])
print(np.sum(A)) # 전체 합
print(A ** 2) # 제곱
print(np.sqrt(A)) # 제곱근
print(np.log2(A)) # 로그 (밑수 = 2)
print(np.log(A)) # 로그 (밑수 = e, = 자연로그)
print(np.exp(A)) # 자연상수(e)의 지수함수

print('삼각함수')
B = np.array([np.pi / 5, np.pi / 3]) # π/5 값과 π/3
print(np.sin(B)) # sin
print(np.cos(B)) # cos
```

- numpy 속성 확인
```python
import numpy as np

def show_info(A : np.ndarray):
  print(A.size) # 원소의 수
  print(A.ndim) # 2차원 벡터 데이터를 가진 행렬
  print(A.shape) # 3 x 3 행렬

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
show_info(A)
```

- triu(상삼각행렬추출), Transpose (전치연산)
  - triu : 위에 삼각형 부분만 남기고 다 삭제 (AI에서 가끔 씀)
  - Transpose : 열과 행을 바꿈 (AI에서 자주 씀)
```python
import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(np.triu(A)) # 행렬에 삼각형 Upper 부분만 남기고, 나머지 다 0으로 만듭니다.
# [[ 1  2  3  4]
#  [ 0  6  7  8]
#  [ 0  0 11 12]
#  [ 0  0  0 16]]

B = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(B)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

C = B.T # Transpose
print(C)
# [[1 3 5 7]
#  [2 4 6 8]]
```

- numpy 의 linspace : linear space, 균일한 간격으로 수를 나눠주는 함수
- matplot library 를 사용하기 위해 (x, y) 값들을 만들어 두고 Library 에 넣어 주면 됩니다.
```python
import numpy as np

# numpy의 Linear space
x = np.linspace(0, 30, 6) # 0 ~ 30 사이를 6 등분
print('x 값 : ', end='')
print(x)
# x 값 : [ 0.  6. 12. 18. 24. 30.]

y = 2 * x + 1
print('y 값 : ', end='')
print(y)
# y 값 : [ 1. 13. 25. 37. 49. 61.]
```

### pandas
- df = pandas.read_csv(링크): data frame 생성
- df.head(num): 상위 num 줄만 출력
- df_sub = df.drop(columns=[시리즈 이름1, 시리즈 이름2(key)]): 시리즈 제거 data frame 생성
  - series(시리즈): coiumn(열)
  - record(레코드): row(행)
