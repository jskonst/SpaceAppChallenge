# -*- coding:utf8 -*-
import socket
import drive
import nxt
import json
import requests
import time
import test_sensors

host = "localhost"
port = 5678



b = nxt.find_one_brick(name='MyNXT')
drive1 = drive.Drive(b, nxt.PORT_B)
drive2 = drive.Drive(b, nxt.PORT_C)
drive1.SetParam(1, 1, 1)
drive2.SetParam(1, 1, 1)
drive1.start()
drive2.start()
drive1.stop()
drive2.stop()
def action(a, drive1, drive2):
    StatusOfButton = nxt.Touch(b, nxt.PORT_3).get_sample()
    if a == "q":
        drive1.stop()
        drive2.stop()
        drive1.join()
        drive2.join()
    else:
        if a == "w":
            print "Вперед"
            if StatusOfButton == True :
                return  
            else:
                drive1.stop()
                drive2.stop()
                drive1.join()
                drive2.join()
                drive1 = drive.Drive(b, nxt.PORT_B)
                drive2 = drive.Drive(b, nxt.PORT_C)
                drive1.SetParam(degree=180)
                drive2.SetParam(degree=180)
                drive1.start()
                drive2.start()
        if a == "s":
            print "Назад"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(-1,degree=180)
            drive2.SetParam(-1,degree=180)
            drive1.start()
            drive2.start()
        if a == "a":
            if StatusOfButton == True :
                return  
            print "Влево"

            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(1, 50,degree=180)
            drive2.SetParam(-1, 50,degree=180)
            drive1.start()
            drive2.start()
        if a == "d":
            if StatusOfButton == True :
                return  
            print "Вправо"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(-1, 50,degree=180)
            drive2.SetParam(1, 50,degree=180)
            drive1.start()
            drive2.start()
        if a == "e":
            print "Стоп"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()



def Connect (Ad, Par):
    #Par = get_sensors(b)
    address = requests.post(Ad,Par)   
     
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.bind((host, port))
#s.listen(1)
#Connect(, "waiting")
while 1:
    r=requests.post("http://localhost", data={'waiting':'salt'})
    #print r.request
    if r.content:
        j=json.loads(r.content)
        #print type(j)
        if isinstance(j,dict):
            status=j['status']
            if status == "c" :
                for i in j['command']:
                    action(i, drive1, drive2)
            else:
                time.sleep (5)

#while 1:
#    Connect("http://192.168.100.169:81/api", "waiting")
#    sock, addr = s.accept()
#    while 1:
#
 #       buf = sock.recv(1024)
  #      if buf == "exit":
   #         sock.send("olol")
   #         break
   #     elif buf:
   #         print buf
   #         action(buf, drive1, drive2)
    #        sock.send(buf)
    #        break
     #   sock.close()

