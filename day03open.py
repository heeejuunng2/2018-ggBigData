# 오픈함수로 파일 만듬 w는 쓰다(write)의 약자
# text.txt는 파일 이름 <<<여기서 확인해보면 파일 생김
#쓰기(write)
f=open("text.txt","w")
for i in range(1,11):
    data="%d번째 줄입니다\n" %i
    f.write(data)
    # print(data)

#읽기(read)
f=open("text.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line)

f=open("text.txt","r")
lines=f.readlines()
for line in lines:
    print(line)

#추가(append)
f=open("text.txt","a")
for i in range(11,20):
    data="%d번째 줄입니다\n" %i
    f.write(data)

# Quiz01>
sum=0
for i in range(1,5):
    a=int(input("점수를 입력하세요"))
    sum+=a
    i+=1
avg=sum/4
print(avg)

# def avg(*arg):  #arg는 리스트
#     # print(len(arg))
#     # print(arg[1])
#     sum=0
#     for i in arg:
#         sum+=i
#     return sum/len(arg)
#
# print(avg(1,2,5,7,9))


# Quiz02>
b=int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
res=0
for i in range(1,10):
    res=b*i
    print("%d*%d=%d"%(b,i,res))
    i+=1

# def gugudan(n):
#     for i in range(1,10):
#         print(n*i)
# gugudan(5)

# Quiz03>
c=int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1,10):
    print(c*i,end=" ")
