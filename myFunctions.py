#
# Python Name: myFunctions
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows


def blankCheck(anyInput):
    if not (anyInput.replace(" ","") == ("")):
        pass
    else:
        raise NameError("Input cannot be blank")
#typeChecks may not work
#def stringCheck(anyInput):
#    if (type(anyInput) is not type(str)):
#        raise TypeError("Input must be a string")
#    else:
#        pass

#typeChecks may not work
#def intCheck(anyInput):
#    if (type(anyInput) is not type(int)):
#       raise TypeError("Input must be a int")
#    else:
#        pass

#typeChecks may not work
#def floatCheck(anyInput):
#    if (type(anyInput) is not type(float)):
#        raise TypeError("Input must be a float")
#    else:
#        pass

def quitCheck(anyInput):
    if not (anyInput.upper() == "QUIT"):
        pass
    else:
        print("Programing ending. Have a nice day!")
        quit()

def positiveCheck(numInput):
    if not (numInput != abs(numInput) and numInput != 0):
        pass
    else:
        raise ValueError("Input cannot be negative")

def negativeCheck(numInput):
    if not (numInput != (abs(numInput) * -1) and numInput != 0):
        pass
    else:
        raise ValueError("Input cannot be positive")

def main(argumentList):
    sumOfNumbers = 0
    print("You are in the main function")
    print("Have a nice day.")
    for arg in argumentList:
        try:
            sumOfNumbers += float(arg)
            print(sumOfNumbers)
        except ValueError:
            print("Value Error")

def printMe(numInput):
    print("I was told to print: " + float(numInput))

def inputInteger(min, max):
    while True:
        try:
            aInput = int(input("Please enter a number between 0 and 10"))
        except:
            print("Exception error!")
            continue
        if (aInput >= min and aInput <= max ):
            return aInput
        else:
            print("Number is not in between the min and max!")
            continue
#power function
def pow2(aNumber):
    result = aNumber * aNumber
    return result


def floatCheck(numInput): #Updated new float check that uses type, old function did not work
    if (str(type(numInput)) == "<type 'float'>"): #Pretty sure theres a better way to do this <--
        print("SUCCESS")
    else:
        print("FAILURE")

testNumber = "456456.04"

if str(testNumber) in ".":
    print("YAY")
else:
    print("NAY")

testBlahBlah = "Happy"
print(testBlahBlah.find("p"))

floatCheck(456)