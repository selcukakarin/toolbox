[Docker CLI Commands](https://docs.docker.com/engine/reference/commandline/rm/)

## For Linux

### Kurulum için önce aşağıdaki iki komutu çalışıtırıyoruz.
```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```
### If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like

### permission hatasını çözmek için çalışıtırılması gereken kod
```  sudo usermod -aG docker selcuk ```
### daha sonra https://docs.docker.com/machine/install-machine/ linkinde gösterildiği gibi aşağıdaki komut çalıştırılır. docker_machine
```
base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo mv /tmp/docker-machine /usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine
```
### daha sonra https://docs.docker.com/compose/install/ linkinde gösterildiği gibi aşağıdaki kodlar çalıştırılır. docker_compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
### Ardından kontrol için aşağıdaki kodlar çalıştırılır
```
# permission hatası alınırsa başına sudo konarak çalıştırılır.
docker version
docker-compose version
docker-machine version
```
### container'ları listelemek için
```
sudo docker image ls
```

```
docker info

docker
```
### bizim örneğimizdeki image_name=nginx ile localde nginx'i arıyor bulamazsa hub.docker.com'dan indiriyor. Var ise nginx server'ini çalıştıracak.
```
docker container run --publish [local_port]:[virtual_port] [image_name]

selcuk@selcuk-Inspiron-7577:~$ docker container run --publish 80:80 nginx

```
### container'ımızın ( muhtemelen image_id ) idsini öğrenmek için - Conteiner çalıştır ve id'sini dön
### -d veya - detach bize id'yi döner ve arka planda çalışır vaziyette gelmesini sağlar.
```
selcuk@selcuk-Inspiron-7577:~$ docker container run --publish 80:80 --detach nginx
e9d2e4acd99142a7581a4ea9912ea05239854b542cf177efacb85c6e53550fe9
```
### container eventları için
```
selcuk@selcuk-Inspiron-7577:~$ docker container + [tab]
attach   create   export   logs     port     restart  start    top      wait     
commit   diff     inspect  ls       prune    rm       stats    unpause  
cp       exec     kill     pause    rename   run      stop     update   
```
### container listesine ulaşmak için
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
e9d2e4acd991        nginx               "nginx -g 'daemon of…"   3 minutes ago       Up 3 minutes        0.0.0.0:80->80/tcp   quizzical_gates
```
### top komutu ile çalışan processlere ulaşılır.
```
docker container top [image_name]

selcuk@selcuk-Inspiron-7577:~$ docker container top quizzical_gates
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                13885               13863               0                   13:11               ?                   00:00:00            nginx: master process nginx -g daemon off;
systemd+            13920               13885               0                   13:11               ?                   00:00:00            nginx: worker process
```
### çalışan container'ı kapatmak için
```
selcuk@selcuk-Inspiron-7577:~$ docker container stop quizzical_gates 
quizzical_gates

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### önceden kapatılmış olan container'ları görmek için
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS                         PORTS               NAMES
643767f50507        nginx                              "nginx -g 'daemon of…"   5 minutes ago       Created                                            eloquent_tereshkova
e9d2e4acd991        nginx                              "nginx -g 'daemon of…"   About an hour ago   Exited (0) 46 seconds ago                          quizzical_gates
cac968d15c5d        nginx                              "nginx -g 'daemon of…"   About an hour ago   Exited (0) About an hour ago                       gifted_roentgen
```
### container'ları silmek için
```
selcuk@selcuk-Inspiron-7577:~$ docker container rm 6437 e9d2
6437
e9d2

selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS                         PORTS               NAMES
cac968d15c5d        nginx                              "nginx -g 'daemon of…"   About an hour ago   Exited (0) About an hour ago                       gifted_roentgen
```
### Remove all stopped containers
```
selcuk@selcuk-Inspiron-7577:~$ docker rm $(docker ps -a -q)
cac968d15c5d
4fa266e1d43b
b91df1647d69
e3192b896940
38080bf35aa0
395781d636a0
8cd72de6d0cd
bd6dcfdd3f43
14fc9e58e6e2
d932afd57652
09c0e9eb39e1
5f56b7d066fb
e7db501742fc
8fd55750c810
5f8b583c5647
833a19c41033
17f2565624c4
9b632f5bfb09
5eebb8ac573b
767fc3b6faa6

selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### isim vererek container oluşturma
```
selcuk@selcuk-Inspiron-7577:~$ docker container run --publish 80:80 --detach --name webDjango nginx
5504a90de8b9ce52ba9ee7d0c85bca1523e157d4140e76b8c7034077a905ea24

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
5504a90de8b9        nginx               "nginx -g 'daemon of…"   6 seconds ago       Up 4 seconds        0.0.0.0:80->80/tcp   webDjango
```
### container loglarını çekme
```
selcuk@selcuk-Inspiron-7577:~$ docker container top webDjango   # processleri görmek için
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                18967               18944               0                   14:23               ?                   00:00:00            nginx: master process nginx -g daemon off;
systemd+            18999               18967               0                   14:23               ?                   00:00:00            nginx: worker process

selcuk@selcuk-Inspiron-7577:~$ docker container 
attach   cp       diff     export   kill     ls       port     rename   rm       start    stop     unpause  wait     
commit   create   exec     inspect  logs     pause    prune    restart  run      stats    top      update   

selcuk@selcuk-Inspiron-7577:~$ docker container logs webDjango 
172.17.0.1 - - [14/Apr/2020:11:24:55 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36" "-"
172.17.0.1 - - [14/Apr/2020:11:24:56 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36" "-"
```
### çalışan container silinemez
```
selcuk@selcuk-Inspiron-7577:~$ docker rm 55
Error response from daemon: You cannot remove a running container 5504a90de8b9ce52ba9ee7d0c85bca1523e157d4140e76b8c7034077a905eing removal or force remove
selcuk@selcuk-Inspiron-7577:~$ docker stop 55
55
selcuk@selcuk-Inspiron-7577:~$ docker rm 55
55
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### docker container help komutu
```
selcuk@selcuk-Inspiron-7577:~$ docker container --help

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
```
### bir container'da mongo db çalıştırma
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d --name db -p 27017:27017 mongo
Unable to find image 'mongo:latest' locally
latest: Pulling from library/mongo
5bed26d33875: Pull complete 
f11b29a9c730: Pull complete 
930bda195c84: Pull complete 
78bf9a5ad49e: Pull complete 
3d7fb3809884: Pull complete 
a7237292ff8a: Pull complete 
c936e28b5159: Pull complete 
3fb56b127f30: Pull complete 
c54a0478af29: Pull complete 
ffc3a4dd1cdc: Pull complete 
236ffdb10499: Pull complete 
c33efe03b109: Pull complete 
1d3609ce2ac9: Pull complete 
Digest: sha256:1e33093260855e83baee0237e29947e243818c58a1d37b1022909e227f624d7a
Status: Downloaded newer image for mongo:latest
501b57d5f43e52e194fcab04e21e05186eb970a78b8f5db6e7502ac71926a28b
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
501b57d5f43e        mongo               "docker-entrypoint.s…"   15 seconds ago      Up 14 seconds       0.0.0.0:27017->27017/tcp   db
```
### container'ın özelliklerini detaylıca incelemek için
```
docker container inspect db
```
### container istatistiklerini görebilmek için - anlık veri akışı -kaynak tüketimleri
```
docker container stats

CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
e642736d0c2e        nginx               0.00%               2.93MiB / 15.51GiB    0.02%               6.21kB / 0B         0B / 0B             2
501b57d5f43e        db                  0.49%               71.45MiB / 15.51GiB   0.45%               9.1kB / 0B          0B / 913kB          32
```
### belli bir container'a ait istatistikler için 
```
docker container stats db
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
501b57d5f43e        db                  0.74%               71.46MiB / 15.51GiB   0.45%               10.8kB / 0B         0B / 1.16MB         32
```
### çalışan container'lara ait bazı bilgiler
```
selcuk@selcuk-Inspiron-7577:~$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
e642736d0c2e        nginx               "nginx -g 'daemon of…"   5 minutes ago       Up 5 minutes        0.0.0.0:80->80/tcp         nginx
501b57d5f43e        mongo               "docker-entrypoint.s…"   6 minutes ago       Up 6 minutes        0.0.0.0:27017->27017/tcp   db
```
### ws isimli bir nginx container'ı aç ve linux bash komutlarını çalıştırabileceğimiz bir terminal ver.
### t, --tty = Allocate a pseudo-TTY = TTY bağlantısı aç ( SSH gibi bağlanıp komut çalıştırmayı sağlar. )
### i, --interactive = Keep STDIN open even if not attached = container'ı oluşturup bağlandıktan sonra kapanma komut çalıştıracağım demek.
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -it --name ws nginx bash
root@d3baf6509c44:/# ls -al
total 72
drwxr-xr-x   1 root root 4096 Apr 14 11:45 .
drwxr-xr-x   1 root root 4096 Apr 14 11:45 ..
-rwxr-xr-x   1 root root    0 Apr 14 11:45 .dockerenv
drwxr-xr-x   2 root root 4096 Mar 27 00:00 bin
drwxr-xr-x   2 root root 4096 Feb  1 17:09 boot
drwxr-xr-x   5 root root  360 Apr 14 11:45 dev
drwxr-xr-x   1 root root 4096 Apr 14 11:45 etc
drwxr-xr-x   2 root root 4096 Feb  1 17:09 home
drwxr-xr-x   1 root root 4096 Mar 31 03:19 lib
drwxr-xr-x   2 root root 4096 Mar 27 00:00 lib64
drwxr-xr-x   2 root root 4096 Mar 27 00:00 media
drwxr-xr-x   2 root root 4096 Mar 27 00:00 mnt
drwxr-xr-x   2 root root 4096 Mar 27 00:00 opt
dr-xr-xr-x 325 root root    0 Apr 14 11:45 proc
drwx------   2 root root 4096 Mar 27 00:00 root
drwxr-xr-x   3 root root 4096 Mar 27 00:00 run
drwxr-xr-x   2 root root 4096 Mar 27 00:00 sbin
drwxr-xr-x   2 root root 4096 Mar 27 00:00 srv
dr-xr-xr-x  13 root root    0 Apr 14 11:45 sys
drwxrwxrwt   1 root root 4096 Mar 31 03:19 tmp
drwxr-xr-x   1 root root 4096 Mar 27 00:00 usr
drwxr-xr-x   1 root root 4096 Mar 27 00:00 var
root@d3baf6509c44:/# exit
exit
# exit'ten sonra container detach ile başlatılmadığı için durdu.
```
### ubuntu container'ı oluşturma
```
docker container run -it --name ubuntuName ubuntu bash
```
### oluşturulan ubuntu container'ı ubuntunun çok basic bir distrosu olduğu için curl'ü yüklememiz gerekiyor.
```
apt-get update
apt-get install curl
```
### amazona curl ile istek attık ve boş bir html response aldık.
```
root@f67856cb7161:/# curl amazon.com
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>Server</center>
</body>
</html>
root@f67856cb7161:/# exit
exit

docker container start --help
-a, --attach               Attach STDOUT/STDERR and forward signals
```
### var olan container'ı yeniden çalıştırıp buna bağlanmak.
```
docker container start -ai ubuntuName 
```
### hali hazırda çalışan normal oluşturulmuş bir container'a bağlanmak.
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d --name ng nginx
109dcd74562e2b80d5f02119d30fc01d3425036b08b6fae902f18c64bfcdf8fe

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
109dcd74562e        nginx               "nginx -g 'daemon of…"   6 seconds ago       Up 4 seconds        80/tcp              ng

selcuk@selcuk-Inspiron-7577:~$ docker container exec -it ng bash

root@109dcd74562e:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

root@109dcd74562e:/# exit
exit
```
### şu anda halen container'ımızı çalışmakta çünkü burda biz sadece bağlandık. Çalıştır komutu dışarda detach olarak verilmişti.
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
109dcd74562e        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute   80/tcp              ng
```
### environment variable'ları configüre edilmiş bir mongodb hazırlamak
### -e environment variable tanımlamak için kullandık.
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d -p 27017:27017 --name db -e MONGO_INITDB_ROOT_USERNAME=selcuk -e MONGO_INITDB_ROOT_PASSWORD=123 mongo
ebd62760e1e91f7d2ffe24018630ac67bf59e75bd50e4260daae3c8be0883bfa
```
### apache server (httpd) ile docker container oluşturmak
```
docker container run -d --name webserver -p 8080:80 httpd
```
### çoklu docker container kapatma
```
selcuk@selcuk-Inspiron-7577:~$ docker container stop webserver proxy db
webserver
proxy
db

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### çoklu container silme
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                         PORTS               NAMES
16f9edabfa0a        httpd               "httpd-foreground"       2 minutes ago       Exited (0) 50 seconds ago                          webserver
883d04acc5f5        node                "docker-entrypoint.s…"   3 minutes ago       Exited (0) 3 minutes ago                           server
f5deb6beebf4        nginx               "nginx -g 'daemon of…"   7 minutes ago       Exited (0) 51 seconds ago                          proxy
ebd62760e1e9        mongo               "docker-entrypoint.s…"   About an hour ago   Exited (0) 51 seconds ago                          db
109dcd74562e        nginx               "nginx -g 'daemon of…"   2 hours ago         Exited (0) About an hour ago                       ng
f67856cb7161        ubuntu              "bash"                   2 hours ago         Exited (0) About an hour ago                       ubuntuName
1963a7be8b93        bash                "docker-entrypoint.s…"   2 hours ago         Exited (127) 2 hours ago                           ubuntu
d3baf6509c44        nginx               "bash"                   2 hours ago         Exited (0) 2 hours ago                             ws
selcuk@selcuk-Inspiron-7577:~$ docker container rm webserver server
webserver
server

selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                          PORTS               NAMES
f5deb6beebf4        nginx               "nginx -g 'daemon of…"   8 minutes ago       Exited (0) About a minute ago                       proxy
ebd62760e1e9        mongo               "docker-entrypoint.s…"   About an hour ago   Exited (0) About a minute ago                       db
109dcd74562e        nginx               "nginx -g 'daemon of…"   2 hours ago         Exited (0) About an hour ago                        ng
f67856cb7161        ubuntu              "bash"                   2 hours ago         Exited (0) About an hour ago                        ubuntuName
1963a7be8b93        bash                "docker-entrypoint.s…"   2 hours ago         Exited (127) 2 hours ago                            ubuntu
d3baf6509c44        nginx               "bash"                   2 hours ago         Exited (0) 2 hours ago                              ws
```
### tüm kapalı container'ları silmek için - prune
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                          PORTS               NAMES
f5deb6beebf4        nginx               "nginx -g 'daemon of…"   8 minutes ago       Exited (0) About a minute ago                       proxy
ebd62760e1e9        mongo               "docker-entrypoint.s…"   About an hour ago   Exited (0) About a minute ago                       db
109dcd74562e        nginx               "nginx -g 'daemon of…"   2 hours ago         Exited (0) About an hour ago                        ng
f67856cb7161        ubuntu              "bash"                   2 hours ago         Exited (0) About an hour ago                        ubuntuName
1963a7be8b93        bash                "docker-entrypoint.s…"   2 hours ago         Exited (127) 2 hours ago                            ubuntu
d3baf6509c44        nginx               "bash"                   2 hours ago         Exited (0) 2 hours ago                              ws

selcuk@selcuk-Inspiron-7577:~$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
f5deb6beebf4d0e813e1cea79406e7461bfd81a59a904b9a5a2ae7bd8a30e9e7
ebd62760e1e91f7d2ffe24018630ac67bf59e75bd50e4260daae3c8be0883bfa
109dcd74562e2b80d5f02119d30fc01d3425036b08b6fae902f18c64bfcdf8fe
f67856cb7161ebedc00c03f3d61c93a874f946f6b3ef243fd19089f2ea8af112
1963a7be8b9303e23a59f6f8d230e1ab1f772fbd17cfd820e9c9d081395a9ce5
d3baf6509c44210befe340c9c1857355980478ab1c3967203d08b50af29f0556

Total reclaimed space: 42.64MB

selcuk@selcuk-Inspiron-7577:~$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### docker container ls komutu yerine yeni gelen komutlar
```
selcuk@selcuk-Inspiron-7577:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

selcuk@selcuk-Inspiron-7577:~$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### docker container ile makinemizin local ip'si farklı
### önce bi apache server oluşturuyoruz.
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d --name apache -p 80:80 httpd
d880bb89393bc6f16de38465f47b7695414841f05d4092e6c923a7b482208ca5
```
### sonra container'ın portundan bizim hangi portumuza nasıl bir yayın yapıtığına bakıyoruz
### burda kendi 80 portundan bizim 80 portumuza tcp yayını yaptığını görüyoruz.
```
selcuk@selcuk-Inspiron-7577:~$ docker container port apache 
80/tcp -> 0.0.0.0:80
```
### aşağıdaki komut ile gelen değerler arasından container'ın ip değerini bulabiliriz.
```
docker container inspect apache 
"IPAddress": "172.17.0.2",
```
### daha sonra kendi makinemizin local ip'sine bakıyoruz
```
ip addr show
192.168.1.13/24
```
### eğer özellikle belirtilmezse tüm container'lar bridge network'üne bağlanır.

![Docker network örnek resim](https://github.com/selcukakarin/ToolBox/blob/master/resimler/dockerNet1.png)

### bridge network'üde sizin firewall'ınız üzerinden sizin fiziksel networkünüze ( host networkünüze) bağlanır.
### host networkü direk sizin hostuna bağlı bir network'tür. Bununla çalışmak güvenlik açıklarına sebep olabilir.
```
selcuk@selcuk-Inspiron-7577:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b1b307000f42        bridge              bridge              local
0e371c58faee        host                host                local
ca17c57a2d12        none                null                local
```
### network detayları için
```
selcuk@selcuk-Inspiron-7577:~$ docker network --help

Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
```
### yeni bir network oluşturmak
```
selcuk@selcuk-Inspiron-7577:~$ docker network create selcukNet
850c455187de13ec22fd2dbb2163310cd81e1053efff7d4c90a013140cae9ed8

selcuk@selcuk-Inspiron-7577:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b1b307000f42        bridge              bridge              local
0e371c58faee        host                host                local
ca17c57a2d12        none                null                local
850c455187de        selcukNet           bridge              local
```
### özel bir ayar yapılmadığı için aşağıda apache serverin bridge bağlı olduğu görülüyor
```
selcuk@selcuk-Inspiron-7577:~$ docker network inspect bridge 
[
    {
        "Name": "bridge",
        "Id": "b1b307000f421d18b2888ec7012652cf86f3b773c019523e38264e7b984d6fbf",
        "Created": "2020-04-14T09:43:32.589677934+03:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "d880bb89393bc6f16de38465f47b7695414841f05d4092e6c923a7b482208ca5": {
                "Name": "apache",
                "EndpointID": "3d300b70937d6b99557535846f828c7c538d79456e3dd01e58ae302905814f58",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```
### apache server container'ımızı selcukNet ağına bağladık
```
docker network connect selcukNet apache 
```
### aşağıdaki kodlar çalıştırılırsa apache'nin iki networke birden bağlı olduğunu gözlemleriz.
```
docker network inspect selcukNet 
docker network inspect bridge
docker container inspect apache 
```
### network ile container arasındaki bağlantıyı koparmak 
```
docker network disconnect selcukNet apache
```
### oluşturulan network'ü silme
```
selcuk@selcuk-Inspiron-7577:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b1b307000f42        bridge              bridge              local
0e371c58faee        host                host                local
ca17c57a2d12        none                null                local
850c455187de        selcukNet           bridge              local

selcuk@selcuk-Inspiron-7577:~$ docker network rm selcukNet 
selcukNet

selcuk@selcuk-Inspiron-7577:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b1b307000f42        bridge              bridge              local
0e371c58faee        host                host                local
ca17c57a2d12        none                null                local
```
### kendi networkümüze container oluşturma
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d --name nginx --network selcukNet nginx
eec0abea38dfd89255d7398f46c568372e42c912c09b8b04b4371a8803127ee0
```
### bir container'dan diğerine ping atmak için

### First enter the bash in the container # 1
```
docker container exec -it CONTAINER bash
```
### In bash, type
```
apt update
```
### then,
```
apt install iputils-ping
```
### then,
```
exit
```
### Yukarıdakiler ile apache server'a ping paketi kuruldu
```
OCI runtime exec failed: exec failed: container_linux.go:349: starting container process caused "exec: \"ping\": executable file not found in $PATH": unknown
# hatasına düşmemek için ping atacağımız container'da ping paketinin kurulu olması gerekiyor.
```
### daha sonra apache'den nginx container'ımıza ping atmak için
```
selcuk@selcuk-Inspiron-7577:~$ docker container exec -it apache ping nginx 
PING nginx (172.19.0.2) 56(84) bytes of data.
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=1 ttl=64 time=0.079 ms
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=2 ttl=64 time=0.091 ms
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=3 ttl=64 time=0.089 ms
```
### yeni bir apache kurduk ve varsayılan olarak bridge networküne bağlandı
```
selcuk@selcuk-Inspiron-7577:~$ docker container run -d --name apache2 httpd
74c4083be98618e599266d09c77664bdbf4a245f43d0ea17c534d50c9f2dfdc0
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
74c4083be986        httpd               "httpd-foreground"       9 seconds ago       Up 7 seconds        80/tcp               apache2
eec0abea38df        nginx               "nginx -g 'daemon of…"   11 minutes ago      Up 11 minutes       80/tcp               nginx
d880bb89393b        httpd               "httpd-foreground"       46 minutes ago      Up 46 minutes       0.0.0.0:80->80/tcp   apache
```
### hatırlarsak diğer iki container selcukNet'e bağlı
```
selcuk@selcuk-Inspiron-7577:~$ docker network inspect selcukNet 
[
    {
        "Name": "selcukNet",
        "Id": "953655091cb61dfd6d442b49dc8c4ccfaee53e883ebf58989e1f511c702504f8",
        "Created": "2020-04-14T17:25:22.788923107+03:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "d880bb89393bc6f16de38465f47b7695414841f05d4092e6c923a7b482208ca5": {
                "Name": "apache",
                "EndpointID": "8e824265967419629b0039cd5cfbb328516e2c8ccbb35deff09143445b73fd4b",
                "MacAddress": "02:42:ac:13:00:03",
                "IPv4Address": "172.19.0.3/16",
                "IPv6Address": ""
            },
            "eec0abea38dfd89255d7398f46c568372e42c912c09b8b04b4371a8803127ee0": {
                "Name": "nginx",
                "EndpointID": "640abf7f7e940510b17004eaa92c68a076c89501f3b1200d463a831c6c73ec79",
                "MacAddress": "02:42:ac:13:00:02",
                "IPv4Address": "172.19.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```
### aynı network'e bağlı olmayan container'lar arası iletişim yoktur.
```
selcuk@selcuk-Inspiron-7577:~$ docker container exec -it apache2 ping nginx 
ping: nginx: Name or service not known

selcuk@selcuk-Inspiron-7577:~$ docker network connect selcukNet apache2

selcuk@selcuk-Inspiron-7577:~$ docker container exec -it apache2 ping nginx 
PING nginx (172.19.0.2) 56(84) bytes of data.
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=1 ttl=64 time=0.083 ms
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=2 ttl=64 time=0.094 ms
64 bytes from nginx.selcukNet (172.19.0.2): icmp_seq=3 ttl=64 time=0.097 ms
```
# Image
### localimizdeki varolan image'lar
```
selcuk@selcuk-Inspiron-7577:~$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        2 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        3 weeks ago         64.2MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
```
### bir image'in güncel versiyonunu çekmek için
```
selcuk@selcuk-Inspiron-7577:~$ docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
Digest: sha256:282530fcb7cd19f3848c7b611043f82ae4be3781cb00105a1d593d7e6286b596
Status: Image is up to date for nginx:latest
docker.io/library/nginx:latest
```
### image'in belli bir sürümünü çekmek
```
selcuk@selcuk-Inspiron-7577:~$ docker pull alpine:3.8.5
3.8.5: Pulling from library/alpine
486039affc0a: Pull complete 
Digest: sha256:2bb501e6173d9d006e56de5bce2720eb06396803300fe1687b58a7ff32bf4c14
Status: Downloaded newer image for alpine:3.8.5
docker.io/library/alpine:3.8.5

selcuk@selcuk-Inspiron-7577:~$ docker image list
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        2 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        3 weeks ago         64.2MB
alpine                      3.8.5               c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
```
### image history sorgulama
```
selcuk@selcuk-Inspiron-7577:~$ docker image history nginx:latest
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
ed21b7a8aee9        2 weeks ago         /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  STOPSIGNAL SIGTERM           0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  EXPOSE 80                    0B                  
<missing>           2 weeks ago         /bin/sh -c ln -sf /dev/stdout /var/log/nginx…   22B                 
<missing>           2 weeks ago         /bin/sh -c set -x     && addgroup --system -…   57.6MB              
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV PKG_RELEASE=1~buster     0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV NJS_VERSION=0.3.9        0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV NGINX_VERSION=1.17.9     0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  CMD ["bash"]                 0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:d1f1b387a158136fb…   69.2MB  
```
### docker image inspect
```
selcuk@selcuk-Inspiron-7577:~$ docker image inspect nginx:latest
[
    {
        "Id": "sha256:ed21b7a8aee9cc677df6d7f38a641fa0e3c05f65592c592c9f28c42b3dd89291",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:282530fcb7cd19f3848c7b611043f82ae4be3781cb00105a1d593d7e6286b596"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2020-03-31T03:19:30.487069362Z",
        "Container": "5c86b143cf5caec0aed5c331922c243f00600152ec0e9ecbe8531771562e72b8",
        "ContainerConfig": {
            "Hostname": "5c86b143cf5c",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.17.9",
                "NJS_VERSION=0.3.9",
                "PKG_RELEASE=1~buster"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:9be1fc3b00d81a66f4de11f5f5bf176e0748434be056cf3152386cc917307e7f",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGTERM"
        },
        "DockerVersion": "18.09.7",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.17.9",
                "NJS_VERSION=0.3.9",
                "PKG_RELEASE=1~buster"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:9be1fc3b00d81a66f4de11f5f5bf176e0748434be056cf3152386cc917307e7f",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGTERM"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 126769107,
        "VirtualSize": 126769107,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/8097c395f2ecbebff28b7a46c81dc293e80583ef437f3e53fa3e843307472605/diff:/var/lib/docker/overlay2/d8409ee8ddd57ae6c21dec9cb34f3ab64ab6d47203621ced733c8afe0d4982de/diff",
                "MergedDir": "/var/lib/docker/overlay2/23803a6144568ea8a6b624812d8f15deaeb6dfc6619043fbbf6499b88d525f89/merged",
                "UpperDir": "/var/lib/docker/overlay2/23803a6144568ea8a6b624812d8f15deaeb6dfc6619043fbbf6499b88d525f89/diff",
                "WorkDir": "/var/lib/docker/overlay2/23803a6144568ea8a6b624812d8f15deaeb6dfc6619043fbbf6499b88d525f89/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:c3a984abe8a88059915bb6c7a1d249fd1ccc16d931334ac8816540b0eb686b45",
                "sha256:99134ec7f247e5a211c7205fec587bf72a6d4aac339b21858b892e9c04f78920",
                "sha256:d37eecb5b7691ec21bd19989e37f8bb4d20b340a775591d0f3db5897d606b0e4"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```
### Aşağıdaki kodlarda görüldüğü gibi nginx'in mainline'ı ve latest'i aslında aynı sürüm ve IMAGE_ID'leri de aynıdır.
### İkisi'de aynı brach olduğu için yeniden indirme yapmadı sadece tag'ledi.(referans verdi)
```
selcuk@selcuk-Inspiron-7577:~$ docker image pull nginx:mainline
mainline: Pulling from library/nginx
Digest: sha256:282530fcb7cd19f3848c7b611043f82ae4be3781cb00105a1d593d7e6286b596
Status: Downloaded newer image for nginx:mainline
docker.io/library/nginx:mainline
selcuk@selcuk-Inspiron-7577:~$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
nginx                       mainline            ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        2 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        3 weeks ago         64.2MB
alpine                      3.8.5               c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
nginx                       1.14.0              ecc98fc2f376        18 months ago       109MB
```
### kendi image'ımızı docker hub'a yükleme
### burada kendi image'ımızı yapmak yerine alpine:3.8.5 sürümünün sadece tag'ini değiştirip hub'a atıyoruz
```
selcuk@selcuk-Inspiron-7577:~$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
nginx                       mainline            ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        2 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        3 weeks ago         64.2MB
alpine                      3.8.5               c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
nginx                       1.14.0              ecc98fc2f376        18 months ago       109MB

selcuk@selcuk-Inspiron-7577:~$ docker image tag alpine:3.8.5 selcukakarin/alpine

selcuk@selcuk-Inspiron-7577:~$ docker image push selcukakarin/alpine
The push refers to repository [docker.io/selcukakarin/alpine]
7444ea29e45e: Pushed 
latest: digest: sha256:954b378c375d852eb3c63ab88978f640b4348b01c1b3456a024a81536dafbbf4 size: 528
```
### bunları yaparken access denied sorunu yaşanırsa docker'a login olunmalı
```
docker login
```
### bir image'i refere eden bir başka tag'li image oluşturmak
```
selcuk@selcuk-Inspiron-7577:~$ docker image tag selcukakarin/alpine:latest selcukakarin/alpine:prod

selcuk@selcuk-Inspiron-7577:~$ docker image push selcukakarin/alpine:prod
The push refers to repository [docker.io/selcukakarin/alpine]
7444ea29e45e: Layer already exists 
prod: digest: sha256:954b378c375d852eb3c63ab88978f640b4348b01c1b3456a024a81536dafbbf4 size: 528
```
### docker file oluşturma ve container'a build etme
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker image build -t custom_nginx .
Sending build context to Docker daemon   47.1kB
Step 1/4 : FROM nginx:latest
 ---> ed21b7a8aee9
Step 2/4 : MAINTAINER Selçuk Akarın "selcuk@gmail.com"
 ---> Running in 54e9acd0dec7
Removing intermediate container 54e9acd0dec7
 ---> 6ce53fe9592b
Step 3/4 : WORKDIR /usr/share/nginx/html
 ---> Running in 3c2e34eeb6ca
Removing intermediate container 3c2e34eeb6ca
 ---> 9507dd00947d
Step 4/4 : COPY index.html index.html
 ---> dda1aff5bae3
Successfully built dda1aff5bae3
Successfully tagged custom_nginx:latest

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
custom_nginx                latest              dda1aff5bae3        8 seconds ago       127MB
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
nginx                       mainline            ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        2 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        3 weeks ago         64.2MB
alpine                      3.8.5               c8bccc0af957        2 months ago        4.41MB
selcuk/alpine               latest              c8bccc0af957        2 months ago        4.41MB
selcukakarin/alpine         latest              c8bccc0af957        2 months ago        4.41MB
selcukakarin/alpine         prod                c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
nginx                       1.14.0              ecc98fc2f376        18 months ago       109MB

# bir daha aynı dosya için build yapılırsa sadece değişiklikleri build eder geri kalanını cache'ten çeker. (using cache)

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker image build -t custom_nginx .
Sending build context to Docker daemon   47.1kB
Step 1/4 : FROM nginx:latest
 ---> ed21b7a8aee9
Step 2/4 : MAINTAINER Selçuk Akarın "selcuk@gmail.com"
 ---> Using cache
 ---> 6ce53fe9592b
Step 3/4 : WORKDIR /usr/share/nginx/html
 ---> Using cache
 ---> 9507dd00947d
Step 4/4 : COPY index.html index.html
 ---> Using cache
 ---> dda1aff5bae3
Successfully built dda1aff5bae3
Successfully tagged custom_nginx:latest

docker container run -d --name test -p 80:80 custom_nginx
```
# Volume
### Docker volume komutları - Verilerin kaybedilmesinin önüne geçmek için volume kullanımları - Persistent data
### burada mongo_db adında bir mongo container'ı oluşturuldu.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name mongo_db mongo
2eee8de21c7d480739e461fdc5a44532199e6e1471ce92321d741dbadced96a6
```
### aşağıdaki inspect komutuyla gelen Volumes özelliğinin attribute'larına birazdan atamalar yapılacaktır.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container inspect mongo_db 
 "Volumes": {
                "/data/configdb": {},
                "/data/db": {}
            },
```
### daha sonra oluşturulmuş tüm volume'ler ve mongo_db container'ı silindi
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               1a9ba8a43e8a687f2f1af6cca0d43628626b34e036a5a5ce556161ebe0219c75
local               7c940b0bb9f687b56f896a2391b852a65f3019088f97bfa361c7a34597a1ffde
local               382bc0218d55b1a8325104e1f3582d4117ced45c4d74562287437fff61cd7ac8
local               875719ceee2855159a3ec8e6133ee03b9a0a2385a52ea2d127a53a51a35361df
local               d576a3ba4a2aab6a92204cf6f753ecd0d24ef7bafe78017c58a56c68acc42aa7
local               daf0ac8a5fc6a536d9e805316db0a009dbaccc14fdf3dbf9b8cac64cdc15ddea

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container stop mongo_db 
mongo_db

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container rm mongo_db 
mongo_db

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
b8194a090182        dda1aff5bae3        "nginx -g 'daemon of…"   17 minutes ago      Exited (0) 12 minutes ago                       test
74c4083be986        httpd               "httpd-foreground"       4 hours ago         Exited (0) 16 minutes ago                       apache2
eec0abea38df        nginx               "nginx -g 'daemon of…"   4 hours ago         Exited (0) 16 minutes ago                       nginx
a1773d84eee7        nginx               "nginx -g 'daemon of…"   4 hours ago         Created                                         i_nginx
d880bb89393b        httpd               "httpd-foreground"       5 hours ago         Exited (0) 16 minutes ago                       apache

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               1a9ba8a43e8a687f2f1af6cca0d43628626b34e036a5a5ce556161ebe0219c75
local               7c940b0bb9f687b56f896a2391b852a65f3019088f97bfa361c7a34597a1ffde
local               382bc0218d55b1a8325104e1f3582d4117ced45c4d74562287437fff61cd7ac8
local               875719ceee2855159a3ec8e6133ee03b9a0a2385a52ea2d127a53a51a35361df
local               d576a3ba4a2aab6a92204cf6f753ecd0d24ef7bafe78017c58a56c68acc42aa7
local               daf0ac8a5fc6a536d9e805316db0a009dbaccc14fdf3dbf9b8cac64cdc15ddea

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
daf0ac8a5fc6a536d9e805316db0a009dbaccc14fdf3dbf9b8cac64cdc15ddea
382bc0218d55b1a8325104e1f3582d4117ced45c4d74562287437fff61cd7ac8
7c940b0bb9f687b56f896a2391b852a65f3019088f97bfa361c7a34597a1ffde
1a9ba8a43e8a687f2f1af6cca0d43628626b34e036a5a5ce556161ebe0219c75
875719ceee2855159a3ec8e6133ee03b9a0a2385a52ea2d127a53a51a35361df
d576a3ba4a2aab6a92204cf6f753ecd0d24ef7bafe78017c58a56c68acc42aa7

Total reclaimed space: 944.9MB

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls   
DRIVER              VOLUME NAME
```
### mongo2 diye bir container oluşturuldu.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name mongo2 mongo
cf7f9a24668c4b72d36c30913ab772dfbcda1ae153647db3b03b11f3d57f28c6

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
local               fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
```
### mongo3 container başlatması 2 farklı volume parametresi atamalarıyla gerçekleşiyor.
### Docker /data/db 'da database bilgilerini, /data/configdb'da ise configurasyon bilgilerini tutar
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name mongo3 -v mongo-db:/data/db -v mongo-configdb:/data/configdb mongo
0c5637209e21c5e9114db8acf2d3894c63b0add822df61fcb33ac6818c0cde9c

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
local               fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
local               mongo-configdb
local               mongo-db

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
0c5637209e21        mongo               "docker-entrypoint.s…"   22 seconds ago      Up 21 seconds       27017/tcp           mongo3
cf7f9a24668c        mongo               "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        27017/tcp           mongo2

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume inspect mongo-configdb 
[
    {
        "CreatedAt": "2020-04-14T21:36:22+03:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/mongo-configdb/_data",
        "Name": "mongo-configdb",
        "Options": null,
        "Scope": "local"
    }
]

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume inspect mongo-db
[
    {
        "CreatedAt": "2020-04-14T21:36:23+03:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/mongo-db/_data",
        "Name": "mongo-db",
        "Options": null,
        "Scope": "local"
    }
]
```
### oluşturulan mongo2 ve mongo3 container'ları silindi.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container rm -f mongo
mongo2  mongo3  

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container rm -f mongo2 mongo3
mongo2
mongo3

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
b8194a090182        dda1aff5bae3        "nginx -g 'daemon of…"   22 minutes ago      Exited (0) 17 minutes ago                       test
74c4083be986        httpd               "httpd-foreground"       4 hours ago         Exited (0) 21 minutes ago                       apache2
eec0abea38df        nginx               "nginx -g 'daemon of…"   4 hours ago         Exited (0) 21 minutes ago                       nginx
a1773d84eee7        nginx               "nginx -g 'daemon of…"   4 hours ago         Created                                         i_nginx
d880bb89393b        httpd               "httpd-foreground"       5 hours ago         Exited (0) 21 minutes ago                       apache

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
local               fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
local               mongo-configdb
local               mongo-db
```
### Var olan volume'leri başka bir container'a bağlamak
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
local               fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
local               mongo-configdb
local               mongo-db

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name mongo4 -v mongo-db:/data/db -v mongo-configdb:/data/configdb mongo
ce129bced70abbc9d4b71203cc612081ed4c11eba236cc9fd8ae9693d10fa2b6

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
ce129bced70a        mongo               "docker-entrypoint.s…"   8 seconds ago       Up 6 seconds        27017/tcp           mongo4
```
### Aşağıdaki kod ile gelen çıktadaki mounts'daki değerlerde mongo4'e bağlanan volume'ler görülmektedir.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container inspect mongo4 

"Mounts": [
            {
                "Type": "volume",
                "Name": "mongo-db",
                "Source": "/var/lib/docker/volumes/mongo-db/_data",
                "Destination": "/data/db",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            },
            {
                "Type": "volume",
                "Name": "mongo-configdb",
                "Source": "/var/lib/docker/volumes/mongo-configdb/_data",
                "Destination": "/data/configdb",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            }
        ],

## Source = bilgisayarda tutulan adres
## Destination = docker container'da bulunan adres
```
### aşağıdaki kodun çıktısında görüldüğü gibi yeni volume değerleri yaratmamış olan değerleri kullanmış. Bu sayede volume'lerdeki veriler yeni container'da kaybolmadı. 
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume ls
DRIVER              VOLUME NAME
local               f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
local               fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
local               mongo-configdb
local               mongo-db
```
### tüm volumeleri ve mongo4'ü silme için
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container rm -f mongo4 
mongo4

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
fb1c5b27b74b6b12bd1af3922514241f26a7f6e1305650519f62947bc98d2eb2
f9c151b1803a7493dff82d315f65fe974ae4a52057906b789d5b5742217f5cd1
mongo-db
mongo-configdb

Total reclaimed space: 629.7MB
```
## Binding: Lokal ile container arasında veri gönderimi.
### bu işlemi yapabilmek için önce my_nginx adında container oluşturduk.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name my_nginx -p 80:80 nginx
c9e9f2fc0c6354ebc05dc2ffa3e86389e87ed250cc4e952c22ef3bfc56982254

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
c9e9f2fc0c63        nginx               "nginx -g 'daemon of…"   7 seconds ago       Up 6 seconds        0.0.0.0:80->80/tcp   my_nginx

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ ls
Dockerfile  docker.md  index.html
```
### daha sonra aşağıdaki komutla binding işlemini gerçekleştiriyoruz
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker container run -d --name nginx2 -v $(pwd):/usr/share/nginx/html -p 8080:80 nginx
c53f0ff7227cc03bef2b466b6303b8ac4b8825d60d0eff026cb811702d38ad69
```
### exec ile container'a bağlandık ve buradaki index.html dosya içeriğini değiştirilmiş ve değiştirilmemiş olarak görüntüledik.
```
selcuk@selcuk-Inspiron-7577:~$ docker container exec -it nginx2 bash

root@c53f0ff7227c:/# cd /usr/share/nginx//html/

root@c53f0ff7227c:/usr/share/nginx/html# ls
Dockerfile  docker.md  index.html

root@c53f0ff7227c:/usr/share/nginx/html# cat index.html 
<html>
  <head>
    <title></title>
    <meta content="">
    <style></style>
  </head>
  <body>
  <h1>Selcuk Akarin selam selcuk</h1>
  </body>
</html>

root@c53f0ff7227c:/usr/share/nginx/html# cat index.html 
<html>
  <head>
    <title></title>
    <meta content="">
    <style></style>
  </head>
  <body>
  <h1>Selcuk Akarin selam selcuk ben degistim</h1>
  </body>
</html>

# locale eklenen a.txt dosyası
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ gedit a.txt

# görüldüğü gibi container'da da anlık olarak dosyalar görüntülenmetedir.
root@c53f0ff7227c:/usr/share/nginx/html# ls
Dockerfile  a.txt  docker.md  index.html
```

# Compose
------------- Bu örnek için docker-compose-sample2 klasörünü kullanın -----------------
### Eğer yml dosyamızın adı docker-compose ise yml'ı ayağa kaldırma için
```
docker-compose up
```
### Eğer yml dosyamızın ismi farklı birşey ise 
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml up
Starting docker_proxy_1 ... 
Starting docker_proxy_1 ... done
Attaching to docker_web_1, docker_proxy_1
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | [Sat Apr 18 11:56:55.925514 2020] [mpm_event:notice] [pid 1:tid 140093524001920] AH00489: Apache/2.4.43 (Unix) configured -- resuming normal operations
web_1    | [Sat Apr 18 11:56:55.925636 2020] [core:notice] [pid 1:tid 140093524001920] AH00094: Command line: 'httpd -D FOREGROUND'
web_1    | 172.18.0.3 - - [18/Apr/2020:11:58:06 +0000] "GET / HTTP/1.0" 200 45
proxy_1  | 172.18.0.1 - - [18/Apr/2020:11:58:06 +0000] "GET / HTTP/1.1" 200 45 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
```
### Eğer container'ın terminal'den [ctrl] + c ile kapatınca kapanmasını istemiyorsak [detach] olarak çalıştırmamız gerek. -d
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml up -d
Starting docker_web_1   ... done
Starting docker_proxy_1 ... done
```
### Logları görmek için
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml logs
Attaching to docker_web_1, docker_proxy_1
proxy_1  | 172.18.0.1 - - [18/Apr/2020:11:58:06 +0000] "GET / HTTP/1.1" 200 45 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.18.0.1 - - [18/Apr/2020:11:59:20 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | [Sat Apr 18 11:56:55.925514 2020] [mpm_event:notice] [pid 1:tid 140093524001920] AH00489: Apache/2.4.43 (Unix) configured -- resuming normal operations
web_1    | [Sat Apr 18 11:56:55.925636 2020] [core:notice] [pid 1:tid 140093524001920] AH00094: Command line: 'httpd -D FOREGROUND'
web_1    | 172.18.0.3 - - [18/Apr/2020:11:58:06 +0000] "GET / HTTP/1.0" 200 45
web_1    | [Sat Apr 18 11:58:10.231756 2020] [mpm_event:notice] [pid 1:tid 140093524001920] AH00492: caught SIGWINCH, shutting down gracefully
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.18.0.2. Set the 'ServerName' directive globally to suppress this message
web_1    | [Sat Apr 18 11:59:15.030594 2020] [mpm_event:notice] [pid 1:tid 139775609234560] AH00489: Apache/2.4.43 (Unix) configured -- resuming normal operations
web_1    | [Sat Apr 18 11:59:15.030871 2020] [core:notice] [pid 1:tid 139775609234560] AH00094: Command line: 'httpd -D FOREGROUND'
web_1    | 172.18.0.3 - - [18/Apr/2020:11:59:20 +0000] "GET / HTTP/1.0" 304 -
```
### Process'leri görmek için
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml top
docker_proxy_1
  UID       PID    PPID    C   STIME   TTY     TIME                        CMD                    
--------------------------------------------------------------------------------------------------
root       24972   24931   0   14:59   ?     00:00:00   nginx: master process nginx -g daemon off;
systemd+   25176   24972   0   14:59   ?     00:00:00   nginx: worker process                     

docker_web_1
 UID      PID    PPID    C   STIME   TTY     TIME            CMD        
------------------------------------------------------------------------
root     24986   24930   0   14:59   ?     00:00:00   httpd -DFOREGROUND
daemon   25085   24986   0   14:59   ?     00:00:00   httpd -DFOREGROUND
daemon   25086   24986   0   14:59   ?     00:00:00   httpd -DFOREGROUND
daemon   25087   24986   0   14:59   ?     00:00:00   httpd -DFOREGROUND
```
### Çalışan veya çalışmayan tüm container'ların statusünü görmek için
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml ps
     Name              Command          State         Ports       
------------------------------------------------------------------
docker_proxy_1   nginx -g daemon off;   Up      0.0.0.0:80->80/tcp
docker_web_1     httpd-foreground       Up      80/tcp       
```
### Help
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose --help
Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file
                              (default: docker-compose.yml)
  -p, --project-name NAME     Specify an alternate project name
                              (default: directory name)
  --verbose                   Show more output
  --log-level LEVEL           Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  --no-ansi                   Do not print ANSI control characters
  -v, --version               Print version and exit
  -H, --host HOST             Daemon socket to connect to

  --tls                       Use TLS; implied by --tlsverify
  --tlscacert CA_PATH         Trust certs signed only by this CA
  --tlscert CLIENT_CERT_PATH  Path to TLS certificate file
  --tlskey TLS_KEY_PATH       Path to TLS key file
  --tlsverify                 Use TLS and verify the remote
  --skip-hostname-check       Don't check the daemon's hostname against the
                              name specified in the client certificate
  --project-directory PATH    Specify an alternate working directory
                              (default: the path of the Compose file)
  --compatibility             If set, Compose will attempt to convert keys
                              in v3 files to their non-Swarm equivalent
  --env-file PATH             Specify an alternate environment file

Commands:
  build              Build or rebuild services
  config             Validate and view the Compose file
  create             Create services
  down               Stop and remove containers, networks, images, and volumes
  events             Receive real time events from containers
  exec               Execute a command in a running container
  help               Get help on a command
  images             List images
  kill               Kill containers
  logs               View output from containers
  pause              Pause services
  port               Print the public port for a port binding
  ps                 List containers
  pull               Pull service images
  push               Push service images
  restart            Restart services
  rm                 Remove stopped containers
  run                Run a one-off command
  scale              Set number of containers for a service
  start              Start services
  stop               Stop services
  top                Display the running processes
  unpause            Unpause services
  up                 Create and start containers
  version            Show the Docker-Compose version information
```
### Docker-compose kapatma
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml down
Stopping docker_web_1   ... done
Stopping docker_proxy_1 ... done
Removing docker_web_1   ... done
Removing docker_proxy_1 ... done
Removing network docker_default

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker$ docker-compose -f sample_docker_compose.yml ps
Name   Command   State   Ports
------------------------------
```
------------- Bu örnek için docker-compose-sample2 klasörünü kullanın -----------------

------------- Bu örnek için docker-compose-sample3 klasörünü kullanın -----------------
### DockerFile ile docker compose işlemi
### yml dosyasında belirttiğimiz html klasörünü yayınlamak için
### Aşağıdaki işlem ile ayağa kaldırdığımız sunucudaki dosyalarda herhangi bir değişiklik olduğunda anında görüntülenecektir.
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker-compose up
Creating network "docker-compose-sample3_default" with the default driver
Building proxy
Step 1/2 : FROM nginx
 ---> ed21b7a8aee9
Step 2/2 : COPY nginx.conf /etc/nginx/conf.d/default.conf
 ---> 8a679c4703aa
Successfully built 8a679c4703aa
Successfully tagged docker-compose-sample3_proxy:latest
WARNING: Image for service proxy was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating docker-compose-sample3_web_1   ... done
Creating docker-compose-sample3_proxy_1 ... done
Attaching to docker-compose-sample3_proxy_1, docker-compose-sample3_web_1
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.21.0.3. Set the 'ServerName' directive globally to suppress this message
web_1    | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.21.0.3. Set the 'ServerName' directive globally to suppress this message
web_1    | [Sat Apr 18 12:18:48.112063 2020] [mpm_event:notice] [pid 1:tid 140002931844224] AH00489: Apache/2.4.43 (Unix) configured -- resuming normal operations
web_1    | [Sat Apr 18 12:18:48.112277 2020] [core:notice] [pid 1:tid 140002931844224] AH00094: Command line: 'httpd -D FOREGROUND'
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET / HTTP/1.1" 200 11111 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET / HTTP/1.0" 200 11111
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/bootstrap/css/bootstrap.min.css HTTP/1.0" 200 140936
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/bootstrap/css/bootstrap.min.css HTTP/1.1" 200 140936 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/fontawesome-free/css/all.min.css HTTP/1.1" 200 48649 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/fontawesome-free/css/all.min.css HTTP/1.0" 200 48649
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/magnific-popup/magnific-popup.css HTTP/1.0" 200 6951
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /css/creative.min.css HTTP/1.0" 200 5398
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/magnific-popup/magnific-popup.css HTTP/1.1" 200 6951 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /css/creative.min.css HTTP/1.1" 200 5398 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/jquery/jquery.min.js HTTP/1.0" 200 86927
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/bootstrap/js/bootstrap.bundle.min.js HTTP/1.0" 200 70966
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/jquery/jquery.min.js HTTP/1.1" 200 86927 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/bootstrap/js/bootstrap.bundle.min.js HTTP/1.1" 200 70966 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/jquery-easing/jquery.easing.min.js HTTP/1.0" 200 2532
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/jquery-easing/jquery.easing.min.js HTTP/1.1" 200 2532 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/scrollreveal/scrollreveal.min.js HTTP/1.0" 200 16526
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/scrollreveal/scrollreveal.min.js HTTP/1.1" 200 16526 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/magnific-popup/jquery.magnific-popup.min.js HTTP/1.1" 200 20216 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /vendor/magnific-popup/jquery.magnific-popup.min.js HTTP/1.0" 200 20216
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:51 +0000] "GET /js/creative.min.js HTTP/1.0" 200 1544
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:51 +0000] "GET /js/creative.min.js HTTP/1.1" 200 1544 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/1.jpg HTTP/1.0" 200 63788
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/2.jpg HTTP/1.0" 200 48101
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/3.jpg HTTP/1.0" 200 48228
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/1.jpg HTTP/1.1" 200 63788 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/2.jpg HTTP/1.1" 200 48101 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/3.jpg HTTP/1.1" 200 48228 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/5.jpg HTTP/1.0" 200 62334
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/4.jpg HTTP/1.0" 200 49055
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/6.jpg HTTP/1.0" 200 53428
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/5.jpg HTTP/1.1" 200 62334 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/4.jpg HTTP/1.1" 200 49055 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/portfolio/thumbnails/6.jpg HTTP/1.1" 200 53428 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /img/header.jpg HTTP/1.0" 200 125976
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /img/header.jpg HTTP/1.1" 200 125976 "http://localhost/css/creative.min.css" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:18:53 +0000] "GET /vendor/fontawesome-free/webfonts/fa-solid-900.woff2 HTTP/1.0" 200 67400
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:18:53 +0000] "GET /vendor/fontawesome-free/webfonts/fa-solid-900.woff2 HTTP/1.1" 200 67400 "http://localhost/vendor/fontawesome-free/css/all.min.css" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:19:01 +0000] "GET /img/portfolio/fullsize/5.jpg HTTP/1.0" 200 62334
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:19:01 +0000] "GET /img/portfolio/fullsize/5.jpg HTTP/1.1" 200 62334 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
proxy_1  | 172.21.0.1 - - [18/Apr/2020:12:19:01 +0000] "GET /img/portfolio/fullsize/6.jpg HTTP/1.1" 200 53428 "http://localhost/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0" "-"
web_1    | 172.21.0.2 - - [18/Apr/2020:12:19:01 +0000] "GET /img/portfolio/fullsize/6.jpg HTTP/1.0" 200 53428

```
### Aynı şekilde detach olarak çalıştırmak için
```
docker-compose up -d
```
### Down etme
```
docker-compose down

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker-compose ps
             Name                      Command          State         Ports       
----------------------------------------------------------------------------------
docker-compose-sample3_proxy_1   nginx -g daemon off;   Up      0.0.0.0:80->80/tcp
docker-compose-sample3_web_1     httpd-foreground       Up      80/tcp            

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker-compose down
Stopping docker-compose-sample3_web_1   ... done
Stopping docker-compose-sample3_proxy_1 ... done
Removing docker-compose-sample3_web_1   ... done
Removing docker-compose-sample3_proxy_1 ... done
Removing network docker-compose-sample3_default

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker-compose ps
Name   Command   State   Ports
------------------------------
```
### Local'deki tüm docker-compose image'larını silmek için
### docker-compose-sample3_proxy silindi
```
selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker image ls
REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
docker-compose-sample3_proxy   latest              8a679c4703aa        7 minutes ago       127MB
custom_nginx                   latest              d319768e326e        3 days ago          127MB
<none>                         <none>              dda1aff5bae3        3 days ago          127MB
httpd                          latest              8326be82abe6        2 weeks ago         166MB
node                           latest              c31fbeb964cc        2 weeks ago         943MB
nginx                          latest              ed21b7a8aee9        2 weeks ago         127MB
nginx                          mainline            ed21b7a8aee9        2 weeks ago         127MB
mongo                          latest              c5e5843d9f5f        3 weeks ago         387MB
bash                           latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                         latest              4e5021d210f6        4 weeks ago         64.2MB
selcukakarin/alpine            latest              c8bccc0af957        2 months ago        4.41MB
selcukakarin/alpine            prod                c8bccc0af957        2 months ago        4.41MB
alpine                         3.8.5               c8bccc0af957        2 months ago        4.41MB
selcuk/alpine                  latest              c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction      latest              76c59512258b        8 months ago        510MB
nginx                          1.14                295c7be07902        12 months ago       109MB
nginx                          1.14.0              ecc98fc2f376        18 months ago       109MB

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker-compose down --rmi local
Removing network docker-compose-sample3_default
WARNING: Network docker-compose-sample3_default not found.
Removing image docker-compose-sample3_proxy

selcuk@selcuk-Inspiron-7577:~/Desktop/repos/ToolBox/docker/docker-compose-sample3$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
custom_nginx                latest              d319768e326e        3 days ago          127MB
<none>                      <none>              dda1aff5bae3        3 days ago          127MB
httpd                       latest              8326be82abe6        2 weeks ago         166MB
node                        latest              c31fbeb964cc        2 weeks ago         943MB
nginx                       latest              ed21b7a8aee9        2 weeks ago         127MB
nginx                       mainline            ed21b7a8aee9        2 weeks ago         127MB
mongo                       latest              c5e5843d9f5f        3 weeks ago         387MB
bash                        latest              78664daf24f4        3 weeks ago         13.2MB
ubuntu                      latest              4e5021d210f6        4 weeks ago         64.2MB
alpine                      3.8.5               c8bccc0af957        2 months ago        4.41MB
selcuk/alpine               latest              c8bccc0af957        2 months ago        4.41MB
selcukakarin/alpine         latest              c8bccc0af957        2 months ago        4.41MB
selcukakarin/alpine         prod                c8bccc0af957        2 months ago        4.41MB
reactioncommerce/reaction   latest              76c59512258b        8 months ago        510MB
nginx                       1.14                295c7be07902        12 months ago       109MB
nginx                       1.14.0              ecc98fc2f376        18 months ago       109MB
```
------------- Bu örnek için docker-compose-sample3 klasörünü kullanın -----------------

# Swarm

![Docker swarm örnek resim](https://github.com/selcukakarin/ToolBox/blob/master/resimler/swarm1.png)
![Docker swarm örnek resim](https://github.com/selcukakarin/ToolBox/blob/master/resimler/swarm2.png)
![Docker swarm örnek resim](https://github.com/selcukakarin/ToolBox/blob/master/resimler/swarm3.png)

### Aşağıdaki kod ile swarm'ın inactive olduğu görülür.
```
selcuk@selcuk-Inspiron-7577:~$ docker info
 Swarm: inactive
```
### Swarm'ı başlatma
### init ile swarm başlatıldığı zaman raft db'si oluturulur ( config dataları vs için ), gerekli güvenlik ayarları yapılır ve bize bir token döner. 
```
selcuk@selcuk-Inspiron-7577:~$ docker swarm init --advertise-addr 127.0.0.1
Swarm initialized: current node (yh1mqqs1c17x8c36k4a93hgml) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-3yvbcq5maoxkh64ilfy7loygpcuzrw6n72y81n2hdjyxcd0ait-7zgx9aaw9n9ogngy0nmsgcz4q 127.0.0.1:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```
### docker info ile swarm'ın active olduğu görülebilir
```
selcuk@selcuk-Inspiron-7577:~$ docker info
 Swarm: active
```
### swarm listesi
```
selcuk@selcuk-Inspiron-7577:~$ docker node ls
ID                            HOSTNAME               STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
yh1mqqs1c17x8c36k4a93hgml *   selcuk-Inspiron-7577   Ready               Active              Leader              19.03.8
```
### local'de swarm için oluşturulan ca certificate'i
```
selcuk@selcuk-Inspiron-7577:~$ docker swarm ca
```
### docker container'a benzer olarak swarm içinde docker service'leri kullanacağız
### help
```
selcuk@selcuk-Inspiron-7577:~$ docker service --help

Usage:  docker service COMMAND

Manage services

Commands:
  create      Create a new service
  inspect     Display detailed information on one or more services
  logs        Fetch the logs of a service or task
  ls          List services
  ps          List the tasks of one or more services
  rm          Remove one or more services
  rollback    Revert changes to a service's configuration
  scale       Scale one or multiple replicated services
  update      Update a service

Run 'docker service COMMAND --help' for more information on a command.
```
### google.com'a ping atan alpine service'i oluşturma
```
selcuk@selcuk-Inspiron-7577:~$ docker service create alpine ping google.com
0hovd4p8wrtdisx9yw43l75u3
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged 
```
### servislerin listesi
```
selcuk@selcuk-Inspiron-7577:~$ docker service ls
ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS
0hovd4p8wrtd        wonderful_albattani   replicated          1/1                 alpine:latest       
```
### servis özelinde bilgi
```
0hovd4p8wrtd --> service id'si - bunun yerine service name'de yazılabilir.
selcuk@selcuk-Inspiron-7577:~$ docker service ps 0hovd4p8wrtd
ID                  NAME                    IMAGE               NODE                   DESIRED STATE       CURRENT STATE           ERROR               PORTS
p33is8fvaarr        wonderful_albattani.1   alpine:latest       selcuk-Inspiron-7577   Running             Running 2 minutes ago      
```
### aynı anda 4 service ayağa kaldırmak
```
selcuk@selcuk-Inspiron-7577:~$ docker service update wonderful_albattani --replicas 4
wonderful_albattani
overall progress: 4 out of 4 tasks 
1/4: running   [==================================================>] 
2/4: running   [==================================================>] 
3/4: running   [==================================================>] 
4/4: running   [==================================================>] 
verify: Service converged 
selcuk@selcuk-Inspiron-7577:~$ docker service ls
ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS
0hovd4p8wrtd        wonderful_albattani   replicated          4/4                 alpine:latest       
```
### swarm özelinde 4 tane aynı konfigürasyonlu servisin çalıştığını görmek için
```
selcuk@selcuk-Inspiron-7577:~$ docker service ps wonderful_albattani 
ID                  NAME                    IMAGE               NODE                   DESIRED STATE       CURRENT STATE                ERROR               PORTS
p33is8fvaarr        wonderful_albattani.1   alpine:latest       selcuk-Inspiron-7577   Running             Running 4 minutes ago                            
9zrgogkzny20        wonderful_albattani.2   alpine:latest       selcuk-Inspiron-7577   Running             Running about a minute ago                       
vkcpnxk8d3tm        wonderful_albattani.3   alpine:latest       selcuk-Inspiron-7577   Running             Running about a minute ago                       
66ay2oq5leg4        wonderful_albattani.4   alpine:latest       selcuk-Inspiron-7577   Running             Running about a minute ago       
```
### docker update --help ile docker service --help arasındaki ayar seçeneklerininin farkı
```
selcuk@selcuk-Inspiron-7577:~$ docker update --help

Usage:  docker update [OPTIONS] CONTAINER [CONTAINER...]

Update configuration of one or more containers

Options:
      --blkio-weight uint16        Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
      --cpu-period int             Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int              Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int          Limit the CPU real-time period in microseconds
      --cpu-rt-runtime int         Limit the CPU real-time runtime in microseconds
  -c, --cpu-shares int             CPU shares (relative weight)
      --cpus decimal               Number of CPUs
      --cpuset-cpus string         CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string         MEMs in which to allow execution (0-3, 0,1)
      --kernel-memory bytes        Kernel memory limit
  -m, --memory bytes               Memory limit
      --memory-reservation bytes   Memory soft limit
      --memory-swap bytes          Swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --pids-limit int             Tune container pids limit (set -1 for unlimited)
      --restart string             Restart policy to apply when a container exits
selcuk@selcuk-Inspiron-7577:~$ docker service update --help

Usage:  docker service update [OPTIONS] SERVICE

Update a service

Options:
      --args command                       Service command args
      --config-add config                  Add or update a config file on a service
      --config-rm list                     Remove a configuration file
      --constraint-add list                Add or update a placement constraint
      --constraint-rm list                 Remove a constraint
      --container-label-add list           Add or update a container label
      --container-label-rm list            Remove a container label by its key
      --credential-spec credential-spec    Credential spec for managed service account (Windows only)
  -d, --detach                             Exit immediately instead of waiting for the service to converge
      --dns-add list                       Add or update a custom DNS server
      --dns-option-add list                Add or update a DNS option
      --dns-option-rm list                 Remove a DNS option
      --dns-rm list                        Remove a custom DNS server
      --dns-search-add list                Add or update a custom DNS search domain
      --dns-search-rm list                 Remove a DNS search domain
      --endpoint-mode string               Endpoint mode (vip or dnsrr)
      --entrypoint command                 Overwrite the default ENTRYPOINT of the image
      --env-add list                       Add or update an environment variable
      --env-rm list                        Remove an environment variable
      --force                              Force update even if no changes require it
      --generic-resource-add list          Add a Generic resource
      --generic-resource-rm list           Remove a Generic resource
      --group-add list                     Add an additional supplementary user group to the container
      --group-rm list                      Remove a previously added supplementary user group from the container
      --health-cmd string                  Command to run to check health
      --health-interval duration           Time between running the check (ms|s|m|h)
      --health-retries int                 Consecutive failures needed to report unhealthy
      --health-start-period duration       Start period for the container to initialize before counting retries towards unstable (ms|s|m|h)
      --health-timeout duration            Maximum time to allow one check to run (ms|s|m|h)
      --host-add list                      Add a custom host-to-IP mapping (host:ip)
      --host-rm list                       Remove a custom host-to-IP mapping (host:ip)
      --hostname string                    Container hostname
      --image string                       Service image tag
      --init                               Use an init inside each service container to forward signals and reap processes
      --isolation string                   Service container isolation mode
      --label-add list                     Add or update a service label
      --label-rm list                      Remove a label by its key
      --limit-cpu decimal                  Limit CPUs
      --limit-memory bytes                 Limit Memory
      --log-driver string                  Logging driver for service
      --log-opt list                       Logging driver options
      --mount-add mount                    Add or update a mount on a service
      --mount-rm list                      Remove a mount by its target path
      --network-add network                Add a network
      --network-rm list                    Remove a network
      --no-healthcheck                     Disable any container-specified HEALTHCHECK
      --no-resolve-image                   Do not query the registry to resolve image digest and supported platforms
      --placement-pref-add pref            Add a placement preference
      --placement-pref-rm pref             Remove a placement preference
      --publish-add port                   Add or update a published port
      --publish-rm port                    Remove a published port by its target port
  -q, --quiet                              Suppress progress output
      --read-only                          Mount the container's root filesystem as read only
      --replicas uint                      Number of tasks
      --replicas-max-per-node uint         Maximum number of tasks per node (default 0 = unlimited)
      --reserve-cpu decimal                Reserve CPUs
      --reserve-memory bytes               Reserve Memory
      --restart-condition string           Restart when condition is met ("none"|"on-failure"|"any")
      --restart-delay duration             Delay between restart attempts (ns|us|ms|s|m|h)
      --restart-max-attempts uint          Maximum number of restarts before giving up
      --restart-window duration            Window used to evaluate the restart policy (ns|us|ms|s|m|h)
      --rollback                           Rollback to previous specification
      --rollback-delay duration            Delay between task rollbacks (ns|us|ms|s|m|h)
      --rollback-failure-action string     Action on rollback failure ("pause"|"continue")
      --rollback-max-failure-ratio float   Failure rate to tolerate during a rollback
      --rollback-monitor duration          Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h)
      --rollback-order string              Rollback order ("start-first"|"stop-first")
      --rollback-parallelism uint          Maximum number of tasks rolled back simultaneously (0 to roll back all at once)
      --secret-add secret                  Add or update a secret on a service
      --secret-rm list                     Remove a secret
      --stop-grace-period duration         Time to wait before force killing a container (ns|us|ms|s|m|h)
      --stop-signal string                 Signal to stop the container
      --sysctl-add list                    Add or update a Sysctl option
      --sysctl-rm list                     Remove a Sysctl option
  -t, --tty                                Allocate a pseudo-TTY
      --update-delay duration              Delay between updates (ns|us|ms|s|m|h)
      --update-failure-action string       Action on update failure ("pause"|"continue"|"rollback")
      --update-max-failure-ratio float     Failure rate to tolerate during an update
      --update-monitor duration            Duration after each task update to monitor for failure (ns|us|ms|s|m|h)
      --update-order string                Update order ("start-first"|"stop-first")
      --update-parallelism uint            Maximum number of tasks updated simultaneously (0 to update all at once)
  -u, --user string                        Username or UID (format: <name|uid>[:<group|gid>])
      --with-registry-auth                 Send registry authentication details to swarm agents
  -w, --workdir string                     Working directory inside the container
```
### docker swarm'da çalışan service'ler aynı zamanda docker'da container'da oluşturur
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
53c9b289bd04        alpine:latest       "ping google.com"   4 minutes ago       Up 4 minutes                            wonderful_albattani.3.vkcpnxk8d3tmpijkuc4tz9n56
5383afd7ca32        alpine:latest       "ping google.com"   4 minutes ago       Up 4 minutes                            wonderful_albattani.2.9zrgogkzny20v082rkmh8v1o8
eef32b567d0a        alpine:latest       "ping google.com"   4 minutes ago       Up 4 minutes                            wonderful_albattani.4.66ay2oq5leg4su8dm4ga42v4b
58caeae62ae4        alpine:latest       "ping google.com"   7 minutes ago       Up 7 minutes                            wonderful_albattani.1.p33is8fvaarr7q3nr7kz45401
```
### docker container swarm'ın düşen(kapanan) service'leri yeniden otomatik açtığını gözlemlemek için
```
selcuk@selcuk-Inspiron-7577:~$ docker container rm -f wonderful_albattani.3.vkcpnxk8d3tmpijkuc4tz9n56 
wonderful_albattani.3.vkcpnxk8d3tmpijkuc4tz9n56

selcuk@selcuk-Inspiron-7577:~$ docker service ls
ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS
0hovd4p8wrtd        wonderful_albattani   replicated          3/4                 alpine:latest      

## Burada swarm service'i anında ayağa kaldırdığı için yine 4 servis açık gözüküyor
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
cd16eb02a9b7        alpine:latest       "ping google.com"   7 seconds ago       Up 2 seconds                            wonderful_albattani.3.ubhpop4hqci701esiy506p314
64e43bf91702        alpine:latest       "ping google.com"   59 seconds ago      Up 54 seconds                           wonderful_albattani.2.awr12wf4gc7lgja0dedkibjzk
eef32b567d0a        alpine:latest       "ping google.com"   6 minutes ago       Up 6 minutes                            wonderful_albattani.4.66ay2oq5leg4su8dm4ga42v4b
58caeae62ae4        alpine:latest       "ping google.com"   9 minutes ago       Up 9 minutes                            wonderful_albattani.1.p33is8fvaarr7q3nr7kz45401

selcuk@selcuk-Inspiron-7577:~$ docker container rm -f wonderful_albattani.2.awr12wf4gc7lgja0dedkibjzk 
wonderful_albattani.2.awr12wf4gc7lgja0dedkibjzk

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
cd16eb02a9b7        alpine:latest       "ping google.com"   38 seconds ago      Up 32 seconds                           wonderful_albattani.3.ubhpop4hqci701esiy506p314
eef32b567d0a        alpine:latest       "ping google.com"   6 minutes ago       Up 6 minutes                            wonderful_albattani.4.66ay2oq5leg4su8dm4ga42v4b
58caeae62ae4        alpine:latest       "ping google.com"   10 minutes ago      Up 10 minutes                           wonderful_albattani.1.p33is8fvaarr7q3nr7kz45401

## Burada swarm service'i anında ayağa kaldırdığı için yine 4 servis açık gözüküyor
selcuk@selcuk-Inspiron-7577:~$ docker service ls
ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS
0hovd4p8wrtd        wonderful_albattani   replicated          4/4                 alpine:latest       

## ps ile swarm'ın history'sini kontrol ettiğimizde bizim kapadığımız servisleri swarm'ın açtığını görüyoruz
selcuk@selcuk-Inspiron-7577:~$ docker service ps wonderful_albattani 
ID                  NAME                        IMAGE               NODE                   DESIRED STATE       CURRENT STATE                ERROR                         PORTS
p33is8fvaarr        wonderful_albattani.1       alpine:latest       selcuk-Inspiron-7577   Running             Running 10 minutes ago                                     
d95ulsqb24lu        wonderful_albattani.2       alpine:latest       selcuk-Inspiron-7577   Running             Running 33 seconds ago                                     
awr12wf4gc7l         \_ wonderful_albattani.2   alpine:latest       selcuk-Inspiron-7577   Shutdown            Failed 39 seconds ago        "task: non-zero exit (137)"   
9zrgogkzny20         \_ wonderful_albattani.2   alpine:latest       selcuk-Inspiron-7577   Shutdown            Failed 2 minutes ago         "task: non-zero exit (137)"   
ubhpop4hqci7        wonderful_albattani.3       alpine:latest       selcuk-Inspiron-7577   Running             Running about a minute ago                                 
vkcpnxk8d3tm         \_ wonderful_albattani.3   alpine:latest       selcuk-Inspiron-7577   Shutdown            Failed about a minute ago    "task: non-zero exit (137)"   
66ay2oq5leg4        wonderful_albattani.4       alpine:latest       selcuk-Inspiron-7577   Running             Running 7 minutes ago                       
```
### docker service silmek için
### aşağıda görüldüğü gibi service silindi fakat container'lar ayakta
```
selcuk@selcuk-Inspiron-7577:~$ docker service rm wonderful_albattani 
wonderful_albattani

selcuk@selcuk-Inspiron-7577:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS

selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
42816f90f3e6        alpine:latest       "ping google.com"   7 minutes ago       Up 7 minutes                            wonderful_albattani.2.d95ulsqb24lubvarndh6s4soh
cd16eb02a9b7        alpine:latest       "ping google.com"   7 minutes ago       Up 7 minutes                            wonderful_albattani.3.ubhpop4hqci701esiy506p314
eef32b567d0a        alpine:latest       "ping google.com"   13 minutes ago      Up 13 minutes                           wonderful_albattani.4.66ay2oq5leg4su8dm4ga42v4b
58caeae62ae4        alpine:latest       "ping google.com"   17 minutes ago      Up 17 minutes                           wonderful_albattani.1.p33is8fvaarr7q3nr7kz45401
```
### bu container'ların silindi biraz süre alıyor. aşağıda görüldüğü gibi container'lar da silindi.
```
selcuk@selcuk-Inspiron-7577:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
### yani docker service rm wonderful_albattani komutu hem swarm service'i siliyor hem replicaları hem de container'ları siliyor.
### geri kalans swarm özelliklerini test etmek için https://labs.play-with-docker.com/# linkinden bize sağlanan 4 saatlik bir test ortamında denemeler yapacağız.
### Ayrıca Vbox'a linux kurulumu yapıp da çalıştırılabilir.
### 2 tane intance oluşturduk ve aşağıdaki komutla birinden diğerine ping attık
```
$ ping 192.168.0.7
```
# docker-machine
### docker machine kurmak için
```
https://docs.docker.com/machine/install-machine/ adresindeki kodu çalıştır. Linux için

$ base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo mv /tmp/docker-machine /usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine
```




