#Author: Leul Adane
#Date: 11/8/22
#Purpose: Roman numeral calculator


import sys


def get_input():
    #parameter- none since input is inside the function
    #returns- userInput and userInput2 are the valid roman numerals. operant is a string giving the valid operation.
    userInput = input("Enter the first roman number: ").upper()   #input to be  checked for validity
    valid_roman_letters = ["M", "C", "D", "L", "X", "I", "V"]#list of valid roman nuumerals
    i=0
    while i < len(userInput):  
        if userInput[i] not in valid_roman_letters:#loops through and checks if string input is valid
            userInput = input("Enter a valid roman letter: ").upper()#asks for valid input if input is invalid
        else:
            i+=1
    userInput2 = input("Enter the second roman number: ").upper()
    j=0
    while j < len(userInput2):  
        if userInput2[j] not in valid_roman_letters:#loops through and checks if string input is valid
            userInput2 = input("Enter a valid roman letter: ").upper()#asks for valid input if input is invalid
        else:
            j+=1
    operant = input("Enter the operation: ")
            
    valid_operations = ["+", "-", "*", "^", "/"]#same as above for operant with ifferent list
    while operant not in valid_operations:
        operant = input("Please enter a valid operator: ")
        
    return userInput, userInput2, operant

def errorCheck(value):
    #parameter- value is an integer to be checked
    #returns- a decimal between 0 and 3999
    #exits program if conditions fulfilled
    if value > 3999:
        sys.exit("The result is too big to be converted to roman numeral")
    elif value <= 0:
        sys.exit("The result is less than 1, and there is no roman numeral for numbers less than 1. ")

def roman_number_to_arabic(inputs):
    #parameter- input is string of roman numerals 
    #returns- integer value of two inputs after conversion
    userInput = inputs[0]
    userInput2 = inputs[1]
    operant = inputs[2]
    j = 0
    num = 0
    while j < len(userInput):
        if j+1<len(userInput) and userInput[j:j+2] in roman_dictionary:
#The first condition checks if the index we are trying to access has a next value
#The 2nd one checks if the first 2 items are in the dictionary if they are
#then it adds their respective values from the dictionary to the varible num
            num+=roman_dictionary[userInput[j:j+2]]
            j+=2
        else:
#if either of the above conditions are false the it just adds that specific value from the dic to the varible num      
            num+=roman_dictionary[userInput[j]]
            j+=1
        
    k = 0
    num2 = 0
    while k < len(userInput2):
        if k+1<len(userInput2) and userInput2[k:k+2] in roman_dictionary:
            num2+=roman_dictionary[userInput2[k:k+2]]
            k+=2
        else:
            num2+=roman_dictionary[userInput2[k]]
            k+=1
    print(f'The first integer is {num}')
    print(f'The second integer is {num2}')
    return num, num2


def do_operation(num, num2, operant):
    #parameters- num and num2 are the integer values to be operated on. operant is a string representing the operation.
    #returns- result is the final output after calculating. remainder is the second output during division.  operant returned to prevent error in line 124.
    remainder = 0 #set to 0 on every case except for dividing to counter
    if operant == "+":
        result = num + num2 
        return result
    elif operant == "-":
        result = num - num2 
        return result
    elif operant == "*":
        result = num * num2
        return result
    elif operant == "^":
        result = num ** num2
        return result
    elif operant == "/":
        result = num // num2
        remainder = num % num2

    return result, remainder, operant



def arabic_to_roman(value):
    #parameter- value is the integer found from previous function: either result or remainder
    #returns- roman_number_string is the integer after it is converted to a string with roman number
    num = value
    roman_num = [] #this empty list saves the converted roman numeral
    for key, value in reversed(roman_dictionary.items()):
        
# The .items() method allows us to loop through both the key and the value of the dic
#we reversed it because we want to go through large numbers first
#Start with the largest symbol value and see if it is less than the number we have so far.
#If it is, we add that respective key from the dic, then subtract value from the integer itself,
#and loop until the num variable becomes positive or there is no value to add on.

        while num > 0:
            if value <= num:
                roman_num.append(key)
                num -= value
            else:
                break
    roman_numbers_string = "".join(roman_num) #Converts the list to string
    return roman_numbers_string
    

roman_dictionary = {"I": 1, "II" : 2, "III" : 3, "IV" : 4, "V" : 5, "VI" : 6,
              "VII" : 7, "VIII" : 8, "IX" : 9, "X" : 10, "XX" : 20, "XXX" : 30,
              "XL" : 40, "L" : 50, "LX" : 60, "LXX" : 70, "LXXX" : 80, "XC" : 90, "C" :
              100, "CC" : 200, "CCC" : 300, "CD" : 400, "D" : 500, "CM" : 900, "M": 1000}

print("Leul's Roman Numeral Calculator")
checker = "" #value that makes loop exit

while checker != "E":   #checks to continue when value is not E           
    inputs = get_input()#calls function to get the user inputs
    operant = inputs[2]#third value of inputs since get_input returns tuple
    result = 0
    remainder = 0
    
    arabic_numbers = roman_number_to_arabic(inputs)#calls function to convert inputs into integers
    if operant != "/":
        result = do_operation(arabic_numbers[0], arabic_numbers[1], operant)
    else:
        result, remainder, operant = do_operation(arabic_numbers[0], arabic_numbers[1], operant)#calls function to do operation and returns result and remainder. reason for operant is explained above.
    errorCheck(result)#calls error checking function before printing result
    result = arabic_to_roman(result)#calls function to convert integer to roman string
    print(f'The result is {result}')#prints result of operation in roman numeral form
    if remainder != 0:
        remainder = arabic_to_roman(remainder)
        print(f'The Remainder is {remainder}')#prints remainder only when remainder is not zero
    checker = input("Enter E to exit the program or any other letter to continue") #user input that restarts or ends program
