#! python3
# WebComicDownloader.py - Downloads the most recent comics from xkcd once a day if new comics have been uploaded

import requests, os, bs4

def main():
    downloadComics()

def downloadComics():
    # Create folder for comics
    os.makedirs('./xkcdComics', exist_ok=True)
    # Check if we already have the most recent comics
    req = requests.get('https://xkcd.com/')
    req.raise_for_status()
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    if checkMostRecentComic(soup):
        print('Comics are up-to-date!')
        return
    # Download comics until most recent comic
    comicNames = os.listdir('./xkcdComics')
    while True:
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Unable to retrieve comic image')
        else:
            fileName = os.path.basename(comicElem[0].get('src'))
            if fileName in comicNames:
                break
            imgReq = requests.get('https:' + comicElem[0].get('src'))
            imgReq.raise_for_status()
            print(f'Downloading {fileName}...')
            comicFile = open(os.path.join('xkcdComics', fileName), 'wb')
            for chunk in imgReq.iter_content(100000):
                comicFile.write(chunk)
            comicFile.close()
        # Go to next comic
        nextURL = 'https://xkcd.com' +  soup.select('a[rel="prev"]')[0].get('href')
        req = requests.get(nextURL)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, 'html.parser')



def checkMostRecentComic(parsedHTML):
    # Checks if the most recent xkcd comic is already downloaded
    # Returns True if most recent xkcd comic is already downloaded
    # Returns False if most recent xkcd comic is not already downloaded

    comicNames = os.listdir('./xkcdComics')
    # Find the name of the most recent comic
    comicElem = parsedHTML.select('#comic img')
    if comicElem == []:
        print('Unable to retrieve most recent image')
        exit(0)

    # Check if the most recent comic is already downloaded
    mostRecentComicName = os.path.basename(comicElem[0].get('src'))
    if mostRecentComicName in comicNames:
        return True
    
    return False

if __name__ == '__main__':
    main()