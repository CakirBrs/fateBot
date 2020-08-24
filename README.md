# fateBot
Siteden karakter kağıdı almk ve zar atmak için yaptığım bir script.
Not: Kodun çalışması için bilgisayarınızda python ve requirements.txt dosyasında bulunan modüller olmalı. Modülleri yüklemek için pythonu yüklediklten sonra komut satırına pip install modlAdı şeklinde sırayla yazmanız yeterli. Örnek:
>pip install Pillow


Başka kullanmak isteyen olursa diye nasıl kurulacağı ve kullanılacağı:

[Önce discord developer portalından bir uygulama oluşturmamız gerekiyor:](https://discord.com/developers/applications)

![GitHub Logo](/tutor/1.jpg)
 
 
 Uygulama için bir isim giriyoruz:
 
![GitHub Logo](/tutor/2.png)


 Buradan botun resmini ayarlayabilirsiniz:
 
![GitHub Logo](/tutor/3.jpg)


 Botu oluşturmak için sol taraftan "Bot" kısmına girip "Add Bot" diyoruz:
 
![GitHub Logo](/tutor/4.jpg)


 Botu oluşturduktan sonra Token'ı kopyalayıp fatedc.py belgesindeki 2. satırda "TOKEN" yazan yere yapıştırıyoruz:
 (fatedc.py dosyasına iki kez tıklayarak açmaya çalışırsanız kod çalışmaya başlar sağ tıklayıp düzenleye basarak açamanız gerekli)
 
![GitHub Logo](/tutor/6.jpg)


 Sol tarafta OAuth2 yazan sekmeye girip Scopes kısmından "bot"u seçtikten sonra altında açılan Bot Permissions kısmından Administrator'ı seçip ortadaki linki açıyoruz:
 
![GitHub Logo](/tutor/7.jpg)


 Açılan pencerede botu hangi discord serverına eklemek istediğimizi seçiyoruz:
 
![GitHub Logo](/tutor/8.png)

Botu çalıştırmak için fatedc.py dosyasını açmanız/çalıştırmanız yeterli
 Şu an botta olan komutlar şu şekilde:
 4 adet Fate zarı atmak için:
 >!zarat
 
 4 adet Fate zarına yanına eklenen - veya + değeri eklemek için:
 >!yzarat +x
 
 kaderoyunu.com'daki karakter özelliklerini alıp yazı kanalına resim olarak atmak için:
 >!karakterAl link
 
 Örnekler:
 
![GitHub Logo](/tutor/9.png)
