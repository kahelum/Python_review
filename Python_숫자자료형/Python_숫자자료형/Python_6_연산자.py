# 연산자 = operator

# 증감 연산자 : 기존에 사용하던 증가/감소 기능을 짧게 이용
# 축약형 => 증감 연산자
# 관계 연산자 : 두 개의 값을 비교하여 관계
# A == B : A와 B가 같은지 판별 => True, False
# A != B : A와 B가 다른지 판별 => True, False
# 논리 연산자 : 여러 개의 수식을 논리적으로 연산
# A and B : A와 B가 모두 참인지 판별
# A or B : A혹은 B가 참인지 판별
# not A : A가 거짓인지 판별

# 증감 연산자
a = 10
a += 10     # a *= 10       a /= 10
print(a)

print()

# 관계 연산자
b = 3
c = 7
print(b == c)   # False
print(b != c)   # True
print(b > c,"\n")    # False

B = "ABC"
C = "DEF"
print(B == C)
print(B < C,"\n")    # 문자열끼리 비교를 할 경우 사전순으로 비교하는 특징을 가짐.

# 논리 연산자
d = True
e = False
print(d and e)  # False
print(d or e)   # True
print(not d)    # False

if 3 > 5 or 7 < 10:
    print("\n출력")
