s1=set("hello")
print(s1)
#set이 집합을 나타내는 함수 이므로 중복된 원소는 1번만 나옴
s2=set([1,2,1,2,1,2,3])
print(s2)

a=True
b=False

print(1==1)
print(2>1)
print(2<1)

k=[1,2,3]
while k: #k값이 있는동안 ...k값 없으면 실행 X
         #데이터가 있으면 true, 없으면 false
    print(k.pop()) #k에서 데이터 하나 꺼내서 출력
    print("hello")
print("end")
#들여쓰기가 되있는 영역까지가 while문의 범위

if[100] :   #[100] : 100이라고 저장되어 있는 리스트,
            #  길이는 1 , 데이터값은 100
            #[]는 데이터가 없으므로 거짓
    print("참")
else:
    print("거짓")

print(bool('bigdata'))
print(bool(''))
#0만 거짓이고 나머지는 전부 다 참임
print(bool(0))
print(bool(-1))

#include <stdio.h> 같은 거랄까..
from copy import copy
#copy"패키지"에서 copy"함수"를 가져와라

a=100
b=copy(a)
print(b)

money=0
card=1
if money or card:
    print("택시로",end="?")
else:
    print("걸어서",end="?")
print(" 간다")
#end="" 붙이면 줄바꿈 X
#end="?" 붙이면 ?도 붙여진 채로 줄바꿈X

money=4000
card=False
#카드가 있거나 돈이 4000원 이상이면
#택시 이용 출력하고 아니면 도보 출력

if money>=4000 or card:
    print("택시 이용")
else:
    print("도보")

pocket=['trash','cellphone']
card=0
if 'money' in pocket :
    print("택시 이용")
elif card :
    print("택시 이용")
else :
    print("도보")

treeHit=0
while treeHit<10 :
    if treeHit==4 : break
    treeHit=treeHit+1
    print("나무를 %d번 찍었어요" %treeHit)
    if treeHit==10:
        print("나무 쓰러집니다")

#1~10까지 수 중에서 홀수만 출력(while)
i=0
while i<10:
    i = i + 1
    if i%2==1:
        print(i,end=" ")

# while i<10:
#     i = i + 1
#     if i%2==0 : continue
#     print(i, end=" ")
print()

#for문
mylist=['one','two','three']
for i in mylist:
    print(i)

a=[(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)

#출력예시(70점 이상 합격)
#1번 학생 축하합니다. 합격입니다.
#2번 학생 안타깝습니다. 불합격입니다.
#...
#5번 학생 축하합니다. 합격입니다.

score=[90,20,60,80,75]
number=0
for s in score:
    number=number+1
    if s<70: print("%d번 학생 안타깝습니다. 불합격입니다." %number)
    else: print("%d번 학생 축하합니다. 합격입니다."%number)

a=range(10) #0포함, 10미포함
print(a)
a=range(1,11) #1~10까지

sum=0
for i in range(1,11):
    sum=sum+i
    print(sum)

for i in range(1,5):
    for j in range(1,3):
        print(i,"와",j)

#1. for문을 이용하여 1부터 1000까지의 자연수 중
# 5의 배수의 해당하는 자연수들의 총합 출력
sum=0
for i in range(1,1001):
    if i%5==0:
        sum=sum+i
print(sum)

#2. 다음은 학생들의 혈액형(A,B,AB,O)에 대한 데이터이다
#['A','B','A','O','AB','AB','O','A','B','O','B','AB']
#for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오

asum=bsum=absum=osum=0
bd = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
for data in bd:
    if data=='A': asum+=1
    elif data=='B' : bsum+=1
    elif data == 'AB':absum += 1
    elif data == 'O': osum += 1
print("A형:",asum)
print("B형:",bsum)
print("AB형:",absum)
print("O형:",osum)

result={}
for b in bd:
    if b in result:
        result[b]+=1
    else :
        result[b]=1 #result {'A'}=1
                    #result {'B'}=1
print(result)

print("="*10+"문제1"+"="*10)
a=[70,60,55,75,95,90,80,80,85,100]
sum=0
avg=0
for i in a:
    sum+=i
avg=sum/len(a)
print(avg)

print("="*10+"문제2"+"="*10)
i=1
while i<5:
    print("*"*i)
    i=i+1

print("="*10+"문제3"+"="*10)
lucky_list=[1,9,23,46]
i=0
while i<4:
    if lucky_list[i]==23: print("야호")
    i=i+1
print("="*10+"문제4"+"="*10)
star=7 #별의 갯수
space=0 #공백의 갯수
while star>0:
   print(' '*space+'*'*star) #공백+별 출력
   star-=2
   space+=1





















