# 파일입출력
# open() : 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w를 사용.
# read() : 파일 객체로부터 모든 내용을 읽는 함수
# readline() : 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines() : 전체 내용을 한 번에 리스트에 담는 함수

f = open("Python_18_input.txt", "r")
f.seek(9)
data = f.read()
print(data)
f.close()

print("---------------------------------")

o = open("Python_18_input.txt", "r")
count = 0
while count < 3:
    data = o.readline()
    count = count + 1
    print("%d번째 줄 : %s" %(count, data), end = "")
o.close()

print()
print("---------------------------------")

p = open("Python_18_input.txt", "r")
list = p.readlines()
print(list)
print("---------------------------------")
for i, data in enumerate(list):
    print("%d번째 줄 : %s" %(i + 1, data), end = '')
p.close()

print()
print("---------------------------------")

with open("Python_18_input.txt", "r") as e:
    list = e.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄 : %s" %(i + 1, data), end = '')

print()
print("---------------------------------")

def process(filename):
    with open(filename, "r") as n:
        # 키 : 알파벳, 값 : 빈도수
        dict = {}
        data = n.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dict = process("Python_18_input.txt")
print(dict)

print("---------------------------------")

# 빈도수를 기준으로 내림차순 정렬 수행
dict = sorted(dict.items(), key = lambda a:a[1], reverse = True)        # dict.items() -> a / 값 -> a[1] *즉 값을 기준으로 정렬하겠다라는 뜻
print(dict)

for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현 : [%c]" %(count, data))
