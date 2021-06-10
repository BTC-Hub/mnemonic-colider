## mnemonic-colider
Программа создана в первую очередь для изучения языка PYTHON
все что реализовано легко просто и доступно для самого обычного пользователя!

Что я реализовано:
создание BIP39 Mnemonic для 9 языков. Возможно использовать все сразу или какие-то отдельно 'english', 'chinese_simplified', 'chinese_traditional', 'french', 'italian', 'spanish','czech','korean','japanese'  
Создан поиск по 7 базам данных (BloomFilter).  
по организации BIP-32 доступно только BTC так как остальные производные.  
по организации BIP-44 Доступно 7 баз данных  'ltc.bf','dash.bf','eth.bf','doge.bf','sv.bf','btc.bf','cash-legacy.bf'  
можно искать во всех или только в интересующих.  
по режимам Случайный, Стандартный, Энтропия

## Установка:  
Зависимости: Python 3.7 и выше  
sudo apt-get install libgmp-dev libmpfr-dev libmpc-dev  
sudo pip3 install simplebloomfilter  
sudo pip3 install bitarray==1.9.2  
sudo pip3 install mnemonic  
sudo pip3 install bip-utils==1.6.0  
sudo pip3 install --user gmpy2==2.1.0a2  
sudo pip3 install ecdsa[gmpy2]  
  
или  
pip install -r requirements.txt  
или  
python -m pip install -r requirements.txt
  
Windows
https://www.lfd.uci.edu/~gohlke/pythonlibs/  
gmpy2‑2.0.8‑cp38‑cp38‑win_amd64.whl  
pip3 install gmpy2-2.0.8-cp38-cp38-win_amd64.whl  

создайте BloobFilter (BF create\Cbloom.py)
пример:
python Cbloom.py <in file> <outfile>  
  in file - текстовый файл с адресами (один адрес на одну срочку)  
  out file - файл блюм фильтра  
  
## Добавлен режим работы  
#### Стандартный:  
Mnemonic->check valid->seed  
работает с языками BIP-39  'english', 'chinese_simplified', 'chinese_traditional', 'french', 'italian', 'spanish','czech','korean','japanese'  
#### Случайный:  
Генерирует SEED 64 байта без проверок  
#### Энтропия:  
Entropy -> Seed  
Генерирует энтропию 128 бит с проверкой CRC и потом генерирует сразу SEED  
языки не поддерживает  

## Однопоточная версия  
  python main.py -b <BIP 32 или 44> -d <директория с файлами блюм фильтра>  
  python main.py -b 32 -d BF  
  
## Многопоточная версия  
  python mainMT.py <BIP 32 или 44> <директория с файлами блюм фильтра> <количество ядер> <режим работы> <описание сервера>  
  python mainMT.py 32 BF 2 s Local_win  
  python mainMT.py 44 BF 3 r Local_linux  

## Не забудьте настроить параметры своей почты для отправки найденных мнемоник  
    host:str = 'smtp.mail.ru'  
    port:int = 25  
    password:str = 'adfgvfdvbfdsgbdf'  
    to_addr:str = 'info@mail.ru'  
    from_addr:str = 'info@mail.ru'  
  
  
  
файлы с адресами брать здесь  
https://gz.blockchair.com/  
  
или на моем ресурсе  
https://drive.google.com/drive/folders/1i7OxFbJ2x-xnqd1ANStF_eIKutAxdfoL?usp=sharing  
  [*] Update file BTC (35M address)
  

D:\WORK\nem>python mainmt.py 44 bf 3 s Local  
* Version:  Pulsar v3.2 multiT  
* Total kernel of CPU: 4  
* Used kernel: 3  
* Mode Search: BIP-44 Стандартный  
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
  

exe файл завернут:  
  pyinstaller --runtime-tmpdir .\temp --onefile --clean --name pulsarMT --add-data "mnemonic;mnemonic" --add-data "rezult.txt;." mainMT.py

