
evet = 1
hayır = 0

# Kullanıcının kaydını almak
kAdi = input("Kullanıcı Adınızı Belirleyiniz: ")
kSifre = input("Şifrenizi Belirleyiniz: ")
print("Başarıyla Kayıt Oldunuz. Giriş İçin Yönlendiriliyorsunuz...")

girishakki = 3

# Kullanıcı girişini kontrol etmek
while girishakki > 0:
    girishakki -= 1
    gkAdi = input("Kullanıcı Adınızı Giriniz: ")
    gSifre = input("Şifrenizi Giriniz: ")

    if gkAdi == kAdi and gSifre == kSifre:
        print(f"{kAdi}, Hoş Geldin... Anasayfa'ya Yönlendiriliyorsun...")
        break
    else:
        print(f"Kullanıcı Adı ya da Şifre Yanlış! Kalan Giriş Hakkınız: {girishakki}")
        continue

# Şifre sıfırlama veya çıkış işlemini gerçekleştirmek
while girishakki == 0:
    try:
        print("Şifrenizi Sıfırlamak İstiyor Musunuz? 1-Evet, 0-Hayır")
        cevap = int(input("Lütfen Birini Seçiniz: "))

        if cevap == evet:
            yenisifre = input("Yeni Şifrenizi Giriniz: ")
            
            if yenisifre == kSifre:
                print("Yeni Şifreniz Eskisiyle Aynı Olamaz!")
            else:
                print("Şifreniz Başarıyla Değiştirilmiştir... Ana Menüye Yönlendiriliyorsunuz...")
                kSifre = yenisifre  # Yeni şifreyi eski şifreyle değiştir
                break

        elif cevap == hayır:
            print("Hesap ile Bağlantınız Kesildi! Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Giriş!")
        continue
    except:
        print("Geçersiz Tuşlama. Lütfen Kontrol Ediniz.")
        continue
