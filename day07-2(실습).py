import pandas as pd
testCSV_path="olive.csv" #d:\\test\\data.csv : 경로 읽어오는 방법
olive_oil=pd.read_csv(testCSV_path)
# print(olive_oil.head(5)) #.head(5) : 앞에서5개 읽어오기
# print(olive_oil.tail(5)) #.tail(5) :뒤에서 5개 읽어오기
olive_oil.index.name='id' #index: 행이름. 행이름을 id로 변경
# print(olive_oil)
# print(olive_oil.columns.values[0]) # Unnamed: 0 출력
olive_oil.columns.values[0]='id_area1'#디폴트 열 이름 Unnamed: 0을 id_area로 변경
# print(olive_oil.head(5))
# 0번 열을 id_area로 변경한 후 출력
# olive_oil.columns.values[0]='id_area'
# print(olive_oil.head(5))
olive_oil.rename(columns={olive_oil.columns[0]:'id_area'},inplace=True)
                            # {무엇을: 무엇으로 바꿀지}
# print(olive_oil.head(5))

# print(olive_oil['id_area'].unique())  #중복있나 없나
#중복된거 하나만 나옴 -> 출력결과보면 다 다름!
# print(len(olive_oil['id_area'].unique()))
#572 출력, 데이터가 572개이므로 모든데이크가 유니크함
# print(olive_oil.shape) #572행 11열

# print(olive_oil.head(5))
# print(olive_oil['id_area']) #id_area열에 해당하는거만 출력
# print(olive_oil['id_area'][0]) #id_area열에 0번행의 데이터
# print(olive_oil['id_area'][0].split('.'))
# #.split('.') :점으로 분리해라 -> [ '1' , 'North-Apulia' ]
# print(olive_oil['id_area'][0].split('.')[0])
#.split('.') :점으로 분리한거중에서 0번째 -> 1
# print(olive_oil['id_area'][0].split('.')[0] +1) #오류 , 여기서 (출력된)1은 문자이기 때문
# print(int(olive_oil['id_area'][0].split('.')[0])-1) #0

# str(int(olive_oil['id_area'][0].split('.')[0])-1) # 0-> '0'
# print(str(int(olive_oil['id_area'][0].split('.')[0])-1)+".")

# str(int(olive_oil['id_area'][0].split('.')[0])-1)+"."+olive_oil['id_area'][0].split('.')[1]
# print(str(int(olive_oil['id_area'][0].split('.')[0])-1)
#       +"."+olive_oil['id_area'][0].split('.')[1])
#-> 증감작업, .. 바꾸기 .. .

# #함수 정의
# sum = lambda a,b : a+b #sum은 람다함수의 이름,
#                         # (함수의 이름을 반드시 줄 필요는 없음)
#                         #이름이 없으면 밖에서 불러서 쓸 필요가 없다는 말
#                        # a,b에는 함수 호출부에서 값들(3,4)이 전달됨
#                        # : 기호 다음엔 함수가 수행할 기능을 기술함,3+4=>7
# print(sum(3,4))
# #sum함수에 3과4를 전달하여 함수를 수행한 결과를 출력해라
#
# def sum2(a,b):
#     return a+b
# print(sum2(3,4))

# olive_oil['id_area']=olive_oil['id_area'].apply(
#     #id_area 값이 x로 전달됨
#     lambda x:str(int(x.split(".")[0])-1)+"_"+x.split(".")[1])
# print(olive_oil['id_area'].head(5))

print(olive_oil['palmitoleic'].head(5)) #75->0.75 , 73->0.73
# 각 데이터를 /100.00 으로 나누어서 타입을 변환하시오
olive_oil['palmitoleic']=olive_oil['palmitoleic'].apply(
    lambda x: x/100.0
)
print(olive_oil['palmitoleic'].head(3))
print(type(olive_oil))

#데이터프레임 -> 파일로 저장
olive_oil.to_csv("my_olive_oil.csv")

csvfile=pd.read_csv("surveys_withAt.csv", sep="@")
#sep="@" 골뱅이 문자로 분리해서 읽어라
print(csvfile.head(3))
print("="*50)

#여러 csv파일 읽기
import glob
import os

filePathList=glob.glob("csv_files\\*.csv")
# print(filePathList)
# print(len(filePathList))
for i in range(0, len(filePathList)) : #0~9까지 반복(10번)
    temp=os.path.basename(filePathList[i])
    # print(temp) #1763.cvs ... 파일명만 출력됨
    # temp1=os.path.basename(filePathList[i].split(".")[0])#파일명만 저장
    temp1=os.path.splitext(temp)
    # print(temp1)
    print(temp.split(".")[0])    #파일명만 저장
    # print(temp.split(".")[1])    #확장자만 저장
    # print("temp: ", temp)
    # print("temp1: ", temp1)
































































