from PyKakao import Message
import requests
import json
import os

rest_api_key = os.environ['KAKAO_REST_API_KEY']

def renew_token():
    with open("kakao_token.json","r") as f:
        token_data = json.load(f)
    refresh_token = token_data["refresh_token"]


    redirect_uri = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": f"{rest_api_key}",
        "refresh_token": refresh_token
    }

    resp = requests.post(redirect_uri, data=data)
    new_token = resp.json()

    with open('token.json','w') as f:
        json.dump(new_token,f)

def load_latest_token():
    with open("token.json", "r") as f:
        latest_token  = json.load(f)
    return latest_token

def post_text_message(new_token,message):

    api = Message(service_key=rest_api_key)
    access_token = new_token["access_token"]
    api.set_access_token(access_token)

    text = message
    link = {
                "web_url": "https://map.naver.com/p/directions/14129734.6092034,4490014.3475417,%EA%B2%BD%EA%B8%B0%20%EA%B5%B0%ED%8F%AC%EC%8B%9C%20%EA%B3%A0%EC%82%B0%EB%A1%9C%20596-15%20%EC%82%B0%EB%B3%B8%20%EC%9D%B4%ED%8E%B8%ED%95%9C%EC%84%B8%EC%83%81%20%EC%84%BC%ED%8A%B8%EB%9F%B4%ED%8C%8C%ED%81%AC,,ADDRESS_POI/14145044.9687655,4510009.7720918,%EB%8F%99%EC%9D%BC%ED%83%80%EC%9B%8C,21818344,PLACE_POI/-/transit?c=11.00,0,0,0,dh",
                "mobile_web_url": "https://map.naver.com/p/directions/14129734.6092034,4490014.3475417,%EA%B2%BD%EA%B8%B0%20%EA%B5%B0%ED%8F%AC%EC%8B%9C%20%EA%B3%A0%EC%82%B0%EB%A1%9C%20596-15%20%EC%82%B0%EB%B3%B8%20%EC%9D%B4%ED%8E%B8%ED%95%9C%EC%84%B8%EC%83%81%20%EC%84%BC%ED%8A%B8%EB%9F%B4%ED%8C%8C%ED%81%AC,,ADDRESS_POI/14145044.9687655,4510009.7720918,%EB%8F%99%EC%9D%BC%ED%83%80%EC%9B%8C,21818344,PLACE_POI/-/transit?c=11.00,0,0,0,dh"
            }
    button_title = "바로 확인"

    api.send_text(text=text, link=link, button_title=button_title)