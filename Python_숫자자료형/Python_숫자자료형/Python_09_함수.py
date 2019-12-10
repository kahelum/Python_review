# 함수(Function) : 특정한 입력을 받아서 처리를 한 이후에, 특정한 출력을 하는 모듈
# 함수를 이용하면 특정한 소스코드의 반복을 줄일 수 있다는 특징
# 가변 인자 : 함수의 매개변수가 가변적일 수 있을 때 사용
# 전역 변수 : 소스코드 전체 어디에서든지 사용 가능한 변수
# 지역 변수 : 특정한 함수(블록) 안에서만 사용할 수 있는 변수
# 파이썬의 함수는 반환 값이 여러 개일 수 있음

def add(a, b):
    sum = a + b
    return sum
print (add(3, 5))

a = add(5, 7)
print(a)

def add1(a, b):
    print(a + b)
add1(5, 10)

def function(*data):        # 가변 인자
    print(data)
function(1, 2, 3)

def add2(a):
    a = a + 5               # 지역 변수

a = 2                       # 전역 변수
add2(a)
print(a)            # def add2(a)에서 선언한 a + 5 의 값이 아닌 a = 2로 선언한 값이 출력됨

def add3():         # global을 이용해서 전역 변수 선언시 매개변수는 삭제
    global a        # 전역 변수 사용
    a = a + 5

a = 5
add3()
print(a)

def function():     # 반환 값이 여러 개
    a = 9
    b = [1, 2, 3]
    c = "Hello"
    return a, b, c

a, b, c = function()
print(a)
print(b)
print(c)
