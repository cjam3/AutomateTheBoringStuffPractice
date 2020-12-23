#! python3
# 2048Player.py - Simple program that plays 2048 by sending up, right, down,
# and left repeatedly

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    # Open 2048 webpage
    browser = webdriver.Firefox()
    browser.get('https://play2048.co/')

    # Get html tag
    htmlTag = browser.find_element_by_tag_name('html')

    gameOver = browser.find_element_by_css_selector('.game-message > p:nth-child(1)')

    # Send keys
    while gameOver.text != 'Game over!':
        htmlTag.send_keys(Keys.UP)
        htmlTag.send_keys(Keys.RIGHT)
        htmlTag.send_keys(Keys.DOWN)
        htmlTag.send_keys(Keys.LEFT)
        gameOver = browser.find_element_by_css_selector('.game-message > p:nth-child(1)')

    score = browser.find_element_by_css_selector('.score-container')
    print('Game over! The program\'s score was %s.' % (score.text))
    browser.close()

    
if __name__ == '__main__':
    main()