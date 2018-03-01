import re

# | 는 or 의 뜻이다
p = re.compile('Crow|Servo')
m = p.match("CrowHello")
print(m)

# ^는 문자열의 맨 처음과 일치함을 의미한다
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $는 문자열의 맨 끝과 매치함을 의미
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A ^와 동일한 의미이지만, re.MULTILINE 을 사용할 경우에 다르게 해석된다
# re.MULTILINE 옵션을 사용할 경우 ^ 은 라인별 문자열의 처음과 매치되지만,
# \A 은 라인과 상관없이 전체 문자열의 처음하고만 매치된다.

# \Z 는 re.MULTILINE 옵션을 사용할 경우 $와 달리 전체문자열의 끝과 매치된다

# \b 는 단어 구분자( whitespace ) 에 의해 구분된다
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))                  #객체 반환
print(p.search('the declassified algorithm'))     # none
print(p.search('one subclass is'))                  # none

# \B는 \b 와 반대의 경우, whitespace 로 구분된 단어가 아닌경우에 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))                  # none
print(p.search('the declassified algorithm'))     # 객체 반환
print(p.search('one subclass is'))                  # none







# 그룹핑

# 그룹을 만들어주는 문자는 바로 () 이다
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search("park 010-1234-1234")
print(m)

# 이름만 뽑아내려면?
p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search("park 010-1234-1234")
print(m.group(1))

# group(0) 매치된 전체 문자열
# group(1) 첫 번째 그룹에 해당되는 문자열
# group(2) 두 번째 그룹에 해당되는 문자열
# group(n) N 번째 그룹에 해당되는 문자열

p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group(2))

# 중첩되었다면 바깥쪽부터 안쪽으로 인덱스가 증가한다
p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group(1))
print(m.group(2))
print(m.group(3))

# \1 은 1번 그룹의 동일한 단어가 연속으로 매치되는걸 의미..?
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())





# 그룹핑 네이밍
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())




# 전방 탐색..?
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

# 긍정형 전방탐색 (?=...)
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# 부정형 전방탐색 (?!...)




# 문자열 바꾸기
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
print(p.sub('colour', 'blue socks and red shoes', count= 1))

