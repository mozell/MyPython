#파일 읽고 쓰기
f = open("새 파일.txt", 'w')    # 파일객체 = open(파일 이름, 파일 열기 모드)
f.close()                        # 열려있는 파일 객체를 닫아주는 역할

# 파일 열기 모드
# r | 읽기모드 = 파일을 읽기만 할 때 사용
# w | 쓰기모드 = 파일에 내용을 쓸 때 사용
# a | 추가모드 = 파일의 마지막에 새로운 내용을 추가할 때 사용

f = open("새 파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

# 파일 읽는 여러가지 방법
# 첫번째 줄을 읽는다
f = open("새 파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# 방법 변형 (모든라인을 읽도록)
f = open("새 파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()

while 1:
    data = input()
    if not data : break
    print(data)

# 모든 라인을 읽어서 각각의 줄을 원소로 갖는 리스트를 리턴하는 readlines
f = open("새 파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 전체 문자열 리턴
f = open("새 파일.txt", 'r')
data = f.read()
print(data)
f.close()


## 파일에 새로운 내용 추가하기
f = open("새 파일.txt", 'a')
for i in range(11,20):
    data = '%d번째 줄입니다~\n'%i
    f.write(data)
f.close()



## with 문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")   # with 문이 끝나면 자동으로 close된다.

############################
#
#   sys 모듈로 입력 인수 주기 ??      page 167
#
#