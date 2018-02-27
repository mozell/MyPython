#01
def q1(s):
    _compare = ""
    cnt = 0
    result = ""

    for compareWord in s :
        if compareWord != _compare:
            _compare = compareWord
            if cnt:
                result += str(cnt)
            result += compareWord
            cnt = 1
        else:
            cnt += 1
    if cnt:
        result += str(cnt)
    return result
print(q1("aaabbcccccca"))

#02
def q2(s):
    result = []
    for num in s :
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
print(q2("0123456789"))
print(q2("01234"))
print(q2("01234567890"))
print(q2("6789012345"))
print(q2("012322456789"))

#03
mosdict = {
    '.-' : 'A',
    '-...' : 'B',
    '-.-.' : 'C',
    '-..' : 'D',
    '.' : 'E',
    '..-.' : 'F',
    '--.' : 'G',
    '....' : 'H',
    '..' : 'I',
    '.---' : 'J',
    '-.-' : 'K',
    '.-..' : 'L',
    '--' : 'M',
    '-.' : 'N',
    '---' : 'O',
    '.--.' : 'P',
    '--.-' : 'Q',
    '.-.' : 'R',
    '...' : 'S',
    '-' : 'T',
    '..-' : 'U',
    '...-' : 'V',
    '.--' : 'W',
    '..' : 'X',
    '-.--' : 'Y',
    '--..' : 'Z'
}
def q3(src):
    result = []
    for word in src.split(" "):
        for char in word.split(" "):
            result.append(mosdict[char])
        result.append(" ")
    return "".join(result)
print(q3(".... . ... .-.. . . .--. ... . .- .-. .-.. -.--"))