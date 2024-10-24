import pandas as pd

data = 'https://raw.githubusercontent.com/kaveai/veribilimiyazokulu/main/Pratikler/data.csv'
df = pd.read_csv(data)

sonuc = df[df['social'] > 3]
sonuc1 = df[(df['gpa']< 4)  & (df['age']< 4)  ]

print(sonuc1)
