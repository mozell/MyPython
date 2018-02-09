# 변수
a = 1
b = "Python"
c = [1,2,3]

# 변수명 = 저장할 값
# 파이썬에서의 변수는 '객체를 가리키는 것'을 뜻한다
a = 3
b = 3
print(a is b)
# 여기서 레퍼런스는 a, b 이고 레퍼런스 카운트는 2가 된다.

# 레퍼런스 카운트를 알려주는 함수
import sys
print(sys.getrefcount(3))

a = b = 'python'
print(a, b)

a = 30
b = 10
a, b = b, a
print("a>>",a,"b>>", b)

# 메모리에 생성된 변수 없애기
del(a)
del(b)

# 리스트에서 혼동하기 쉬운 '복사'
a = [1,2,3]
b = a
a[0] = 0
print(a) #[0, 2, 3]
print(b) #[0, 2, 3]
# --> a와 b는 동일한 리스트를 가르키는 이름만 다른 레퍼런스이다.

a = [1,2,3]
b = a[:]
a[0] = 0
print(a) #[0, 2, 3]
print(b) #[1, 2, 3]
# --> 리스트 전체 복사를 의미하는 [:] 이용

from copy import copy
b = copy(a)   # b = a[:]와 동일한 명령
print(b is a) # b와 a는 서로 다른 객체임을 알 수 있다.