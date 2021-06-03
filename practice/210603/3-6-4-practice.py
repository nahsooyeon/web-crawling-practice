import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
#chrome_options.add_argument("--headless")
# chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section3/3-6(all)/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)
driver.get('https://shopping.naver.com/')


driver.implicitly_wait(2)

# 검색어 입력하기

driver.find_element_by_name('query').send_keys('운동화')

driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

driver.implicitly_wait(2)
# 검색 후 리뷰 많은 순으로 정렬하기
driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/a[5]').click()

driver.sleep(2)
driver.implicitly_wait(2)
