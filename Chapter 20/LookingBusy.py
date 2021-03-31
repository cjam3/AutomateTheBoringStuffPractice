#! python3
# LookingBusy.py - Moves the mouse slightly every 10 seconds in order to avoid looking idle on instant messenger apps

import pyautogui

def main():
    print('To end the program, move mouse to corner or use Crtl-C')
    moveMouse()

def moveMouse():
    pixelMovement = 5
    try:
        while True:
            pyautogui.sleep(10)
            pyautogui.move(pixelMovement, 0, 0.25)
            pixelMovement *= -1
    except pyautogui.FailSafeException:
        print('Mouse detected in corner. Ending program.')

if __name__ == '__main__':
    main()