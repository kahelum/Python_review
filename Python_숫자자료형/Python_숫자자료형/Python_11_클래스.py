# 클래스(Class) : 반복되는 불필요한 소스코드를 최소화 하면서 현실 세계의 사물을 컴퓨터 프로그래밍 상에서
#                 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
# 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수
# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수. 메소드라고 부름
# 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재
# 자식 클래스 : 부모 클래스를 상속 받은 클래스


class Car:
    def __init__(self, name, color):    # 클래스의 생성자
        self.name = name                # 클래스의 멤버
        self.color = color              # 클래스의 멤버
    
    def __del__(self):                  # 클래스의 소멸자    
        print("인스턴스를 소멸시킵니다.")

    def show_info(self):
        print("이름 : ", self.name, " / 색상 : ", self.color)

    def set_name(self, name):           # Setter 메소드
        self.name = name

car1 = Car("람보르기니", "빨간색")
car1.show_info()
car1.set_name("포르쉐")        # Setter 메소드를 이용해서 name 변경
print(car1.name, "을(를) 구매했습니다.")

car2 = Car("부가티", "검정색")
car2.show_info()
print(car2.name, "을(를) 구매했습니다.")

car3 = Car("벤츠", "흰색")
car3.show_info()
print(car3.name, "을(를) 구매했습니다.")
del car3                        # car3의 인스턴스 삭제
#car3.show_info()               # 오류발생 car3의 인스턴스가 없음

print("\n-----------------------------\n")

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(self.name,"이(가) 공격을 수행합니다. [ 전투력 :", self.power,"]")

unit = Unit("후리주리", 9999)
unit.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def show_info(self):
        print("몬스터 이름 :", self.name, "/ 몬스터 종류 : ", self.type)
monster = Monster("슬라임", 10, "초급")
monster.show_info()
monster.attack()
