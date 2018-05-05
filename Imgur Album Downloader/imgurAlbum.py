#! /usr/bin/python3
import bs4
import requests
import os


url = input('Enter Imgur Album URL : ')
os.makedirs('Album', exist_ok=True)

# Downloading HTML
print('Downloading ' + url + '...')
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
albumPapers = soup.select('.post-image-placeholder')
for i in range(len(albumPapers)):
    # Downloading Image
    imgsrc = albumPapers[i]['src']
    res = requests.get('https:'+imgsrc)
    res.raise_for_status()
    # Saving Image
    imageFile = open(os.path.join('Album', os.path.basename(imgsrc[2:])), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print((i+1), 'of', len(albumPapers))
