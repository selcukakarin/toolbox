## mysql kurulumu

[Kaynak](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)

## ubuntu 

```
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo mysql_install_db
sudo mysql_secure_installation
```

### create a database and database user

```
mysql -u root -p
CREATE DATABASE myproject CHARACTER SET UTF8;
CREATE USER myprojectuser@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myproject.* TO myprojectuser@localhost;
grant all privileges on *.* to 'parsa'@'localhost';
grant all privileges on `database_name`.`table_name` to 'user_name'@'hostname';
FLUSH PRIVILEGES;
exit
```

```
pip install django mysqlclient
```

### django configurasyonları
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Gerekli komutlar

```
mysql -u user -p
USE database_name;
SHOW DATABASES;
```
+--------------------+
| Database          |
+--------------------+
| information_schema |
| mysql             |
| performance_schema |
| sys               |
+--------------------+
4 rows in set (0.00 sec)
```
CREATE DATABASE blog_data;
CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL ON blog_data.* TO 'djangouser'@'%';
FLUSH PRIVILEGES;
```
```
SHOW TABLES;
```
+----------------------------+
| Tables_in_database_name    |
+----------------------------+
| actions                    |
| permissions                |
| permissions_roles          |
| permissions_users          |
| roles                      |
| roles_users                |
| settings                   |
| users                      |
+----------------------------+
8 rows in set (0.00 sec)
```
SHOW FULL TABLES;
```
+----------------------------+------------+
| Tables_in_database_name    | Table_type |
+----------------------------+------------+
| actions                    | VIEW       |
| permissions                | BASE TABLE |
| permissions_roles          | BASE TABLE |
| permissions_users          | BASE TABLE |
| roles                      | BASE TABLE |
| roles_users                | BASE TABLE |
| settings                   | BASE TABLE |
| users                      | BASE TABLE |
+----------------------------+------------+

8 rows in set (0.00 sec)
```
SHOW TABLES FROM database_name;
SHOW TABLES LIKE pattern;
SHOW TABLES LIKE 'permissions%';
```
+-------------------------------------------+
| Tables_in_database_name (permissions%)    |
+-------------------------------------------+
| permissions                               |
| permissions_roles                         |
| permissions_users                         |
+-------------------------------------------+
3 rows in set (0.00 sec)
```
mysql -u user -p -e 'SHOW TABLES FROM database_name;'
```
+----------------------------+
| Tables_in_database_name    |
+----------------------------+
| actions                    |
| permissions                |
| permissions_roles          |
| permissions_users          |
| roles                      |
| roles_users                |
| settings                   |
| users                      |
+----------------------------+
```
mysqlshow database_name
```
### Django settings for mysql
[Kaynak](https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}

you also need to create the /path/to/my.cnf file with similar settings from above

[client]
database = DB_NAME
host = localhost
user = DB_USER
password = DB_PASSWORD
default-character-set = utf8

1. OPTIONS.
2. NAME, USER, PASSWORD, HOST, PORT
3. MySQL option files.
```

## Mysql workbench installation

[Kaynak](https://linuxhint.com/installing_mysql_workbench_ubuntu/)

### Using the apt repository
#### Step 1: Download configuration file from the apt repository
[Download apt](https://dev.mysql.com/downloads/repo/apt/)
```
$ cd Downloads
$ ls
```
#### Step 2: Configuration of MySQL apt config
```
$ sudo apt install ./mysql-apt-config_0.8.15-1_all.deb
say ok all prompts
```
#### Step 3: Update apt-cache
```
$ sudo apt update
```
#### Step 4: Installing MySQL Workbench on Ubuntu 20.04
```
$ sudo apt install mysql-workbench-community
```
#### Step 5: Launch MySQL Workbench
```
$ mysql-workbench
```
### Install MySQL workbench using Deb packages
#### Step 1:
[Download workbench deb](https://dev.mysql.com/downloads/workbench/)
#### Step 2:
```
$ sudo apt install ./mysql-workbench-community_8.0.20-1ubuntu20.04_amd64.deb
```
#### Uninstall MySQL Workbench
```
$ sudo apt remove mysql-workbench-community
```

### db installation with code

```
mysql < employees.sql
```

### db test - see records

```
mysql -t < test_employees_md5.sql
# OR
mysql -t < test_employees_sha.sql
```