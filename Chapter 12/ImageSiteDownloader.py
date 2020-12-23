#! python3
# ImageSiteDownloader.py - Downloads the preview images from imgur for a user given search term
import os, bs4, requests

def main():
    # Get search term
    searchTerm = input('Imgur Search: ')
    searchTermForURL = '+'.join(searchTerm.split())
    URL = 'https://imgur.com/search?q=' + searchTermForURL

    # Create folder
    os.makedirs(searchTerm, exist_ok=True)
    
    # Download the page
    res = requests.get(URL)
    res.raise_for_status()

    # Parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('img[alt=""]')
    
    # Download each image
    for elem in elems:
        imageURL = 'https:' + elem.get('src')
        print('Downloading image %s' % (imageURL) )
        res = requests.get(imageURL)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('Unable to download %s. Received error %s.' % (imageURL, exc))
            continue

        # Write image to memory
        imageFile = open(os.path.join(searchTerm, os.path.basename(imageURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

if __name__ == '__main__':
    main()