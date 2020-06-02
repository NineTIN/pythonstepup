# 빈 셋 생성
ex_set = set()
print(ex_set) # 결과 : set()
'''
ex_set = {} 이 아닌 이유는 이미 딕셔너리에서 사용 중이기 때문이다.
'''

# 셋 생성하기
numbers_ex = {0,2,4,6,8}
print(numbers_ex) # 결과 : {0, 2, 4, 6, 8}

str_ex = set('letters')
print(str_ex) # 딕셔너리와 동일하게 Key이기 때문에 중복값 없음 결과 : {'e', 'l', 't', 'r', 's'}

list_ex = set(['list1',
'list2',
'list3',
'list4'])
print(list_ex) # 결과 : {'list1', 'list3', 'list4', 'list2'}

tuple_ex = set(('tuple1',
'tuple2',
'tuple3',
'tuple4'))
print(tuple_ex) # 결과 : {'tuple4', 'tuple2', 'tuple3', 'tuple1'}

dict_ex = set({'dict1':'abc',
'dict2':'efg',
'dict3':'hij',
'dict4':'klm'})
print(dict_ex) # Key만 가져온다. 결과 : {'dict4', 'dict1', 'dict2', 'dict3'}

# 셋 콤비네이션과 연산자
a = {1,2}
b = {2,3}

# 인터섹션(intersection) 
# 교집합 : 양쪽 셋에 모두 들어 있는 항목, 기호는 「&」 를 이용한다.
print(a & b) # 결과 : {2}

# 유니온(union)
# 합집합 : 각 셋의 항목 모두, 기호는 「|」 를 이용한다.
print(a | b) # 결과 : {1,2,3}

# 디퍼런스(difference) 
# 차집합 : 첫번째 셋에는 있지만 두번째 셋에는 없는 항목, 기호는 「-」 를 이용한다.
print(a - b) # 결과 : {1}

# 익스클루시브(exclusive) 
# 대칭 교집합 : 한쪽 셋에는 들어 있지만 양쪽 모두에 들어 있지않은 항목, 기호는 「^」 를 이용한다.
print(a ^ b) # 결과 : {1,3}

a={1,2}
b={1,2,3}

# 서브셋(subset)
# 부분집합 : 해당 집합이 다른 집합에 부분집합 인가, 기호는 「<=」 를 이용한다.
print(a<=b) # 결과 : True 

