from typing import Optional
import uvicorn 
from fastapi import FastAPI
import requests
from shodan import Shodan
from pydantic import BaseModel
import shodan

app = FastAPI()
api = Shodan("SokScNZPwvp63UA9VrYylWmGcAkucAqj")

#get
@app.get("/ip/{ip}")
def get_ip_info_request(ip : str):    
    try:
        ipInfo = api.host({ip})
        return {'Ip': ipInfo['ip_str'],
                'Pays': ipInfo['country_name'],
                'Ville': ipInfo['city'],
                'Os': ipInfo['os'],
                'Ports': ipInfo['ports']
                }
    except shodan.APIError as e:
        return {'error': str(e)}
       

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")


