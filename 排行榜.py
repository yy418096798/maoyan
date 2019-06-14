import requests
from lxml import etree


def pai(n):
    url = f'https://maoyan.com/board/4?offset={n*10}'
    r = requests.get(url)
    html = r.text
    text = etree.HTML(html)
    name = text.xpath("//div/div/div/p/a/@title")
    star = text.xpath("//div/div/p[@class='star']/text()")
    releasetime = text.xpath("//div/div/div/p[@class='releasetime']/text()")
    s = ":"
    for i,j ,k in zip(name, star, releasetime):
        with open ("top100.txt", 'a', encoding="utf-8") as f:
            f.write(i)
            f.write(s)
            f.write(j)
            f.write(s)
            f.write(k)

        print(i ,j, k)


for n in range(10):
    pai(n)