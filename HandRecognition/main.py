import cv2
import random
from cvzone.HandTrackingModule import HandDetector
import threading
import time

def func():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cur=0

    if len(hands) == 1:
        if detector.fingersUp(hands[0]) == [1, 0, 0, 0, 0]:
            cur =6
        elif detector.fingersUp(hands[0]) == [1, 0, 0, 0, 1]:
            cur =10
        elif detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0]:
            cur =7
        elif detector.fingersUp(hands[0]) == [1, 1, 1, 0, 0]:
            cur =8
        elif (detector.fingersUp(hands[0]) == [1, 1, 1, 1, 0]) or (detector.fingersUp(hands[0]) == [1, 0, 1, 1, 1]):
            cur =9
        elif detector.fingersUp(hands[0]) == [1, 1, 1, 1, 1]:
            cur =5
        elif detector.fingersUp(hands[0]) == [0, 1, 0, 0, 0]:
            cur = 1
        elif detector.fingersUp(hands[0]) == [0, 1, 1, 0, 0]:
            cur = 2
        elif (detector.fingersUp(hands[0]) == [0, 1, 1, 1, 0]) or (detector.fingersUp(hands[0]) == [0, 0, 1, 1, 1]):
            cur = 3
        elif detector.fingersUp(hands[0]) == [0, 1, 1, 1, 1]:
            cur = 4
    cv2.imshow("Image", img)
    cv2.waitKey(10)
    return cur
cap = cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8,maxHands=1)
prev=5
cur=0
l=[1,2,3,4,5,6,7,8,9,10]

score=0
while(True):
    cur=func()
    if prev!=cur and cur!=0:
        z=random.choice(l)
        print(z, end="  ")
        print(cur)
        score+=cur
        if z==cur:
            print("Out")
            print("score=",score)
            score=0
        prev=cur
    if cur==0:
        prev=0




