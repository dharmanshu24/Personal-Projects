#! /usr/bin/python3

import os
import bs4
import requests
from pathlib import Path

urlParent = 'https://www.smbc-comics.com'
url = urlParent
os.makedirs('smbc', exist_ok=True)

while True:
    print('Downloading', url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Getting Image Location
    comicElm = soup.select('#cc-comic')
    if comicElm == []:
        print('No Image Found')
    else:
        comicUrl = str(comicElm[0]['src'])
        # Downloading image
        print('Downloading Image')
        print('Image Url = ', urlParent + comicUrl)
        filePath = Path('smbc/', comicUrl[8:])
        if filePath.exists():
            print('Image already downloaded')
        else:
            res = requests.get(urlParent + comicUrl)
            imageFile = open(os.path.join('smbc', os.path.basename(comicUrl[2:])), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = prevLink.get('href')
