from pathlib import Path
import re


def main():
    madLib()


def madLib():
    file = Path.cwd() / 'Chapter 9/madlib.txt'
    fo = open(file, 'r')
    string = fo.read()
    fo.close()

    # Ask the user for an adjective, noun, and verb
    adjective = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    noun2 = input('Enter a noun: ')

    # Find and substitute words using regex
    adjReg = re.compile(r'ADJECTIVE')
    nounReg = re.compile(r'NOUN')
    verbReg = re.compile(r'VERB')

    string = adjReg.sub(adjective, string, 1)
    string = nounReg.sub(noun1, string, 1)
    string = verbReg.sub(verb, string, 1)
    string = nounReg.sub(noun2, string, 1)

    # Write the string to the file
    fo = open(file, 'w')
    fo.write(string)
    fo.close()


if __name__ == '__main__':
    main()
