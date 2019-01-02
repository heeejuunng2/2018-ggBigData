import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

traffic_path="traffic accident.csv"
traffic_accident=pd.read_csv(traffic_path, encoding="euc-kr")
traffic_accident=traffic_accident[['발생건수','사상자수','사망자수','중상자수','경상자수']]
traffic_accident.rename(columns={traffic_accident.
                           columns[0]:'Number of occurrences',
                           traffic_accident.columns[1]:'Casualties',
                           traffic_accident.columns[2]: 'The death toll',
                           traffic_accident.columns[3]: 'The number of serious injuries',
                           traffic_accident.columns[4]: 'Ordinary embroidery'}
                           ,inplace=True)
traffic_accident.index.name="구분"
print(traffic_accident.head())
traffic_accident.hist()
# plt.legend()
plt.grid()
plt.show()
