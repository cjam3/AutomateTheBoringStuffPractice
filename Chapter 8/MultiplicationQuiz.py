import random, time

def main():
    multiplicationQuiz()

def multiplicationQuiz():
    numberCorrect = 0
    for i in range(10):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        product = num1 * num2
        t0 = time.time()

        for j in range(3):
            response = input(f'What is the product of {num1} and {num2}?: ')
            if response.isdigit():
                if int(response) == product:
                    if time.time() - t0 < 8:
                        print(f'{response} is correct!')
                        numberCorrect += 1
                        break
                    else:
                        print(f'{response} was correct but you took too long!')
                        break
                else:
                    print(f'{response} is incorrect.')
            else:
                print(f'{response} is not a number')
        
    print('You answered %s questions correctly out of 10' % numberCorrect)

if __name__ == '__main__':
    main()