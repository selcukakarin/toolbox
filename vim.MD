### Vim installation

[Kaynak](https://phoenixnap.com/kb/how-to-install-vim-ubuntu)

[Kaynak](https://www.cyberciti.biz/faq/howto-install-vim-on-ubuntu-linux/)

```
sudo apt-get install libncurses5-dev libncursesw5-dev
sudo apt install git
sudo apt install make
sudo apt install build-essential
sudo git clone https://github.com/vim/vim.git
cd vim/src
sudo make
sudo make install
vim -v
sudo apt remove vim
```

#### Vim commands

```
insert mode = i
command mode = esc
top of page = H
bottom of page = L
middle of page = M
move to first line = ((
move to last line = ))
undo changes = u
redo changes = ctrl + r
command mode delete like backspace = X
command mode delete = x
insert mode delete = backspace
command mode copy current line = yy
command mode paste = p
command mode selected copy current line = select and press y
case sensitive search = /searchkey enter
find next = n
find previous = right shit + n
case insensitive search = /\csearchkey enter
replace = :%s/previousval/nextval/gci
g = Extend search and replace for all matches
c = Confirm your actions
i = Case insensitive search
y = yes,replace this match
n = No, dont replace this match and move to the next one
a = QUIT without replacing any match
I = Replace this match
^E = Scroll the screen up
^Y = Scroll the screen down
save = :w
save and quit = :wq
quit = :q
quit force = :q!
```