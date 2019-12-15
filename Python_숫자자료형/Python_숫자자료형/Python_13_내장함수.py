# 내장함수(Built in functions)
# input() : 사용자로부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 변환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 최소값을 반환
# bin(), hex() : 10진수 -> 2진수 변환, 10진수 -> 16진수 변환
# round() : 반올림을 수행
# type() : 자료형의 종류

user_input = input('정수를 입력하세요 : ')
print("제곱 : ", int(user_input) ** 2)

print("-----------------------------------")

a = "12345"
print(int(a))
b = 12.5
print(int(b))
c = 10
print(float(c))

print("-----------------------------------")

list = [5, 6, 7, 8, 2, 4, 9, 11]
print(max(list))
print(min(list))

print("-----------------------------------")

print(bin(128))             # 문자열로 반환   # 10진수 -> 2진수 변환
print(hex(230))             # 10진수 -> 16진수 변환
print(int('0xe6', 16))      # 16진수 -> 10진수 변환

print("-----------------------------------")

print(round(123.678))
print(round(123.678, 2))        # 두번째 매개변수를 통해 소수점 몇번째에서 반올림을 수행할지 정할수있음
print(round(123.678, -1))

print("-----------------------------------")

int = 1
str = "문자열"
list = [1, 2, 3]
dict = {'apple' : '사과'}

print(type(int))
print(type(str))
print(type(list))
print(type(dict))



