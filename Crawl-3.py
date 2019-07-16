import bs4
import urllib.request as url

moviename = input("Enter movie name : ")
moviename = moviename.split()
movie = '+'.join(moviename)
path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+movie
http = url.urlopen(path)

page = bs4.BeautifulSoup(http,'lxml')
td = page.find('td',class_='result_text')
#print(td)

href = td.find('a').attrs['href']
newPath = "https://www.imdb.com"+href

http = url.urlopen(newPath)
page = bs4.BeautifulSoup(http,'lxml')
title = page.find('div',class_='title_wrapper')

title = title.text.replace("\n","")
tokens = title.split()
title = ' '.join(tokens)
print(title)

summary = page.find('div',class_='summary_text')
print(summary.text.strip())

