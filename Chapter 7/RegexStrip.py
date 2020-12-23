import re

def main():
    string = 'potato'
    stripString = regStrip(string, '-')
    print(stripString)

def regStrip(string, replace = ''):
    regBegin = re.compile(r'^\s+')
    regEnd = re.compile(r'\s+$')
    beginMo = regBegin.search(string)
    if beginMo != None:
        beginSize = len(beginMo.group())
        begin = regBegin.sub(replace * beginSize, string)
    else:
        begin = string
    
    endMo = regEnd.search(begin)
    if endMo != None:
        endSize = len(regEnd.search(begin).group())
        ret = regEnd.sub(replace * endSize, begin)
    else:
        ret = begin

    return ret

if __name__ == '__main__':
    main()