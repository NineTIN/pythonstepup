# 형변환
# 형변환 정수
print(int(True)) # 결과 : 1
print(int(False)) # 결과 : 0
print(int(98.9)) # 결과 : 98
print(int(1.0e4)) # 결과 : 10000
#print(int('98.9')) # 결과 : ValueError가 발생한다. int()는 소수 or 숫자 이외에는 처리하지 않는다.

# 형변환 소수
print(float(True)) # 결과 : 1
print(float(False)) # 결과 : 0
print(float(10)) # 결과 : 10.0
print(float('10')) # 결과 : 10.0 ※int()와는 다르게 문자열도 처리한다.

# 형변환 문자열
print(str(True)) # 결과 : True
print(str(False)) # 결과 : Flase
print(str(10)) # 결과 : 10
print(str(98.9)) # 결과 : 98.9
# ※참고. print()를 호출 할때 내부적으로 str()를 한번 거친다.