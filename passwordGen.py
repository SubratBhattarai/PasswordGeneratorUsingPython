import random
import math
import os

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q', 'R','S','T','U','V', 'W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['!','@','$','%','^','&','*']


def storing(password):
    f = open("""Path for the File to be read or created""", 'a')
    f.write(f'{password}\n')
    f.close()

def reading():
    if os.path.exists("""Path for the File to be read or created"""):    ## Keep your path 
        f = open("""Path for the File to be read or created""", 'r')      
        print()
        print("Passwords")
        print()
        for lines in f.readlines():
            print(lines)
        f.close()
    else:
        print("file Doesn't exist")



def passWordCreation(): 
    password = '' ## Empty String
    value3 = generating()
    for value in value3:
        password += str(value)
    storing(password) 


def generating():
    while True:
        numberOfCharacters = input("Enter your desired length of password: ")
        
        value1 = []
        value2 = []
        value3 = []

        if (numberOfCharacters.isdigit()): ## Checking if the string is number string else it will loop again
            numberOfCharacters = int(numberOfCharacters)
            num = 0
            alpha = 0
            for i in range(numberOfCharacters):
                choice = round(random.random())
                alphaValue = round(random.random())
                if choice == 1: 
                    if alphaValue == 1: ## Rounding chioce to get True of False and keep lower alpha if true
                        value1.append(alphabets[alpha].lower())
                    else:
                        alpha = random.randint(0, 26) ## Interval [0,26] Alphbet
                        value1.append(alphabets[alpha])
                else:
                    num = random.randint(0, 9) ## Interval [0, 10] Number
                    value2.append(numbers[num]) 


            ## Putting values1 list in value 3
            for i in (value1):
                value3.append(i)
            ## Putting values2 list in value 3
            for j in (value2):
                value3.append(j)
            ## Putting random Special in value 3
            value3.append(specials[math.ceil(random.randint(0, 6))]) ## Interval [0, 7] special Key
            numberOfCharacters = str(numberOfCharacters)
            return value3

        else:
            os.system('cls') ## Clearing Screen
            print("Enter a number. Try Again!")
            



def mainMenu():
    
    print("1. Generate and Store password.")
    print("2. Read Passwords.")
    print("3. Exit")
    userInput = input("Enter your choice: ")

    while True:
        if userInput.isdigit():
            userInput = int(userInput)
            if(userInput == 1):
                passWordCreation()
                break
            elif(userInput == 2):
                reading()
                break
            elif(userInput == 3):
                break
            else:
                print("Please write a valid number.")
        else:
            print("Please write a valid number.")


def main():
    print("Welcome To password Generator.")
    print("Recommendation: Genererate a password atleast of 8 characters. ")
    print("Note: Special Keys don't count in length.")
    print()
    mainMenu()


if __name__ == '__main__':
    main()


