#클래스
result = 0
def adder(num):
    global result
    result += num
    return result
print(adder(3))
print(adder(4))

result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1
def adder2(num):
    global result2
    result2 += num
    return result2
print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))

#---> 계산기가 여러번 필요할 때는 어떻게 할 것인가??
#---> 해결 : 클래스

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Simple:
    pass
a = Simple()
print(a)        # Simple 클래스의 인스턴스를 만들어냄


class Service:
    secret = "영구는 배꼽이 두 개다!"
    def setname(self,name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        print("[%s]님 %d + %d = %d 입니다."%(self.name, a, b, result))
pey = Service()
print(pey.secret)
pey.setname("홍길동")
pey.sum(4,5)
# --> setname을 실행하지 않으면 오류 발생!!

class Service:
    secret = "영구는 배꼽이 두 개다!"
    def __init__(self,name):            # 인스턴스를 만들 때 항상 실행된다.
        self.name = name
    def sum(self,a,b):
        result = a+b
        print("[%s]님 %d + %d = %d 입니다."%(self.name, a, b, result))
pey = Service("홍길똥")
pey.sum(1,1)