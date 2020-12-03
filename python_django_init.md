## Vs code kurulumu

` sudo snap install --classic code ` komutu ile öncelikjle vs code'umuzu kurmalıyız.

## python kurulum

Start by updating the packages list and installing the prerequisites:
```
sudo apt update

sudo apt install software-properties-common
```
Next, add the deadsnakes PPA to your sources list:
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
When prompted press Enter to continue:

Press [ENTER] to continue or Ctrl-c to cancel adding it.

Once the repository is enabled, install Python 3.7 with:
```
sudo apt install python3.7
```
At this point, Python 3.7 is installed on your Ubuntu system and ready to be used. You can verify it by typing:
```
python3.7 --version

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1      komutu ile standart python3 sürümünü 3.7 olarak seçiyoruz

sudo update-alternatives --config python

sudo update-alternatives  --set python /usr/bin/python3.7       eğer yukarıdaki komut işe yaramaz ise standart python3 sürümünü 3.7 olarak seçiyoruz

alias python=python3

python --version

alias python='/usr/bin/python3'
```
[Source](https://stackoverflow.com/questions/41986507/unable-to-set-default-python-version-to-python3-in-ubuntu)

## Pip kurulumu

` sudo apt install python3-pip ` komutu ile pip paket yükleyicisi kurulur. Django vs için pip kullanılacaktır.

## Django kurulumu

`__init__.py` myapp klasörünün bir python dosyası olduğunu gösterir

`settings.py` ayarlarımızı bulunduran dosya

`urls.py` site yönlendirme (map ayarları) işlemleri yapılır.
[Django kurulum](https://tecadmin.net/install-django-on-ubuntu/)
```
pip3 install Django==2.1.7      kodu ile kurulum gerçekleştirilir.

pip3 install -U Django==2.1.7       kodu ile mevcut sürüm güncelleştirilir.

python3 -m django --version     ile sürüm kontrolü yapılmaktadır.

pip3 uninstall Django       kodu ile kaldırma işlemi yapılmaktadır.
```

### proje oluşturma kodu
```python
django-admin.py startproject linkerp
```

#### Django projemizi local hostta çalıştırıyoruz
```python
python3 manage.py runserver
```
#### Postgresql - Kullanılacak veritabanını yükleme

[postgres yükleme kılavuzu](https://github.com/selcukakarin/ToolBox/blob/master/postgres.md)
    
#### Database ayarlarını settings.py dosyasından yapabiliriz
```
DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
        'NAME': 'dbName',
        
        'USER': 'userName',
        
        'PASSWORD': '***',
        
        'HOST': 'localhost',
        
        'PORT': '',
        
    }
    
}
```
#### setting.py deki değişiklikleri veritabanına yansıtmak için kullanılan komutlar
```python
python manage.py makemigrations #ilk defa oluşturulan tablolar için 

python manage.py migrate  #app'lerimiz içindeki veritabanları oluşturulur

python manage.py sqlmigrate post 0001 # post = app name 0001 = migration name
```
#### admin sayfasına bağlanmak için pgadmin4 üzerinden bir server tanımlaması yapmamız gerekli.

### superuser oluşturuyoruz
```python
python manage.py createsuperuser
```
### uygulama oluşturma kodu
```python
python manage.py startapp erpDb
```
### Article model oluşturma ve Admin arayüzüne ekleme

#### models.py
```python
class Article(models.Model):

    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    
    title=models.CharField(max_length=50,verbose_name="Başlık")
    
    content=models.TextField(verbose_name="İçerik")
    
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
``` 

#### admin.py - Article modelimizi admin panelimize kayıt ediyoruz
```python
from .models import Article

#Register your models here.

#admin.site.register(Article)

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):

    #Article sayfasında hangi özelliklerin gösterileceğini seçmek için
    
    list_display=["title","author","created_date","content"]

    #Article sayfasında hangi özelliklerin link alacağını belirler
    
    list_display_links=["title","author","created_date"]
        
    #Article sayfasında title'a göre arama özelliği geldi
    
    search_fields=["title"]
    
    #Article sayfasında sağ köşede bir süzgeç menü oluşturulur.
    
    #list_filter=["content"]
    
    list_filter=["title"]

    #Meta class'ı python'ın bize önerdiği bir classtır. ismi değiştirilemez. model=Article yardımıyla Article ile ArticleAdmini bağlar.
    
    class Meta:
    
        model=Article
```        
#### myapp/setting.py
```python
INSTALLED_APPS = [

    'django.contrib.admin',
    
    'django.contrib.auth',
    
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    
    'django.contrib.messages',
    
    'django.contrib.staticfiles',
    
    "article",
    
]
```
#### Template (html dosyalarımızı) templates klasörü altında tutmak için uygulamamız olan myapp/settings.py dosyasına aşağıdaki kodu ekliyoruz
```python
TEMPLATES = [

    {
    
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': ["templates"], #Artık html sayfalarımızın yolu templates klasörü olabilir
        
        'APP_DIRS': True,
        
        'OPTIONS': {
        
            'context_processors': [
            
                'django.template.context_processors.debug',
                
                'django.template.context_processors.request',
                
                'django.contrib.auth.context_processors.auth',
                
                'django.contrib.messages.context_processors.messages',
                
            ],
            
        },
        
    },
    
]
```
#### Eğer "" yani localhost url'imiz için HttpResponse yani bir string göndermek ister isek aşağıdaki gibi yaparız

#### önce views.py'de bir method yazarız
```python
from django.shortcuts import render,HttpResponse

### Create your views here.

def index(request):

    return HttpResponse("<h3> Anasayfa </h3>")
```
#### daha sonra myapp/urls.py ye şunları ekleriz
```python
from django.contrib import admin

from django.urls import path

from article.views import index ###

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.
    
]
```
#### eğer HttpResponse yerine bir html dönmek istersek aşağıdaki kodu uygularız
```python
return render(request,"index.html")
```
### static file (css,js vs) kullanımı

#### Öncelikle app'imizin içerisine static klasörü oluştururuz.

#### settings.py'ye eklenmeli
```python
STATIC_URL = '/static/'
```
#### app'imiz içindeki static file'ımızı kullanabilmek için
```
{% load static %} ## app'imiz içindeki static file'ımızı kullanabilmek için bu tanımlama yapılır

<img src="{% static "my_app/example.jpg" %}" alt="My image"/>

<!DOCTYPE html>

{% load static %}

<html lang="en">
    
<head>
    
    <meta charset="UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    <title>Selçuk Site</title>
    
    <link rel="stylesheet" href="{% static "style.css" %}">
    
</head>

<body>
    
    <h3>Anasayfa</h3>
    
    <p>Design by Selçuk Akarın</p>
    
</body>

</html>
```

### Eğer static dosyalarımızı app'lerimiz içinde değil de projemiz içinde tanımlamak istersek projenin settings.py dosyasına eklenir
```python
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, "static"),
    
    '/var/www/static/',
    
]
```
```
<!DOCTYPE html>

{% load static %}

<html lang="en">
    
<head>
    
    <meta charset="UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    <title>Selçuk Site</title>
    
    <link rel="stylesheet" href="{% static "style.css" %}">
    
</head>

<body>
    
    <h3>Anasayfa</h3>
    
    <p>Design by Selçuk Akarın</p>
    
</body>

</html>
```
### uygulamamıza (app) özel bir urls.py tanımlamak için 

#### myproject/urls.py dosyasına aşağıdaki gibi tanımlama yapmalıyız
```python
from django.contrib import admin

from django.urls import path,include

from article import views   

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', views.index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.
    
    path('about/', views.about,name="about"),
    
    path('detail/<int:id>', views.detail,name="detail"), # dinamik url tanımlama için
    
    path('article/',include("article.urls")),
    
]
```
#### app'imizdeki tanımlama aşağıdaki gibi olmalı
```
from django.contrib import admin

from django.urls import path

from . import views

app_name="article"

urlpatterns = [

    path('create/',views.index,name="index"),
    
]
```
### bir register formu tasarlıyoruz
```python
from django import forms

class RegisterForm(forms.Form):

    username=forms.CharField(max_length=50,label="Kullanıcı Adı: ")
    
    password=forms.CharField(max_length=20,label="Parola: ",widget=forms.PasswordInput)
    
    confirm=forms.CharField(max_length=20,label="Parolayı Doğrula: ",widget=forms.PasswordInput)
    
    #clean metodu bize parolaların kontrolünü sağlayıp giriş yapılıp yapılmayacağı konusunda bize yetki verir
    
    #clean metodu sadece views.py'de form.is_valid() fonksiyonu yardımıyla çağrılır
    
    def clean(self):
    
        username=self.cleaned_data.get("username")
        
        password=self.cleaned_data.get("password")
        
        confirm=self.cleaned_data.get("confirm")
        
        
        if password and confirm and password!=confirm:
        
            raise forms.ValidationError("Parolalar eşleşmiyor.")
            
            
        values={
        
            #burada hangi key ile döndüysek views'da yine username=form.cleaned_data.get("username") bu şekilde yakalamamız gerek
            
            "username":username,
            
            "password":password
            
        }
        
        return values
```
#### register.html'e bir form oluşturuyoruz
```
{% extends "layout.html" %}

{% block body %}

<h3>Kayıt Ol!</h3>

<hr>

<form method="post">
    
    {% csrf_token %} <!--Cross in the middle attacklarına karşı korumayı sağlayan bir kod-->
    
    {{form.as_p}}
    
    <br>
    
    <button type="submit" class="btn btn-danger">Kayıt Ol</button>
    
</form>

{% endblock body %}
```
#### user/urls.py dosyamıza aşağıdaki eklemeleri yapıyoruz
```python
from django.contrib import admin

from django.urls import path

from . import views   

app_name="user"

urlpatterns = [

    path('register/',views.register,name="register"),
    
    path('login/',views.loginUser,name="login"),
    
    path('logout/',views.logoutUser,name="logout"),
    
]
```
#### myproject/urls.py aşağıdaki gibi düzenlenir
```python
urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', views.index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.
    
    path('about/', views.about,name="about"),
    
    path('detail/<int:id>', views.detail,name="detail"), # dinamik url tanımlama için
    
    path('article/',include("article.urls")), #article/...
    
    path('user/',include("user.urls")), #user/register user/...
    
]
```
#### user/views.py de aşağıdaki işlemler yapılır
```python
from django.shortcuts import render,redirect # yönlendirme işlemi için redirect'i import ettik

from .forms import RegisterForm

from django.contrib import messages #django mesajlarını kullanabilmek için

from django.contrib.auth.models import User #user modelinden nesne oluşturmak için import ediyoruz

from django.contrib.auth import login # login yapabilmek için import ediyoruz

#Create your views here.

def register(request):

    #request post ise formdaki bilgilerle form oluşturulur
    
    #request get ise boş bir form oluşur
    
    form=RegisterForm(request.POST or None)
    
    if form.is_valid(): #parolalarımızın eşleşip eşleşmediğini kontrol ediyoruz
    
        username=form.cleaned_data.get("username")
        
        password=form.cleaned_data.get("password")
        

        newUser=User(username=username)
        
        newUser.set_password(password)
        
        newUser.save() #kullanıcı bilgilerini alıp veritabanımıza kayıt ediyoruz
        
        login(request,newUser) # giriş yapıyoruz
        
        messages.success(request,"Başarıyla kayıt oldunuz") #kayıt olduğuna dair layout.html sayfasına başarı mesajı iletiyoruz
        
        

        return redirect("index") #anasayfaya yönlendiriyoruz
        
        #post request olsa bile parolalar eşleşmiyor ise aynı sayfayı geri dönüyoruz
        
    context={
    
        "form":form
        
    }
    
    return render(request,"register.html",context)
    

    """
    
    if request.method=="POST": #metodumuzun post olma durumunu kotrol ediyoruz
    
        form=RegisterForm(request.POST) #post ise post'tan gelen verileri form değişkenine alıyoruz
        
        if form.is_valid(): #parolalarımızın eşleşip eşleşmediğini kontrol ediyoruz
        
            username=form.cleaned_data.get("username")
            
            password=form.cleaned_data.get("password")
            

            newUser=User(username=username)
            
            newUser.set_password(password)
            
            newUser.save() #kullanıcı bilgilerini alıp veritabanımıza kayıt ediyoruz
            
            login(request,newUser) # giriş yapıyoruz
            
            return redirect("index") #anasayfaya yönlendiriyoruz
            
        #post request olsa bile parolalar eşleşmiyor ise aynı sayfayı geri dönüyoruz
        
        context={
        
            "form":form
            
        }
        
        return render(request,"register.html",context)
        

    else:
    
        #eğer bir sayfa yenilemesi olduysa yani get request olduysa formumuzu boş döndürüyoruz
        
        form=RegisterForm()
        
        context={
        
            "form":form
            
        }
        
        return render(request,"register.html",context)
        
    """
    

    """form=RegisterForm()
    
    context={
    
        "form":form
        
    }
    
    return render(request,"register.html",context)
    
    """
    
def loginUser(request):

    return render(request,"login.html")
    
def logoutUser(request):

    pass
```
#### Danger message
```
<div style="margin-top:100px;" class="container">
    
        {% if messages %}
        
        
                <!-- aşağıdaki yapı ile djangoda olmayan danger mesajını kullanabiliriz-->
                
                {% for message in messages %}
                
                <!-- <div{% if message.tags %} class="alert alert-{{ message.tags }}"{% endif %}>{{ message }}</div> -->
                
                {% if message.tags == "info" %}
                
                <div class="alert alert-danger">{{ message }}</div>
                
                {% else %}
                
                <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                
                {% endif %}
                
                {% endfor %}
                
            
        {% endif %}
        
        {% block body %}
        
        
        {% endblock  %}
        

    </div>
```
### crispy formları kullanmak için
```
pip install --upgrade django-crispy-forms
```
#### hata vermesi durumunda 
```
pip3 install --user django-crispy-forms
```

#### setting.py için
```python
INSTALLED_APPS = (

    ...
    
    'crispy_forms',
    
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
#### login.html aşağıdaki gibi düzenlenmeli
```
{% extends "layout.html" %}

{% block body %}

{% load crispy_forms_tags %}

<div class="row">
    
  <div class="col-md-6 offset-md-3">
    
    <h3>Giriş yap</h3>
    
    <hr>

    <form method="post">
    
    {% csrf_token %}
    
    {{form|crispy}}
    
    <br>
    
    <button type="submit" class="btn btn-danger">Giriş yap</button>

    </form>

  </div>
  
</div>

{% endblock body %}
```
### dinamik url yapısı
```
<a class="navbar-brand" href="{% url 'index' %}">LinkErp</a>   <!-- dinamik url yapısı kullanıldı -->

<li class="nav-item active">
    
    <a class="nav-link" href="{% url 'erpDb:dashboard' %}">Kontrol Paneli <span class="sr-only">(current)</span></a>
    
</li>
```
### Form'ların tasarımını aldığı Models'ta alanların alabileceği farklı parametreler
```python
#dropdownbox

TITLE_CHOICES = (

    ('MR', 'Mr.'),
    
    ('MRS', 'Mrs.'),
    
    ('MS', 'Ms.'),
    
)

title = models.CharField(max_length=3, choices=TITLE_CHOICES)
```
```
python3 manage.py migrate --fake erpDb zero

python3 manage.py migrate erpDb
```
### Deploy

[DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
[Heroku](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

### Yüklenebilecek bazı paketler
```
pip3 install django-bootstrap4
pip3 install django-model-utils
pip3 install django-bootstrap-datepicker-plus
pip install reportlab
pip install --upgrade --force-reinstall reportlab
pip install django-redis

Hata = ImportError: No module named requests
Çözüm = https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
Use $ sudo pip install requests (or pip3 install requests for python3)
python -m pip install requests

pip3 install numpy
pip3 install pyspark
pip3 install pandas

```
[mongoDb yükleme](https://github.com/selcukakarin/ToolBox/blob/master/mongo_db.md)

[conda yükleme](https://github.com/selcukakarin/ToolBox/blob/master/ubuntu_commands.md)

[pyspark yükleme](https://medium.com/tinghaochen/how-to-install-pyspark-locally-94501eefe421)

## django internationalization komutları

```
django-admin.py makemessages -l tr
django-admin.py makemessages -l tr -i venv
django-admin makemessages --all --ignore venv
django-admin compilemessages --ignore=cache --ignore=outdated/*/locale
python manage.py compilemessages -i "venv*"
```