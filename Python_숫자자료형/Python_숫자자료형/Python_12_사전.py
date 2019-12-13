# 사전(Dictionary) : 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형


dict = {}
dict['안녕'] = 'Hello'
dict['영어'] = 'English'
dict['연습'] = 'Practice'
print(dict)

if '연습' in dict:
    print("[연습] 키가 존재합니다.")

print('--------------------------')

for i, k in enumerate(dict):
    print("[ 인덱스 :", i, "]", "한글 :", k, "/ 영어 :", dict[k])

print('--------------------------')

dict['안녕'] = 'Hi'       # Hello -> Hi로 바뀜
keys = dict.keys()        # 키(Key)만 출력
values = dict.values()
print(dict)
print()
print("키 : ", keys)      # 키(Key)만 출력
key_list = list(keys)
print("키 : ", key_list)
value_list = list(values)
print("값 : ", value_list)  # 값(Value)만 출력

print('--------------------------')

del dict['영어']          # 삭제
print(dict)

print('--------------------------')

dict.clear()              # 전부 삭제
print(dict)
print("사전 자료형의 길이 : ", len(dict))

print('--------------------------')

scores = {}
scores['김현민'] = 92
scores['이창희'] = 95
scores['이종길'] = 97
print(sorted(scores))       # 키로 정렬하기 ( 사전순 A - B - C / 가 - 나 - 다 )
print(sorted(scores, reverse = True))       # 키로 내림차순 정렬
print(sorted(scores.values()))
print(sorted(scores.values(), reverse = True))
