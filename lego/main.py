# -*- coding=utf8 -*-
'''
Created on 14.04.2011

@author: jskonst
'''
import drive
import nxt
b = nxt.find_one_brick(name='MyNXT')
drive1 = drive.Drive(b, nxt.PORT_B)
drive2 = drive.Drive(b, nxt.PORT_C)
drive1.SetParam(1, 1, 1)
drive2.SetParam(1, 1, 1)
drive1.start()
drive2.start()
drive1.stop()
drive2.stop()

while 1:
    a = raw_input()
    if a == "q":
        drive1.stop()
        drive2.stop()
        drive1.join()
        drive2.join()
        break
    else:
        if a == "w":
            print "Вперед"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()
            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)
            drive1.SetParam()
            drive2.SetParam()
            drive1.start()
            drive2.start()
            continue
        if a == "s":
            print "Назад"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(-1)
            drive2.SetParam(-1)
            drive1.start()
            drive2.start()
            continue
        if a == "a":
            print "Влево"

            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(1, 50)
            drive2.SetParam(-1, 50)
            drive1.start()
            drive2.start()
            continue
        if a == "d":
            print "Вправо"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(-1, 50)
            drive2.SetParam(1, 50)
            drive1.start()
            drive2.start()
            continue
        if a == "e":
            print "Стоп"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            continue
