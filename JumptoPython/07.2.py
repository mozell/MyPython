# [] 안의 문자중에 한 개라도 매치가 된다면 매치!
# [] 안의 두 문자 사이에 하이픈(-)을 넣으면 범위를 의미한다
# ^를 사용하면 not의 의미이다  ex) [^0-9] => 숫자가 아닌 문자만 매치

# \d == [0-9]
# \D == [^0-9]
# \s == [ \t\n\r\f\v]       ==> 화이트 스페이스 문자들,.,
# \S == [^ \t\n\r\f\v]
# \w == [a-zA-Z0-9]
# \W == [^a-zA-Z0-9]





# . 은 두 문자 사이에 하나이상의 문자가 있어야 하며, \n(줄바꿈)을 제외한 모든 문자와 매치됨.



### 반복에 관한 정규식
# * 은 바로 앞에 있는 문자가 0번이상 반복되면 매치
# ca*t ==> ct, cat, caaat 다 매치

# + 는 바로 앞에 있는 문자가 1번이상 반복되면 매치
# ca+t ==> ct 만족X, cat, caaat 매치

# {m,n}, ?
# {m} => ca{2}t => 2번 반복되면 매치
# {m,n} => ca{2,5}t => 2~5번 반복되면 매치
# ? == {0,1} => ca?t => 0~1번 반복되면 매치


import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m)            # 매치된 객체가 리턴

m = p.match("3python")
print(m)            # 매치가 안됫으니 none 리턴


############################
#### 정규표현식의 흐름도  ####
############################
# p = re.compile('정규표현식')
# m = p.match('조사할 문자열')
# if m :
#     print('찾았다 매치!', m.group())
# else :
#     print('매치 없다~')
############################
# 매치의 결과만 있을때 다음 작업을 수행
############################

# 문자열 전체를 검색 (search)
m = p.search("python")
print(m)
m = p.search("3python")
print(m)

# findall 각각 정규식에 매치되는 리스트로 리턴
result = p.findall("life is too short")
print(result)

# finditer
result = p.finditer("life is too short")
print(result)
for r in result: print(r)
# findall 과 동일하지만 그 결과로 반복 가느한 객체를 리턴한다. (match 객체를 리턴)



########################
# match 객체의 메소드

import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
n = p.search('3python')
print(n.group())
print(n.start())
print(n.end())
print(n.span())


###################
#  컴파일 옵션

import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)        # 매치되지 않음

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)        # re.DOTALL 은 \n 에 상관없이 검색하고자 할 때 많이 사용


# re.I 는 대소문자 구분 없이 수행하고자 할 때의 옵션
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))



p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))  # ['python one']

p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))  # ['python one', 'python two', 'python three']


charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
&[#]                    # 주석주석 뿅뿅
(
    0[0-7]+             # 주석주석 뿅뿅
  | [0-9]+              # 주석주석 뿅뿅
  | x[0-9a-fA-F]+      # 주석주석 뿅뿅
)
;                       # 주석주석 뿅뿅
""",re.VERBOSE)



####### 백슬래시 문제

p = re.compile('\\section')     # \section
p = re.compile('\\\\section')   # \\section
p = re.compile(r'\\section')    # \\section

