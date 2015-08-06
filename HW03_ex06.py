import math
#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare
# Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

def compare(x,y):
    print
    print ("Operating in compare")
    print
    print ("Value of X: "+str(x))
    print ("Value of Y: "+str(y))
    if (x > y):
        print ("X is greater than Y. Return: 1")
        return 1
    elif (x==y):
        print ("X is equal to Y. Return: 0")
        return 0
    else :
        print ("X is less than Y. Return: -1")
        return -1


################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.
# Use incremental development to write a function called hypotenuse 
# that returns the length of the hypotenuse of a right triangle 
# given the lengths of the two legs as arguments. 
# Record each stage of the development process as you go.

def hypotenuse(x,y):
    print
    print ("Operating in hypotenuse")
    print
    print ("Length of the first side : "+str(x))
    print ("Length of the second side : "+str(y))

    sqrX = x**2
    print("Squared value of first side (x) : "+str(sqrX))

    sqrY = y**2
    print("Squared value of second side (y) : "+str(sqrY))

    sumOfSqrs = sqrX + sqrY
    print("Sum of squared value of the first and the second sides : "+str(sumOfSqrs))

    hypotenuse = math.sqrt(sumOfSqrs)
    print ("Length of the hypotenuse : "+str(hypotenuse))



################################################################################
# Exercise 3
# When you submit only include your final function: is_between
# Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.

def is_between(x,y,z):
    print
    print ("Operating in is_between")
    print
    if((x <= y) and (y <=z)):
        print("x <= y <= z is True")

    else :
       print("x <= y <= z is False") 


################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(str):
    print
    print ("Operating in is_palindrome")
    print
    if (len(str) == 0):
        print("The string entered is an emptry string. Cannot check for a palindrome")

    elif (len(str) == 1):
        print ("Single character entered. Cannot check for a palindrome")

    else :
        if(str == str[::-1]):
            print ("The entered sequence '"+str+"' is a palindromic sequence")
        else :
            print ("The entered sequence '"+str+"' is NOT a palindromic sequence")


################################################################################
# Exercise 7
# When you submit only include your final function: is_power

#A number, a, is a power of b if it is divisible by b and a/b 
#is a power of b. 
#
#Write a function called is_power that takes parameters a and b and 
#returns True if a is a power of b. Note: you will have to think 
#about the base case.

def is_divisible(a,b):
    quotient = float(a)/b
    if(int(quotient) == quotient):
        return True

def is_power(a,b):
    print
    print ("Operating in is_power")
    print
    if(is_divisible(a,b)):
        c = a/b
        if(is_divisible(c,b)):
            print ("'a' ("+str(a)+") is a power of 'b' ("+str(b)+")")

        else :
            print ("'a' ("+str(a)+") is NOT a power of 'b' ("+str(b)+")")

    else :
        print ("'a' ("+str(a)+") is NOT a power of 'b' ("+str(b)+")")


################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")

    ############################################################################
    # Uncomment the below to test and before commiting:
    # Exercise 1
    compare(1,1)
    compare(1,2)
    compare(2,1)
    # Exercise 2
    hypotenuse(1,1)
    hypotenuse(3,4)
    hypotenuse(1.2,12)
    # Exercise 3
    is_between(1,2,3)
    is_between(2,1,3)
    is_between(3,1,2)
    is_between(1,1,2)
    # Exercise 6
    is_palindrome("Python")
    is_palindrome("evitative")
    is_palindrome("sememes")
    is_palindrome("oooooooooooo")
    # Exercise 7
    is_power(28,3)
    is_power(27,3)
    is_power(248832,12)
    is_power(248844,12)


if __name__ == "__main__":
    main()