## Vm'de kurulu Ubuntu'ya shared folder oluşturma

[Kaynak](https://gist.github.com/estorgio/0c76e29c0439e683caca694f338d4003)
```
- önce vm'de >> Aygıtlar ( devices ) >> Paylaşılan Klasörler ( Shared Folder ) >> Yeni bir shared folder oluşturulur sadece kalıcı yap ( persistence ) özelliğinde tik olmalıdır.

- Yine aygıtlar sekmesindeki misafir kalıbını yerleştir seçeneği ile yükleme işlemi gerçekleşmelidir.

- sudo shutdown -r now komutu ile restart işlemi yapılmalıdır.

- mkdir ~/shared ile Home klasöründe shared klasörü oluşturuldu.

- sudo mount -t vboxsf windowstaOlusturulanKlasorAdi ~/shared
```
### Her restart'da shared folder'ın oto-mount edilmesi için
```
- sudo nano /etc/fstab

- UbuntuGate	/home/< username >/shared	vboxsf	defaults	0	0        -- son satıra eklenmeli

*Örnek Yazım
- UbuntuGate	/home/selcuk/shared	vboxsf	defaults	0	0        -- son satıra eklenmeli

- UbuntuGate = windowstaOlusturulanKlasorAdi

- eklendikten sonra ctrl+x'e tıklanır gelen soruya y yanıtı verilip kayıt gerçekleştirilir.

- sudo nano /etc/modules

- vboxsf        -- son satıra eklenmeli

- eklendikten sonra ctrl+x'e tıklanır gelen soruya y yanıtı verilip kayıt gerçekleştirilir.

- sudo shutdown -r now
```

## For windows
host ubuntu guest windows

source : https://www.youtube.com/watch?v=ibSUJajxgO4