from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import json
from PyKakao import Message
import requests
import json
import os


def post_initial_token():
    rest_api_key = os.environ['KAKAO_REST_API_KEY']
    id = os.environ['ID']
    pw = os.environ['PW']
    print(id)

    api = Message(service_key=rest_api_key)
    auth_url = api.get_url_for_generating_code()


    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(service=service, options=options)

    url = f'{auth_url}'
    driver.get(url)

    time.sleep(5)

    WebDriverWait(driver, 10)

    driver.find_element(By.XPATH,'//*[@id="loginId--1"]').send_keys(f'{id}')
    driver.find_element(By.XPATH,'//*[@id="password--2"]').send_keys(f'{pw}')
    driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    time.sleep(30)
    WebDriverWait(driver, 30)
    new_url = driver.current_url
    authorize_code = new_url.split('code=')[1]
    driver.quit()

    url = 'https://kauth.kakao.com/oauth/token'

    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'code': authorize_code
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open("kakao_token.json", "w") as f:
        json.dump(tokens,f)
    print("신규 access_token 발급 성공")
    

if __name__ == '__main__':
    post_initial_token()