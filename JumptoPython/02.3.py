#리스트 자료형
a1 = []
a2 = [1,2,3]
a3 = ['Life', 'is', 'too', 'short']
a4 = [1,2, 'Life','is']
a5 = [1,2,['Life','is']]

b = [1, 2, 3]
print(b[0]+b[2])

c = [1, 2, 3, ['a', 'b', 'c']]
print(c[-1])
print(c[3])
print(c[-1][0])

d1 = [1, 2, 3, 4, 5]
print(d1[0:2])
d2 = '12345'
print(d2[0:2])

#리스트 연산자
a1 = [1,2,3]
a2 = [4,5,6]
print(a1 + a2)
print(a1*3)

    #하나의 값 수정
a1[2] = 4
print(a1)
    #연속된 범위의 값 수정
a1[1:2] = ['a', 'b', 'c']
print(a1)
    #삭제
a1[1:3] = []
print(a1)
    #del 함수를 이용한 삭제
del a1[1]
print(a1)

# 리스트 관련 함수들
# append, sort, reverse, index, insert, remove, pop, count, extend
    # append
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5,6])
print(a)

    # sort
a = [1, 4, 3, 2]
a.sort()        # sort() 함수 실행하면 바로 반환되어 저장된다
print(a)

a = ['d', 'a', 'c', 'b']
a.sort()
print(a)

    # reverse
a = ['a', 'b', 'c']
a.reverse()
print(a)

    # index
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# 없는요소를 찾으면 에러 발생

    # insert
a = [1, 2, 3]
a.insert(0,4) # a[0] 위치에 4를 삽입한다.
print(a)
a.insert(2,5)
print(a)

    # remove
a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 처음으로 나온 '3' 을 삭제한다.
print(a)
a.remove(3)
print(a)

    # pop
a = [1, 2, 3]
print(a.pop())  # 마지막 요소 반환 후 삭제
print(a.pop(1)) # '1'번째 요소 반환 후 삭제

    # count
a = [1, 2, 3, 1]
anum = a.count(1)  # 리스트의 요소 중에 '1'이 몇개있는지 조사하여 개수를 돌려줌
print(anum)

    # extend
a = [1, 2, 3]
a.extend([4,5])
print(a)
b = [6, 7]
a.extend(b)
print(a)