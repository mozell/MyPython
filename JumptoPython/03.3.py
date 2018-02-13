#for
test_List = ['one', 'two', 'three']
for i in test_List:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
    print(first+last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number+1
    if mark >= 60:
        print("%d번 학생은 합격입니다"%number)
    else:
        print("%d번 학생은 불합격입니다"%number)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number+1
    if mark < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다."%number)

a = range(10)
print(a)        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

a = range(1,11)
print(a)        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

sum = 0
for i in range(1, 11):
    sum += i
print(sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

for i in range(2,10):
    for j in range(1,10):
        print("%3d"%(i*j), end='')
    print()

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

# 뭐야 이거 무서워... 복잡해
result = [num*3 for num in a]
print(result)

result = [num*3 for num in a if num%2==0]
print(result)

result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result)