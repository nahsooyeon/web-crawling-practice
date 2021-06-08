import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import simplejson as json
import pyperclip





sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome(options=chrome_options, executable_path=r'/Users/devpomme/Desktop/chromedriver')
# driver = webdriver.Chrome('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section3/3-6(all)/chrome/chromedriver')


driver.get('https://shopping.naver.com/')
driver.implicitly_wait(2)

# 검색어 입력하기

driver.find_element_by_name('query').send_keys('운동')
driver.implicitly_wait(2)

#검색 버튼 누르기
driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

driver.implicitly_wait(2)



# 스크롤 끝까지 내리기
while True:
# 화면 최하단으로 스크롤 다운
    SCROLL_PAUSE_TIME = 2
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 페이지 로드 기다리기
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)

# 업데이트된 스크롤 높이 계산하고 마지막으로 기록된 스크롤 높이와 비교하기
    new_height = driver.execute_script("return document.body.scrollHeight")
    last_height = new_height

# 새로운 높이가 이전 높이와 같을 경우 스크롤 종료
    if new_height == last_height:
        break
# 스크롤 다운이 되는 경우엔 창 높이를 새로운 높이로 갱신
    last_height = new_height


# 검색 결과 10페이지 크롤링 후 파일 저장




##file = open("네이버쇼핑매크로.txt", "w", encoding = "UTF-8")  # txt파일로 저장
file = open("/Users/devpomme/Desktop/네이버쇼핑매크로.json", "w", encoding = "UTF-8") #json 파일로 저장하기
soup = BeautifulSoup(driver.page_source, 'lxml')
count = len(soup.find_all('div', class_='basicList_title__3P9Q7'))
naver_macro = []
page = 0

while True :
    print("page = ", page, "크롤링 완료")  # 결과 확인 위한 출력

    for i in range(0, count) :
        metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
    # 상품명
        title = metadata.a.get('title')
        if title != None :
            title = metadata.a.get('title')
            #print("<제품명> : ", title) # title
        elif title == None :
            title = metadata.a.get_text()
            #print("<제품명> : ", title)

    # 상품 URL
        url = metadata.a.get('href')
        #print("<url> : ", url)
    # 상품 가격
        metadata2 = soup.find_all('div', class_='basicList_price_area__1UXXR')[i]
        price = metadata2.find('span', class_='price_num__2WUXn')
        if price != None :
            price = price.text.replace('원', '').strip()
            price = int(price.replace(',','').strip())
            #print("<가격> : ", price)
        elif price == None :
            price = price = metadata2.strong.get_text()
            #print("<가격> :", price)
    # 리뷰 수
        metadata3 = soup.find_all('div', class_='basicList_etc_box__1Jzg6')[i]
        review = metadata3.find('em', class_='basicList_num__1yXM9')
        if review != None :
            review = int(review.text.replace(',', '').strip())
            #print("<리뷰 수> : ", review)
        elif review == None :
            review = 0
            #print("<리뷰 수> : ", review )
    # 찜 개수
        metadata4 = soup.find_all('button', class_='basicList_btn_zzim__2MGkM')[i]
        zzim = metadata4.find('em', class_='basicList_num__1yXM9')

        if zzim != None:
            if zzim.text.find('만') != -1:
                zzim = int(float(zzim.text.replace('만', '').strip())*10000)
                type(zzim)
            else:
                zzim = int(float(zzim.text.replace(',', '').strip()))
                type(zzim)
            #print("<찜 수> : ", zzim )
        elif zzim == None:
            zzim = 0
            type(zzim)
            #print("<찜 수> : ", zzim )
    #print("===================================================")

    #file.write(str(title) + "\t" + str(price) + "\t" + str(url) + "\n")

        naver_macro.append({'상품명' : title , '가격' : price, 'URL' : url, '리뷰': review, '찜': zzim }) #리스트 안에 딕셔너리 값 append
#
    if driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/a'):
        next_btn = driver.find_element_by_class_name('pagination_next__1ITTf')
        next_btn.click()
        print('다음 페이지를 크롤링합니다')
        page += 1
    else:
        print('크롤링을 종료합니다')
        break
#

file.write(json.dumps(naver_macro, ensure_ascii=False, indent=4))

file.close()


driver.quit()


# pandas로 부르기, excel 저장

import pandas as pd

df = pd.read_json("/Users/devpomme/Desktop/네이버쇼핑매크로.json")
# for j in df:
#     print(j)

writer = pd.ExcelWriter("/Users/devpomme/Desktop/네이버쇼핑매크로.xlsx")
df.to_excel(writer, "sheet1")
writer.save()
