# f = open("나없는파일.txt", 'r')
# print(4/0)
# a = [1,2,3]; print(a[4])
############################ 위는 다양한 오류의 예

# try ... except
try:
    print(4/0)
except ZeroDivisionError as e:
    print(e)




# try ... else
try:
    f = open("foo.txt", 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
    print(data)



# try ... finally
f = open('foo.txt', 'w')
try:
    #무언가를 수행한다
    pass
finally:
    f.write('Life is short, you need Python')
    f.close()



# 오류 회피하기
try:
    f = open("나없는파일!@#", 'r')
except FileNotFoundError:
    pass


# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
# eagle.fly()         # 오류 발생

class Pigeon(Bird):
    def fly(self):
        print("very fat")


pigeon = Pigeon()
pigeon.fly()