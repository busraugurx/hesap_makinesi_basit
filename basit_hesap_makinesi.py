#BASİT HESAP MAKİNESİ
"""
1)TOPLAMA
2)ÇIKARMA
3)ÇARPMA
4)BÖLME
"""
"""a=float(input("Birinci sayıyı giriniz: "))
b=float(input("İkinci sayıyı giriniz: "))

işlem=int(input("işlem numarasını giriniz: "))

if(işlem==1):
    print("{} ile {} nin toplamı {} dir" .format(a,b,a+b))
elif(işlem==2):
    print("{} ile {} nin farkı {} dir." .format(a,b,a-b))
elif(işlem==3):
    print("{} nin {} a bölümü {} dir" .format(a,b,a/b))
elif(işlem==4):
    print("{} ile {} çarpımı {} dir" .format(a,b,a*b))
else:
    print("HATALI GİRİŞ YAPILDI !!")"""

'''print("""**********************
KULLANICI GİRİŞİ
**********************""")

kullanıcı_adı = "busra_ugurx"
kullanıcı_şifre = "12345"

kullanıcıadı = input("KULLANICI ADINIZI GİRİN: ")
şifre = input("ŞİFRENİZİ GİRİN: ")

if (kullanıcı_adı == kullanıcıadı and şifre==kullanıcı_şifre ):
    print("BAŞARILI GİRİŞ")
elif (kullanıcıadı != kullanıcı_adı and şifre == kullanıcı_şifre):
    print("KULLANICI ADI HATALI")
elif (kullanıcıadı == kullanıcı_adı and kullanıcı_şifre!= şifre):
    print("ŞİFRE YANLIŞ!!")
elif (kullanıcıadı != kullanıcı_adı and kullanıcı_şifre != şifre ):
    print("KULLANICI ADI VE ŞİFRE HATALI!!!") '''


"""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez"""

print("****************** BEDEN KİTLE ENDEXİ ******************")

kilo=float(input("KİLONUZU GİRİN: "))
boy=float(input("BOYUNUZU CM CİNSİNDEN GİRİN: "))

beden_kitle_endexi = kilo/((boy*boy)/10000)


if(beden_kitle_endexi<18.5):
    print("ZAYIFSINIZ")
elif( beden_kitle_endexi < 25 and beden_kitle_endexi>=18.5 ):
    print("NORMAL KİLONUZDASINIZ.")
elif( beden_kitle_endexi>=25 and beden_kitle_endexi<=30):
    print("AŞIRI KİLOLUSUNUZ!!")
else:
    print("OBEZSİNİZ")








