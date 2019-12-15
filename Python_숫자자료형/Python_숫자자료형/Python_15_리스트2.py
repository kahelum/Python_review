# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
# reverse() : 리스트의 원소를 뒤집기
# sum(리스트 자료형) : 리스트의 모든 원소의 합
# range() : 특정 범위를 지정
# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환
# all() / any() : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
# sort() : 리스트의 원소를 정렬
# count() : 특정한 원소의 개수를 추출
# del : 리스트의 특정 원소를 제거
# insert() : 리스트에 특정 원소를 삽입
# append() : 리스트의 가장 마지막 원소로서 원소를 삽입

list2 = ['이태일', '박한울', '이선우', '김현민']
print(list2.index('박한울'))

print('-----------------------------')

list1 = [1, 2, 3, 4, 5]
print(list1[::-1])
"""
list1 = list1[::-1]
print(list1)
"""
list1.reverse()
print(list1)

print('-----------------------------')

#list1 = [1, 2, 3, 4, 5, "123"]         # 문자열 자료형이 포함될 경우 오류메시지 출력
print(sum(list1))

print('-----------------------------')

my_range = range(5, 10)
my_list = list(my_range)
print(my_list)

print('-----------------------------')

list3 = [True, False, True]
print(all(list3))
print(any(list3))

print('-----------------------------')

list4 = ['이태일', '박한울', '김현민', '강종구', '이선우']
result = list(enumerate(list4))
print(result)

for i, k in enumerate(list4):
    print("인덱스 : ", i, " / 원소 : ", k)

list4.sort()
print(list4)

print('-----------------------------')

list5 = ['이태일', '박한울', '김현민', '이태일', '이선우']
print(list5.count("이태일"))

print('-----------------------------')

list6 = ['123', '456', '789']
del list6[1]
print(list6)
list6 = ['123', '456', '789']
del list6[1:3]
print(list6)

list6 = ['123', '456', '789']
list6.insert(2, '-1')
print(list6)

list6.append('999')
print(list6)
