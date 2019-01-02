# 읽기
f=open("sample.txt","r")
sum=0
avg=0
count=0
while True:
    line = f.readline()
    if not line: break
    sum+=int(line)
    count+=1
avg=sum/count
print("평균:"+str(avg))

# 쓰기
f=open("result.txt","w")
f.write("평균:"+str(avg))

f.close()

# 선생님 코드
# f=open("sample.txt")
# lines = f.readlines(_)
#
# total=0
# for line in lines:
#     score = int(line)
#     total t= score
# average=total/len(lines)
#
# f=open("result.txt","w")
# f.write(str(average))
# f.close()

