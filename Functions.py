def printText():
    print('Enter Your Name:')
    myName = input()
    print('Hello,{}'.format(myName))
    return myName


def largerString():
    arrayString = ['dgd', 'fdgfdg', 'kaondooooo']
    stringNumber = 0
    stringNeeded = arrayString[0]
    # builtIn
    # stringMax = max(arrayString, key=len)
    # stringMin = min(arrayString, key=len)
    # print(stringMax)
    # print(stringMin)
    # not built in
    for string in arrayString:
        if stringNumber > len(string):
            stringNeeded = string
    print(stringNeeded)
    # if len(string) > len(stringNumber):
    #     print(string)


def testLambda(a, b):
    ans = a + b
    return print(ans)


def testTernary():
    ans = 4 if (4 > 0) else 0  # ternary condition
    return print(ans)


def calculateSum():
    sum = 0
    i = 0
    list = [2, 76, 98, 32, 76, 45]
    for number in list:
        print('Number {}:', number)
        sum = sum + number
        # print(sum)
    return print('sum is', sum)


def start_string(r):
    for x in range(r):
        print("r", r)
        print("x", x)
        print(' ' * (r - x - 1) + '*' * (2 * x + 1))


def splitString():
    text = "kaondo kaondo yusuph!"
    text.split(' ')
    print(text)


def palindrome():
    a = input("text character:")
    b = a[::-1]
    # print("value of reverse a", a[::-1])
    if a == b:
        print("this word is palindrome")
    else:
        print("not a palindrome word")


def primeNumber():
    number = int(input("enter number:"))
    if number > 1:
        for x in range(2, number):
            if number % x == 0:
                print(number, "number is not prime")
                break
            else:
                print(number, "Number is prime number...")
    else:
        print(number, "Number is not prime number")


# Happy birthday Yusuph Kaondo.
age = 27


def happyBirthday():
    print("Yusuph's new age is Loading....!!")
    years_old = age  # current years old
    birthdate = input("Enter Yusuph's birth date:")
    if birthdate == "04/06/2022":
        years_old += 1
        print("Happy birthday Yusuph kaondo")
        print("Current years old:", years_old)
        print("...For new age days count...")
    else:
        print(birthdate, "This date is not my birthdate")

    return print("***** My current age is ", years_old, " *****")


def TemperatureConversion():
    F = 48.2
    c = (F - 32) * 5 / 9
    F=(c * 9/5) + 32
    print(F)
    return print(c,F)
