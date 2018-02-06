#정수형
a1, a2, a3 = 123, -178, 0
print("정수형 >> ",a1, a2, a3)

#실수형
b1, b2 = 1.2, -3.5
print("실수형 >> ",b1, b2)

#실수형 지수 표현 방식
b3, b4 = 4.24e10, 4.24E-10
print("실수(지수 표현) >> ",b3 ,b4)

#8진수 16진수
c1 = 0o177
c2, c3 = 0x8ff, 0xABC
print("8진수 >> ",c1)
print("16진수 >> ",c2, c3)

#복소수
d1, d2 = 1+2j, 3-4J
print("복소수 >> ",d1, d2)
print("복소수 실수 >> ",d1.real, d2.real)
print("복소수 허수 >> ",d1.imag, d2.imag)
print("켤레복소수 >> ",d1.conjugate(), d2.conjugate())
print("절대값 >> ",abs(d1) ,abs(d2))

###########################################################

a = 3
b = 4

print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a%b=",a/b)
print("a^b=",a**b)
print("a%b 나머지 =",a%b)
print("a%b 몫=",a//b)