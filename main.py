# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.con
import math
from Functions import printText, largerString, testLambda, testTernary, calculateSum, start_string, splitString, \
    palindrome, primeNumber, happyBirthday, TemperatureConversion


def calculateAvg(myArray):
    avarage = sum(myArray) / len(myArray)
    print(f'TOTAL MARKS IS {sum(myArray)}')
    print("*********BELOW IS YOUR FINAL RESULT AVARAGE*******")
    return print(f'Your Avarage is  {"%.1f" % avarage}')


def kiswahil(kisw):
    if kisw >= 90:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is A')
    if kisw >= 80:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is B+')
    if kisw >= 70:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is B')
    if kisw >= 60:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is C')
    if kisw >= 50:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is D')
    if kisw >= 40:
        return print(f'Kiswahili score marks is, {kisw}  and Your grade is FAIL')


def English(eng):
    if eng >= 90:
        return print(f'English score marks is, {eng}  and Your grade is A')
    if eng >= 80:
        return print(f'English score marks is, {eng}  and Your grade is B+')
    if eng >= 70:
        return print(f'English score marks is, {eng}  and Your grade is B')
    if eng >= 60:
        return print(f'English score marks is, {eng}  and Your grade is C')
    if eng >= 50:
        return print(f'English score marks is, {eng}  and Your grade is D')
    if eng >= 40:
        return print(f'English score marks is, {eng}  and Your grade is FAIL')


def Mathematics(math):
    if math >= 90:
        return print(f'Mathematics score marks is, {math}  and Your grade is A')
    if math >= 80:
        return print(f'Mathematics score marks is, {math}  and Your grade is B+')
    if math >= 70:
        return print(f'Mathematics score marks is, {math}  and Your grade is B')
    if math >= 60:
        return print(f'Mathematics score marks is, {math}  and Your grade is C')
    if math >= 50:
        return print(f'Mathematics score marks is, {math}  and Your grade is D')
    if math >= 40:
        return print(f'Mathematics score marks is, {math}  and Your grade is FAIL')


def studentGrade(math, kisw, eng):
    myArray = [math, kisw, eng]
    calculateAvg(myArray)


# Press the green button in the gutter to run the script.
def checkNumber(number):
    x = number % 2
    if x == 0:
        print("this number is even number:", number)
    else:
        print("this number not even number")


def userInput():
    name = input("please enter your full name:")
    print(f'Hi, {name}')
    print("**********PLEASE ENTER YOUR SCORE BELOW***********")
    eng = int(input("please enter your Eng score marks:"))
    kisw = int(input("please enter your Kisw score marks:"))
    math = int(input("please enter your Math score marks:"))
    print("*******HERE YOUR SCORES********")
    English(eng)
    kiswahil(kisw)
    Mathematics(math)
    studentGrade(math, kisw, eng)


def calculateArea():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("area", area)


def calculateAvg():
    i = 0
    sum = 0
    product = 1
    count = int(input("enter count:"))
    for i in range(count):
        x = int(input("ent number:"))
        sum = sum + x
    print("summation", sum)
    avg = sum / count
    print("avarage", avg)

    for i in range(count):
        x = float(input("Enter a real number: "))
        product = product * x
    print("The product of the numbers is: ", product)


def revs():
    rev = 0
    number = int(input("Enter a positive integer: "))
    while (number != 0):
        digit = number % 10
        rev = (rev * 10) + digit
        number = number // 10
    print(rev)


def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("this is leap year")
            else:
                print("this is not leap year")
        print("this is leap year")
    else:
        print("this is  not leap year")


name_list = ['kaondo', 'grace', 'yushytre', 'ayakaiuytr', 'shedrack']


# def smallestString():
#       smallest=max(name_list,key=len)
#       print(smallest)
#  return 0


# def calculateSum():
#
#     my_list = [2, 3, 5, 4, 6]
#     sum = 0
#     for i in my_list:
#         sum = sum + i
#     return print(sum)


#  loops
def loopTesting():
    i = 0
    my_list = [2, 76, 98, 32, 76, 45]
    my_list2 = ['ismail', 'suleiman', 'kaondo']
    # while i < len(my_list):
    #     v = my_list[i]
    #     print(v)
    #     i += 1
    # print(v)

    # -----for loop-----
    # for i in range(len(my_list)):
    #     i=my_list[i]
    #     print(i)
    # normal loop
    #    for i in my_list:
    #        print(i)

    # value with index
    # print(list(enumerate(my_list)))
    # for i in range(len(my_list)):
    #     v = my_list[i]
    #     print(i, v)
    # ----for with enumerate----
    # for index, value in enumerate(my_list):
    #     print(index, value)
    # -----zip iterable----

    # for name, number in zip(my_list2, my_list):
    #     print(
    #         name, number
    #     )
    # dict iterable
    # print(dict(zip(my_list, my_list2)))
    #  yield and generator
    # for i in my_list:
    #     if i % 2 == 0:
    #         yield i


# calculate sum

if __name__ == '__main__':
    TemperatureConversion()
    # happyBirthday()
    # primeNumber()
    # palindrome()
    # splitString()
    # start_string(6)
    # loopTesting()
    # calculateSum()
    # printText()
    # largerString()
    # smallestString()
    # testLambda(3,5)
    # calculateSum()
    # testTernary()
    # list1 = [0,-10, 21, -4, -45, -66, 93]
    # for i in list1:
    #     if i >=0:
    #         print(i)
    # list = [2, 4, 5, 11, 86]
    # max = list[0]
    # min = list[0]
    # secondMin=list[0]
    # for i in list:
    #     # print(i)
    #     if (i > max):
    #         max = i
    #     if (i < min):
    #         min = i
    #     # if ((i < secondMin) and  (!= min)):
    #     if i < secondMin and i != min:
    #         secondMin = i
    # print('max number', max)
    # print('min number', min)
    # print('second min number',  secondMin)

    # number = int(input("enter number between 90 and 80 :"))
    # if (number <= 90 and number >= 80):
    #     print(number)
    #     print('xyz')
    # else:
    #      print('number not in range of 80 up to 90, your number is', number)

# print(numbers)
# x = int(input("Enter the position of the element to be deleted: "))
# leapYear(x)
# numbers.pop(x)
# print(numbers)
# numbers = [8, 3, 1, 6, 2, 4, 5, 9]
# count = 0
# for i in numbers:
#     # print(i)
#     if (i % 2 != 0):
#        print("The number of odd numbers in the list are: ", i)
# breakpoint()
# def print_till_zero(n):
#     if (n == 0):
#         return
#     print(n)
#     n = n - 1
#     print_till_zero(n)
#
#
# print_till_zero(8)
# num = int(input("Enter an integer greater than 1: "))
# for n in range(2, num):
#     for i in range(2, n):
#         if (n % i == 0):
#             break
#     else:
#         print(n)
# isprime = 1  # assuming that num is prime
# for i in range(2, num // 2):
#     if (num % i == 0):
#         isprime = 0
#         break
# if (isprime == 1):
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
# for i in range(100, 200):
#     num = i
#     sum = 0
#
#     while (num != 0):
#         digit = num % 10
#         sum = sum + digit
#         num = num // 10
#     if (sum % 2 == 0):
#         print(i)

# revs()
# calculateAvg()
# calculateArea()
# print(5 // 2)
# a = input("enter sequence")
# b = a[::-1]
# if a == b:
#     print("palindrome")
# else:
#     print("Not a Palindrome")
# Fahrenheit = int(input("enter number:"))
# # checkNumber(int(value))
# # calculate celcius
# Celsius = (Fahrenheit - 32) * 5 / 9
# print("celsius", Celsius)
# CelsiusToFahrenheit = 9.0 / 5.0 * Celsius + 32
# print("Fahrenheit", CelsiusToFahrenheit)

# userInput()
#     max = 0
# y = [2, 4, 6, 50, 43, 70, 234]
# for i in y:
#     if i > max:
#         max = i
# print("max number is ", max)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
