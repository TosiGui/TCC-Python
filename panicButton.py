from flask import Flask, request
import requests

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        requests.get(url='https://maker.ifttt.com/trigger/test/json/with/key/dn_6ohL8PU0W4byjYLYsYr')
        return "Webhook received!"

app.run(host='0.0.0.0', port=8000)