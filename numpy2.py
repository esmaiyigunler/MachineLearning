import numpy as np

dizi1 = np.random.randint(0,100)
dizi2 = np.random.randint(0,100)

print(dizi1)
print(dizi2)

toplam = dizi1 + dizi2
print(toplam)
################################################

dizi = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("ikinci satırdan ikinci sutundan itibaren")
print(dizi[1:,1:])
print("ilk iki satır ve ilk iki sutun")
print(dizi[:2,:2])
print("Tüm satırların ikinci Sutunu")
print(dizi[:,1])
#############################################

dizi = np.array([10,20,30,40,50])
ortalama = np.mean(dizi)
standartSapma = np.std(dizi)
toplama = np.sum(dizi)
print(f"Dizinin ortalaması:{ortalama}, Dizinin standart sapması:{standartSapma}, Dizinin toplamı:{toplama}")
###################################################

dizi = np.random.randint(0,100,size=10)

print(dizi)

for i in dizi:
  if i<=33:
    print(f"{i} düşük eleman")
  elif 33<i<=66:
    print(f"{i} orta seviyeli eleman")
  else:
    print(f"{i} yüksek seviyeli eleman")
