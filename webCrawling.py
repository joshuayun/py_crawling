import requests
from bs4 import BeautifulSoup



req = requests.get('https://gausad.com/common/info')

html = req.text

soup = BeautifulSoup(html,'html.parser')
gaus_title = soup.head.title
gaus_img = soup.select('#contanier > div.GAUS_box > img')
ttimg = gaus_img[0].get('alt')

print(ttimg)


