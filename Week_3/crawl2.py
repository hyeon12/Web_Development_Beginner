import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/category/bestseller')
soup = BeautifulSoup(res.text, 'html.parser')

for i in range(3):
    idx = str(i+1)
    sstr = '#bestList > ol > li.num' + idx + ' > p:nth-child(3) > a'
    ts = soup.select_one(sstr)

    link = ts.attrs.get('href')
    
    res2 = requests.get('https://www.yes24.com' + link)
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    sp = soup2.select_one('#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum ')
    
    #첫번째 판매지수 삭제
    idx = sp.text.find('판매')
    point = sp.text[idx+5:]

    #두번째 뒷부분 판매지수 삭제
    idx = point.find('판매')
    point = point[:idx-1]

    print(ts.text, point)