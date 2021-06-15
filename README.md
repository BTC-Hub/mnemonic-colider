## mnemonic-colider
Программа создана в первую очередь для изучения языка PYTHON!

Что реализовано:  
#### создание BIP39 Mnemonic для 9 языков. Возможно использовать все сразу или какие-то отдельно 
english, chinese_simplified, chinese_traditional, french, italian, spanish, czech, korean, japanese  

#### Создан поиск по 7 базам данных (BloomFilter).  
по организации BIP-32 доступно только BTC так как остальные производные.  
по организации BIP-44 Доступно 7 баз данных  'ltc.bf','dash.bf','eth.bf','doge.bf','sv.bf','btc.bf','cash-legacy.bf'  
можно искать во всех или только в интересующих.  
по режимам Случайный, Стандартный, Энтропия

## Установка:  
Зависимости: Python 3.7 и выше  
sudo apt-get install libgmp-dev libmpfr-dev libmpc-dev  
sudo pip3 install simplebloomfilter  
sudo pip3 install bitarray==1.9.2    
sudo pip3 install bip-utils  
  
или  
pip install -r requirements.txt  
или  
python -m pip install -r requirements.txt
  
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
Entropy -> Mnemonic -> check valid-> Seed  
Генерирует энтропию 128 бит
  
## Многопоточная версия  
  python mainMT.py -b <BIP 32 или 44> -d <директория с файлами блюм фильтра> -t <количество ядер> -m <режим работы> -c <описание сервера>  
  python mainMT.py -b 32 -d BF -t 2 -m s -c Local_win  
  python mainMT.py -b 44 -d BF -t 3 -m r -c Local_linux  

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
  

    * Version:  Pulsar v3.3.0 multiT  
    * Total kernel of CPU: 6  
    * Used kernel: 2  
    * Mode Search: BIP-32 Стандартный  
    * Dir database Bloom Filter: BF  
    ---------------Load BF---------------  
    Bloom Filter btc.bf Loaded  
    -------------All BF loaded-----------  
    [*] cycle: 1 | total key: 1260 | key/s: 372 in process cpu0 | Found 0  
    [*] cycle: 1 | total key: 1260 | key/s: 376 in process cpu1 | Found 0  
  
------------------------------------------------------------  
    * Version:  Pulsar v3.3.0 multiT  
    * Total kernel of CPU: 6  
    * Used kernel: 2  
    * Mode Search: BIP-44 Энтропия  
    * Dir database Bloom Filter: BF  
    ---------------Load BF---------------  
    Bloom Filter ltc.bf Loaded  
    Bloom Filter dash.bf Loaded  
    Bloom Filter eth.bf Loaded  
    Bloom Filter doge.bf Loaded  
    Bloom Filter cash.bf Loaded  
    Bloom Filter sv.bf Loaded  
    Bloom Filter btc.bf Loaded  
    -------------All BF loaded-----------  
    [*] cycle: 1 | total key: 1260 | key/s: 880 in process cpu0 | Found 0  
    [*] cycle: 2 | total key: 2520 | key/s: 909 in process cpu0 | Found 0  
    [*] cycle: 1 | total key: 1260 | key/s: 922 in process cpu1 | Found 0  
    

exe файл завернут:  
  pyinstaller --runtime-tmpdir .\temp --onefile --clean --name pulsarMT --add-data "mnemonic;mnemonic" --add-data "rezult.txt;." mainMT.py  

