#! /usr/bin/python3
import bs4
import requests
import os
from pathlib import Path


url = 'https://www.xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading ' + url + '...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Image url
    comicElm = soup.select("#comic img")
    if comicElm == []:
        print('No Image found')
    else:
        comicUrl = comicElm[0]
        comicUrl = str(comicUrl['src'])
        # Downloading Image
        print("Downloading Image")
        print('Image url = ' + str(comicUrl[2:]))
        filePath = Path('xkcd/' + comicUrl[23:])
        print("Image source " + comicUrl[23:])
        if filePath.exists():
            print(comicUrl[23:] + ' is already downloaded')
        else:
            res = requests.get('https://' + comicUrl[2:])
            res.raise_for_status()
            # Saving Image
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl[2:])), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
