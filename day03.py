# 함수란? 입력->처리(함수)->출력. 기능을 수행하는 것
# y=x+2 일차함수(직선 방정식)
# x에 3입력 -> 5=3+2 ->5출력

# 함수 선언하는 법
def sum(a=5,b=4):
    return a+b

x=3
y=2
c=sum(x)
print(c)
c=sum()
print(c)

# 함수의 활용(다른언어들과 다른 특징)
def sum_and_mul(a,b):
    return a+b, a*b
res=sum_and_mul(3,4)
print(res)
print(res[0])
print(res[1])

res1, res2=sum_and_mul(3,4)
print(res1)
print(res2)

def say_myself(name,old,man=True):
    print("내 이름은 %s" %name)
    print("나이는 %d살" %old)
    if man:
        print("남자")
    else:
        print("여자")

say_myself("전희정",18,False)


# 함수이름 : intro()
# 인수:학교명, 학년, 반, 이름
# 출력예시: 군포e비즈고 3학년 2반 홍길동입니다.

def intro(school,hak,ban,name):
    # print(school+" "+str(hak)+"학년 "+str(ban)+"반 "+name+"입니다.")
    # format함수 이용
    print("{0} {1}학년 {2}반 {3}입니다.".format(school,hak,ban,name))
    # print("%s %d학년 %d반 %s입니다." % (school,hak,ban,name))

intro("경기모바일과학고",2,7,"전희정")

print("="*50)

# 입력
a=input("나이를 입력하세요")
print("내 나이는 "+str(a)+" 입니다")























































































































































