[kaynak](https://www.pythontr.com/makale/docker-container-nedir-ne-ise-yarar-668)

Docker Container kullanımı hakkında ipuçları
Docker Container Nedir?
Docker Container uygulamaların çalıştırıldığı ortamlar olarak tanımlayabiliriz.


Örnek Nginx Uygulaması Oluşturulması ve Çalıştırılması

docker container run --publish 80:80 nginx
docker container run -p 80:80 --name nginx2 -d nginx
#belirli bir version uygulama indirmek ve çalıştırmak için
docker container run -p 80:80 --name nginx2 -d nginx:1.12
docker container run -p 33306:3306 --name database mariadb
image'lar esasen uygulamalardır daha önce kullandığınız bir image yoksa docker bunu kendi sitesi "hub.docker.com" üzerinden indirir. Bu konu daha detaylı bir konu olacağı için ileride bir yazı yazmayı düşünüyorum.

Komut satırındaki publish parametresindeki değerler 80:80 ve 3306:3306 numaraları in ve out port numaralarıdır. Bunlar uygulama içinden ve dışından yönlendirelecek port numaralarını gösterir.

--name parametresi uygulamaya isim vermek istiyorsak kullanabileceğimiz bir paremtredir.

-d yada --detach parametresi nginx i arka planda çalıştırmak için kullanılır. Bu paramtre kullanıldığında bize uniq bir değer döner.


Container Listeleme
docker container ls containerları listeler. docker container ls -a ise tüm containerları listeler.


Container Loglarını Görüntüleme
-d veya --detach parametresini kullanmadığımız zaman logları normal şartlarda görebiliyoruz, fakat bu parametreleri kullandığımız zaman arka planda çalışacakları için docker container logs container_ismi şeklinde görüntülememiz gerekir.


docker container logs container_ismi
Container'ın hangi aşamalarda geçtiğini görmek için ise docker container top container_ismi şeklinde bir kullanım yapabiliriz.


docker container top container_ismi
Çalışan Container'ı Durdurma

docker container stop container_ismi
Container Silme

docker container rm container_ismi1  container_ismi2 
# yada
docker container rm container_ismi1  container_id
Container id üzerinden silme işlemi yapmak istiyorsanız ilk üç harf yada karakteri girmeniz yeterli olacaktır.


Bütün durdurulmuş container'ları silmek için
docker container prune
Container üzerinde çalışan prosesslerin gösterilmesi
docker container top container_ismi
Container kofigürasyon dosyasının incelenmesi
docker container inspect container_ismi
Container'ların cpu ve memory kullanımları
docker container stats container_ismi
stats parametresi için container_ismi opsiyoneldir kullanılmadığı takdirde bütün aktif conteynarları döner.


Docker Container Bağlanma
Bağlantı yapabilememiz için -it parametrelerini kullanırız -i parametresi kurduğumuz bağlantıyı açık tutmamıza yarar, -t parametreside tty yani terminali kurmamızı sağlar.


docker container run -it --name container_ismi nginx bash
nginx linux distribition olduğu için bash komutu ile çalıştırabiliriz.

Durmuş bir container a tekrar bağlanmak için start parametresiyle birlikte attach parametresini kullanırız.


docker container start -ai container_ismi
Bu kod bu konteynerı başlat ve proxy_test'i attach etmesini sağlar.


docker container run -it --name container_ismi debian
Debian conteiner tekrar kullanmak için.


docker container start -ai container_ismi
Çalışan bir container'a bağlanma

docker container exec -it proxy bash
Docker Network

Container hangi portları kullandığını öğrenmek için
docker container port container_ismi
Network'ün listelenmesi
docker network ls
docker network inspect
Yeni bir network katmanı oluşturulması
docker network create network_ismi
Docker network için container bağlanması
docker network connect network_ismi container_ismi
Docker network için bağlı container'ı network ten çıkarma
docker network disconnect network_ismi container_ismi
network alias
Network alias containerlar'ı network üzerinden birbirine bağlamada kullanacağımız isimlendirme için kullanırız. Bu özellikle container'lara load balance özelliği vermek için birebirdir. Container oluştururken isim üzerinden gideceğimiz için port belirtmemize gerek yoktur. Domain name olarak düşünebiliriz.

Aşağıda işleyeceğimiz örnek ile bir centos contaynerı üzerinden bir adet nginx ve bir adet apache için çağrı yapalım. Debian'cı biriyim neden Centos diyebilirsiniz Centos içerisinde curl yüklü geliyor. Bazen güvenlikten dolayı apt komutları ofis ortamlarında çalışmayabiliyor uğraşmayın.


docker network create pythontr
docker container run -d --network pythontr --network-alias webserver nginx
docker container run -d --network pythontr --network-alias webserver apache2
docker container run -it --network pythontr centos:7
Şimdi curl komutu ile hangi sunucuların nasıl çalıştığını görebiliriz.


curl webserver