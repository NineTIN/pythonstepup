# 문자열 핸들링
# 문자열 복제
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.' * 2
print(start + middle + end) 
# 결과 : Na Na Na Na 
#       Hey Hey Hey 
#       Goodbye. Goodbye.

# 문자열 문자 추출
example = 'abcdefghijk'
print(example[0]) # 결과 : a
print(example[1]) # 결과 : b
print(example[-1]) # 결과 : k
print(example[-2]) # 결과 : j
#print(example[100]) # IndexError가 발생한다. 길이를 초과했으므로

# 문자열 자르기 [start:end:step]
example = 'abcdefghijk'
print(example[:]) # 결과 : abcdefghijk
print(example[0:]) # 결과 : abcdefghijk
print(example[2:]) # 결과 : cdefghijk
print(example[:-1]) # 결과 : abcdefghij
print(example[2:4]) # 결과 : cd
print(example[2:8:2]) # 결과 : ceg

# 문자열의 길이 알아내기
ex = 'abcd'
print(len(ex)) # 결과 : 4
ex = ''
print(len(ex)) # 결과 : 0

# 문자열 나누기
cheat = 'show,me,the,money'
print(cheat.split(',')) # 결과 : ['show', 'me', 'the', 'money'] 배열로 만들어진다.

# 문자열 결합
cheat_list = ['show', 'me', 'the', 'money']
cheatStr = ','.join(cheat_list)
print(cheatStr) # 결과 : show,me,the,money 배열이 아니게 된다.

# 문자 찾기
cheat = '''show me the money
Operation CWAL
Power Overwhelming
Black Sheep Wall
Modify the phase variance.
'''
print(cheat.startswith('show')) # show로 시작하는가? 결과 : True 
print(cheat.endswith('show')) # show로 끝나는가? 결과 : False
print(cheat.find('Black'))  # Black은 몇번째에 있는가? 결과 : 52
print(cheat.find('black'))  # black은 몇번째에 있는가? 결과 : -1 (※일치하지 않음)
print(cheat.count('the'))  # the가 몇번 출현하는가? 결과 : 2
print(cheat.isalnum())  # 글자와 숫자뿐인가? 결과 : False (※마지막에 마침표(.)가 있기 때문)

# 문자의 대소문자와 배치
ex = 'A duck goes into A bar...'
print(ex.upper()) # 결과 : A DUCK GOES INTO A BAR...
print(ex.lower()) # 결과 : a duck goes into a bar...
print(ex.swapcase()) # 결과 : a DUCK GOES INTO a BAR...
print(ex.strip('.')) # 양끝에 . 시퀀스 삭제 결과 : a duck goes into a bar
print(ex.capitalize()) # 첫번째 단어를 대문자로 결과 : A duck goes into a bar...
print(ex.title()) # 모든 단어의 첫글자를 대문자로 결과 : A Duck Goes Into A Bar...

# 문자열 대체
print(ex.replace('duck','girl')) # 결과 : A girl goes into A bar...
