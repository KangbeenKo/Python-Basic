# #주의) 파일이름이 모듈이름인 random과 같을 경우 "random is not callablepylint(not-callable)"라는 오류가 발생한다.
from random import *

print(random()) #0.0이상 1.0미만 랜덤실수 출력
print(random()*10) #0.0이상 10.0미만

print(int(random()*10)) #0이상 10미만 랜덤정수
print(int(random()*10)+1) #1이상 10이하(11미만) 랜덤정수

#Lotto 번호 생성기 1
for i in range(0,6):
    print(randrange(1, 46))

#Lotto 번호 생성기 2
for i in range(0,6):
    print(randint(1,45))

#Lotto 번호 생성기 3 - list 형태 / 중복제외
print(sample(range(1,51),5)) # sample(a, b) - a에서 b개를 뽑는다.


# Suffle - 7강 이후 추가
list = [1,2,3,4,5]
print(list)
shuffle(list)
print(list)