# 네임스페이스와 스코어
animal = 'cat'
def print_global():
    print('inside print_global:',animal)

'''
# 함수 안에서 글로벌 변수를 바꾸려고 하면 에러가 난다.
def change_and_print_global():
    print('inside change_and_print_global',animal)
    animal = 'bat'
    print('after the change:',animal) # 에러 발생

change_and_print_global()
# UnboundLocalError: local variable 'animal' referenced before assignment
'''

def change_local():
    animal = 'bat' # 지역 변수
    print('inside change_local:', animal,id(animal))

change_local() # 함수콜
# 결과 : inside change_local: bat 4448413712

'''
전역변수에 접근 할때는 반드시 global을 명시 해줘야 한다.
'''
def chage_and_print_global():
    global animal
    animal = 'dog'
    print('inside change_and_print_global:',animal)

print(animal)
chage_and_print_global() # 함수콜

# 글로벌 또는 로컬 네임스페이스 가져오기
name = 'smith'
def local_variable():
    name = 'chris'

print('locals:',locals())
# 결과 :
# locals: {'__name__': '__main__',
# '__doc__': None,
# '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x100f8d198>,
# '__spec__': None,
# '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>,
# '__file__': '12.py',
# '__cached__': None,
# 'animal': 'dog',
# 'print_global': <function print_global at 0x100e60400>,
# 'change_local': <function change_local at 0x100f95268>,
# 'chage_and_print_global': <function chage_and_print_global at 0x100f952f0>,
#  'name': 'smith',
# 'local_variable': <function local_variable at 0x100f95378>}

print('globals:',globals())
# 결과 :
# globals: {'__name__': '__main__',
# '__doc__': None,
# '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x100f8d198>,
# '__spec__': None,
# '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>,
# '__file__': '12.py',
# '__cached__': None,
# 'animal': 'dog',
# 'print_global': <function print_global at 0x100e60400>,
# 'change_local': <function change_local at 0x100f95268>,
# 'chage_and_print_global': <function chage_and_print_global at 0x100f952f0>,
#  'name': 'smith',
# 'local_variable': <function local_variable at 0x100f95378>}

# 더블 언더스코어 (__) 의 사용
'''
파이썬 내부에 빌트 인(built-in) 되어 있는 함수를 위해 예약되어 있다.
'''
def builtin():
    '''
    sample function
    :return: None
    '''
    print('function is named:',builtin.__name__)
    print('docstring is:', builtin.__doc__)

builtin() # 함수콜
# 결과 :
# function is named: builtin
# docstring is:
#     sample function
#     :return: None
