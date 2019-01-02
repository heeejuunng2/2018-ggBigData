import pandas as pd
import numpy as np
from gensim.models import Word2Vec
import re

# file=open('moby1.txt','r')
# # print(file) #<_io.TextIOWrapper name='moby1.txt' mode='r' encoding='cp949'>
# moby_dick=file.read()
# print(moby_dick)
#
# print("<raw_doc","-"*100) #가공되지 않은 문서, 원본문서
#
# # moby_dick=re.split("[\n]",moby_dick) #한줄 단위로 컴마로 구분된 리스트가 만들어짐
# # print(moby_dick)
#
# moby_dick=re.split("[\n\.]",moby_dick)
# # 줄 바꿈 문자 또는 .(마침표) 로 분리된 문장으로 리스트 생성
# print(moby_dick)
#
# print("<split_doc","-"*100)
#
# #공백제거
# while ' ' in moby_dick:
#     moby_dick.remove(' ')
# print(moby_dick)
#
# print("<remove_blank_doc","-"*100)
#
# #데이터프레임 저장
# df_Mobydic=pd.DataFrame() #빈 데이터프레임
# df_Mobydic['sentences']=moby_dick #데이터 추가 ..
# # df_Mobydic['sentences']=np.asarray(moby_dick)
# print(df_Mobydic)
# print('before','-'*100)
#
# df_Mobydic['separates']=df_Mobydic['sentences'].apply(lambda x:x.replace(',',''))
# df_Mobydic['separates']=df_Mobydic['separates'].apply(lambda x:x.replace(';',''))
# df_Mobydic['separates']=df_Mobydic['separates'].apply(lambda x:x.replace('\n',''))
# df_Mobydic['separates']=df_Mobydic['separates'].apply(lambda x:x.replace('-',''))
# df_Mobydic['separates']=df_Mobydic['separates'].apply(lambda x:x.replace('.',''))
#
# print(df_Mobydic)
# print('after','-'*100)
#
# df_Mobydic['separates']=df_Mobydic['separates'].apply(lambda x:x.split())
# print(df_Mobydic)
#
# model=Word2Vec(df_Mobydic['separates'], hs=1, size=300, min_count=5)
# print(model)
# for word, score in model.most_similar('some'):
#     print(word)
































