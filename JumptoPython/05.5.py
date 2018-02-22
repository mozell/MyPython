#내장함수
print(abs(3))       # 절대값
print(abs(-3))
print(abs(-1.2))

print(all([1,2,3])) # 모두 참인지?
print(all([1,2,3,0]))

print(any([1,2,3,0])) # 하나라도 참인지?
print(any([0,""]))

print(chr(97))      # 아스키 코드에 해당하는 문자를 출력
print(chr(48))

print(ord('a'))     # 아스키 코드값 리턴
print(ord('0'))

print(dir([1,2,3]))     # 객체가 자체적으로 가지고있는 변수나 함수를 보여줌
print(dir({'1':'a'}))

print(divmod(7,3))      # 몫, 나머지
print(divmod(1.3,0.2))

for i, name in enumerate(['body', 'foo', 'bar']):   # 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 객체를 리턴
    print(i, name)

print(eval('1+2'))      # 실행 가능한 무자열을 입력으로 받아 결과값을 리턴
print(eval("'hi'+'a'"))
print(eval('divmod(3,4)'))

def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return  result
print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x:x>0, [1, -3, 2, 0, -5, 6])))


print(hex(234))     # 16진수로 변환하여 리턴
print(hex(3))


a = 3
print(id(3))
print(id(a))
b = a
print(id(b))   # 3개 모두 같은 객체를 가르킨다.
print(id(4))


# 사용자 입력을 받는 함수
# a = input()
# print(a)
# b = input("Enter: ")
# print(b)

print(int('3'))     # 정수로 리턴
print(int(3.4))
print(int('11', 2))  # b 진수로 표현된 a 를 10진수로 변환하여 리턴
print(int('1A', 16))


class Person: pass
a = Person()
# 인스턴스가 해당하는 클래스의 인스턴스인지 판별
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))


# lambda , 함수를 생성할 때 사용하는 예약어, def와 동일한 역할
# lambda 인수1, 인수2, ... : 인수를 이용한 표현식
sum = lambda a, b : a+b
print(sum(3,5))

myList = [lambda a,b: a+b, lambda a,b: a*b]
print(myList)
print(myList[0])
print(myList[0](3,4))
print(myList[1](3,4))


print(len("python"))        # 길이 출력
print(len([1,2,3]))
print(len((1,'A')))


print(list("python"))       # 리스트형태로 변환
print(list((1,2,3)))

print(tuple("python"))       # 튜플 형태로 변환
print(tuple((1,2,3)))

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)
#----> 쉽게 map 으로
def two_times1(x):return x*2
print(list(map(two_times1, [1,2,3,4])))
print(list(map(lambda a:a*2, [1,2,3,4])))


def plus_one(x):
    return x+1
print(list(map(plus_one, [1,2,3,4,5])))


print(max([1,2,3]))
print(max('python'))

print(min([1,2,3]))
print(min('python'))


print(oct(34))      # 8진수로 변환
print(oct(12345))

print(pow(2,4))     # 제곱한 결과
print(pow(3,3))


print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

print(sorted([3, 1, 2]))        # 결과를 정렬만 할 뿐 리턴하지 않는다
print(sorted(['c', 'a', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

print(str(3)) # 문자열로 변환
print(str("hi"))

print(type("abc"))
print(type([]))
print(type(open("asdasdasdasd", 'w')))

print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))