#문자열 자료형
s1 = "Hello World"
s2 = 'Python is fun'
s3 = """Life is too short, You need python"""
s4 = '''Life is too short, You need python'''
print(s1)
print(s2)
print(s3)
print(s4)

# 문자열에 큰 따옴표, 작은 따옴표 포함하기
food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
print(food)
print(say)

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline1 = "Life is too short\nYou need python"
multiline2 = """Life is too short
You need python"""
multiline3 = '''Life is too short
You need python'''
print(multiline1)
print(multiline2)
print(multiline3)

#문자열 연산
head = "Python"
tail = " is fun!"
print(head+tail)

p = "python"
print(p*3)

print("+"*10)
print("곱하기 응용")
print("+"*10)

#############################
# 문자열 인덱싱, 문자열 슬라이싱
#############################
a = "Life is too short, You need Python"
print(a[3])
print(a[0], a[-0]) # 0은 같은것이기 때문에 앞에서 처음 문자
print(a[12])
print(a[-1]) # 뒤에서 첫번째 문자
print(a[-2])
print(a[-5])

# 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])

print(a[0:2])
print(a[5:7])
print(a[12:17])

print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date, weather)

year = a[:4]
day = a[4:8]
print(year, day, weather)

##############
# 문자열 포매팅
##############
str1 = "I eat %d apples."%3
print(str1)
str2 = "I eat %s apples."%"five"
print(str2)
num = 2
str3 = "I eat %d apples."%num
print(str3)

num = 10
day = "three"
str4 = "I ate %d apples. so I was sick for %s days."%(num, day)
print(str4)

#문자열에 % 사용하고 싶으면 %%로 사용한다.
str5 = "Loading is %d%%"%num
print(str5)

# 포맷 코드와 숫자 함께 사용하기
print("%10s"%"hi")           # >> ________hi
print("%-10sjane"%"hi")     # >> hi________jane

print("%0.4f"%3.141592)      
print("%10.4f"%3.141592)    # ____3.1415

#문자열 관련 함수들
a="Python is best choice"
print(a.count('c'))     # 문자 'c' 의 갯수

print(a.find('b'))      # 'b'가 나온 처음 위치
print(a.find('z'))      # 없으면 -1 반환

print(a.index('t'))     # 't'가 나온 처음 위치
#print(a.index('z'))     없으면 오류 발생

aaa=","
print(",".join(a))      #문자열 'a' 사이에 ","를 삽입(변수로 줘도 됨)
print(aaa.join(a))

print(a.upper())
print(a.lower())

b = "   :Python:   "
print(b.lstrip())
print(b.rstrip())
print(b.strip())

print(a.replace("Python","Study"))

print(a.split())        # 공백을 기준으로 나눔
print(b.split(":"))     # 기호 ":"를 기준으로 나눔