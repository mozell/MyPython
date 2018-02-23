import pickle
f = open("test.txt", 'wb')
data = {
    1:'python',
    2:'you need'
}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()


import os
print(os.environ)       # 현재 시스템 환경 변수 값들
print(os.environ["PATH"])


import shutil       # 파일을 복사해주는 모듈
# shutil.copy('a.txt', 'b.txt')

import glob         # 파일이름을 알아야 할 때
print(glob.glob('d:/__Python/Jumptopython/*.txt'))

import tempfile     # 파일을 임시로 만듬


import time
print(time.time())

print(time.localtime(time.time()))
curtime = time.localtime(time.time())
for i in curtime:
    print(i,end=' ')
print()

print(time.asctime(time.localtime(time.time()))) # 보기쉬운 형태로

print(time.ctime())     # 현재 시간만을 보기 쉬운 형태로


for i in range(2):
    print(i)
    time.sleep(1)  # 일정한 시간간격을 줄 수 있다.





import calendar
print(calendar.calendar(2018))
print(calendar.prmonth(2018, 12))
print(calendar.weekday(2018, 2, 23))        # 해당 요일 출력
print(calendar.monthrange(2018, 2))         # 1일이 무슨요일인지? , 며칠까지 있는지?



import random
print(random.random())  # 0.0 ~ 1.0 사이의 실수중 난수값 리턴
print(random.randint(1,10))     # 해당 값 사이의 정수중 난수 리턴
print(random.randint(1,45))


def random_pop(data):
    number = random.randint(0, len(data) - 1 )
    return data.pop(number)


data = [1, 2, 3, 4, 5]
while data:
    print(random_pop(data))