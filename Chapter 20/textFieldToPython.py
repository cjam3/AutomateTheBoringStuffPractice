#! python3
# textFieldToPython.py - Uses pyautogui to select text in notepad and pyperclip to copy it to a string

import pyautogui, pyperclip

def main():
    print(selectAllFromNotepadAndCopy())

def selectAllFromNotepadAndCopy():
    # Copies all text in a notepad window to a string and adds that to a list of strings
    # Does this for each notepad window currently open
    # Returns the list of strings
    notepadWindows = pyautogui.getWindowsWithTitle('Notepad')
    strings = []
    for notepadWindow in notepadWindows:
        notepadWindow.activate()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        strings.append(pyperclip.paste())

    return strings

if __name__ == '__main__':
    main()