import pandas as pd
isimler=["Ahmet","Ayşe","Mehmet","Fatma"]
yaslar=[15,21,25,22]
sehirler=["İstanbul","Ankara","İzmir","Bursa"]

data={
"İsim":isimler,
"Yaş":yaslar,
"Şehir":sehirler
}
df=pd.DataFrame(data)
print(df["İsim"])
print(df["Yaş"])

okul=["A","B","C","D"]
df["okul"]=okul
sonuc=df[df["Yaş"]>16]
print(sonuc)

