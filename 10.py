# 기본적인 함수
def do_nothing():
    pass # 아무것도 하지 않는다.

do_nothing() # 함수콜
# 결과 : 
# --------------------------------
def do_print():
    print('do print call!')

do_print() # 함수콜
# 결과 : do print call!
# --------------------------------
def do_isBool():
    return True

if do_isBool(): # 함수콜
    print('do_isBool call!')
else:
    print('nothing?')
# 결과 : do_isBool call!
# --------------------------------

# 함수에 인자 전달하기
def echo(anything):
    return anything + ' is cool!!'

print(echo('Symphony')) # 함수콜
# 결과 : Symphony is cool!!
# --------------------------------

# 함수의 키워드 인자
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
'''
올바른 케이스
'''
print(menu('chardonnay','chicken','cake'))
# 결과 : {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}
# --------------------------------

'''
잘못된 케이스
wine = chicken 처럼 잘못 된 인자를 전달 할 수도 있다.
'''
print(menu('chicken','cake','chardonnay'))
# 결과 : {'wine': 'chicken', 'entree': 'cake', 'dessert': 'chardonnay'}
# --------------------------------

'''
키워드를 지정한 경우 
인자의 전달 순서와 상관없이 지정한 키워드로 값이 전달 된다.
'''
print(menu(dessert='cake', entree='chicken', wine='chardonnay'))
# 결과 : {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}
# --------------------------------

# 함수에 기본 매개변수 값 지정하기
def menu2(wine,entree,dessert='pudding'):
    return {'wine':wine,'entree':entree,'dessert':dessert}
'''
디저트를 지정하지 않아도 「pudding」이 기본값으로 반환된다.
'''
print(menu2('cel24','stake')) # 함수콜
# 결과 : {'wine': 'cel24', 'entree': 'stake', 'dessert': 'pudding'}
print(menu2('cel24','stake','orange')) # 함수콜
# 결과 : {'wine': 'cel24', 'entree': 'stake', 'dessert': 'orange'}
# --------------------------------

# 함수 매개변수의 라이프 사이클
def appendTest(arg, result=[]):
    result.append(arg)
    print(result)
'''
함수를 호출 할때 마다 result가 사라지지 않고 이전 값을 가지고 있다.
'''
appendTest('a') # 결과 : ['a']
appendTest('b') # 결과 : ['a', 'b']
appendTest('c') # 결과 : ['a', 'b', 'c']
# --------------------------------

# 위치 인자 모으기 : *
def print_arg(*args):
    print('argument tuple:',args)
'''
파이썬에는 C/C++와 같은 포인터(*)가 없다.
매개변수를 모두 모아서 튜플(tuple)로 만들어주는 역활을 한다.
'''
print_arg() # 함수콜
# 결과 : argument tuple: ()
print_arg(1,2,3,'a','b','c') # 함수콜
# 결과 : argument tuple: (1, 2, 3, 'a', 'b', 'c')
print_arg('show','me','the','money',123,444,333) # 함수콜
# 결과 : argument tuple: ('show', 'me', 'the', 'money', 123, 444, 333)

# 키워드 인자 모으기 : **
def print_kwargs(**keyword_args):
    print('keyword arguments:',keyword_args)
'''
** 를 쓸 경우 튜플(tuple)이 아니라 딕셔너리(dict)로 만들어 준다. 
마찬가지로 무엇을 넣든, 갯수가 몇개든 상관없다.
'''
print_kwargs() # 함수콜
print_kwargs(name='ig',age=30,gender='male') # 함수콜
