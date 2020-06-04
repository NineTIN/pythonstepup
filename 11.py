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