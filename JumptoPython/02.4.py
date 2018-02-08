# 튜플 자료형
t1 = ()
t2 = (1,)           # 1개의 값만 가지면 반드시 ,추가
t3 = (1, 2, 3)
t4 = 1, 2, 3        # ()생략해도 무방하다
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# 삭제도 안되고 수정도 안된다.
#del t5[0]
#t5[0] = 'c'

# 인덱싱과 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

print(t1[1:])

# 튜플 더하기와 곱하기
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
