## postgresql kurulumu

[Kaynak](https://tecadmin.net/install-postgresql-server-on-ubuntu/)

Start with the import of the GPG key for PostgreSQL packages.
```
sudo apt-get install wget ca-certificates

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
Now add the repository to your system.
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

sudo apt-get update

sudo apt-get install postgresql-11 

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

sudo apt-get --purge remove postgresql

dpkg -l | grep postgres

sudo apt-get --purge remove postgresql postgresql-doc postgresql-common
```
## pgadmin4 kurulumu
```
sudo apt-get install postgresql-11 pgadmin4
```
## postgresql servis başlatma
```
sudo service postgresql start
```
## postgresql işlemleri

--------------------------

eğer pgadmin4'e postgres ile server eklenemiyorsa aşağıdaki adımları izleyin:
```
1 - sudo -u postgres psql

2 - ALTER USER postgres PASSWORD 'newPassword';
```
--------------------------

### Öncelikle sağ click ile bir server oluşturulur server host = localhost olabilir
```sql
sudo su - postgres

psql

CREATE DATABASE LNKCLOUDERP;

CREATE USER linkuser WITH PASSWORD '***';

ALTER ROLE linkuser SET client_encoding TO 'utf8';

ALTER ROLE linkuser SET default_transaction_isolation TO 'read committed';

ALTER ROLE linkuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE LNKCLOUDERP TO linkuser;

\q

exit
```
## psycopg2 veritabanımızda değişikliğe izin veriyor.
```
pip install django psycopg2
```

## eğer hata çıkarsa
```
apt-get install libpq-dev
```