# 빈 딕셔너리 생성
empty_dict = {}
print(empty_dict) # 결과 : {}

# 딕셔너리 생성 (key:value)
ex_dict = {"hyundai":"avante",
"kia":"k3",
"toyota":"86"}
print(ex_dict) # 결과 : {'hyundai': 'avante', 'kia': 'k3', 'toyota': '86'}

# 딕셔너리로 변환하기
list_type = [['kia','k5'],['hyundai','sonata'],['honda','civic']]
list_result = dict(list_type) # 리스트형을 딕셔너리로 
print(list_result) # 결과 : {'kia': 'k5', 'hyundai': 'sonata', 'honda': 'civic'}

tuple_type = [('toyota','86'),('hyundai','avante'),('kia','k3')]
tuple_result = dict(tuple_type) # 튜플형을 딕셔너리로
print(tuple_result)  # 결과 : {'toyota': '86', 'hyundai': 'avante', 'kia': 'k3'}

str_array_type = ['ab','cd','ef']
# str_array_type = ['ab','cde','fghi'] # 2문자 이상일 경우 ValueError가 발생한다.
str_array_result = dict(str_array_type) # 문자열을 딕셔너리로
print(str_array_result)  # 결과 : {'a': 'b', 'c': 'd', 'e': 'f'}

# 딕셔너리 항목추가/변경
example_dict = {"Michael Jackson":"Sriller",
"Queen":"Bohemian Rhapsody",
"Beatles":"Let It Be"}

example_dict['Michael Jackson'] = 'Thriller' # Sriller를 Thriller로 바르게 수정
print(example_dict) # 결과 : {'Michael Jackson': 'Thriller', 'Queen': 'Bohemian Rhapsody', 'Beatles': 'Let It Be'}

example_dict['Kwang Seok Kim'] = 'About Thirty' # Key가 존재하지 않을 경우에는 추가 한다. (김광석 - '서른즈음에'를 추가)
print(example_dict) # 결과 : {'Michael Jackson': 'Thriller', 'Queen': 'Bohemian Rhapsody', 'Beatles': 'Let It Be', 'Kwang Seok Kim': 'About Thirty'}

# 딕셔너리 결합하기
a_dict = {"Pikotaro":"PPAP",
"Beatles":"Let It Be"}

b_dict = {'Kwang Seok Kim': 'About Thirty',
"Queen":"Bohemian Rhapsody"}

a_dict.update(b_dict)
print(a_dict) # 결과 : {'Pikotaro': 'PPAP', 'Beatles': 'Let It Be', 'Kwang Seok Kim': 'About Thirty', 'Queen': 'Bohemian Rhapsody'}

# 딕셔너리 항목 삭제하기
del a_dict['Pikotaro']
print(a_dict) # 결과 : {'Beatles': 'Let It Be', 'Kwang Seok Kim': 'About Thirty', 'Queen': 'Bohemian Rhapsody'}

# 딕셔너리 모든 항목 삭제하기
a_dict.clear() # a_dict = {} 빈 딕셔너리를 생성해서 같은 효과
print(a_dict) # 결과 : {}

# 딕셔너리 Key의 존재 유무확인
example_dict = {'Chapman':'Graham',
'Cleese':'John',
'Jones':'Terry',
'Palin':'Michael'}

print('Chapman' in example_dict) # 결과 : True
print('John' in example_dict) # 결과 : False

# 딕셔너리 값(Value) 얻기
example_dict = {"Michael Jackson":"Thriller",
"Queen":"Bohemian Rhapsody",
"Beatles":"Let It Be"}

# 방법.1
print(example_dict['Beatles']) # 결과 : Let It Be
'''
의외로 이 방법은 비추천 하는 방법
존재하지 않는 키를 사용시 에러가 발생하기 때문

# 예제
print(example_dict['Kwang Seok Kim']) 
Traceback (most recent call last):
  File "7.py", line 70, in <module>
    print(example_dict['Kwang Seok Kim'])
KeyError: 'Kwang Seok Kim' 
'''

# 방법.2
print(example_dict.get('Beatles')) # 결과 : Let It Be
print(example_dict.get('Kwang Seok Kim')) # 존재 하지 않는 Key에도 대응한다. 결과 : None 
print(example_dict.get('Kwang Seok Kim','Not Found Key!')) # None대신에 옵션을 줄 수 있다. 결과 : Not Found Key!

# 딕셔너리 모든 Key 얻기
print(example_dict.keys()) # 결과 : dict_keys(['Michael Jackson', 'Queen', 'Beatles'])

# 딕셔너리 모든 Value 얻기
print(example_dict.values()) # 결과 : dict_values(['Thriller', 'Bohemian Rhapsody', 'Let It Be'])

# 딕셔너리 모든 Key-Value 얻기
print(example_dict.items()) # 결과 : dict_items([('Michael Jackson', 'Thriller'), ('Queen', 'Bohemian Rhapsody'), ('Beatles', 'Let It Be')])

# 딕셔너리 복사
a_dict = {'abc':'efg',
'hij':'klm',
'nop':'qrs'}

b_dict = a_dict # a_dict를 b_dict에 대입

a_dict['abc'] = '123' # a_dict 수정
print(a_dict) # 결과 : {'abc': '123', 'hij': 'klm', 'nop': 'qrs'}
print(b_dict) # b_dict가 영향을 받는다. 결과 : {'abc': '123', 'hij': 'klm', 'nop': 'qrs'}

a_dict = {'abc':'efg',
'hij':'klm',
'nop':'qrs'}

b_dict = a_dict.copy() # a_dict를 b_dict에 복사(Copy)

a_dict['abc'] = '123' # a_dict 수정
print(a_dict) # 결과 : {'abc': '123', 'hij': 'klm', 'nop': 'qrs'}
print(b_dict) # b_dict가 영향을 받지 않는다. 결과 : {'abc': 'efg', 'hij': 'klm', 'nop': 'qrs'}
