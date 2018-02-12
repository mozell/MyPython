#Q1
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#02
pin = "881120-1068234"
print(pin[7])

#03
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#04
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#05
a = (1, 2, 3)
a = a + (4,)
print(a)

#06
a = {
    'A' : 90,
    'B' : 80,
    'C' : 70
}
result = a.pop('B')
print(a)
print(result)

#07
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#08
a = b = [1, 2, 3]
a[1] = 4
print(b)
# a와 b는 동일한 객체를 가르키는 이름만 다른 레퍼런스이기 때문이다