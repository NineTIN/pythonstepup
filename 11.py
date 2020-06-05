# 객체
'''
파이썬에서 객체는 숫자,문자열,튜플,리스트,딕셔너리,함수를 포함한다.
'''
def answer():
    print(30)

def run_something(func):
    func()

run_something(answer) # 함수콜
# 결과 : 30

# 내부 함수
'''
코드 중복이나 함수 내에서 또 다른 복잡한 작업을 처리해야 할 경우 사용한다. 
'''
def something(saying):
    def inner(quote):
        return "this is inner say: %s" % quote
    return inner(saying)

print(something('Hello!')) # 함수콜
# 결과 : this is inner say: Hello!

# 클로져
def something2(saying):
    def inner2():
        return "this is inner2 say: %s" % saying
    return inner2

a = something2('Hello!1') # 함수콜
b = something2('Hello!2') # 함수콜
print(a)
# 결과 : <function something2.<locals>.inner2 at 0x10c5f4950>
print(b)
# 결과 : <function something2.<locals>.inner2 at 0x10c5f49d8>
'''
inner2는 함수 something2가 전달받은 saying 변수를 알고 있다.
코드에서 return inner2에는 inner2함수의 특별한 복사본은 반환한다.
즉, 그 함수의 변수값을 알고 있는 함수가 클로져다.
'''

# 익명함수: lambda()
'''
람다 사용전에 간단한 함수를 구현
'''
stairs = ['thud','meow','thud','hiss']

def edit_story(words,func):
    for word in words:
        print(func(word))

def eliven(word):
    return word.capitalize() + '!' # 뒤에 느낌표 붙이기

edit_story(stairs,eliven)
# 결과 : 
# Thud!
# Meow!
# Thud!
# Hiss!
#----------------------
'''
함수 eliven을 람다로 구현 해보자
'''
edit_story(stairs, lambda word: word.capitalize() + '!')
# 결과 : 
# Thud!
# Meow!
# Thud!
# Hiss! 
#----------------------

# 데코레이터
'''
소스 코드의 변경 없이 사용하고 있는 함수를 수정 하고 싶을때 사용
하나의 함수를 취해서 또 다른 함수를 반환 하는 함수이다.
필요한 것은
*args (위치인자 모으기)
**keyword_args (키워드 인자 모으기)
내부 함수
함수 인자
'''
def document_it(func):
    def new_func(* args,**kwargs):
        print('Running Function:',func.__name__)
        print('Positional arguments:',args)
        print('keyword arguments:',kwargs)
        result = func(*args, **kwargs)
        return result
    return new_func

def add_ints(a,b):
    return a + b

coller_add_ints = document_it(add_ints) # 데커레이터를 수동으로 할당
print(coller_add_ints(3,5))
# 결과 : 
# Running Function: add_ints
# Positional arguments: (3, 5)
# keyword arguments: {}
# 8

# 데코레이터 어노테이션
'''
수동으로 할당하는 방법 말고 어노테이션을 써서 할당 할 수도 있다.
'''
@document_it
def add_ints2(a,b):
    return a + b

print(add_ints2(3,5))
# 결과 : 
# Running Function: add_ints2
# Positional arguments: (3, 5)
# keyword arguments: {}
# 8