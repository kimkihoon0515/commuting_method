from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(service=service, options=options)

url = "https://map.naver.com/p/directions/14129734.6092034,4490014.3475417,%EA%B2%BD%EA%B8%B0%20%EA%B5%B0%ED%8F%AC%EC%8B%9C%20%EA%B3%A0%EC%82%B0%EB%A1%9C%20596-15%20%EC%82%B0%EB%B3%B8%20%EC%9D%B4%ED%8E%B8%ED%95%9C%EC%84%B8%EC%83%81%20%EC%84%BC%ED%8A%B8%EB%9F%B4%ED%8C%8C%ED%81%AC,,ADDRESS_POI/14138490.1988488,4507890.0897346,%EC%84%9C%EC%B4%88%EC%97%AD1%EB%B2%88%EC%B6%9C%EA%B5%AC,21406506,PLACE_POI/-/car?c=11.00,0,0,0,dh"
# url = "https://map.naver.com/p/directions/14129734.6092034,4490014.3475417,%EA%B2%BD%EA%B8%B0%20%EA%B5%B0%ED%8F%AC%EC%8B%9C%20%EA%B3%A0%EC%82%B0%EB%A1%9C%20596-15%20%EC%82%B0%EB%B3%B8%20%EC%9D%B4%ED%8E%B8%ED%95%9C%EC%84%B8%EC%83%81%20%EC%84%BC%ED%8A%B8%EB%9F%B4%ED%8C%8C%ED%81%AC,,ADDRESS_POI/14138490.1988488,4507890.0897346,%EC%84%9C%EC%B4%88%EC%97%AD1%EB%B2%88%EC%B6%9C%EA%B5%AC,21406506,PLACE_POI/-/walk?c=11.00,0,0,0,dh"
driver.get(url)

time.sleep(5)

WebDriverWait(driver, 10)

subway_hour = 1

subway_miniute = 20

bus_hour = 0

bus_miniute = 0

bus_remain_time = 28

real_time = ""

flag = True

for i in range(1, 5):
    try:
        element = driver.find_element(
            By.XPATH,
            f'//*[@id="section_content"]/div/div/div/div/div[2]/div/div[2]/ul/li[1]/div/div/div[2]/strong/span[{i}]',
        )
        # element = driver.find_element(By.XPATH,f'//*[@id="section_content"]/div/div/div/div/div[2]/div/div[1]/ul/li[1]/div/div/strong/span[{i}]')
        real_time += element.text

        if element.text.isdigit() and flag:
            if int(element.text) >= 10:
                bus_miniute += int(element.text)
                continue
            bus_hour += int(element.text)
            flag = False
        elif element.text.isdigit() and not flag:
            bus_miniute += int(element.text)
    except Exception:
        pass

if bus_miniute + bus_remain_time >= 60:
    bus_miniute = bus_miniute + bus_remain_time - 60
    bus_hour += 1
else:
    bus_miniute += bus_remain_time

if bus_hour > subway_hour:
    print(f"전철이 더 빠르고 {subway_hour}시간 {subway_miniute}분 걸립니다.")
else:
    if bus_hour == subway_hour:
        if bus_miniute > subway_miniute:
            print(f"전철이 더 빠르고 {subway_hour}시간 {subway_miniute}분 걸립니다.")
        else:
            print(f"버스가 더 빠르고 {bus_hour}시간 {bus_miniute}분 걸립니다.")
    else:
        print(f"버스가 더 빠르고 {bus_hour}시간 {bus_miniute}분 걸립니다.")

driver.quit()
