import bs4
import urllib.request as url

http = url.urlopen("https://www.flipkart.com/search?q=iphone%20xs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#print(http)

page = bs4.BeautifulSoup(http,'lxml')
div = page.findAll("div", class_='_3wU53n')

#print(div.text)
for item in div:
    print(item.text)
