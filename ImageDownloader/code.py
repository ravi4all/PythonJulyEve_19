import urllib.request as url
import bs4

http = url.urlopen("https://www.marvel.com/")
page = bs4.BeautifulSoup(http, 'lxml')
images = page.find_all('img')
# print(len(images))
# src = images[10]['src']
# print(src)

# print(type(images[6]['src']))

for i in range(len(images)):
    src = images[i]['src']
    print(src)
    if src != '#' or src != '':
        url.urlretrieve(src,'img_{}.jpg'.format(i))
