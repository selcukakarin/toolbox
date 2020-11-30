### Move etmek isterken permission denied sorununu aşağıdaki komut ile çözebiliriz
```
sudo mv lnkclouderp.bak /var/lib/postgresql
```
### ubuntuda yüklü tüm paketler
```
dpkg --get-selections

pip freeze
```

### linux'ta requirements.txt oluşturmak için
```
pip freeze > requirements.txt
```

### linux'ta bir dosyayı bir klasöre kopyalama sırasında permission denied hatası almanın çözümü
```
sudo nautilus
```

## Vs Code Kurulum
```
sudo snap install --classic code
```

## Virtual environment install
```
FOR UBUNTU

sudo apt-get install python3-venv

python3 -m venv myvenv

source myvenv/bin/activate

deactivate
```
```
FOR WINDOWS

- önce venv için bir klasor oluştur

- cd blog

- pip install virtualenv 

- virtualenv venv

- venv\Scripts\activate

- deactivate

```

## pip kurulum
```
sudo apt install python3-pip
```

## ImageField için pillow yüklenmeli
```
pip3 install Pillow
```
[kaynak](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

## Conda
[Kaynak](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

## Hayat kurtaran yeniden ubuntu paketlerini yükleme kodu
```
sudo apt-get install --reinstall ubuntu-desktop
```

## Ubuntu sistem özellikleri
```
sudo lshw -html > system_info.html
```

## Jupyter kurulum
```
sudo apt install jupyter-notebook
```

## Sqlite kurulum
[Kaynak](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/)
```
sudo apt-get update
sudo apt-get install sqlite3
sqlite3 --version
sudo apt-get install sqlitebrowser
```

## Typora setup
[Kaynak](https://connectwww.com/how-to-install-typora-on-ubuntu-real-live-preview-markdown-editor/60679/#:~:text=Open%20your%20terminal%20app%20in,terminal%20to%20add%20the%20key.&text=type%20your%20ubuntu%20password.,terminal%20to%20add%20its%20PPA.)
```
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
sudo apt-get install typora
sudo apt remove typora
sudo apt autoremove
```

## pygraphviz setup
[Kaynak](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
[Kaynak2](https://stackoverflow.com/questions/40266604/pip-install-pygraphviz-fails-failed-building-wheel-for-pygraphviz)
```
sudo apt-get install python-dev graphviz libgraphviz-dev pkg-config
pip install pygraphviz
pip install pyparsing pydot
add django_extensions to installed_apps
pip install django-extensions
from django.conf import settings; 'django_extensions' in settings.INSTALLED_APPS
```

## run a sh file on ubuntu
Give execute permission to your script:
```
chmod +x /path/to/yourscript.sh
```
And to run your script:
```
/path/to/yourscript.sh
```

## create ppk file using pem file
[Kaynak](https://aws.amazon.com/premiumsupport/knowledge-center/convert-pem-file-into-ppk/)

To install PuTTY, run one of the following commands:
```
$sudo apt-get install putty-tools
```
On the instance shell, run the puttygen command to convert your .pem file to a .ppk file:
```
$ sudo puttygen pemKey.pem -o ppkKey.ppk -O private
```
Run the puttygen command to convert a .ppk file into a .pem file:
```
$ sudo puttygen ppkkey.ppk -O private-openssh -o pemkey.pem
```

## Nginx kurulum aşamaları
```
sudo apt-get remove apache2*

sudo apt install nginx

sudo systemctl enable nginx.service

sudo systemctl start nginx.service

sudo systemctl status nginx.service
```

### How to Uninstall/Clean MySQL from Windows completely

[Source](https://old.windowsvalley.com/uninstall-mysql-from-windows/)

Run Command Prompt as Administrator and execute the following command to stop and remove MySQL service.

Net stop MySQL

Sc delete MySQL

Go to Control Panel >> Programs >> Programs and Features, select MySQL Server 5.x and click Uninstall. (If you can uninstall MySQL from Control Panel)

Open Windows Explorer and go to Organize > Folder and search options, Select the “View” tab and under “Hidden files and Folders” choose “Show hidden files and folders”. Now explore the following locations and delete following folders.

C:\Program Files\MySQL

C:\Program Files (x86)\MySQL

C:\ProgramData\MySQL

And if exists, delete it too

C:\Users\[User-Name]\AppData\Roaming\MySQL

Restart your PC and reinstall MySQL. That’s all!

### uninstall anaconda in ubuntu

[Source](https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-18-04/#uninstalling-anaconda)

### remove jupyter notebook password

[Source](https://stackoverflow.com/questions/48230706/how-to-remove-password-for-jupyter-notebooks-and-set-token-again)

### jupyter notebook permission denied resolution

[Source](https://github.com/jupyter/notebook/issues/4500)
