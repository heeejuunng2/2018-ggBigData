# Numpy : 행렬 연산 라이브러리, 대규모 다차원 배열과 행렬 연산에
import numpy as np
# print(np.__version__)
# 사진 : 높이 28, 폭: 28, 각 픽셀은 3개의 채널로 구성(rgb)
# shape=(28,28,3)인 3차원 배열로 나옴
# axis=0(첫번째 차원), axis=1(두번째 차원), axis=2(세번째 차원)
#
# def pprint(arr):
#     print("타입:{}".format(type(arr)))
#     print("shape:{}, 차원:{}, 타입:{}"
#           .format(arr.shape, arr.ndim, arr.dtype))
#     #shape는 배열 모양 1차원의 3개짜리니까 (3, )나옴
#     print("배열 데이터:\n",arr)
#
# arr=[1,2,3]
# a=np.array([1,2,3])
# pprint(a)

arr=np.arange(0,4*2*4)
print(len(arr))
print(arr)
v=arr.reshape([4,2,4])  #2행 4열 짜리가 4열 =>면 4개라고 봄
#2행 4열의 4면이라고 함
print(v)
print(v.ndim) #몇차원이냐 ?
print(v.sum()) #모든 데이터의 합

print(v.sum(axis=2)) #요소별로 더해짐
#axis는 축, 3차원이므로 3가지 축 0,1,2에 따라 요소별로 더해짐




















