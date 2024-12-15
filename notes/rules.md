### Kural Belirleme
Burada oltalama amaçlı gönderilen bir SMS'te genel olarak karşılaşabileceğimiz belli başlı durumları listeleyeceğim.

Bu liste zamanla genişletilebilir ve güncellenebilir. Üretken yapay zekâ faktörünü de düşünürsek, çok daha yakın vakitte güncellenmesi ve/veya üzerine eklemeler yapılması gerekebilir.

Tahmin ederim ki buradaki kurallar illegal bahis sitelerinden gelecek iletileri engellemeye öngörülebilir bir süre daha yeterli olacak (:

1. Bir SMS'te link varsa, hele de kısaltılmış link var ise bunu doğrudan oltalama iletisi kategorisine alalım derim. 
   * Burada gelen SMS'lerde yer alan linkleri tıklanamaz hâle getirmek iyi bir önlem olur diye düşünüyorum bkz. [url defanging](https://trustifi.com/url-defang-tool/) 
    İlla tıklamak istiyorlarsa "emin misin..." diye sormak suretiyle url yeniden tıklanılabilir hâle getirilir.
2. Anahtar kelime listesi yapılarak bunları doğrudan oltalama iletisi olarak sınıflandırmayı makûl buluyorum. 
   * "Kazan", "Çevrimsiz", "Hemen tıkla", "Acil tıkla", "Hemen üye ol", "Boş yok", "Promosyon kazan" _bunların ingilizce karakterlerle yazılmış hâllerini de hesaba katmak gerek_.
3. Aciliyet ya da bir çeşit tehdit içeren iletileri de elemeli, bunun için doğal dil işleme yöntemlerinden yararlanmak daha verimli olacak. O sebepten bir üstteki kurala eklemiyorum örneklerini. 
4. Dilbilgisi yanlışlarını ekleyecek olursak ortalık karışabilir, eli yüzü düzgün ileti yazan kişi sayısı çok çok azınlıkta zira.
5. Gönderici numarasına bakabiliriz. Türkçe SMS oltalama tespit etmeye çalıştığımızdan mütevellit, +90 ile başlayan bir numaradan ileti gelince bunu doğrudan spam olarak algılamakta bir mahzur görmüyorum 28 yıllık yaşam tecrübemden ve bunun bir dönem ödevi olmasından kaynaklanan cüretkârlık ile.
6. Ardışıl ünlemler!!!
7. Ardışıl BÜYÜK HARFLER
8. Sahte linkler 
9. Typosquatting bkz. [yazım tuzağı](https://www.kaspersky.com/resource-center/definitions/what-is-typosquatting) 


**NOT** Buradaki kuralları vakitle genişletmeye çalışacağım. Niyetim makine öğrenmesi bloğundan evvel kural tabanlı bir filtreleme yapmak. _Her şeyin ilacı olarak YZ ve MÖ_ reçetesine güvenmiyorum.

