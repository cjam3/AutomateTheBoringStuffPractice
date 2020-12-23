#! Python3
# Program takes a gmail username, password, and message and sends email to target email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip
import time


def main():
    # Get username, password, and message
    username = pyip.inputStr("Username: ")
    password = pyip.inputPassword("Password: ", '*')
    subject = pyip.inputStr("Subject: ")
    message = pyip.inputStr("Message: ")
    targetEmail = pyip.inputStr("Recipient: ")

    # Sign into gmail and send message
    browser = webdriver.Firefox()
    signInAndEmail(browser, username, password, targetEmail, subject, message)

    browser.close()


def signInAndEmail(browser, username, password, targetEmail, subject, message):
    # Get to login page
    browser.get('https://stackoverflow.com/')
    time.sleep(5)
    stackLoginButton = browser.find_element_by_css_selector('.s-btn__filled')
    stackLoginButton.click()
    time.sleep(5)
    logInWithGoogleButton = browser.find_element_by_css_selector('button.s-btn__icon:nth-child(1)')
    logInWithGoogleButton.click()
    time.sleep(5)

    # Gmail login restriction bypass using stack overflow
    usernameBox = browser.find_element_by_css_selector('#identifierId')
    usernameBox.send_keys(username)
    time.sleep(1)
    usernameBox.send_keys(Keys.ENTER)
    time.sleep(1)
    passwordBox = browser.find_element_by_name('password')
    passwordBox.send_keys(password)
    time.sleep(1)
    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

    # Go to gmail
    browser.get('https://gmail.com')

    # Compose email
    time.sleep(15)
    composeEmailButton = browser.find_element_by_css_selector('.T-I-KE')
    composeEmailButton.click()
    time.sleep(2)
    recipientBox = browser.find_element_by_name('to')
    recipientBox.send_keys(targetEmail)
    subjectBox = browser.find_element_by_name('subjectbox')
    subjectBox.send_keys(subject)
    messageBox = browser.find_element_by_xpath("//*[@role='textbox']")
    messageBox.send_keys(message)
    sendButton = browser.find_element_by_xpath("//*[@data-tooltip='Send ‪(Ctrl-Enter)‬']")
    sendButton.click()



if __name__ == '__main__':
    main()
