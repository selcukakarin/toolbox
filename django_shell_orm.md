## Django Shell ile ORM sorgularını kullanma

### Shell ekranımızı açıyoruz interactive console
```
python manage.py shell
```
### Djangonun içinde bulunan hazır User modelini import ediyoruz
```python
from django.contrib.auth.models import User
```
### Bizim oluşturduğumuz Article modelini de import ediyoruz
```python
from article.models import Article
```
### User modelinden newUser nesnemizi türetiyoruz ve server'ımıza ekliyoruz
```python
newUser=User(username="userselcuk",password="123")

newUser.save()
```
### Diğer tanımlama methodları
```python
newUser2=User(username="alikullanici")

newUser2.set_password("123")

newUser2.save()

newUser3=User()

newUser3.username=("mustikullanici")

newUser3.set_password("123")

newUser3.first_name="musti"

newUser3.save()
```
### Article modelimizden article nesnemizi tanımlıyoruz 
```python
article=Article(title="Django Shell Deneme",content="İçerik",author=newUser3)

article.save()
```
### Diğer tanımlama yöntemleri
```python
article2=Article()

article2.title="deneme 15"

article2.content="İçerik"

article2.author=newUser3

article2.save()

Article.objects.create(title="Deneme 21",content="21",author=newUser2)

<Article: Deneme 21>

article=Article.objects.create(title="Yazı Başlık",content="Yazı içerik",author=newUser2)

article.title

'Yazı Başlık'

article.title="Yazı Başlık Değişti"

article.save()
```
### Article nesnelerimizi çekiyoruz
```python
Article.objects.all()

<QuerySet [<Article: 1>, <Article: 2>, <Article: 3>, <Article: Django Shell Deneme>, <Article: deneme 15>, <Article: Deneme 21>, 

<Article: Yazı Başlık Değişti>]>
```
### title'ı "Django Shell Deneme" olan article'ı çekiyoruz
```python
article=Article.objects.get(title="Django Shell Deneme")

article.title

'Django Shell Deneme'
```
### article'ı siliyoruz
```python
article.delete()

(1, {'article.Article': 1})
```
### Article'larımız görünüyor
```python
Article.objects.all()

<QuerySet [<Article: 1>, <Article: 2>, <Article: 3>, <Article: deneme 15>, <Article: Deneme 21>, <Article: Yazı Başlık Değişti>]>
```
### id değeri 1 olan article'ımızı alıyoruz
```python
article=Article.objects.get(id=1)

article

<Article: 1>

article.delete()

Article.objects.all()

<QuerySet [<Article: 2>, <Article: 3>, <Article: deneme 15>, <Article: Deneme 21>, <Article: Yazı Başlık Değişti>]>
```
### **__contains** komutu ile içerisinde "en" geçen article'larımızı sorguluyoruz
```python
Article.objects.filter(title__contains="en")

<QuerySet [<Article: deneme 15>, <Article: Deneme 21>]>
```


### user1'in tüm postlarını sorgularız
```python
from django.contrib.auth.models import User

user1=User.objects.get(id=1)

user1.get_full_name()

'selcuk akarin'

user1.post_set.all()

<QuerySet [<Post: bu başlık türkçe karakter içerir333>, <Post: türkçe karakter içerir ızgara>]>

#### post modelinde ForeignKey'e posts isminde bir related name oluşturuldu.

>>> from django.contrib.auth.models import User

>>> user1 = User.objects.get(id=1)

>>> user1.posts.all()

<QuerySet [<Post: bu başlık türkçe karakter içerir333>, <Post: türkçe karakter içerir ızgara>]>


```