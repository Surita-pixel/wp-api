from fastapi import FastAPI

import requests
import json
app = FastAPI()

@app.post("/send")
def receiveMessage(message: str):
    url = "https://qp.full-sms.uno/v2/bot/93e841fa-67a4-471a-8e1d-81a3a6768fd2/sendtext"
    payload = json.dumps({
    "recipient": "573026680708@s.whatsapp.net",
    "message": f"{message}"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return {"message": message}


@app.post("/receive")
def receiveMessage():
    url = "https://qp.full-sms.uno/93e841fa-67a4-471a-8e1d-81a3a6768fd2"

    payload = json.dumps({
    "url": "https://n8n.sufficit.com.br/webhook-test/localquepasa",
    "forwardinternal": False,
    "extra": {
        "optional": "ok"
    }
    })
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.dumps(response.text)

