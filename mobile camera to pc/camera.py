import requests

import numpy as np
import cv2

while True: 
    images=requests.get("/shot.jpg") #download ip webcam app from play store in your phone and then insert the ip address in here 
    video=np.array(bytearray(images.content),dtype=np.uint8)
    render = cv2.imdecode(video,-1)
    cv2.imshow('frame',render)
    
    if (cv2.waitkey(1) and 0xFF==ord('q')):
        break
