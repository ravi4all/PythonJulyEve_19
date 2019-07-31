import json
import urllib.request as url

toSearch = input("Enter your input : ")
toSearch = toSearch.replace(" ","+")
http = url.urlopen(f'http://api.giphy.com/v1/gifs/search?q={toSearch}&api_key=bc56161131654faeb550630b83e0c977&limit=5')
jsonData = json.load(http)
# print(jsonData)

data = jsonData['data']
for i in range(len(data)):
    img = data[i]['images']
    imgUrl = img['downsized_large']['url']
    url.urlretrieve(imgUrl, 'img_{}.gif'.format(i))