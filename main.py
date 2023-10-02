import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Şifre kaç haneli olsun?"))

olusturulan_parola = ""

for _ in range(parola_uzunlugu):

    rastgele_karakter = random.choice(karakterler)
    olusturulan_parola += rastgele_karakter


print("Olusturulan parola :" , olusturulan_parola)

                  

