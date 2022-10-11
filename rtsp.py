import cv2
import requests

cap = cv2.VideoCapture("rtsp://admin:pepsizero0@192.168.0.151:554/cam/realmonitor?channel=1&subtype=0")
detector = cv2.QRCodeDetector()
while(cap.isOpened()):
    ret, frame = cap.read()
    data, bbox, _ = detector.detectAndDecode(frame)
    cv2.imshow('frame', frame)
    print(data)
    if(data == "https://pt.wikipedia.org"):
        requests.get(url='https://maker.ifttt.com/trigger/chamar_alexa/json/with/key/dn_6ohL8PU0W4byjYLYsYr')
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()