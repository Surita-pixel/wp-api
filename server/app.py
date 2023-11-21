import requests
import json
from fastapi import FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()
allowed_hosts = ['*']

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=allowed_hosts
)


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