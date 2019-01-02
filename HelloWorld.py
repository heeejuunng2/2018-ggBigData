print("안녕?")
a=12
print(a)
a=3.14
print(a)
a="안녕"
print(a)
a=2.1e-10
print(a)
a=574876745435468764214354868788522
b=4454411345465497878787789862122343913651
print(a*b)

a=10
b=3
print(a**b)

print(5%3)
print(5/3)

print(divmod(17,3))

print("우리는\n고등학생\n입니다")

print("""
우리는
빅데이터를
공부합니다
""")

print("-"*50)
#띄어쓰기를 50칸 한 이후에 안녕 출력

print(" "*50+"안녕")
jumin="180101-1234567"
print(jumin[:6]) #0~5까지
print(jumin[3:6]) #3~5까지, 6포함 ㄴㄴ
print(jumin[8:]) #8~끝까지

#연습문제
#1. 다음 점수의 평균을 구하시오.
a=90
b=70
c=80
hap=a+b+c
avg=hap/3
print(avg)

#2. 학교 및 학년 반 등을 출력하시오.
print("""
경기모바일과학고등학교
2학년 7반
4번
전희정
""")

#3. 다음 주민번호에서 생년월일만 출력하시오.
jumin="180202-2345678"
print(jumin[:6])
print(jumin[:4])
print(jumin[4])
print(jumin[4:])
a="life is too short, you need python"
print(a.find("short"))
print(a.replace(" ","$"))