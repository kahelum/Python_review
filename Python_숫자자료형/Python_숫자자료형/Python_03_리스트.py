# print ('한줄 주석')
"""
print ("여러줄 주석")
"""

a = [
    [90, 95, 87, 77, 68, 25, 33, 64, 40, 56],
    [57, 66, 59, 23, 72, 81, 62, 80, 91, 73]
    ]

sum = 0
english = a[0]
for i in english:
    sum = sum + i
print ("영어 평균 점수 :", sum / len(english))

sum = 0
math = a[1]
for i in math:
    sum = sum + i
print ("수학 평균 점수 :", sum / len(math), "\n")


b = [90, 80, 95, 90, 85]

print (b.count(90))     # count(원소)     리스트 내 특정 원소가 몇 개 포함되어 있는지 반환
print (b.index(85))     # index(원소)     리스트 내 특정 원소의 인덱스 반환

b.append(87)            # append(원소)    리스트 뒤쪽에 새로운 원소 삽입
print (b)

b.sort()                # sort()        오름차순 정렬
print(b)

c = [31, 24, 27]
b.extend(c)             # extend(리스트)    리스트 뒤쪽에 다른 리스트 삽입
print(b)

c.insert(2, 98)         # insert(인덱스, 원소)   특정한 위치에 원소 삽입
print(c)

b.remove(80)            # remove(원소)    리스트 내 특정 원소 삭제
print(b)

c.pop(0)                # pop(원소)   리스트 내 특정 인덱스의 원소 삭제
print(c)

c.reverse()             # reverse()     리스트 뒤집기
print(c)