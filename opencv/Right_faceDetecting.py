#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import cv

capture = cv.CaptureFromCAM(0)  

while True:  
    image = cv.QueryFrame(capture)  
    cv.NamedWindow('Face detection', cv.CV_WINDOW_AUTOSIZE)
    cv.SaveImage("./img.jpg", image)
    image_size = cv.GetSize(image)
    center_of_image_size = image_size[0]/2
    grayscale = cv.CreateImage(image_size, 8, 1)

    storage = cv.CreateMemStorage(0)
    cascade = cv.Load('haarcascade_frontalface_default.xml')
    cv.CvtColor(image, grayscale, cv.CV_RGB2GRAY)

    cv.EqualizeHist(grayscale, grayscale)
    faces = cv.HaarDetectObjects(image=grayscale, cascade=cascade, 
        storage=storage, scale_factor=1.2, 
        min_neighbors=2, flags=cv.CV_HAAR_DO_CANNY_PRUNING)

    if faces:
        print 'face detected!'
        for i in faces:
            print i
            cv.Rectangle(image, (i[0][0], i[0][1]),
                     (i[0][0]+i[0][2], i[0][1]+i[0][3]),
                     (255, 255, 0), 3, 8, 0) 
            max = faces[0]
            pos = 0
            if len(faces)>1 :             
                for j in range(0,len(faces)):
                    if faces[j]>max: max=faces[j];pos=j
            print ("max=", max, ", pos=", pos)
            max_face=faces[pos]
            coordinates = max_face[0]
            x = coordinates[0]
            y = coordinates[1]
            wight = coordinates[2]
            height = coordinates [3]
            center_of_rectangle = wight/2
            print center_of_rectangle
            print center_of_image_size     
            difference = center_of_image_size - center_of_rectangle    
            print difference         


    cv.ShowImage('Face detection', image)
    if cv.WaitKey(10) == 27:  # Ждем нажатия кнопки Esc и после 10 милисекунд
        break  # Выходим из цикла
cv.DestroyWindow('Face detection')
