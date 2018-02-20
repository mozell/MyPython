class HousePark:
    lastname  = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다."%(self.fullname, where))

pey = HousePark("응용")
pey.travel("부산")
pes = HousePark("심화")
pes.travel("태국")


###########################
# 상속!!
# class 상속받을 클래스명 (상속할 클래스명)
class HouseKim(HousePark):
    lastname = "김"
juliet = HouseKim("줄리엣")
juliet.travel("독도")


###########################
# 메서드 오버라이딩
class HouseHan(HousePark):
    lastname = "한"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네."%(self.fullname, where, day))
me = HouseHan("승구")
me.travel("미국", 15)



###########################
# 연산자 오버로딩
class HousePark:
    lastname  = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다."%(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네"%(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네"%(self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 서로 싸웠네"%(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))
pey = HousePark("응용")
juliet = HouseHan("줄리엣")
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet