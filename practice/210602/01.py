# 웹 크롤링 - 네이버 스토어 상품명, 가격 가져오는 함수 만들기

from urllib.request import urlopen
from bs4 import BeautifulSoup


# 스토어 상품명 가져오기

def getClassValue(url, tag, className):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    content = bsObject.body.find(tag, {"class", className})
    return content.text

url_list = [
    "https://smartstore.naver.com/soommask/products/4828127993",
    "https://smartstore.naver.com/aseado/products/4837257765",
    "https://smartstore.naver.com/aseado/products/4837266971",
    "https://smartstore.naver.com/aseado/products/3765693172",
    "https://smartstore.naver.com/aer-shop/products/4722827602",
    "https://smartstore.naver.com/aer-shop/products/4722827602",
    "https://smartstore.naver.com/korea-mask/products/4825762296",
    "https://m.smartstore.naver.com/ygfac/products/3905641271",
    "https://smartstore.naver.com/gonggami/products/4705579501"
];


titles = []

productTag = 'h3'
productClass = '_3oDjSvLwq9'

for url in url_list :
    titles.append(getClassValue(url, productTag, productClass))

print (titles)


# 상품 가격 가져오기

prices = []

priceTag = 'span'
priceClass = '_1LY7DqCnwR'

for url in url_list:
    prices.append(getClassValue(url, priceTag, priceClass))

print (prices)
