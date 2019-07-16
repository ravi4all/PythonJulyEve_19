import bs4
import urllib.request as url


for i in range(10):
    path = "https://www.flipkart.com/redmi-note-7s-ruby-red-64-gb/product-reviews/itmfh75fae8bbtff?pid=MOBFGGJ85BAHVRUV"+'&page={}'.format(i+1)
    http = url.urlopen(path)
    page = bs4.BeautifulSoup(http,'lxml')

    para = page.find_all('p', class_='_2xg6Ul')
    rating = page.find_all('div',class_='hGSR34 E_uFuv')
    for p,r in zip(para,rating):
        print("Review :",p.text)
        print("Rating :",r.text)
        print("------------------")
