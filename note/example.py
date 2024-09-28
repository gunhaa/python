
my_list = ['a', 'b', 'c', ['d', 'e'] ] 

print(my_list[-1][0])
#음수는 뒤에서 부터 샌다.
#3번 인덱스는 d,e가 들어있는 리스트이다. 뒤로 한칸, 첫번째 = 'd' 이다.

print(type(my_list))
#class의 type을 가진다. my_list
print(type(my_list[-1]))

print(type(my_list[-1][0]))

my_list = list(range(10))
print(my_list)

#my_list에서 다섯번째 데이터까지 출력하기
print(my_list[:5])

#my_list에서 세번째부터 마지막까지 출력하기
print(my_list[2:])

#문자열 인덱싱&슬라이싱
c="1998-03-24"

print(c[0:4])
print(c[6:7])
print(c[-1])
#c의 복사본 생성. 동일한 결과이지만 메모리상으로는 독립적인 복사본(얕은복사)
print(c[:])

#for문

python_score = [57, 86 , 63, 92, 35 , 79]

a=1
for i in python_score :
    if i >= 80 :
        grade = 'A'
    elif i>= 60 :
        grade = 'B'
    else :
        grade = 'C'
    print(f"{a}번은 {i}점이며, {grade}등급 입니다")
    a += 1

#range 이용법
#range(stop)
#range(start, stop[, step])

bundle = [1,2,3,4,5,6,7,8,9]
total = 0
for x in bundle :
    total += x

print(total)
