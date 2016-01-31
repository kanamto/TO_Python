
# coding: utf-8

# In[33]:

#HW2, Problem 1: Fibonacci Sequence Calculator

def fib(n): #function fib takes variable n (integer type)
    fibo=[0,1]
    i=0
    while fibo[i] < n: #While loop comparing index of a vector to user input integer n
        print (fibo[i]) #Prints integer of indexed position that is still (based on a true while loop) less than n
        nextfibo = fibo[i] + fibo[i+1] #Establishies the next number in Fibonacci sequence.
        i +=1 #up the counter to find the next Fibonacci sequence.
        fibo.append(nextfibo) #Appends vector with next number of Fibonacci sequence. 
    # When n <= fibo[i], while loop stops.
    
print(fib(55), '\n')


# In[22]:

#HW2, Problem 2: Max of Two 

## Best practice is to return the values without calling the print function.

def my_max(x,y): #function takes two variables, x and y (both integer type), and compares them.
    a = "The largest is %d" #String statement with %d (string formatting) as a placeholder for double variable.
    if x > y: #If x is bigger than y, then x is printed.
        return a %(x)       #Define %d as variable x
    elif x == y: #If x is equal to y, then the function prints that they're equal.
        return "they're equal"
    else: #If it's not the two possible outcomes above, then only y>x is left, so y is printed as the largest.
        return a %(y)       #Define %d as variable y
    
print(my_max(0,0))
print(my_max(3,0))
print(my_max(0,4))


# In[25]:

#HW2, Problem 3: Max of Three

## Best practice is to return the values without calling the print function.

def max_of_three(x,y,z): #function takes three variables and compares them.
    a = "The largest is %d" #String statement with %d (string formatting) as a placeholder for double variable.
    b = "The two largest are %d" #Second scenario of comparing numbers. 
    if x > y: #If x>y...
        if x > z: #...and x>z, then x is largest.
            return a %(x)   #Define %d as variable x
        elif x == z:#...and x=z, then the two are equally large. 
            return b %(x)
    elif y > z: #If y>z...
        if y > x: #...and y>x, then y is largest.
            return a %(y)
        elif y == x: #...and y=z, then the two are equally large. 
            return b %(y)
    elif z > x:
        if z > y: #...and z>y, then z is largest.
            return a %(z)
        elif y == z: #...and y=z, then the two are equally large.  
            return b %(z)
    else: #Otherwise, they're all equal.
        return "they're all equal"
    
print(max_of_three(1,2,3)) #All combinations of possible outcomes when comparing three integers. 
print(max_of_three(6,5,4))
print(max_of_three(7,9,8))
print(max_of_three(1,1,0))
print(max_of_three(0,1,1))
print(max_of_three(1,0,1))
print(max_of_three(0,0,0))


# In[26]:

#HW2, Problem 4: List or String Length

def mylen(a): #Function takes variable a (vector,list, or string type)
    i = 0 #initialize counter variable, i (integer type) at 0
    for n in a: #For each value stored in each index position:
        i+=1    #Increase the counter i by 1
    return i   #When loop is done, all items of the vector/list/string is counted once, totaling the number (or length) of the value in a. 
     
print(mylen([1,2,3])) #Testing vector
print(mylen("Dog"))   #Testing string     


# In[27]:

#HW2, Problem 5: Vowels or Consonants

def vowel(letter): #Function taking a single letter (string type) and identifying vowels (or not)
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u": #Combination of or-logic makes the statement true if any single statement is true. Therefore, if the letter is equal to any of the vowels...
        return True #... then it's a vowel.
    else:           #If it's not a vowel, it's a consonant.
        return False 
           
print(vowel("e"))
print(vowel("f"))


# In[30]:

#HW2, Problem 6: Translate

def translate(string): #Function taking string (string type) and counting vowels twice.
    word = "" #Initialize output as empty string.
    for letter in string: #For each letter (value in indexed position starting at 0) in string....
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == " " : 
            word += letter #...adds the character to the string if it's a vowel or a space using combined or-logic statement above
        else:
            word += letter + "o" + letter #...or if it's not a vowel or space (therefore a consonant), then add the letter twice with an O between.
    return word #After all letters in the string are scanned once, the output will be the translated word
    
print(translate("hello hola"))


# In[31]:

#HW2, Problem 7: Sum and Multiply (of Lists)

def sum(a): #Function to sum all numbers in variable a (list type).
    b=0     #Initialize at 0 because we do not want whatever stored in b to affect the sum
    for n in a: #For each value of n (indexed value) of vector a 
        b+=n    #Add the indexed value (assumed to be a number) to b
    return b   #Return the total, which is the sum of all indexed values 

def multiply(a): #Function to multiply all numbers in variable a (list type).
    b=1          #Initialize at 1 because initializing at 0 would only return 0 
    for n in a:  #For each value (assumed to be a number type) of n (indexed value) of vector a
        b*=n     #Multiply the indexed value (assumed to be a number) with the existing value of b
    return b    #Return the total, which is the product of all indexed values 

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))


# In[32]:

#HW2, Problem 8: esreveR 

def reverse(string): #Function to reverse "string" (string type).
    esrever = ""     #Initialize empty string for reverse.
    b = len(string)-1 #String length - 1 represents the position of the last indexed character in the string (because python indexes at 0)
    while b+1 > 0:    #Starting while loop at b+1 because we want the loop to run as many times as there are letters in "string" 
        esrever += string[b] #Add the last letter of "string" to the "esrever" variable 
        b-=1                 #Move 1 index position towards the first character of "string"
    return esrever    #when b=0, the loop will have run through all the letters, and return the reverse of the "string" value.   
    
print(reverse("horseshoe"))
print(reverse("what is that?"))



# In[33]:

#HW2, Problem 9: Palindromes 

def is_Palindrome(string): #Function to identify palindromes in "string" (string type).
    grints = ""            #Set reverse of string as empty string
    b = len(string)-1      #Set counter to 1 less than the length (last indexed position of the string)
    while b+1 > 0:         #Reverse the string value and saves to variable grints
        grints += string[b]
        b-=1
    if string == grints:   #If reverse is identical to original string, then return true (is a palindrome)
        return True
    else:                  #If not, return false (not a palindrome)
        return False
    
print(is_Palindrome("amanaplanacanalpanama"))
print(is_Palindrome("horsehoe"))


# In[36]:

#HW2, Problem 10: Are you a member?

## This function should take two parameters, not just one.

# def is_member(x): #Function to check variable x (any type) against values in a list.
#     a = ["georgetown","pilcher","math", 510, 25.4] #Predefine a membership list for comparison.
#     result = 0    #Set function output to 0 (assumes not a member until proven otherwise)
#     for n in a:   #For each value in vector a,...
#         if n == x:     #... if the value, n, is equal to x,
#             result = 1     # set counter to 1 (meaning the outcome is true everytime a match is found)
#         else:          #... if the value is not equal,
#             result += 0    # add 0 to the counter (which does not affect the counter if it already 0 or 1). The counter is not affected by any instance where there is no match.
#     return bool(result) #If there is at least 1 match (anywhere in the list), result = 1, and boolean of 1 is True. Otherwise, result = 0 and boolean is False.
#
# print(is_member("math"))
# print(is_member(25.4))
# print(is_member("whatever"))


# In[37]:

#HW2, Problem 11: Checking for Overlap

def overlapping(x,y): #Function takes two variables, x and y (both list type), and compares values in them.
    result = 0  #Set result to no match (0) until proven otherwise
    for n in x: #For each value in list x...
        for m in y: #...take each value in list y
            if n == m: #If the two are equal...
                result = 1 #...then result is equal to 1 (meaning true, there's at least 1 match)
            else:      #Otherwise, there are no matches...
                result += 0 #... and the result value is not affected whenever there are no matches
    return bool(result) #If you can prove there is overlap (because result initially is 0, meaning no matches), then true is returned. 

print(overlapping([1,2,3,4],[0,9,8,7,6,5]))
print(overlapping([1,2,3,4],[0,9,8,7,6,4]))


# In[ ]:

def overlapping(x,y): #Function takes two variables, x and y (both list type), and compares values in them.
    result = 0  #Set result to no match (0) until proven otherwise
    for n in x: #For each value in list x...
        for m in y: #...take each value in list y
            if n == m: #If the two are equal...
                result = 1 #...then result is equal to 1 (meaning true, there's at least 1 match)
            else:      #Otherwise, there are no matches...
                result += 0 #... and the result value is not affected whenever there are no matches
    return bool(result) #If you can prove there is overlap (because result initially is 0, meaning no matches), then true is returned. 

print(overlapping([1,2,3,4],[0,9,8,7,6,5]))
print(overlapping([1,2,3,4],[0,9,8,7,6,4]))


# In[38]:

#HW2, Problem 12: Generate Characters

def generate_n_chars(n,c): #function takes n (integer type) and c (character type) to create a new string.
    m = 0  #Initialize counter to 0
    d = "" #Initialize new empty string
    while m < n: #While counter is less than the number (because I should not simplify this loop with a multiplication of variables expression), 
        d += c   #variable c is concatenated onto new string d.  
        m += 1   #loop runs five times since m starts at 0 (0, 1, 2, 3, 4)
    return d     #resultant new string d is a string c repeated n times  

print(generate_n_chars(5,"char"))

##TEST CASES

print('#1\n')
fib(500)
print('\n')

print('#2\n')
print(my_max(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(vowel('e'))
print(vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_Palindrome('radar'))
print(is_Palindrome('Gerhard'))
print('\n')

print('#11\n')
# print(is_member('dog', ['cat', 'dog', 'zebra']))
# print(is_member(3, [1,2,3,4]))
# print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))

