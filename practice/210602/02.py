# 스마트스토어에서 검색한 키워드로 노출되는 상품명 및 가격 찾기
import sys
import io
import urllib.request as dw
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


t_list = []
n_list = []
r_list = []
p_list = []

keyword = "감귤"
driver = webdriver.Chrome(r"/Users/devPomme/Desktop/chromedriver")
driver.get("https://search.shopping.naver.com/search/all?query={}".format(keyword))

item_source = BeautifulSoup(driver.page_source, 'lxml')
item_list = item_source.find_all('li', class_='basicList_item__2XT81')

for item in item_list:
    title = item.find('a', class_='basicList_link__1MaTN').string
#     price = item.find('span', class_='num').text
#     if item.find_all('a', class_='graph'):
#         review = item.find_all('a', class_='graph')[0].text
#         if len(item.find_all('a', class_='graph')) == 2:
#             buy_num = item.find_all('a', class_='graph')[1].text
#         else:
#             buy_num = '없음'
#
    t_list.append(title)
#     p_list.append(price)
#     r_list.append(review.repace('리뷰', ''))
#     n_list.append(buy_num.replace('구매건수', ''))



print(t_list)
pd.DataFrame({'상품명': t_list})
#
# pd.DataFrame({'상품명':t_list, '가격':p_list, '리뷰수':r_list, '구매건수':n_list})
