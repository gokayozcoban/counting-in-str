# Stirng içerisindeki karakterleri saymak:
# Mesela a harfinden kaç tane var?

metin = input("Metni girin: ")
harf = input("Sorgulanmak istenilen harf hangisi: ")
sayı = 0
for i in metin:
    if harf == i:
        sayı += 1
print(sayı)
input()
##Önce metni yaz.
##kullanıcıdan input() ile sorgulanmak istenilen harfi al,
##bunu sayacağın için bir sayı değişkeni hazırla,
##dögüyü başlat: metnin içinde i için:
##    kullanıcıdan alınan harf eşitse i'ye:
##         sayı değişkenine 1 ekle
##topladığın sayı değişkenini print() ile yazdır


