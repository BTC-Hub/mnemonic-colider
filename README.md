# mnemonic-colider

Создание Мнемоник из 9 языков 'english', 'chinese_simplified', 'chinese_traditional', 'french', 'italian', 'spanish','czech','korean','japanese'
Одновременый поиск по 7 базам адресов 'ltc.bf','dash.bf','eth.bf','doge.bf','cash.bf','sv.bf','btc.bf','cash-legacy.bf'
Режимы работы BIP32, BIP44

Зависимости:  
Python 3.7 и выше  
sudo apt-get install libgmp2-dev  
sudo apt-get install libmpfr-dev 
sudo apt-get install libmpc-dev 
sudo pip3 install simplebloomfilter  
sudo pip3 install bitarray==1.9.2  
sudo pip3 install mnemonic  
sudo pip3 install bip-utils==1.6.0  
sudo pip3 install --user gmpy2==2.1.0a2  
sudo pip3 install ecdsa[gmpy2]  


Windows
https://www.lfd.uci.edu/~gohlke/pythonlibs/  
gmpy2‑2.0.8‑cp38‑cp38‑win_amd64.whl  
pip3 install gmpy2-2.0.8-cp38-cp38-win_amd64.whl  

создайте BloobFilter (BF create\Cbloom.py)
пример:
python Cbloom.py <in file> <outfile>  
  in file - текстовый файл с адресами (один адрес на одну срочку)  
  out file - файл блюм фильтра  
  
используйте программу  
  python main.py -b <BIP 32 или 44> -d <директория с файлами блюм фильтра>  
  
файлы с адресами брать здесь  
https://gz.blockchair.com/
  
или на моем ресурсе  
https://drive.google.com/drive/folders/18goTXQiM6MIYmK67ej5jwjRu5nfLCyxw?usp=sharing
