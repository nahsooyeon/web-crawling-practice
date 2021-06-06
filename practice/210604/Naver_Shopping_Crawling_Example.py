from bs4 import BeautifulSoup
from urllib.request import urlopen
import request



URL = 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003'
Directory = '/Users/devpomme/Desktop'

with urlopen('{}'.format(URL)) as response:
    soup = BeautifulSoup(response, 'html.parser')
    save = []
    for anchor in soup.select("p,cont"):
        data = anchor.get_text()
        save.append(data)

save_2 = []
for i in range(0, len(save)):
    save_2.append(save[i].replace('\n', '')+'\n')
f = open("{}/네이버쇼핑_2.txt".format(Directory), 'w', encoding='UTF-8')
f.writelines(save_2[7 : -3])
f.close()
