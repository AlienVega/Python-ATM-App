# liste = [1,3,5,7,36,78]
# liste2 =[]

# for i in range(liste[0],liste[-1]+1,2):
#     if i not in liste:
#         liste2.append(i)
# print(liste2)

                                # ATM UYGULAMASI
def atm():
    kullanıcı="admin"
    sifrem="1234"
    bakiye=5000
    borc=3000
    hak=3
    while True:
        hesap=input("kullanıcı adınızı giriniz=")
        sifre=input("şifrenizi giriniz=")
        hak-=1
        if hesap == kullanıcı and sifre==sifrem:
            print("hoşgeldiniz")
            while True:
                print("""İŞLEMLER:
                1-para çekme
                2-para yatırma
                3-para gönderme
                4-borç yatırma
                5-şifre değiştirme
                6-bakiye sorgulama
                7-çıkış                
                """)
                islem=int(input("yapmak istediğniz işlemi yazınız"))
                if islem==1:
                    while True:
                        cek=int(input("çekmek istediğiniz miktarı giriniz:"))
                        if cek<=bakiye:
                            bakiye-=cek
                            print("çekilan miktar: {}tl güncel bakiye: {}tl".format(cek,bakiye))
                            break
                        else:
                            print("yetersiz bakiye")
                elif islem==2:
                    yatır=int(input("yatırmak istediğiniz miktarı giriniz:"))
                    bakiye+=yatır
                    print("yatırılan miktar: {} tl güncel bakiyeni : {} tl".format(yatır,bakiye))          
                elif islem==3:
                    while True:
                        gonder = int(input("göndermek istediğinz miktarı giriniz:"))
                        if gonder<=bakiye:
                            hesapNo=int(input("gönderilecek hesabı giriniz:"))
                            print(f"{hesapNo} hesabında {gonder}tl gönderme işlemini onaylıyor musunuz? E/H ")
                            while True:
                                onay =input()
                                if onay=="e" or "E":
                                    bakiye-=gonder
                                    print(f"gönderilen miktar: {gonder} tl güncel bakiyen: {bakiye} tl ")
                                    break
                                elif onay =="h" and "H":
                                    print("işlem iptal ediliyor")
                                    break
                                else:
                                    print("geçersiz işlem")
                        else:
                            print("yetersiz bakiye")
                elif islem==4:
                    if borc>0 :
                        print(f"mevcut borcunuz: {borc}")
                        
                        while True:
                            borcyatır=int(input("yatırmak istediğinz borcu giriniz:"))
                            if borcyatır<=borc:
                                if borcyatır<=bakiye:
                                    bakiye-=borcyatır
                                    borc-=borcyatır
                                    print(f"{borcyatır} tl yatırıldı.kalan borcunuz {borc}tl güncel bakiyeniz {bakiye}tl")
                                    break
                                else:
                                    print("yetersiz bakiye")
                            else:
                                print("mevcut borcunuzdan fazlası girilemez")
                    else:
                        print("borcunuz yoktur")  
                elif islem==5:
                    yenihak=0
                    while True:
                        eskisifre=input("mevcut şifrenizi giriniz")
                        yenihak+=1
                        if eskisifre==sifrem:
                            yenisifre=input("yeni şifreyi giriniz")
                            sifrem=yenisifre
                            print("şifreniz güncellendi")
                            break
                        elif yenihak==3:
                            print("hakkınız bitti işlem sonlanıyor")
                            break
                        else:
                            print("şifreler uyuşmuyor")
                elif islem==6:
                    print(f"mevcut bakiye {bakiye} tl")
                elif islem==7:
                    break
            print("program kapanıyor")
            break
        elif hak==0:
            print("hakkınız bitti program kapanıyor")
            break
        else:
            print("kullanıcı adı veya şifre hatalı")
        
atm()