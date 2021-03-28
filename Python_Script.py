import time
import hashlib
F=''
counter = 0
counter2 =0
fo = open("ttt.txt", "r+") #from "arm-none-eabi-readelf -x <elfname> > input.txt"
for _ in range(2):
        next(fo)
strb = ''
m = hashlib.sha256()
#m2 = hashlib.sha256()
while True:
        #str = fo.readline()
        #str = str[12:48]
        #str = str.replace(' ', '')
        #F += str
        #print(F)
        #counter=counter+1

        #Remove later (Bytes)
        #b = '10b5054c' # test first address
        str = fo.readline()
        str = str[12:48]
        str = str.replace(' ', '')
        #print(type(b))
        #strb = strb + str
        A = (bytes.fromhex(str))
        #B = (bytes.fromhex(b))
        #print(m.update(A))
        #hash = m.digest()
        #print(hash)
        #m2.update(B)
        #print(m2.digest())
        #time.sleep(3)
        #AA = print(type(bytes.fromhex(b)))
        #print(A)
        #B = byteobj = b.encode('latin-1')
        #print(type(byteobj))
        m.update(A)
        counter = counter + 1
        #hash = m.digest()
        #F = ''
        #print('hash of 10b5054c is: ',hash)
        #time.sleep(5)
        #Remove later
        if counter2<7: #this counter to read 7 blocks each is 16KB
            if counter == 1024 : #Counter that hashes 16KB and stores it in output.dat
                hash = m.digest()
                #hs = hashlib.sha256(bytes(F, encoding='utf8'))
                #hash = hs.hexdigest()
                #F=''
                f = open("output.dat", "ab+")
                f.write(bytes(hash))
                print(hash)
                #time.sleep(5)
                #print(strb)
                #time.sleep(52)
                counter=0
                counter2=counter2+1
                time.sleep(5)
                m = hashlib.sha256()
                #m = hashlib.sha256()
