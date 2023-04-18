import cv2 as cv
import colorama
colorama.init()
asciilst = [" ",".","^","!","&","?","#","%","@"]
imgres = (250,100)     
def toAscii(i):
    global asciilst
    return asciilst[int(i/29)]
vidCap = cv.VideoCapture(0)
if not vidCap.isOpened():
    print("Cant open camera")
    exit()
while True:
    print('\033[2J\033[H', end='')
    ret, frame = vidCap.read()
    frame = cv.resize(frame, imgres)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)   
    print("\n".join(''.join(list(map(toAscii,i)))for i in frame), end = '')          
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
vidCap.release()    
cv.destroyAllWindows()