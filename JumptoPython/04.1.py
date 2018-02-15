#함수
def sum(a, b):
    return a+b
a = 3
b = 4
c = sum(a, b)
print(c)


def sum(a, b):
    result = a + b
    return result
a = sum(3, 4)
print(a)


def say():
    return "Hi"
a = say()
print(a)


def sum(a, b):
    print("%d + %d = %d"%(a,b,a+b))
sum(4,5)

a = sum(3,4)
print(a)


def say():
    print("Hi")
say()


# 입력값이 몇 개가 될지 모를 때는 ??
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
result = sum_many(1,2,3,10)
print(result)
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
result = sum_mul("sum",1,2,3,4,5)
print(result)
result = sum_mul("mul",1,2,3,4,5)
print(result)


# 결과값은 언제나 하나이다
def sum_and_mul(a, b):
    return a+b, a*b
result = sum_and_mul(3, 4)
print(result)
# 여러개로 리턴하면 튜플로 리턴한다!
sum, mul = sum_and_mul(6, 7)
print(sum)
print(mul)


##### return의 또다른 쓰임새
def say_nick(nick):
    if nick == '바보':
        return
    print("내 별명은 %s입니다"%nick)
say_nick('야호')
say_nick('바보')
say_nick('뿌룽')

def say_myself(name, old, man=True):
    print("내 이름은 %s입니다"%name)
    print("나이는 %s살입니다"%old)
    if man:
        print("그리고 남자입니다.")
    else:
        print("그리고 여자입니다.")
say_myself("파이썬", 19)
say_myself("파이썬", 25, True)
say_myself("파이순", 20, False)
# 입력인수에 초기값을 주려면 맨 뒤에다가 줘야한다.


# 함수 밖 변수 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

b = 1
def vartest():
    global b
    b = b + 1
vartest()
print(b)