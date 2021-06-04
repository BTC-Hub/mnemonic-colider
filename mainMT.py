# #!/usr/bin/python3
# encoding=utf8
# -*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import freeze_support
import smtplib
from bip_utils import Bip32, Bip32Utils, Bip44, Bip44Coins, Bip44Changes
from bloomfilter import BloomFilter
from mnemonic import Mnemonic
import sys, os
import time
from colorama import init, Fore, Back, Style
init()


class email:
    host:str = 'smtp.timeweb.ru'
    port:int = 25
    password:str = 'Vfhbyfl66$'
    subject:str = '--- Find Mnemonic ---'
    to_addr:str = 'info@quadrotech.ru'
    from_addr:str = 'info@quadrotech.ru'


class inf:
    version:str = ' Pulsar v3.0 multiT '
    mnemonic_lang = ['english', 'chinese_simplified', 'chinese_traditional', 'french', 'italian', 'spanish']
    #fl_44:list = ['ltc.bf','dash.bf','eth.bf','doge.bf','cash.bf','sv.bf','btc.bf']
    #fl_32:list = ['btc.bf']
    count_32:int = 720
    count_44:int = 840
    process_count_work:int = 1 #количество процессов
    type_bip:int = 32
    dir_bf:str = ''
    process_time_work = 0.0


def load_BF(bf_file):
    global bf_ltc
    global bf_dash
    global bf_eth
    global bf_doge
    global bf_cash
    global bf_sv
    global bf_btc
    try:
        fp = open(inf.dir_bf+'/'+bf_file, 'rb')
    except FileNotFoundError:
        print('\n'+'File: '+ fl + ' не найден.')
        sys.exit()
    else:
        if bf_file == 'ltc.bf':
            bf_ltc = BloomFilter.load(fp)
        if bf_file == 'dash.bf':
            bf_dash = BloomFilter.load(fp)
        if bf_file == 'eth.bf':
            bf_eth = BloomFilter.load(fp)
        if bf_file == 'doge.bf':
            bf_doge = BloomFilter.load(fp)
        if bf_file == 'cash.bf':
            bf_cash = BloomFilter.load(fp)
        if bf_file == 'sv.bf':
            bf_sv = BloomFilter.load(fp)
        if bf_file == 'btc.bf':
            bf_btc = BloomFilter.load(fp)
        print('Bloom Filter '+bf_file+' Loaded')



def send_email(text):
    BODY:str = '\r\n'.join(('From: %s' % email.from_addr, 'To: %s' % email.to_addr, 'Subject: %s' % email.subject, '', text)).encode('utf-8')
    server = smtplib.SMTP(email.host,email.port)
    server.login(email.from_addr, email.password)
    try:
        server.sendmail(email.from_addr, email.to_addr, BODY)
    except UnicodeError:
        print('\n'+'Error Encode UTF-8')
    finally:
        server.quit()


def save_rezult(text:str):
    try:
        f_rez = open('rezult.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        print('\n'+'Файл rezult.txt не найден.')
    else:
        try:
            tf:str = text+'\n'
            f_rez.write(tf)
        except UnicodeError:
            print('\n'+'Error Encode UTF-8')
        finally:
            f_rez.close()


def work32(bf_btc):
    for mem in inf.mnemonic_lang:
        mnemo = Mnemonic(mem)
        mnemonic:str = mnemo.generate(strength=128)
        seed_bytes:bytes = mnemo.to_seed(mnemonic, passphrase='')
        bip32_ctx = Bip32.FromSeed(seed_bytes)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0'/" + str(num))  # Bitcoin Core address primary m/0'/0'/0
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0'/" + str(num) + "'")  # Bitcoin Core hardened addresses primary m/0'/0'/0'
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0/" + str(num))  # Miltibit HD address
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0/" + str(num) + "'")  # Miltibit HD address
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("44'/0'/0'/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
        #----------------------------------------------------------------


def work44(bf_ltc,bf_dash,bf_eth,bf_doge,bf_cash,bf_sv,bf_btc):
    for mem in inf.mnemonic_lang:
        mnemo = Mnemonic(mem)
        mnemonic:str = mnemo.generate(strength=128)
        seed_bytes:bytes = mnemo.to_seed(mnemonic, passphrase="")

        # btc
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_btc:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)

        # btc_cash
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_CASH)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()[12:]
            if bip_addr in bf_cash:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
        # ltc
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.LITECOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_ltc:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | LITECOIN'
                print(res)
                save_rezult(res)
                send_email(res)

        # dash
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DASH)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_dash:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | DASH'
                print(res)
                save_rezult(res)
                send_email(res)

        # ETH
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_eth:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | ETHEREUM'
                print(res)
                save_rezult(res)
                send_email(res)

        # DOGE
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DOGECOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_doge:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | DOGECOIN'
                print(res)
                save_rezult(res)
                send_email(res)

        # sv
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_SV)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_sv:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | BITCOIN_SV'
                print(res)
                save_rezult(res)
                send_email(res)


def run32(bf_btc):
    ind:int = 1
    while ind > 0:
        start_time = time.time()
        work32(bf_btc)
        inf.process_time_work = time.time() - start_time
        print(Fore.YELLOW+'cycle: {:d} | total key: {:d} | key/s: {:d} in process {:s}'.format(ind, inf.count_44*(ind), int(inf.count_32/inf.process_time_work), multiprocessing.current_process().name),flush=True)
        ind +=1


def run44(bf_ltc,bf_dash,bf_eth,bf_doge,bf_cash,bf_sv,bf_btc):
    ind:int = 1
    while ind > 0:
        start_time = time.time()
        work44(bf_ltc,bf_dash,bf_eth,bf_doge,bf_cash,bf_sv,bf_btc)
        inf.process_time_work = time.time() - start_time
        print(Fore.YELLOW+'[*] cycle: {} | total key: {} | key/s: {:d} in process {:s}'.format(ind, inf.count_44*(ind), int(inf.count_44/inf.process_time_work), multiprocessing.current_process().name),flush=True)
        ind +=1

if __name__ == "__main__":
    freeze_support()
    print('* Version: {} '.format(inf   .version))
    if len (sys.argv) == 4:
        inf.type_bip:int = int(sys.argv[1])
        inf.dir_bf:str = os.getcwd()+'/'+sys.argv[2]
        inf.process_count_work:int = int(sys.argv[3])
        print('* Total kernel of CPU: {} '.format(multiprocessing.cpu_count()))
        print('* Used kernel: {}'.format(inf.process_count_work))
        print('* Mode Search: BIP-{}'.format (inf.type_bip))
        print('* Dir database Bloom Filter: {}'.format (inf.dir_bf))
    else:
        print ("Не хватает параметров.")
        sys.exit()
    if inf.process_count_work < 1:
        print('количество процессов должно быть больше 0')
        sys.exit()
    if inf.process_count_work > multiprocessing.cpu_count():
        print('Указаное количество процессов превышает допустимое')
        print('ИСПРАВЛЕНО на допустимое количество процессов')
        inf.process_count_work = multiprocessing.cpu_count()

    if inf.type_bip == 32:
        print('---------------Load BF---------------')
        load_BF('btc.bf')
        procs = []
        try:
            for index in range(inf.process_count_work):
                proc = multiprocessing.Process(target=run32, name= 'cpu'+str(index), args = (bf_btc, ))
                procs.append(proc)
                proc.start()
            for proc in procs:
                proc.join()
        except KeyboardInterrupt:
            print('\n'+'Прервано пользователем.')
            for proc in procs:
                proc.terminate()
            sys.exit()
#--------------------------------------------------
    if inf.type_bip == 44:
        print('---------------Load BF---------------')
        load_BF('ltc.bf')
        load_BF('dash.bf')
        load_BF('eth.bf')
        load_BF('doge.bf')
        load_BF('cash.bf')
        load_BF('sv.bf')
        load_BF('btc.bf')
        procs = []
        try:
            for index in range(inf.process_count_work):
                #proc = multiprocessing.Process(target=work32, name= 'cpu'+str(index),args = (bf_btc, ))
                proc = multiprocessing.Process(target=run44, name= 'cpu'+str(index), args = (bf_ltc,bf_dash,bf_eth,bf_doge,bf_cash,bf_sv,bf_btc,))
                procs.append(proc)
                proc.start()
            for proc in procs:
                proc.join()
        except KeyboardInterrupt:
            print('\n'+'Прервано пользователем.')
            for proc in procs:
                proc.terminate()
            sys.exit()
    print('\n'+'Программа завершила работу')