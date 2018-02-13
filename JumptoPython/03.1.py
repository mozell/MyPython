#if
money = 1
if money :
    print("택시 가즈아~")
else :
    print("걸어 가즈아~")

x = 3
y = 2
print(x>y)
print(x<y)
print(x==y)
print(x!=y)

money = 2000
if money >= 3000:
    print("택시 가즈아~")
else:
    print("걸어 가즈아~")


money = 2000
card = 1
if money >= 3000 or card :
    print("택시 가즈아~")
else:
    print("걸어 가즈아~")

a = [1, 2, 3]
print(1 in a)
print(1 not in a)

a = ('a', 'b', 'c')
print('a' in a)
print('j' not in a)

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print("택시 가즈아~")
else:
    print("걸어 가즈아~")

pocket = ['paper', 'cellphone', 'money']
if 'money' not in pocket:
    pass
else:
    print("카드를 꺼내자")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시 가즈아~")
else:
    if card:
        print("택시 가즈아~")
    else:
        print("걸어 가즈아~")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시 가즈아~")
elif card:
    print("택시 가즈아~")
else:
    print("걸어 가즈아~")