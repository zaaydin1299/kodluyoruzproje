# Kullanıcı Girişi ve Liste Oluşturma

Bu Python programı, kullanıcıdan girdi alarak iki farklı türde işlem yapar: sayı girişi ve metin girişi. Kullanıcı seçimine göre program, girdiyi işleyerek bir liste oluşturur ve ekrana basar.

## Kullanım

1. **Başlangıç**
   - Programı çalıştırdığınızda, size bir seçim yapmanızı isteyecektir: "metin" veya "sayı".
   - Seçiminize göre program, metin veya sayı girişi yapmanızı bekler.

2. **Sayı Girişi**
   - Eğer "sayı" seçeneğini seçerseniz, program virgülle ayrılmış sayıları girmenizi isteyecektir.
   - Girdiğiniz sayıları virgülle ayırarak liste haline getirir ve ekrana basar.

3. **Metin Girişi**
   - Eğer "metin" seçeneğini seçerseniz, program virgülle ayrılmış metinleri girmenizi isteyecektir.
   - Girdiğiniz metinleri virgülle ayırarak liste haline getirir ve ekrana basar.

4. **Geçersiz Seçim**
   - Eğer "metin" veya "sayı" dışında bir seçim yaparsanız, program geçersiz seçim olduğunu bildirir ve tekrar seçim yapmanızı ister.

## Örnekler

### Sayı Girişi
Metin girişimi? Sayı girişi mi? (metin/sayı): sayı
Virgülle ayrılacak olan sayıları girin: 10, 20, 30, 40
Sayılar: [10.0, 20.0, 30.0, 40.0]



### Metin Girişi
Metin girişimi? Sayı girişi mi? (metin/sayı): metin
Virgülle ayrılacak olan metinleri girin: elma, armut, çilek, muz
Metinler: ['elma', 'armut', 'çilek', 'muz']



## Hata Durumu
Metin girişimi? Sayı girişi mi? (metin/sayı): harf
Geçersiz bir seçim! Lütfen, metin veya sayı girişi yapınız.
