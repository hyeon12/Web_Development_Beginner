#bestList > ol > li.num1 > p:nth-child(3) > a
#bestList > ol > li.num2 > p:nth-child(3) > a
#bestList > ol > li.num3 > p:nth-child(3) > a

import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.yes24.com/24/category/bestseller")
soup = BeautifulSoup(res.text, "html.parser")

for i in range(40):
    idx = str(i+1)
    if idx == "19":
        idx = "19_line"
    elif idx == "20":
        idx = "20_line"

    sstr = "#bestList > ol > li.num" + idx + " > p:nth-child(3) > a"
    ts = soup.select_one(sstr)
    print(ts.text)