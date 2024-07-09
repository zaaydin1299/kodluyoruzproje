
#Burada int değeri girilmesi istenmiştir.
a = int(input("Bir tamsayı giriniz: "))
print(a) #çıktı a olur.

#Kullanıcıdan bir isim veya herhangi bir metin girmesini isteyin ve bunu metin (string) olarak işleyin.
b = str(input("Bir isim veya herhangi metin giriniz :  "))
print(b)

#Kullanıcıdan birden fazla değer (örneğin, virgülle ayrılmış sayılar) girmesini isteyin ve bu değerleri bir listeye dönüştürülür.

# virgülle sayı girmesi istenilir.
seçim= input(" Metin girişimi? Sayı girişi mi? (metin/sayı): ").strip().lower()

#Kullancının seçimine göre işlem yapılır.
if seçim == 'sayı' :
    girdi = input("Virgülle ayrılacak olan sayıları girin: ")

    # Girdiyi virgüllerle bölerek bir listeye dönüştürün
    eleman_listesi= girdi.split(",")
    # Her bir öğeyi sayıya dönüştürün
    sayi_listesi = [float(eleman.strip()) for eleman in eleman_listesi]
#Sayı listesini ekrana yazdırın.
    print("Sayılar:", sayi_listesi)
elif seçim == 'metin':
    girdi = input("Virgülle ayrılacak olan metinleri girin: ")

    eleman_listesi= girdi.split(",")
    metin_listesi = [(eleman.strip()) for eleman in eleman_listesi]

    print("Metinler", metin_listesi)

else:
    print("Geçersiz bir seçim! Lütfen, metin veya sayı girişi yapınız.")




