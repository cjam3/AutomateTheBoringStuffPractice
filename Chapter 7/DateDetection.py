import re

def main():
    date = '01/20/2020'
    dateDetection(date)

def dateDetection(date):
    reg = re.compile(r'(\d{2})(/)(\d{2})(/)(\d{4})')
    mo = reg.search(date)
    if mo == None:
        print('No valid date is found')
        return
    
    month = int(mo.group(1))
    day = int(mo.group(3))
    year = int(mo.group(5))
    isLeapYear = False
    
    if year < 1000 or year > 2999:
        print("%s is not a valid year" % year)
        return
    
    if year % 4 == 0:
        isLeapYear = True
        if year % 100 == 0 and not year % 400 == 0:
            isLeapYear = False
    
    if month > 12 or month < 1:
        print("%s is not a valid month" % month)
        return

    maxDays = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    if day > 31 or day < 1:
        print("%s is not a valid day" % day)
        return
    if day > maxDays[month]:
        if month != 2 or not isLeapYear or not day == 29:
            print("%s is not a valid day" % day)
            return

    print('The day is %s' % day)
    print('The month is %s' % month)
    print('The year is %s' % year)

if __name__ == '__main__':
    main()