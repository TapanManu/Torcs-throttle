import cv2
import numpy as np
import time
from pynput.keyboard import Key,Controller
keyboard=Controller()
cap=cv2.VideoCapture(0)
hand_cascade=cv2.CascadeClassifier("rpalm.xml")
prev_x,prev_y=0,0
count=0
prev_key=Key.up
while True:
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hands=hand_cascade.detectMultiScale(gray,1.2,5)
	prev_key=Key.up
	#identify central location
	cv2.circle(frame,(300,200),100,(0,255,255),2)
	cv2.circle(frame,(300,200),10,(0,255,0),-1)
	for x,y,w,h in hands:
		#time.time()
		cv2.circle(frame,(int(x+w/2),int(y+h/2)),10,(0,0,255),-1)
		print(x+w/2,y+h/2)
		keyboard.press(Key.up)
		if count>0:
			keyboard.release(Key.right)
			keyboard.release(Key.left)
			if (y+h/2)<200:
				keyboard.release(prev_key)
				keyboard.press(Key.up)
				prev_key=Key.up
				print('up')
				with keyboard.pressed(Key.up):
					if (x+w/2)>340 :
						keyboard.press(Key.left)
						prev_key=Key.left
						print('left')
					elif (x+w/2)<260 :
						keyboard.press(Key.right)	
						prev_key=Key.right
						print('right')
					else:
						keyboard.press(Key.up)
						print('up')
				keyboard.release(Key.up)
			elif (y+h/2)>230 :
				keyboard.release(prev_key)
				keyboard.press(Key.down)
				prev_key=Key.down
				print('down')		
				with keyboard.pressed(Key.down):
					if (x+w/2)>340 :
						keyboard.press(Key.left)
						prev_key=Key.left
						print('left')
					elif (x+w/2)<260 :
						keyboard.press(Key.right)	
						prev_key=Key.right
						print('right')
					else:
						keyboard.press(Key.down)
						print('down')
			else:
				keyboard.release(prev_key)	
				keyboard.press(Key.up)	
	#time.time()
	count+=1
	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
