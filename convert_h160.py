import base58

i = 0
ii = 0
adr58:str = ""

with open("sv.txt", "r") as f:
    for adr58 in f:
        if i >= 1000:
            ii = ii + i
            i = 1
            print(str(ii),end='\r')
        #print(adr58)
        adr160 = base58.b58decode_check(adr58).hex()[2:]
        open('sv160.txt', 'a').write(adr160+'\n')
        i = i + 1