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

'''
잘못된 케이스
wine = chicken 처럼 잘못 된 인자를 전달 할 수도 있다.
'''
print(menu('chicken','cake','chardonnay'))
# 결과 : {'wine': 'chicken', 'entree': 'cake', 'dessert': 'chardonnay'}

'''
키워드를 지정한 경우 
인자의 전달 순서와 상관없이 지정한 키워드로 값이 전달 된다.
'''
print(menu(dessert='cake', entree='chicken', wine='chardonnay'))
# 결과 : {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}
