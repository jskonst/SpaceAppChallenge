# -*- coding:utf8 -*-
import socket
import drive
import nxt

host = "192.168.100.176"
port = 5678



def action(a):
    b = nxt.find_one_brick(name='MyNXT')
    drive1 = drive.Drive(b, nxt.PORT_B)
    drive2 = drive.Drive(b, nxt.PORT_C)
    drive1.SetParam(1, 1, 1)
    drive2.SetParam(1, 1, 1)
    drive1.start()
    drive2.start()
    drive1.stop()
    drive2.stop()
    if a == "q":
        drive1.stop()
        drive2.stop()
        drive1.join()
        drive2.join()
    else:
        if a == "w":
            print "Вперед"
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
while 1:
    sock, addr = s.accept()
    while 1:
        buf = sock.recv(1024)
        if buf == "exit":
            sock.send("olol")
            break
        elif buf:
            print buf
            action(buf)
            sock.send(buf)
            break
        sock.close()

