#all required packages
import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import screen_brightness_control as sbc
import pygetwindow as gw
import pyautogui

#variables
width, height =1280,720
folderPath = "Presentation"

#camera setup
cap =cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#Get the list of presentation images
pathImage = sorted(os.listdir(folderPath), key=len)
#print(pathImage)

#variables
imgNumber =0
hs, ws = int(120*1),int(213*1)
gestureThreshold = 300
buttonPressed =False
buttonCounter=0
buttonDelay= 30
annotations =[[]]
annotationNumber =0
annotationStart = False

#Hand Detector
detector = HandDetector(detectionCon=0.8,maxHands=1)

# Function to adjust brightness
def adjust_brightness(change):
    current_brightness = sbc.get_brightness(display=0)[0]
    new_brightness = max(0, min(100, current_brightness + change))
    sbc.set_brightness(new_brightness)

while True:
    # imports images
    success, img= cap.read()
    img =cv2.flip(img, 1)
    pathFullImage= os.path.join(folderPath,pathImage[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img =detector.findHands(img)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(255,255,0),10)
    print(annotationNumber)
    if hands and buttonPressed is False:
        hand =hands[0]
        fingers=detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        #Constraint value for easier drawing
        xVal = int(np.interp(lmList[8][0],[width//2,w], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150 ,height-150], [0, height]))
        indexFinger =xVal, yVal

        #gesture for slide navigation
        if cy <=gestureThreshold:
            annotationStart =False
            # gesture 1 -left
            if fingers == [1,0,0,0,0]:
                 annotationStart = False
                 print("Left")
                 if imgNumber>0:
                    buttonPressed = True
                    annotations =[[]]
                    annotationNumber=0
                    imgNumber -=1

            # gesture 2 -right
            if fingers == [0, 0, 0, 0, 1]:
                 annotationStart = False
                 print("Right")
                 if imgNumber<len(pathImage)-1:
                    buttonPressed = True
                    annotations =[[]]
                    annotationNumber = 0
                    imgNumber += 1

        # gesture 3 -show pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotationStart = False

        # gesture 4 -line drawing
        if fingers == [0, 1, 0, 0, 0]:
             if annotationStart is False:
                 annotationStart = True
                 annotationNumber +=1
                 annotations.append([])
             cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
             annotations[annotationNumber].append(indexFinger)
        else:
             annotationStart = False

        # gesture 5 - Erase
        if fingers ==[0,1,1,1,0]:
            if annotations:
                if annotationNumber >= 0:
                     annotations.pop()
                     annotationNumber -= 1
                     buttonPressed = True

        # gesture 6 - screen Brightness control
        # Increase brightness
        if fingers == [1, 1, 0, 0, 0]:
            adjust_brightness(10)
            if annotations:
                if annotationNumber >= 0:
                     annotations.pop()
                     annotationNumber -= 1
                     buttonPressed = True

        # Decrease brightness
        if fingers == [1, 1, 1, 0, 0]:
            adjust_brightness(-10)
            if annotations:
                if annotationNumber >= 0:
                     annotations.pop()
                     annotationNumber -= 1
                     buttonPressed = True

        # Minimize Slide Window (ring and pinky fingers up)
        if fingers == [0, 0, 0, 1, 1]:  # Ring and pinky fingers up
            try:
                window = gw.getWindowsWithTitle("Slides")[0]  # Replace "Slides" with the exact title
                if not window.isMinimized:
                    window.minimize()
                    print("Window Minimized")
            except IndexError:
                print("Slide window not found. Please check the window title.")
            except Exception as e:
                print(f"An error occurred: {e}")
            if annotations:
                if annotationNumber >= 0:
                     annotations.pop()
                     annotationNumber -= 1
                     buttonPressed = True

        # Maximize Slide Window
        if fingers == [0, 0, 1, 1, 1]:  # middle , Ring and pinky fingers up
            try:
                window = gw.getWindowsWithTitle("Slides")[0]  # Replace "Slides" with the exact title
                if window.isMinimized:
                    window.maximize()
                    print("Window Maximized")

            except IndexError:
                print("Slide window not found. Please check the window title.")
            except Exception as e:
                print(f"An error occurred: {e}")
            if annotations:
                 if annotationNumber >= 0:
                     annotations.pop()
                     annotationNumber -= 1
                     buttonPressed = True

        # Play/Pause media
        if fingers == [1, 1, 1, 1, 1]:  #all fingers up
            pyautogui.press('space')
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop()
                    annotationNumber -= 1
                    buttonPressed = True

    else:
        annotationStart = False


    #button pressed iteration
    if buttonPressed:
        buttonCounter +=1
        if buttonCounter >buttonDelay:
            buttonCounter=0
            buttonPressed= False

    for i in range (len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j],(0,0,200), 12)


    #Adding webcam images on the slides
    imgSmall = cv2.resize(img,(ws,hs))
    h,w,_ =imgCurrent.shape
    imgCurrent[0:hs, w-ws:w]= imgSmall

    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgCurrent)

    key =cv2.waitKey(1)
    if key ==ord('q'):
        break