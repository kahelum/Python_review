# 모듈(Module) : 미리 작성된 함수 코드를 모아 놓은 파이썬 파일

import math
print(math.pow(2, 5))       # 2의 5제곱
print(math.sqrt(64))        # 제곱근
print(math.gcd(72, 24))     # 최대 공약수

print()

import Python_10_lib
print(Python_10_lib.add(3, 7))
print(Python_10_lib.subtraction(15, 7))

print()

from Python_10_lib import add       # 모듈파일이 클 경우 특정한 모듈에서 특정한 기능만 이용하고 싶을 때
print(add(8, 7))

print()

import Python_10_lib as t           # 모듈파일의 이름이 길 경우 별칭 부여 가능
print(t.add(10, 15))