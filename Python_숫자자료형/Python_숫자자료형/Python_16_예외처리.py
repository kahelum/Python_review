# 예외처리(Exception Handling)

try:
    #print(3 / 0)
    print(3 / 1)
except:
    print("0으로는 나눌 수 없습니다.")
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.")

print()

try:
    print(3 / 0)
except Exception as e:              # 오류메시지를 직접 출력
    print(e)

