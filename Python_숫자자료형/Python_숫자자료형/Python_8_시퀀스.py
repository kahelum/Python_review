# 시퀀스(Sequence) : 문자열, 리스트, 튜플 등의 인덱스(Index)를 가지는 자료형
# len(시퀀스 자료형) : 시퀀스 자료형의 길이를 출력하는 함수
# 반복문 등에서 사용될 수 있음

string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

print(string)
print(list)
print(tuple,'\n')

print(string[0])
print(list[0])
print(tuple[0],'\n')

print(string[0: 5])
print(list[0: 5])
print(tuple[0: 5],'\n')

for i in string:
    print(i)

print ('----------------------')

for j in list:
    print(j)

print ('----------------------')

string1 = ", Python"

print(string + string1)
print(len(string + string1))

print ('----------------------')

list1 = [1, 2, 3, 4, 5]
print (4 in list1)
print (6 in list1)

if 3 in list1:
    print("3을 포함하고 있습니다.")

