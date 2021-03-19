#! python3
# PrettifiedStopwatch.py - Creates a better looking version of the stopwatch example in chapter 17

import time, pyperclip

def main():
    stopWatch()

def stopWatch():
    print('Press Enter to begin. Afterward, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')
    input()
    print('Started')
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    output = ''

    # Start tracking the time
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap #' + str(lapNum).rjust(3) + ':' + str(totalTime).rjust(7) + ' (' + (str(lapTime) + ')').rjust(6), end='')
            output += 'Lap #' + str(lapNum).rjust(3) + ':' + str(totalTime).rjust(7) + ' (' + (str(lapTime) + ')').rjust(6) + '\n'
            lapNum += 1
            lastTime = time.time()
    except KeyboardInterrupt:
        print('\nDone')
        pyperclip.copy(output)

if __name__ == '__main__':
    main()