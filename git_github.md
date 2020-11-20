## **Ubuntu**
![git resim](https://github.com/selcukakarin/ToolBox/blob/master/resimler/git.png)
### **Git Yükleme**
`sudo apt-get update`

`sudo apt-get install git`

**git --version**

# **Git Komutlar**

GitHub adresinden bir projeyi yerel makinamıza çekip, değişiklikler yaptıktan sonra gönderene kadar hangi komutları giriyoruz hızlıca bakalım.

Üzerinde çalışacağımız proje eğer farklı bir repoda ise, projeyi fork seçeneği ile kendi repomuza çekiyoruz. Sonra kendi repomuz üzerinden bağlantısını kopyalıyoruz. Daha sonra makinamızda, projeyi kuracağımız dizinde, git bash ekranını açıyoruz.
(Eğer kendi reponuz üzerinden bir proje yürütmek istiyorsanız, Create a new repository seçeneği ile bir repo oluşturup onun bağlantısını kopyalayın.)

`$ git clone kopyalanan_link`

Proje artık yerel makinamızda olduğuna göre üzerinde çalışmaya başlayabiliriz. İlk önce cd projeadi komutu ile terminalde projenin içine giriyoruz. Bu işlemden sonra değişiklikleri kimin yaptığını bildirmek için isim ve mail adresi giriyoruz.
Bunu sadece ilk seferde, ilk kez git kullanıyorken yapıyoruz. Daha sonraki işlemlerde bu ayarları yapmamıza gerek yok.

`$ git config --global user.name "selçuk"`

`$ git config --global user.email "selcuk@gmail.com"`

Proje içerisinde farklı klasörlere giriş yapıp farklı dosyalar oluşturabiliriz veya olanı silebilir, güncelleme yapmak isteyebiliriz. Bu gibi değişiklikleri yaptıktan sonra, bash ekranına geçelim.

`$ git status` ile durumumuzu kontrol edelim. Yeni eklenen dosyalar kırmızı renk ile gösterilmektedir.

Şimdi bu dosyaları git’ e ekleyelim.

`$ git add index.html` şeklinde, sadece bir veya birkaç dosya ekleyebiliriz.

`$ git add .` ile dosyaların hepsi eklenir.

`$ git add .` ile (dosya, klasör) yaptığımız tüm değişiklikleri git’e ekliyoruz.

Genelde `$ git add .` ile tüm değişiklikleri ekleriz. Siz de bu komutu girin.

`$ git status` ile durumumuza bakalım. Sonradan eklenen dosyalar yeşil renk ile gösterilmektedir.

`$ git diff `ile de yaptığımız farklılıkları listeleyebiliriz (Eğer bu komutu çalıştırdıysanız **ctrl+z **ile farklılıklar listesinden çıkış yapabilirsiniz).

Şimdi commit ile git’e eklediğimiz dosyaları onaylayalım ve yaptığımız değişiklikler için bir mesaj ekleyelim.

`$ git commit -a ` tüm dosyaları commit etmektir.

`$ git commit -m "index sayfası değiştirildi"` değişikliği mesaj ile ilettik.

`$ git commit -am "index değiştirildi"` iki işlemi bir arada yapmış olduk. İki satır komut girmek yerine tek satır ile iki işlemi yaptık.

Ancak biz bir önceki adımda `$ git add .` ile tüm değişiklikleri eklediğimiz için şimdi `$ git commit -m "index sayfası değiştirildi"` formatında bir commit mesajı ekleyeceğiz.

Şimdi değişiklikleri GitHub’a gönderelim.

`$ git push origin master ` komutu ile GitHub üzerindeki projenin master dalına değişiklikleri gönderdik. Origin linki işaret eder. Tekrar link vermemek için kullanılır.

Burada proje bizim kendi repomuza eklenmiş oldu. Eğer bu yaptığımız değişiklikleri projenin esas sahibine ulaştırmak istiyorsak, GitHub üzerinde pull request seçeneği ile istek atıyoruz (Eğer kendi reponuzda çalıştıysanız bu işleme gerek yok. Sizin reponuzda projenin esas sahibi sizsiniz).

## Özetle

`$ git clone kopyalanan_link`

`$ git status`

`$ git add .`

`$ git commit -m "commit mesajı"`

`$ git push origin master`

### Projeyi Güncelleme

Github üzerinde projede değişiklikler olduğunda yerel makinamıza değişiklikleri çekmek için;

`$ git pull origin dal_ismi` GitHub üzerindeki dalı bizim yereldeki dala merge etmeyi sağlar. Güncellemeler olduğunda, yenilikleri elimizdeki projeye dahil etmek için bu komutu kullanırız.

### Dallanma
GitHub üzerindeki bir projeyi farklı bir dala çekmek için,

`$ git fetch` bu komutla, GitHub’daki değişiklikler farklı bir dala alınır.

`$ git merge FETCH_HEAD` bizim yereldeki master dalımıza projenin güncel halini ekledik. Yereldeki master dalının adı head.

`$ git branch ` mevcut dalları listeler.

`$ git branch Yenidal_ismi` yeni dal oluşturmak için isim verilir.

`$ git checkout Yenidal `master dalından Yenidal’a geçtik.

`$ git checkout -b Yenidal2_ismi `Yeni bir dal oluşturup geçiş yapmayı sağlar.

`$ git branch -d Yenidal `oluşturulan yeni dalı siler (Yerelde).

`$ git branch -dr Yenidal` oluşturulan yeni dalı siler (Yerelde ve GitHub’da).

(Silme işlemlerini yaparken master dalında olduğunuzdan emin olun.)

Farklı dallar oluşturup, bu dallarda projeleri farklı yapılandırabliriz. İki farklı dalı birleştirebiliriz.

`$ git merge Yenidal` ile Yenidal’daki değişiklikler master dalına aktarılıp birleştirildi. Yenidal ile ilgili işlem yapılacağı zaman master dalına geçmiş olmamız gerekir. Dolayısıyla birleştirme işlemi de master dalındayken yapılır.

### Silme
`git push origin :silinecek_dal_ismi `bu komut sayesinde uzak sunucudaki branch silinir.

`git reset --hard HEAD` komutu yerelde yapılan değişiklikleri silmek için kulanılır.

### Yerelde Proje Oluşturup Github’a Gönderme

Github hesabımızda proje için bir repository oluşturuyoruz. Aynı isimle yerelde bir proje klasörü oluşturduktan sonra; terminalde, proje dizininde;

`git init `komutunu çalıştıralım. Ardından reponun linkini kopyalayıp;

`git remote add origin https://github.com/kullanici_adi/repo.git `şeklinde repo ile bağlantıyı kuralım.

Projenizdeki değişiklikler için;

`git add . && git commit -m "ilk commit"` komutunu çalıştırdık.

`git push -u origin master `komutu ile projeyi repoya gönderdik.

İyi çalışmalar.
Daha detaylı bilgi için;
1) https://legacy.gitbook.com/book/vigo/git-puf-noktalari/details
2) https://aliozgur.gitbooks.io/git101/content/bolum_1_-_baslangic/versiyon__kontrolu_nedir.html
3) https://try.github.io/levels/1/challenges/1


## git önceki versiyona dönme işlemi
`git log   `--  (previous log )
`git checkout <gitlog dan dönen karakter dizini> .`    <------ nokta koyarsak projenin tamamı gelir. nokta yerine dosya ismi yazrsak sadece o dosyanın önceki versiyonu gelir

## git ssh işlemleri
1- Uç birim terminal ekranını açıyoruz.

2- Aşağıdaki satırdaki kodu yapıştırıp enter tuşuna basıyoruz.

`ssh-keygen -t rsa -b 4096 -C "eposta@adresiniz.com"`

3- Bu aşamada SSH anahtarının bulunduğu dosyanın nereye kaydedileceğini soruyor. Özel konum istemiyorsanız enter tuşuna basabilirsiniz. SSH için dizin oluşturulacaktır.
4- Bir anahtar kelime belirlememizi istiyor. Belirtmek istemiyorsanız enter tuşuna basarak geçebilirsiniz.
İşlem sonucunda dosya belirlediğiniz dizinde oluşturulur.
5- Şimdi sıra geldi SSH anahtar kodumuzu ekrana yazdırmaya. Bunun için şu komutu veriniz:

`cat  /.ssh/id_rsa.pub`
Kodu fareyle seçtikten sonra kopyala deyin.

Haydi bu kodu GitLab hesabımıza ekleyelim. 
6- GitLab.com 1 'da oturum açıyoruz.

7- Profil menüsünden Settings’e tıklıyoruz.
8- SSH Keys 'e tıklıyoruz.
9- Form’a hafızadaki kodu yapıştırıyoruz. Ardından Add key tuşuna basıyoruz.
SSH kodunu GitLab’a tanıttık.

10- Şimdi işlemin başarıyla gerçekleşip gerçekleşmediğini test edelim.

Uçbirim Terminal ekranında şu komutu verelim.

`ssh -T git@gitlab.com`


# Git Senaryo

## Özet Kodlar

### Git yükleme

terminal ekranı : `sudo apt-get install git` --> git'i yükle

terminal ekranı : `git --version` --> git için versiyon kontrolü yap

terminal ekranı : `git config --global user.name "Selçuk Akarın"` -- git global config ayarlarnı yap

terminal ekranı : `git config --global user.name` 

terminal ekranı : `git config --global user.email "selcukakarin@gmail.com"` 

terminal ekranı : `git config --global user.email`

### Proje dosyasını git dosyası olarak tanımlama
 
terminal ekranı : `pwd` --> bulunduğum dizini getir

terminal ekranı : `cd Desktop` 

selcuk@selcuk-VirtualBox: /Desktop$ `cd proje_dizin/` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git init` --> bulunduğum klasörü git reposu haline getir

### Git reposunda ekleme silme işlemleri

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls -a`  --> gizli dosyaları gösterir

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` --> tüm dosyaları staged area'ya yolla

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "ilk commit"` --> tüm dosyaları uzak repoya commit et

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log ` --> git'e atılan commitlerin loglarını getir

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` --> bulunduğum klasördeki dosyalar ile uzak repoyu karşılaştır.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add cikarma.py` --> cikarma.py dosyasını staged area'ya yolla

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "cikarma methodu eklendi."` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add carpma.py`  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add bolme.py ` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "bolme ve carpma dosyaları eklendi"` 

### Diff komutu

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff` --> dosyalarda yapılan değişiklikleri gösterir 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "ekleme yapıldı"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff cikarma.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff main.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff --staged`  --> staged area'daki dosyalardaki yapılan değişiklikleri gösterir

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "değişiklikler yapıldı."` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm carpma.py`  --> carpma.py dosyasını klasörden siler

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "carpma.py silindi"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm bolme.py`  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "bolme.py silindi" bolme.py silindi` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "klasör oluşturuldu"`

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm -r silinecekler/` --> silinecekler isimli klasör silindi 

**-r parametresi recursive anlamı taşır**

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "klasör silindi"` 

### Dosya İsimlendirme & Taşıma 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "cikarma.py --> deneme1.txt"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git mv deneme1.txt deneme2.txt` --> deneme1.txt ismi deneme2.txt ile değişir.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "deneme1.txt -> deneme2.txt` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git mv deneme2.txt dosyalar/` --> deneme2.txt dosyası dosyalar adlı klasöre taşındı

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "deneme2.txt -> dosyalar/deneme2.txt` 

### Versiyonlar arası geçiş işlemleri

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon1"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout -- index.py` --> index.py'de yapılan değişiklikler geri alındı (local)

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add index.py`  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git reset HEAD index.py` --> staged area'ya eklenen index.py'deki değişiklikler geri alındı

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout -- index.py` --> staged area'da yapılan geri alma işlemi local'e işlendi.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon2"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm dosya1.py dosya2.py`  --> dosya1.py ve dosya2.py silindi

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon3"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout d99a0b6db652c7e40b0f312522c0a6236aedb365 -- .` --> versiyon2 isimli commite geri dönüldü

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon2'den kopyalandı"` 

### Git reposunu github ile bağlama işlemi

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git remote add githubReposu https://github.com/selcukakarin/git-testing.git` --> git reposu github'daki repoya bağlandı (githubReposu alias gibi bir görev alır - takma isim)

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git remote` --> bağlantı kontrolü yapılır.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` --> yapılan değişiklikler github reposuna eklendi

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm dosya1.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "dosya1.py silindi"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

### .gitignore dosyası

**.gitignore'a tanımlanan dosyalar git tarafından görünmez oluyor. Yani veritabanı dosyası gibi git tarafından takip edilmesi istenmeyen

dosyaları gitignore'a tanımlamak gerekli.** 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `cat >> .gitignore` --> git .ignore oluşturuldu

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m ".gitignore eklendi"`

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `gedit .gitignore` -- .gitignore dosyası text editor ile açıldı.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status belgeler/` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "gitignore değiştirildi"` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git pull` --> github reposundaki projenin güncel hali local'e çekildi

### Branch kullanımı

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch` --> local'deki branch'ler listelendi

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch --all`  --> tüm branch'ler listelendi.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch yandal3` --> yandal3 isimli branch'e oluşturuldu

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout yandal3` --> yandal3 isimli branch'e geçiş yapıldı.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m yandal3'de dosya oluşturuldu --> dosya11.html` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout master` --> master branch'ine geçiş yapıldı

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff master yandal3` --> master ile yandal3 arasındaki branch'ler arasındaki farklar görüntülendi. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git merge yandal3` --> yandal3'deki değişiklikler master branch'ine eklendi.

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` --> master branchi yapılan değişikliklerle beraber github reposuna eklendi.

## Özet kodlar bitti

### git kurulumu ubuntu 

[git indir](https://git-scm.com/downloads) 

terminal ekranı : `sudo apt-get install git` 

terminal ekranı : `git --version` 

git version 2.17.1 

terminal ekranı : `git config --global user.name "Selçuk Akarın"` 

terminal ekranı : `git config --global user.name` 

Selçuk Akarın 

terminal ekranı : `git config --global user.name "Selçuk Akarın"` 

terminal ekranı : `git config --global user.name` 

sakarin@linkbilgisayar.com.tr 

### git projesi oluşturma 

terminal ekranı : `pwd` 

/home/selcuk 

terminal ekranı : `cd Desktop` 

selcuk@selcuk-VirtualBox: /Desktop$ `cd proje_dizin/` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git init` 

**gizli dosyaları görmek için ls komutuna -a parametresini veririz** 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls -a` 

.  ..  .git 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "ilk commit"` 

[master (root-commit) 267f9bf] ilk commit 

 1 file changed, 2 insertions(+) 

 create mode 100644 main.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log ` 

commit 267f9bfa26f3fcf3c4373fd951f20bf9304c5538 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:20:14 2019 +0300 

 

    ilk commit 

### Status komutu 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	cikarma.py 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add cikarma.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	new file:   cikarma.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "cikarma methodu eklendi."` 

[master 531935b] cikarma methodu eklendi. 

 1 file changed, 2 insertions(+) 

 create mode 100644 cikarma.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log ` 

commit 531935b859ea5a40d62138b1d9b42fdc4fe387dc (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:22:00 2019 +0300 

 

    cikarma methodu eklendi. 

 

commit 267f9bfa26f3fcf3c4373fd951f20bf9304c5538 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:20:14 2019 +0300 

 

    ilk commit 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

### Git iş akışı 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	bolme.py 

	carpma.py 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add carpma.py`  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	new file:   carpma.py 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	bolme.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add bolme.py ` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	new file:   bolme.py 

	new file:   carpma.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "bolme ve carpma dosyaları eklendi"` 

[master 55edccc] bolme ve carpma dosyaları eklendi 

 2 files changed, 4 insertions(+) 

 create mode 100644 bolme.py 

 create mode 100644 carpma.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 55edccc82095fb95edba06052f4e270de3ee57e9 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:24:47 2019 +0300 

 

    bolme ve carpma dosyaları eklendi 

 

commit 531935b859ea5a40d62138b1d9b42fdc4fe387dc 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:22:00 2019 +0300 

 

    cikarma methodu eklendi. 

 

commit 267f9bfa26f3fcf3c4373fd951f20bf9304c5538 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:20:14 2019 +0300 

 

    ilk commit 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	modified:   main.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff` 

diff --git a/main.py b/main.py 

index c9c5d9a..3862f49 100644 

--- a/main.py 

+++ b/main.py 

@@ -1,2 +1,4 @@ 

 def topla(x,y): 

        return x+y 

+def merhaba(): 

+       print("selam") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "ekleme yapıldı"` 

[master d4c04c6] ekleme yapıldı 

 1 file changed, 2 insertions(+) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit d4c04c63e83e1f579ad1dece18776479e37f0f4a (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:25:42 2019 +0300 

 

    ekleme yapıldı 

 

commit 55edccc82095fb95edba06052f4e270de3ee57e9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:24:47 2019 +0300 

 

    bolme ve carpma dosyaları eklendi 

 

commit 531935b859ea5a40d62138b1d9b42fdc4fe387dc 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:22:00 2019 +0300 

 

    cikarma methodu eklendi. 

 

commit 267f9bfa26f3fcf3c4373fd951f20bf9304c5538 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:20:14 2019 +0300 

 

    ilk commit 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	modified:   cikarma.py 

	modified:   main.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff` 

diff --git a/cikarma.py b/cikarma.py 

index c2a77e4..e69de29 100644 

--- a/cikarma.py 

+++ b/cikarma.py 

@@ -1,2 +0,0 @@ 

-def cikarma(x,y): 

-       return x-y 

diff --git a/main.py b/main.py 

index 3862f49..05e1b44 100644 

--- a/main.py 

+++ b/main.py 

@@ -1,4 +1,4 @@ 

-def topla(x,y): 

+def carpma(x,y): 

        return x+y 

 def merhaba(): 

        print("selam") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff cikarma.py` 

diff --git a/cikarma.py b/cikarma.py 

index c2a77e4..e69de29 100644 

--- a/cikarma.py 

+++ b/cikarma.py 

@@ -1,2 +0,0 @@ 

-def cikarma(x,y): 

-       return x-y 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff main.py` 

diff --git a/main.py b/main.py 

index 3862f49..05e1b44 100644 

--- a/main.py 

+++ b/main.py 

@@ -1,4 +1,4 @@ 

-def topla(x,y): 

+def carpma(x,y): 

        return x+y 

 def merhaba(): 

        print("selam") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff --staged` 

diff --git a/cikarma.py b/cikarma.py 

index c2a77e4..e69de29 100644 

--- a/cikarma.py 

+++ b/cikarma.py 

@@ -1,2 +0,0 @@ 

-def cikarma(x,y): 

-       return x-y 

diff --git a/main.py b/main.py 

index 3862f49..05e1b44 100644 

--- a/main.py 

+++ b/main.py 

@@ -1,4 +1,4 @@ 

-def topla(x,y): 

+def carpma(x,y): 

        return x+y 

 def merhaba(): 

        print("selam") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "değişiklikler yapıldı."` 

[master 378067e] değişiklikler yapıldı. 

 2 files changed, 1 insertion(+), 3 deletions(-) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ git log  

commit 378067e6602bdafec02eac3ef5392fecae720ee8 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:27:49 2019 +0300 

 

    değişiklikler yapıldı. 

 

commit d4c04c63e83e1f579ad1dece18776479e37f0f4a 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:25:42 2019 +0300 

 

    ekleme yapıldı 

 

commit 55edccc82095fb95edba06052f4e270de3ee57e9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:24:47 2019 +0300 

 

    bolme ve carpma dosyaları eklendi 

 

commit 531935b859ea5a40d62138b1d9b42fdc4fe387dc 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:22:00 2019 +0300 

 

    cikarma methodu eklendi. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add/rm <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	deleted:    carpma.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ Dosya silme 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm carpma.py`  

rm 'carpma.py' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	deleted:    carpma.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "carpma.py silindi"` 

[master bc43b16] carpma.py silindi 

 1 file changed, 2 deletions(-) 

 delete mode 100644 carpma.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit bc43b16cedc9acdc0e13090c55626addcd849c7c (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:29:20 2019 +0300 

 

    carpma.py silindi 

 

commit 378067e6602bdafec02eac3ef5392fecae720ee8 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:27:49 2019 +0300 

 

    değişiklikler yapıldı. 

 

commit d4c04c63e83e1f579ad1dece18776479e37f0f4a 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:25:42 2019 +0300 

 

    ekleme yapıldı 

 

commit 55edccc82095fb95edba06052f4e270de3ee57e9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:24:47 2019 +0300 

 

    bolme ve carpma dosyaları eklendi 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm bolme.py`  

rm 'bolme.py' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	deleted:    bolme.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "bolme.py silindi"[master 070d9f7] bolme.py silindi` 

 1 file changed, 2 deletions(-) 

 delete mode 100644 bolme.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "klasör oluşturuldu"` 

[master 26cd7ef] klasör oluşturuldu 

 2 files changed, 4 insertions(+) 

 create mode 100644 silinecekler/bir.py 

 create mode 100644 silinecekler/iki.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 26cd7ef30426189664c831e52808b0fdd4d1e8ec (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:30:39 2019 +0300 

 

    klasör oluşturuldu 

 

commit 070d9f74b9935bd3fc281db3e5f2e4c19d9e3a96 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:30:07 2019 +0300 

 

    bolme.py silindi 

 

commit bc43b16cedc9acdc0e13090c55626addcd849c7c 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:29:20 2019 +0300 

 

    carpma.py silindi 

 

commit 378067e6602bdafec02eac3ef5392fecae720ee8 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:27:49 2019 +0300 

 

    değişiklikler yapıldı. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls` 

cikarma.py  main.py  silinecekler 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm -r silinecekler/` 

rm 'silinecekler/bir.py' 

rm 'silinecekler/iki.py' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status`  

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	deleted:    silinecekler/bir.py 

	deleted:    silinecekler/iki.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "klasör silindi"` 

[master 14349d7] klasör silindi 

 2 files changed, 4 deletions(-) 

 delete mode 100644 silinecekler/bir.py 

 delete mode 100644 silinecekler/iki.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 14349d721c65570f48baaf04221b17a3bb397b5e (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:32:14 2019 +0300 

 

    klasör silindi 

 

commit 26cd7ef30426189664c831e52808b0fdd4d1e8ec 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:30:39 2019 +0300 

 

    klasör oluşturuldu 

 

commit 070d9f74b9935bd3fc281db3e5f2e4c19d9e3a96 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:30:07 2019 +0300 

 

    bolme.py silindi 

 

commit bc43b16cedc9acdc0e13090c55626addcd849c7c 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:29:20 2019 +0300 

 

    carpma.py silindi 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `Dosya İsimlendirme & Taşıma (mv)bash: syntax error near unexpected token 'mv'` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add/rm <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	deleted:    cikarma.py 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	deneme1.txt 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	renamed:    cikarma.py -> deneme1.txt 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "cikarma.py --> deneme1.txt"` 

[master 4612c72] cikarma.py --> deneme1.txt 

 1 file changed, 0 insertions(+), 0 deletions(-) 

 rename cikarma.py => deneme1.txt (100%) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git mv deneme1.txt deneme2.txt` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	renamed:    deneme1.txt -> deneme2.txt 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "deneme1.txt -> deneme2.txt` 

deneme1.txt -> deneme2.txt 

 1 file changed, 0 insertions(+), 0 deletions(-) 

 rename deneme1.txt => deneme2.txt (100%) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit ea895bd41259518a46fd3fcac933068534d87a35 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:36:31 2019 +0300 

 

    deneme1.txt -> deneme2.txt 

 

commit 4612c725970f8cf49d44dde706731f95e1d133b9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:35:34 2019 +0300 

 

    cikarma.py --> deneme1.txt 

 

commit 14349d721c65570f48baaf04221b17a3bb397b5e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:32:14 2019 +0300 

 

    klasör silindi 

 

commit 26cd7ef30426189664c831e52808b0fdd4d1e8ec 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:30:39 2019 +0300 

 

    klasör oluşturuldu 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git mv deneme2.txt dosyalar/` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	renamed:    deneme2.txt -> dosyalar/deneme2.txt 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "deneme2.txt -> dosyalar/deneme2.txt` 

[master df9e3bc] deneme2.txt -> dosyalar/deneme2.txt 

 1 file changed, 0 insertions(+), 0 deletions(-) 

 rename deneme2.txt => dosyalar/deneme2.txt (100%) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit df9e3bcf24c16835c193457668e1d4ed0250b96e (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:37:28 2019 +0300 

 

    deneme2.txt -> dosyalar/deneme2.txt 

 

commit ea895bd41259518a46fd3fcac933068534d87a35 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:36:31 2019 +0300 

 

    deneme1.txt -> deneme2.txt 

 

commit 4612c725970f8cf49d44dde706731f95e1d133b9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:35:34 2019 +0300 

 

    cikarma.py --> deneme1.txt 

 

commit 14349d721c65570f48baaf04221b17a3bb397b5e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:32:14 2019 +0300 

 

    klasör silindi 

### Değişikliği Geri Alma (Çalışma Dizini) 

bash: syntax error near unexpected token (' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	index.py 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon1"` 

[master 9026141] versiyon1 

 1 file changed, 2 insertions(+) 

 create mode 100644 index.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 90261419e0e458bd6e9e4e21eba2f6f19ac6b654 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:36:08 2019 +0300 

 

    versiyon1 

 

commit df9e3bcf24c16835c193457668e1d4ed0250b96e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:37:28 2019 +0300 

 

    deneme2.txt -> dosyalar/deneme2.txt 

 

commit ea895bd41259518a46fd3fcac933068534d87a35 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:36:31 2019 +0300 

 

    deneme1.txt -> deneme2.txt 

 

commit 4612c725970f8cf49d44dde706731f95e1d133b9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:35:34 2019 +0300 

 

    cikarma.py --> deneme1.txt 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	modified:   index.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout -- index.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add/rm <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	deleted:    index.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout -- index.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `ls` 

dosyalar  index.py  main.py 

### Değişikliği Geri Alma (Geçiş Bölgesi) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add index.py`  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	modified:   index.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git reset HEAD index.py` 

Unstaged changes after reset: 

M	index.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes not staged for commit: 

  (use "git add <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	modified:   index.py 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout -- index.py` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

### Versiyon Değiştirme 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 90261419e0e458bd6e9e4e21eba2f6f19ac6b654 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:36:08 2019 +0300 

 

    versiyon1 

 

commit df9e3bcf24c16835c193457668e1d4ed0250b96e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:37:28 2019 +0300 

 

    deneme2.txt -> dosyalar/deneme2.txt 

 

commit ea895bd41259518a46fd3fcac933068534d87a35 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:36:31 2019 +0300 

 

    deneme1.txt -> deneme2.txt 

 

commit 4612c725970f8cf49d44dde706731f95e1d133b9 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:35:34 2019 +0300 

 

    cikarma.py --> deneme1.txt 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon2"` 

[master d99a0b6] versiyon2 

 3 files changed, 8 insertions(+) 

 create mode 100644 dosya1.py 

 create mode 100644 dosya2.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit d99a0b6db652c7e40b0f312522c0a6236aedb365 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:41:04 2019 +0300 

 

    versiyon2 

 

commit 90261419e0e458bd6e9e4e21eba2f6f19ac6b654 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:36:08 2019 +0300 

 

    versiyon1 

 

commit df9e3bcf24c16835c193457668e1d4ed0250b96e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:37:28 2019 +0300 

 

    deneme2.txt -> dosyalar/deneme2.txt 

 

commit ea895bd41259518a46fd3fcac933068534d87a35 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:36:31 2019 +0300 

 

    deneme1.txt -> deneme2.txt 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm dosya1 dosya2` 

fatal: pathspec 'dosya1' did not match any files 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm dosya1.py dosya2.py`  

rm 'dosya1.py' 

rm 'dosya2.py' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon3"` 

[master f77faba] versiyon3 

 3 files changed, 1 insertion(+), 9 deletions(-) 

 delete mode 100644 dosya1.py 

 delete mode 100644 dosya2.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit f77fabadf880825c0ee8a31c1c3101a128ca026d (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:41:54 2019 +0300 

 

    versiyon3 

 

commit d99a0b6db652c7e40b0f312522c0a6236aedb365 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:41:04 2019 +0300 

 

    versiyon2 

 

commit 90261419e0e458bd6e9e4e21eba2f6f19ac6b654 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:36:08 2019 +0300 

 

    versiyon1 

 

commit df9e3bcf24c16835c193457668e1d4ed0250b96e 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 17:37:28 2019 +0300 



    deneme2.txt -> dosyalar/deneme2.txt 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout d99a0b6db652c7e40b0f312522c0a6236aedb365 -- .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Changes to be committed: 

  (use "git reset HEAD <file..." to unstage) 

 

	new file:   dosya1.py 

	new file:   dosya2.py 

	modified:   index.py 

 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "versiyon2'den kopyalandı"` 

[master 54f8a44] versiyon2'den kopyalandı 

 3 files changed, 9 insertions(+), 1 deletion(-) 

 create mode 100644 dosya1.py 

 create mode 100644 dosya2.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

nothing to commit, working tree clean 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git log`  

commit 54f8a44daff97477e57dad5e08152416ce0571c5 (HEAD -> master) 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:42:55 2019 +0300 

 

    versiyon2'den kopyalandı 

 

commit f77fabadf880825c0ee8a31c1c3101a128ca026d 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:41:54 2019 +0300 

 

    versiyon3 

 

commit d99a0b6db652c7e40b0f312522c0a6236aedb365 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:41:04 2019 +0300 

 

    versiyon2 

 

commit 90261419e0e458bd6e9e4e21eba2f6f19ac6b654 

Author: Selçuk Akarın <sakarin@linkbilgisayar.com.tr> 

Date:   Wed Dec 11 19:36:08 2019 +0300 

 

    versiyon1 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git remote add githubReposu https://github.com/selcukakarin/git-testing.git` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git remote` 

githubReposu 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

Username for 'https://github.com': selcukakarin 

Password for 'https://selcukakarin@github.com':  

Counting objects: 41, done. 

Delta compression using up to 4 threads. 

Compressing objects: 100% (32/32), done. 

Writing objects: 100% (41/41), 4.17 KiB | 1.04 MiB/s, done. 

Total 41 (delta 6), reused 0 (delta 0) 

remote: Resolving deltas: 100% (6/6), done. 

To https://github.com/selcukakarin/git-testing.git 

 * [new branch]      master -> master 

Branch 'master' set up to track remote branch 'master' from 'githubReposu'. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git rm dosya1.py`  

rm 'dosya1.py' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "dosya1.py silindi"` 

[master 168705e] dosya1.py silindi 

 1 file changed, 3 deletions(-) 

 delete mode 100644 dosya1.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

Username for 'https://github.com': selcukakarin 

Password for 'https://selcukakarin@github.com':  

Counting objects: 2, done. 

Delta compression using up to 4 threads. 

Compressing objects: 100% (2/2), done. 

Writing objects: 100% (2/2), 245 bytes | 245.00 KiB/s, done. 

Total 2 (delta 1), reused 0 (delta 0) 

remote: Resolving deltas: 100% (1/1), completed with 1 local object. 

To https://github.com/selcukakarin/git-testing.git 

   54f8a44..168705e  master -> master 

Branch 'master' set up to track remote branch 'master' from 'githubReposu'. 

### .gitignore kullanımı 

**.gitignore'a tanımlanan dosyalar git tarafından görünmez oluyor. Yani veritabanı dosyası gibi git tarafından takip edilmesi istenmeyen

dosyaları gitignore'a tanımlamak gerekli.** 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Your branch is up to date with 'githubReposu/master'. 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	"veritaban\304\261.py" 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Your branch is up to date with 'githubReposu/master'. 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	veritabani.py 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `cat >> .gitignore` 

veritabani.py 

^C 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `cat .gitignore`  

veritabani.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Your branch is up to date with 'githubReposu/master'. 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	.gitignore 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m ".gitignore eklendi"` 

[master 94aa520] .gitignore eklendi 

 1 file changed, 1 insertion(+) 

 create mode 100644 .gitignore 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `gedit .gitignore` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

On branch master 

Your branch is ahead of 'githubReposu/master' by 1 commit. 

  (use "git push" to publish your local commits) 

 

Changes not staged for commit: 

  (use "git add <file..." to update what will be committed) 

  (use "git checkout -- <file..." to discard changes in working directory) 

 

	modified:   .gitignore 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	belgeler/ 

 

no changes added to commit (use "git add" and/or "git commit -a") 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status belgeler/` 

On branch master 

Your branch is ahead of 'githubReposu/master' by 1 commit. 

  (use "git push" to publish your local commits) 

 

Untracked files: 

  (use "git add <file..." to include in what will be committed) 

 

	belgeler/dosya1.html 

 

nothing added to commit but untracked files present (use "git add" to track) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m "gitignore değiştirildi"` 

[master 574ec32] gitignore değiştirildi 

 2 files changed, 4 insertions(+) 

 create mode 100644 belgeler/dosya1.html 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

Username for 'https://github.com': selcukakarin 

Password for 'https://selcukakarin@github.com':  

Counting objects: 7, done. 

Delta compression using up to 4 threads. 

Compressing objects: 100% (4/4), done. 

Writing objects: 100% (7/7), 766 bytes | 766.00 KiB/s, done. 

Total 7 (delta 1), reused 0 (delta 0) 

remote: Resolving deltas: 100% (1/1), done. 

To https://github.com/selcukakarin/git-testing.git 

   168705e..574ec32  master -> master 

Branch 'master' set up to track remote branch 'master' from 'githubReposu'. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$  

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git pull` 

remote: Enumerating objects: 7, done. 

remote: Counting objects: 100% (7/7), done. 

remote: Compressing objects: 100% (6/6), done. 

remote: Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 

Unpacking objects: 100% (6/6), done. 

From https://github.com/selcukakarin/git-testing 

   fb7d0ff..9c84fcc  master     -> githubReposu/master 

Updating fb7d0ff..9c84fcc 

Fast-forward 

 README.md                               |  13 +++++++++++++ 

 Screenshot from 2019-12-11 12-29-59.png | Bin 0 -> 326539 bytes 

 2 files changed, 13 insertions(+) 

 create mode 100644 README.md 

 create mode 100644 Screenshot from 2019-12-11 12-29-59.png 

 ## branches

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch` 

x master 

  yandal2 

**uzak git reposundaki dalları görmek için git branch komutuna --all parametresi geçilmelidir.** 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch --all` 

x master 

  yandal2 

  remotes/githubReposu/master 

  remotes/githubReposu/yandal1 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch yandal3` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch` 

x master 

  yandal2 

  yandal3 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout yandal3` 

Switched to branch 'yandal3' 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git branch` 

  master 

  yandal2 

x yandal3 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git add .` 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git status` 

O n branch yandal3 

Changes to be committed: 

  (use "git reset HEAD <file.. to unstage) 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git commit -m yandal3'de dosya oluşturuldu --> dosya11.html` 

yandal3'de dosya oluşturuldu --> dosya11.html 

 1 file changed, 1 insertion(+) 

 create mode 100644 dosya11.html 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git checkout master` 

Switched to branch 'master' 

Your branch is up to date with 'githubReposu/master'. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ ls 

 belgeler       dosyalar   README.md                                  yandal2 

 dosya10.html   index.py  'Screenshot from 2019-12-11 12-29-59.png' 

 dosya2.py      main.py    veritabani.py 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ git diff 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ git diff master yandal 

fatal: ambiguous argument 'yandal': unknown revision or path not in the working tree. 

Use '--' to separate paths from revisions, like this: 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git diff master yandal3` 

diff --git a/dosya11.html b/dosya11.html 

new file mode 100644 

index 0000000..c48cc00 

--- /dev/null 

+++ b/dosya11.html 

@@ -0,0 +1 @@ 

+yandal1 tarafından oluşturuldu. 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git merge yandal3` 

Updating 9c84fcc..b7da90d 

Fast-forward 

 dosya11.html | 1 + 

 1 file changed, 1 insertion(+) 

 create mode 100644 dosya11.html 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ ls 

 belgeler       dosyalar   'Screenshot from 2019-12-11 12-29-59.png' 

 dosya10.html   index.py    veritabani.py 

 dosya11.html   main.py     yandal2 

 dosya2.py      README.md 

selcuk@selcuk-VirtualBox: /Desktop/proje_dizin$ `git push -u githubReposu master` 

Username for 'https://github.com': selcukakarin 

Password for 'https://selcukakarin@github.com':  

Counting objects: 2, done. 

Delta compression using up to 4 threads. 

Compressing objects: 100% (2/2), done. 

Writing objects: 100% (2/2), 274 bytes | 274.00 KiB/s, done. 

Total 2 (delta 1), reused 0 (delta 0) 

remote: Resolving deltas: 100% (1/1), completed with 1 local object. 

To https://github.com/selcukakarin/git-testing.git 

   9c84fcc..b7da90d  master -> master 

Branch 'master' set up to track remote branch 'master' from 'githubReposu'. 


### Önemli kodlar

selcuk@selcuk-Latitude-6430U:~/Desktop/repos/selcuk/git-testing$ `git branch --all`

selcuk@selcuk-Latitude-6430U:~/Desktop/repos/selcuk/git-testing$ `git branch -a`

[kaynak](https://stackoverflow.com/questions/10312521/how-to-fetch-all-git-branches)

You can fetch all branches from all remotes like this:

selcuk@selcuk-Latitude-6430U:~/Desktop/repos/selcuk/git-testing$ `git fetch --all `

`git fetch --all` and `git remote update` are equivalent.

selcuk@selcuk-Latitude-6430U:~/Desktop/repos/selcuk/git-testing$ `git branch`


`git pull --all # To update local branches which track remote branches:` 

However, this can be still insufficient. It will work only for your local branches which track remote branches. To track all remote branches execute this oneliner BEFORE git pull --all:

`git branch -r` | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done



`git init `komutunu çalıştıralım. Ardından reponun linkini kopyalayıp;

`git remote add origin https://github.com/kullanici_adi/repo.git `şeklinde repo ile bağlantıyı kuralım.

Projenizdeki değişiklikler için;

`git add . && git commit -m "ilk commit"` komutunu çalıştırdık.

`git push -u origin master `komutu ile projeyi repoya gönderdik.

`ls -a`  # hidden file ile göster

`git add .` # staging areaya yolla

`git commit -m "ilk commit"` # commit at

`git status`

`git push origin :silinecek_dal_ismi `bu komut sayesinde uzak sunucudaki branch silinir.

`git reset --hard HEAD` komutu yerelde yapılan değişiklikleri silmek için kulanılır.

`$ git checkout -b Yenidal2_ismi `Yeni bir dal oluşturup geçiş yapmayı sağlar.

`$ git branch -d Yenidal `oluşturulan yeni dalı siler (Yerelde).

`$ git branch -dr Yenidal` oluşturulan yeni dalı siler (Yerelde ve GitHub’da).

If you want to see which files will be deleted you can use the -n option before you run the actual command:

`git clean -n`

Then when you are comfortable (because it will delete the files for real!) use the -f option

`git clean -f`

Here are some more options for you to delete directories, files, ignored and non-ignored files

To remove directories, run `git clean -f -d or git clean -fd`

To remove ignored files, run `git clean -f -X or git clean -fX`

To remove ignored and non-ignored files, run `git clean -f -x or git clean -fx`


Local olarak branch silme komutu :
git branch -d yandal2
Github daki branchi kalıcı olarak silme komutu :
git push --delete githubRepo yandal2

## Git delete branch (remote or local)

[Source](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely)

Executive Summary
```
$ git push -d <remote_name> <branch_name>
$ git branch -d <branch_name>
```
Note that in most cases the remote name is origin. In such a case you'll have to use the command like so.
```
$ git push -d origin <branch_name>
```
Delete Local Branch
To delete the local branch use one of the following:
```
$ git branch -d branch_name
$ git branch -D branch_name
```
Note: The -d option is an alias for --delete, which only deletes the branch if it has already been fully merged in its upstream branch. You could also use -D, which is an alias for --delete --force, which deletes the branch "irrespective of its merged status." [Source: man git-branch]
