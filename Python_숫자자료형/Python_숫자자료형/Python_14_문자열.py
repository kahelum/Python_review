# 문자열 자료형 뒤집기 : 슬라이싱 활용
# len() : 문자열의 길이를 출력
# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(), lower() : 문자열을 대문자 혹은 소문자로 변환해주는 함수
# strip() : 좌우로 특정한 문자열을 제거하는 함수
# eval() : 문자열 수식 계산해주는 함수

str = "Hello World"
str1 = "12345"
str2 = "abc12345"
print(str[::-1])
print(len(str))
print(str.isalpha())            # 중간에 공백이 있어서 False
print(str1.isdigit())           # 공백이 있으면 False ( 오직 숫자 )
print(str2.isalnum())           # 공백, 특수문자등 다른 것이 있으면 False

print('-----------------------------')

list = ["Hello", "World", "홍길동"]
print('='.join(list))

print('-----------------------------')

str3 = "sorted"

list1 = sorted(str3)            # 오름차순으로 각 문자를 정렬
print(list1)
print(''.join(list1))
list1 = sorted(str3, reverse = True)    # 내림차순
print(''.join(list1))

print('-----------------------------')

str4 = "I want to get a job."
list2 = str4.split(' ')
print(list2)
print(str4.find('t'))            # 문자열이 포함되어 있지 않은 경우 -1 반환
print(str4.find('t',6))          # 같은 문자열이 포함되어 있을 경우 인덱스 6 이후의 문자열을 찾을때

print('-----------------------------')

print(str.upper())
print(str.lower())

print('-----------------------------')

str5 = "  Hello World  "
print(str5.strip())             # 매개변수에 어떠한 내용도 넣지 않으면 기본적으로 공백 제거
print(str5.lstrip())            # 왼쪽 특정한 문자열 제거
print(str5.rstrip())            # 오른쪽 특정한 문자열 제거
str6 = "ttHello Worldtt"
print(str6.strip('t'))

print('-----------------------------')

exp = "(203+705)*3-(30/6)"
print(eval(exp))

