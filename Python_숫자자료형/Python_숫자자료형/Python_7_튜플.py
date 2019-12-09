# 튜플(Tuple) : 리스트(list)와 비슷한 자료형
# 인덱싱, 슬라이싱 등의 문법도 그대로 사용이 가능

tuple = (1, 2, 3)
for i in tuple:
    print(i)
print(tuple)

print()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
tuple[0][1] = 7            # 튜플에 포함된 리스트의 값을 바꿈 ( list1 의 원소값을 바꿈 )
# tuple[0] = [7, 8, 9]      오류 - 원소의 값을 다시 바꾸는것 불가능
print(tuple)
print(tuple[0][1])

print()

tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple[0:5])
print(tuple[0:5]*3)
