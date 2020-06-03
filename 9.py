# if , elif,  else
str_color = 'red'
if str_color == 'red':
    print('is red')
elif str_color != 'red':
    print('is not red')
else:
    print('none')
# 결과 : is red
'''
비교 연산자
== 같다.
!= 다르다.
< 보다 작다
<= 보다 작거나 같다.
> 보다 크다.
>= 보다 크거나 같다.
in ... 멤버십
'''

# while
count = 1
while count <= 5:
    print(count)
    count += 1
# 결과 :
# 1
# 2
# 3
# 4
# 5

# while & break & continue
count = 1
while count <= 5:
    if count == 2:
        count += 1
        continue
    if count == 5:
        break
    print(count)
    count += 1
# 결과 : 
# 1
# 3
# 4

# break 확인하기
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: # break가 호출되지 않을 경우 실행, if문의 else가 아니라 while문의 else다.
    print('No even number found')

# for
for i in range(1, 10):
    print(i)
# 결과 : 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
'''
파이썬의 for는 기본적으로 이터레이터(iterator)가 쓰인다.
'''
output_lists = ['hello','wolrd','python','fun']
for output in output_lists:
    print(output)
# 결과 : 
# hello
# wolrd
# python
# fun

# 여러 시퀀스 이터레이터(iterator)하기: zip()
days = ['Mon','Tue','Wed']
fruits = ['banana','orange','peach']
drinks = ['coffe','tea','beer']
desserts = ['tiramisu','ice creame','pie','pudding']

for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,'= eat:',fruit,',drink:',drink,',enjoy:',dessert)
# 결과 :
# Mon = eat: banana ,drink: coffe ,enjoy: tiramisu
# Tue = eat: orange ,drink: tea ,enjoy: ice creame
# Wed = eat: peach ,drink: beer ,enjoy: pie
'''
zip()의 경우 가장 짧은 시퀀스 이터레이터가 완료되면 작업이 끝난다.
desserts의 pudding이 출력되지 않는 것은 각각의 배열의 길이가 맞지 않기 때문이다.
'''

# zip()응용 - 리스트
english = 'Monday','Tuesday','Wedesday'
korean = '월요일','화요일','수요일'
genList = list(zip(english,korean))
print(genList)
# 결과 : [('Monday', '월요일'), ('Tuesday', '화요일'), ('Wedesday', '수요일')]

# zip()응용 - 딕셔너리
english = 'Monday','Tuesday','Wedesday'
korean = '월요일','화요일','수요일'
genDict = dict(zip(english,korean))
print(genDict)
# 결과 : {'Monday': '월요일', 'Tuesday': '화요일', 'Wedesday': '수요일'}

# 숫자 시퀀스 생성: range()
'''
0~3 까지
'''
for x in range(0,3):
    print(x)
# 결과 :
# 0
# 1
# 2

'''
3~0 까지
'''
for x in range(3,-1,-1):
    print(x)
# 결과 : 
# 2
# 1
# 0
'''
0~2씩 증가 (짝수)
'''
for x in range(0,11,2):
    print(x)
# 결과 : 
# 0
# 2
# 4
# 6
# 8
# 10
