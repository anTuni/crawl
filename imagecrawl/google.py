from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
# 검색어 배열
candidates = ['유재석', '안철수', '제니', '박지성', '엄홍길', '김택진', '기안84', '데니스홍']
#이미지 저장 경로
savepath = "D:/sources/crawl/imagecrwal/images/"
#배열 map
for candidate in candidates:
    #크롬 드라이버 열기
    driver = webdriver.Chrome()
    #크롬 검색 사이트로 이동
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    #검색어 입력창 선택 
    elem = driver.find_element_by_name("q")
    #검색어 입력
    elem.send_keys(candidate)
    #검색어 입력 후 enter   
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll = 0
    while scroll < 5:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            if not os.path.exists(savepath + candidate):
                os.makedirs(savepath + candidate)
            urllib.request.urlretrieve(imgUrl, savepath + candidate + "/" + str(count) + ".jpg")
            count = count + 1
        except:
            pass

    driver.close()
