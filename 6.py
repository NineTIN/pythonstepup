# 튜플
'''
특징 
・리스트와 다르게 「추가」, 「삭제」, 「수정」을 할 수 없다.
・튜플은 더 적은 공간을 사용한다.
・튜플을 딕셔너리 키로 사용 할 수 있다.
・네임드 튜플은 객체의 대안이 될 수 있다.
・함수의 인자들은 튜플로 전달된다.
'''
# 빈 튜플 만들기
ex = ()
print(ex) # 결과 : ()

# 요소 하나의 튜플 만들기
ex = 'cat',
print(ex) # 결과 : ('cat',)

# 요소 두개 이상 튜플 만들기
ex = 'cat','dog','rabbit' # 두개 이상일뺀 마지막에 , 를 붙이지 않는다.
print(ex) # 결과 : ('cat', 'dog', 'rabbit') 

# 튜플을 여러 변수에 할당하기 (튜플 언패킹)
ex = 'cat','dog','rabbit'
a,b,c = ex
print(a) # 결과 : cat
print(b) # 결과 : dog
print(c) # 결과 : rabbit

# 다른 객체를 튜플로 만들기
ex_list = ['cat','dog','rabbit']
print(ex_list) # 결과 : ['cat', 'dog', 'rabbit']
print(tuple(ex_list)) # 결과 : ('cat', 'dog', 'rabbit')