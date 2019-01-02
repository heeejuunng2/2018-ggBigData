head="big"
tail="data"
print(head+tail)
print(tail*5)
print("="*70)
print(head+tail)
print("="*70)
tail="data"
print(tail[2])
print(tail[-2]) #a의 인덱스는 -1

a="Life is too short, You need Python"
print(a[5:7])
print(a[19:]+" and Java")

print("I eat %.2f apples" %3.14) #c언어하고 비슷, c언어에는 %자리에 ,
print("I ate {0} apples, so I was sick for {1} days".format(10,3))
print("I ate {1} apples, so I was sick for {0} days".format(10,3))
num=10
print(f"I ate {num+5} apples")
      #f를 붙이면 num+5가 변수임을 알 수있게함
#print("I ate {num+5} apples, so I was sick for {day} days".format(num=3,day=10))

a="hobby"
print(a.count('b')) #b라는 문자가 2개 있다는 뜻
print(a.index('y'))
b=","
print(b.join(a))
print(a.upper())
print("BIG".lower())

a="     hello     "
b="hi"
print(a+b)
print(a.lstrip()+b) #왼쪽(l) 공백 제거(strip)
print(a.rstrip()+b)
print(a.strip()+b) #공백 모두 제거

a="경기 big data 전문인력 양성"
print(a.split())
#파이선에서 대괄호 [ ]는 리스트를 의미함

num=[1,3,5,7,9]
a=[]
b=['a','b','c']
c=[1,2,'a','b']
print(num)
print(a)
print(b)
print(c)
d=['x','y']
e=[1,2,'a',d,'b']
print(e)
#리스트는 리스트안에 또다른 리스트 저장이 가능함
f=list()
print(f)
a=[3,4,['x','y','z']]
print(a) # a = a[:] = a[0:]
print("="*30+"구분선"+"="*30)
print(a[2])
print(a[-2])
#y 출력
print(a[-1][-2])

a="gunpo"
print(a[1:4])

b=[3,4]
c=[7,9]
print(b+c)
print(c*5)

a=[1,2,3]
print(str(a[1])+"hi") #숫자와 문자를 결합하려고 해서 오류
#따라서 str로 묶어줘서 a[1]을 문자열로 바꿔줌
print(a[1]+3)

print("="*50)
#삭제
print(a)

a[1]=[]
print(a)

del a[1]
print(a)

print("="*50)
#추가
print(a)
a.append(4)
print(a)

b=[5,6,7]
b.reverse()
print(b)
print(a)
print(a.index(3)) #3의 인덱스를 찾아라

print(a)
a.insert(2,7) #인덱스2에 7을 추가
print(a)

print("="*50)
#제거
a.remove(4)
print(a)

print(a.pop())
print(a.pop())
print(a.pop())
#뒤에서 부터 하나씩 출력 == stack구조

b=[1,2,3,1,2]
print(b.count(2))

print("="*50)

# dictionary : {키:값}
#          ex) {'이름':'전희정','학교':'모바일고','학년':2}

a={1:'hi'}
print(a)
print(a[1])
a[3]='hello' #3이 키, hello가 값
print(a)
print(a[3])

a['이름']='전희정'
print(a)
print(a['이름'])

a['별명']='체리'
print(a)

#값이 여러개일경우 리스트 이용
a['nick']=['체리','파이썬달인','데이터과학자']
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a['nick'])
print(a.get('nick')) #윗줄이랑 같음
print(a.get('birth','0703'))
#birth키의 값이 없으므로 None
#0703를 넣어서 디폴트값 줌
print("="*50)
print(a)
#a안에 이름이라는 키가 있는가?
print('이름' in a)

print("="*50)

#문제 1
a=['Life','is','too','short','you','should','need','python']
print(a[4]+" "+a[2])
#문제 2
a=['Life','is','too','short']
b=" "
print(b.join(a))
#문제 3
a=[1,2,3]
print(a.__len__())
#문제 4
a=[1,3,5,4,2]
a.sort() #숫자 순서대로 배열
a.reverse()
print(a)
#문제 5
a=[1,2,3,4,5]
a.remove(2)
a.remove(4)
print(a)
























