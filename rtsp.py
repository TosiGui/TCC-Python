import cv2
import requests
from pymongo import MongoClient
from fastapi import FastAPI
from dotenv import dotenv_values

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tcc"]
user = mydb["customers"]

for x in mycol.find({},{ "name": 1, "urlRTSP": 1, "urlIFTTT": 1, "password": 1 }):
    cap = cv2.VideoCapture(x.urlRTSP)
    detector = cv2.QRCodeDetector()
    while(cap.isOpened()):
        ret, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)
        cv2.imshow('frame', frame)
        print(data)
        if(data == password):
            requests.get(url=x.urlIFTTT)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    app.mongodb_client.close()

def shutdown_db_client():
    app.mongodb_client.close()
