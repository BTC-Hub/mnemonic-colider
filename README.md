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
  

D:\WORK\nem>python mainmt.py 44 bf 3  
* Version:  Pulsar v3.0 multiT  
* Total kernel of CPU: 4  
* Used kernel: 3  
* Mode Search: BIP-44  
* Dir database Bloom Filter: D:\WORK\nem\bf  
---------------Load BF---------------
Bloom Filter ltc.bf Loaded  
Bloom Filter dash.bf Loaded  
Bloom Filter eth.bf Loaded  
Bloom Filter doge.bf Loaded  
Bloom Filter cash.bf Loaded  
Bloom Filter sv.bf Loaded  
Bloom Filter btc.bf Loaded  
name process: cpu1 | cycle: 4493 | total key: 3774120 | key/s: 688    
name process: cpu2 | cycle: 4487 | total key: 3769080 | key/s: 676  
name process: cpu0 | cycle: 4481 | total key: 3764040 | key/s: 674  
  

  

