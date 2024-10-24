import pandas as pd

df = pd.DataFrame({
'İsim': ['Ahmet','Ayşe','Mehmet','Fatma'],
'Yaş': [23, 21, 25, 22],
'Şehir': ['İstanbul','Ankara','İzmir','Bursa']},index=['A','B','C','D'])
print(df.loc['A','İsim'])
print(df.loc['B':'C','Yaş'])
print(df.iloc[0,1])
print(df.iloc[1:3,0])
