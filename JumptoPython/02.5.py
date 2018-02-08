# 딕셔너리 자료형
dic = {
    'name' : 'han',
    'phone' : '01011112222',
    'birth' : '0924'
}
print(dic)

# key 로 정수값, value로 문자열 사용 가능하고, value에 리스트를 넣을 수도 있다.
a = {
    1 : 'hi',
    'a' : ['a', 'b', 'c']
}
print(a)

# 딕셔너리 쌍 추가하기
a = {
    1 : 'a'
}
a[2] = 'b' # {2:'b'} 쌍 추가
print(a)
a['name'] = 'han'
print(a)
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 Key를 사용하여 Value 얻기.
grade = {
    'han' : 90,
    'lee' : 80
}
print(grade["han"])
print(grade["lee"])
# --> 딕셔너리는 인덱싱이나 슬라이싱 기법을 사용할 수 없고 오로지 key 로 값을 뽑을수 있다.

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 키를 중복으로 저장하면 나중에 저장된 값으로 저장된다.
a = {
    1:'a',
    1:'b'
}
print(a)

# # 리스트를 키로 쓸 수 없다.
# a = {
#     [1,2] : 'hi'
# }
# print(a)

####################
# 딕셔너리 관련 함수들
####################

# Key 리스트 만들기 (keys)
print(dic.keys())  # dict_keys 라는 객체를 반환한다
for key in dic.keys():
    print(key,":",dic[key])
# dict_keys 객체를 리스트로 저장하려면
print(list(dic.keys()))

# Value 리스트 만들기 (values)
print(dic.values()) # dict_values 라는 객체를 반환한다.

# key, value 쌍 얻기 (items)
print(dic.items())

# key, value 쌍 모두 지우기 (clear)
grade.clear()
print(grade)

# key 로 value 얻기 (get)
print(dic.get('name'))      # dic.get('name') == dic['name']
print(dic.get('birth'))
print(dic.get('nonekey'))   # dic.get('nonekey') 은 None 반환, dic['nonekey'] 는 오류 발생
print(dic.get('nonekey', 'DEFAULT')) # 키값이 없으면 정해둔 Default 값을 리턴

# 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
print('name' in dic)
print('email' in dic)