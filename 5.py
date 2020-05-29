# 자료구조
# 리스트 만들기
ex = ['ab','cd','ef'] # ','로 구분
print(ex) # 결과 : ['ab', 'cd', 'ef']

ex = list() # 빈 리스트를 넣을 수도 있다.
print(ex) # 결과 : []

ex = list('cat') # 문자열을 리스트로 변환 할 수도 있다.
print(ex) # 결과 : ['c', 'a', 't']

target = '1919/12/25'
ex = target.split('/') # split를 이용 하는것도 방법
print(ex) # 결과 : ['1919', '12', '25']

# 리스트의 리스트 (다중 배열)
compact_cars = ['avante','pride']
discontinue_cars = ['Pony','Excel','Tuscani']
suv_cars = ['kona','Nexo','santa fe']
all_cars = [compact_cars,discontinue_cars,'Genesis',suv_cars]
print(all_cars) # 결과 : [['avante', 'pride'], ['Pony', 'Excel', 'Tuscani'], 'Genesis', ['kona', 'Nexo', 'santa fe']]
print(all_cars[0]) # 결과 : ['avante', 'pride']
print(all_cars[0][1]) # 결과 : pride ※ 0번째 배열 요소의 1번째 요소를 가져온다.

# 리스트 요소 바꾸기
compact_cars[1] = 'K5'
print(compact_cars) # 결과 : ['avante', 'K5']

# 슬라이스로 요소 추출하기
print(discontinue_cars[0:2]) # 결과 : ['Pony', 'Excel'] ※ 슬라이스도 리스트다.

# 리스트에 요소 더하기
compact_cars.append('i30')
print(compact_cars) # 결과 : ['avante', 'K5', 'i30'] ※ 새요소는 맨 마지막에 추가가된다.

# 지정된 위치에 요소 더하기
suv_cars.insert(1,'Palisade')
print(suv_cars) # 결과 : ['kona', 'Palisade', 'Nexo', 'santa fe']

# 리스트 병합
car_makers = ['porsche','mercedes benz','bmw']
others = ['vw','audi']
car_makers.extend(others)
# car_makers += others # ※ ← 이것도 같은 결과가 나온다.
print(car_makers) # 결과 : ['porsche', 'mercedes benz', 'bmw', 'vw', 'audi']

# 리스트 요소 삭제하기 (오프셋)
del car_makers[3] # 몇번째 인지만 알고 있을 경우
print(car_makers) # 결과 : ['porsche', 'mercedes benz', 'bmw', 'audi']

# 리스트 요소 삭제하기 (값지정)
suv_cars.remove('Palisade') # 요소의 값만 알고 있을 경우
print(suv_cars) # 결과 : ['kona', 'Nexo', 'santa fe']

# 요소 얻은 후 삭제하기 (Stack) = LIFO
jpn_car_makers = ['toyota','honda','subaru','mazda','nissan']
print(jpn_car_makers.pop()) # 결과 : nissan
print(jpn_car_makers) # 결과 : ['toyota', 'honda', 'subaru', 'mazda'] ※ 맨 마지막 요소가 사라졌다.

# 요소 얻은 후 삭제하기 (Que) = FIFO
jpn_car_makers = ['toyota','honda','subaru','mazda','nissan']
print(jpn_car_makers.pop(0)) # 결과 : toyota
print(jpn_car_makers) # 결과 : ['honda', 'subaru', 'mazda', 'nissan'] ※ 첫 요소가 사라졌다.

# 값으로 요소 오프셋 찾기
print(jpn_car_makers.index('mazda')) # 결과 : 2

# 요소의 존재 유무확인
print('honda' in jpn_car_makers) # 결과 : True
print('hyundai' in jpn_car_makers) # 결과 : False

# 요소의 값 세기
ex = ['cola','cola','cola','beer']
print(ex.count('cola')) # 결과 : 3
print(ex.count('orange')) # 결과 : 0

# 리스트의 정렬 (sort)
target_list = ['drive','beta','apple','contact','2','1','3']
target_list.sort() # 정렬 실행
print(target_list) # 결과 : ['1', '2', '3', 'apple', 'beta', 'contact', 'drive']

# 리스트의 정렬 (sorted)
target_list = ['drive','beta','apple','contact','2','1','3']
sorted_list = sorted(target_list)
print(sorted_list) # 결과 : ['1', '2', '3', 'apple', 'beta', 'contact', 'drive'] ※ target_list의 정렬된 결과가 복사된다.
print(target_list) # 결과 : ['drive', 'beta', 'apple', 'contact', '2', '1', '3'] ※ 따라서 target_list 자체는 영향이 없다.
'''
Python 소팅룰 
숫자인 경우 '오름차순' 정렬
문자열인 경우 '알파벳순'
'''

# 리스트의 복사
a = ['1','2','3']
b = a
a[0] = '4'
print(a) # 결과 : ['4', '2', '3']
print(b) # 결과 : ['4', '2', '3'] ※ b는 a를 참조하고 있기 때문에 a가 변경되면 영향을 받는다.

a = ['1','2','3']
b = a.copy()
a[0] = '4'
print(a) # 결과 : ['4', '2', '3']
print(b) # 결과 : ['1', '2', '3'] ※ b는 a를 복사 했기 때문에 a가 변경되어도 영향을 받지 않는다.
