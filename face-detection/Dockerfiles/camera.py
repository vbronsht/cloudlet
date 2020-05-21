#camera.py
# import the necessary packages
#from numba import jit, cuda, numba
import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("alg.xml")
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture("y2mate.com - How to Start a Robot Revolution - Trailer_5hjlyA2eE9A_1080p.mp4")
    def __del__(self):
        #releasing camera
        self.video.release()
    def get_frame(self):
       #extracting frames
        ret, frame = self.video.read()
        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)                    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.ocl.setUseOpenCL(true)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         break
        # encode OpenCV raw frame to jpg and displaying it
      #  frameU =  cv2.UMat.get(frameU)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
