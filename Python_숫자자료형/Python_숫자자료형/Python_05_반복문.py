# 반복문 = iterative

# 숫자 범위 표현 : range(시작, 끝)
# continue : continue를 만났을 때 더 이상 명령을 실행하지 않고 다음 반복을 진행한다.
# break : break를 만났면 반복문을 벗어난다.

'''
sum = 0
for i in range(1, 10):
    print(i)
    sum = sum + i
print("합계 : ", sum,"\n")
'''

'''
count = 0
for j in "Hello World":
    print(j)
'''

"""
count = 0
for j in "Hello World":
    if j == 'o':
        count = count + 1
print("o의 개수는 :", count, "개 입니다")
"""

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    sum = sum + i
print("합계 : ", sum)
'''

"""
list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1:      # 홀수일 때
        continue
    print(i)
"""

""" 잘못된 예
    list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1:      # 홀수일 때
        continue
print(i)                # print부분의 들여쓰기를 잘못 씀.
"""

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1:      # 홀수일 때
        continue
    sum = sum + i
print("합계 : ", sum)
'''

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1:      # 홀수일 때
        break
    sum = sum + i
print("합계 : ", sum)     # 리스트의 첫번째 수가 1이기 때문에 바로 탈출
'''

i = 0
sum = 0
while i < 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + i
print("합계 : ", sum)
