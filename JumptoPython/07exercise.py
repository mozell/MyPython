#01
import re
p = re.compile('a[.]{3,}b')
print(p.match("acccb"))
print(p.match("a....b"))    # 매치
print(p.match("aaab"))
print(p.match("a.cccb"))


#02
import re
p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end())
print(m.start())
print(m.end())


#03
import re
s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####",s)

print(result)


#04
import re

pat = re.compile(".*[@].*[.](?:com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))