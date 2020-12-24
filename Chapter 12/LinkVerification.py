#! Python3
# LinkVerification.py - Program takes a website link and finds every link on the website
# Checks every link on the page for a 404 status
# Prints the name of all links that return a 404 status
# Example use - python3 LinkVerification.py https://www.python.org/

import requests, bs4, sys

def main():
    if len(sys.argv) != 2:
        print('Run the program on the commmand line using a webpage as the only command line argument')
        exit(0)

    verifyLinks(sys.argv[1])

def verifyLinks(link):
    # Verify status of link provided to command line
    try:
        res = requests.get(link)
        res.raise_for_status()
    except Exception as exc:
        print('ERROR! Link provided to command line was not valid')
        print(f'Exception: {exc}')
        return

    # Find all links on the webpage
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elemsOnPage = soup.select('a[href]')
    
    # Check each link by checking status code
    notFoundLinks = []
    for elem in elemsOnPage:
        href = elem.attrs['href']
        if href.startswith('//'):
            linkToCheck = 'http:' + href
        elif href.startswith('/'):
            if link[-1] == '/':
                linkToCheck = link[:-1] + href
            else:
                linkToCheck = link + href
        elif href.startswith('http'):
            linkToCheck = href
        elif href.startswith('#'):
            continue
        else:
            print(f'"{href}" is not a valid link. Skipping...')
            continue

        try:
            res = requests.get(linkToCheck)
        except Exception as exc:
            print(f'ERROR! Request failed with exception: {exc}')
            continue

        if res.status_code == 404:
            notFoundLinks.append(linkToCheck)

    # Print links that resulted in 404
    if len(notFoundLinks) == 0:
        print('No links on the webpage returned a 404 status code.')
    else:
        print('\nLinks that resulted in a 404:')
        for notFound in notFoundLinks:
            print(notFound)

if __name__ == '__main__':
    main()