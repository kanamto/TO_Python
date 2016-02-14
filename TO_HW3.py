
# coding: utf-8

# In[88]:

#HW3, Problem 1

def histogram(list):
    '''Prints asterisks equal to values in list.
    
     The items in list must be integers.'''
    for item in list: #For each item
        print(item*"*") #the function prints the amount of stars based on the item's integer value.
        "\n"            #The next output is printed on a new line.  


# In[93]:

#HW3, Problem 2

def max_in_list(list):
    '''Returns the maximum value of a list.
    
    Takes list (of integers) and returns an integer. The items in list must be integers.'''
    result = list[0]      #Set the first item in list as the max
    for each in list:     #For each item in list
        if each > result: #If each item is greater than current result...
            result = each #...then set the max to the current item.
    return result         #After each value is compared, the max should be stored in result variable.
    


# In[17]:

#HW3, Problem 3

def mapping(list):
    '''Maps a list of character strings into a list of integers. 
    
    Takes list (of strings) input and returns list (of integers). The each integer corresponds to length of string in the original list.'''
    result = []             #Initialize a empty list to map to.
    for each in list:       #For each string in the list of strings...
        i = 0               #Start a counter of how many letters are in the string
        for letter in each: #For each character in each string,  
            i+=1            #increase the counter by 1
        result.append(i)    #When each character is counted, add that number to the new list 
    return result



# In[8]:

#HW3, Problem 4

def find_longest_word(list):
    '''Returns the length of the longest word in a list.
    
    Takes list input and returns integer. Combines mapping() and max_in_list() functions.'''
    return max_in_list(mapping(list)) #After mapping a list of words to list of lengths, find the max length (integer) 



# In[18]:

#HW3, Problem 5

def filter_long_word(list,n):
    '''Returns a list with strings of minimum length n.
    
    Takes a list (of strings) and returns a list (of strings). Uses mapping() output and compare against n.'''
    result = []                     #Initialize blank output list
    i = 0                           #Initialize a counter to reference indexed value of the list of words
    for each in mapping(list):      #For each item (which will be integers) in the output of mapping()..
        if each > n:                #if each integer is greater than n,
            result.append(list[i])  #then append the indexed word to the result list.
        i +=1                       #Increase the counter to next indexed word to corresponded to the next integer in the for loop
    return result


# In[30]:

#HW3, Problem 6

def palindrome2(string):
    '''Returns True or False depending on recognition of a Palindrome.
    
    Takes string input and returns boolean. This function ignores punctuation, capitalization, and spacing.'''
    lowercase_string = string.lower()       #Make all capitalized characters lower case. This function has no effect on symbols.
    original = ""                           #Initialize empty string for original string with punctuation and spacing. 
    reverse = ""                            #Initialize empty string for reverse of original string variable.
    alphabet = "qwertyuiopasdfghjklzxcvbnm" #Assign complete alphabet (as a string) to variable  
    for char in lowercase_string:           #For each char in lower case version of sentence,
        for letter in alphabet:              #and for each letter in the alphabet,
            if char == letter:                #if character and letter are the same (basically, if character is a letter),
                original += char                #update the original string with that letter.
                                            #At the end of for loop, only alphabet characters of the string remain.
    b = len(original)-1         #Set counter to 1 less than the length (last indexed position of the string)
    while b+1 > 0:              #While loop to cycle through each letter of original string (backwards). 
        reverse += original[b]  #Update reverse string with original string characters backwards (starting at the last position)
        b-=1                    #Update counter to one in front of the last character (and so on)
    if original == reverse:   #If reverse is identical to original string, then return true (is a palindrome)
        return True
    else:                  #If not, return false (not a palindrome)
        return False
            


# In[1]:

#HW3, Problem 7

def pangram(string):
    '''Returns True or False depending on recognition of a pangram.
    
    Takes string input and returns boolean. This function ignores punctuation, capitalization, and spacing.'''
    string = string.lower()                  #Make all capitalized characters lower case. This function has no effect on symbols.
    result = 0                               #Result is set to false (0) until proven otherwise 
    alphabet = "qwertyuiopasdfghjklzxcvbnm"  #Assign complete alphabet as a string to variable
    for letter in alphabet:                    #For each letter in the alphabet string,
        if letter in string:                    #if that letter is in the sentence,
            result += 1                        #then update the counter by 1.
        else:                                 #otherwise (if alphabet character in not in the sentence, it is not a pangram.
            return False
    if result == 26:                         #If the result = 26 (because each letter of the alphabet is counted once), then it is a pangram.
        return True


# In[4]:

#HW3, Problem 8

def bottles():
    '''Prints song verses of 99 bottles of Coke.
    
    Takes no variable as input and prints strings.'''
    i = 9          #Set bottle count to 99
    while i != 0:   #While bottle count is not 0, print the verse with number variable placeholders (%d) reflecting current bottle counts before and after drinking 1 more bottle.
        print('%d bottles of coke on the wall, %d bottles of coke. \nTake one down, pass it around, %d bottles of coke on the wall. \n' % (i,i,i-1))
        i -=1       #Lower bottle count after drinking 1 bottle. 


# In[15]:

#HW3, Problem 9

def translate(list):
    '''Translates English words into Swedish words.
    
    Takes list (of words) and returns list (of words). Only words in the predefined dictionary can be translated.'''
    lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} #Dictionary of English words with Swedish translations. 
    translated = []                          #Initialize empty list for translations
    for word in list:                        #For each word in the list,
        if word in lexicon:                   #if the word is in the dictionary as a key,
            translated.append(lexicon[word])   #then append the translation to the translated list.
    return translated         

    


# In[13]:

#HW3, Problem 10
## Should return the string instead of printing it
def char_freq(string):
    '''Build dictionary counting frequency of characters.
    
    Takes string input and prints dictionary with keys representing the characters and key values corresponding to the frequency that character occurs in the string.'''
    dict ={}                 #Initialize empty dictionary
    for char in string:      #For each character in a string,
        if char not in dict:  #if the character is not in the dictionary,
            dict[char] = 1     #Set that character as key with value 1, which adds the character to the dictionary be association.
        elif char in dict:    #if character is in the dictionary already,
            dict[char] += 1    #increase its count by 1.
    print(dict)


# In[14]:

#HW3, Problem 11
## Should return the string instead of printing it
def ROT13(string):
    '''Decodes or encodes a message based on Caesar Cipher.
    
    Takes string input and prints string. Caesar cipher shifts each letter 13 spaces to decode/encode a message.'''
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    result = ""        #After defining key, initialize empty string for resultant message
    for char in string:          #For each character in the string, 
        if char in key:           #if the character is in the dictionary (if it's not punctuation or spacing), 
            result += key[char]    #then update the result with shifted letter to encode/decode
        else:                     #otherwise (if it's punctuation or spacing),
            result += char         #update the result with the exact punctuation or spacing
    print(result)
        


# In[10]:

#HW3, Problem 12
## Should return the string instead of printing it
def correct(string):
    '''Corrects spacing errors in a sentence.
    
    Takes a string input and prints string. Corrects the following:
    1) Two or more occurrences of the space character is compressed into one, and 
    2) Inserts an extra space after a period if the period is directly followed by a letter. '''
    corrected = ""                                   #Initialize empty string for corrected sentence.
    i = 0                                            #Initialize counter.
    while i < len(string):                           #While counter is less than string length,
        if string[i] == "." and string[i+1] != " ":   #if string indexed character a period and the next character is not a space,
            corrected += ". "                          #then update the corrected sentence by adding a space. 
            i += 1                                     #Update the counter.
        elif string[i] == " ":                        #if the indexed character is a space, 
            corrected += " "                           #First update the sentence with the space.
            i += 1                                     #Update the counter.
            while string[i] == " ":                     #While the next character is a space, 
                corrected += ""                            #Replace with space with nothing in the corrected sentence.
                i += 1                                     #Update the counter. At the end of this loop, only one space will be preserved in the corrected sentence between words
        else:                                         #if the character is not period or string,
            corrected += string[i]                     #Update the corrected sentence without changing the original character.
            i += 1                                     #Update the counter.
    print (corrected)  #After each action the counter is updated to reflect moving on through all characters of the original string.



# In[11]:

#HW3, Problem 13

def make_3sg_form(verb):
    '''Heuristic method to conjugate infinitive verbs into 3rd person singular form.
    
    Takes string input and returns string. Only works on words'''
    if verb[-1:] == "y":          #Isolating the last character of the word. If it is y,
        verb = verb[:-1] + "ies"   #then third person singular form deletes y and adds ies. 
    elif verb[-1:] == "o" or verb[-1:] == "s" or verb[-1:] == "x" or verb[-1:] == "z" or verb[-2:] == "ch" or verb[-2:] == "sh":
        verb += "es"              #If the last letter is o,s,x, or z, or last two letters are ch or sh, then third person singular form adds es.
    else:                         #Otherwise, 
        verb += "s"                #verbs are updated with s to represent third person singular form.
    return verb                   #Return updated verb.


# In[7]:

#HW3, Problem 14
## Doesn't work in all cases, see my test cases - Prof G
def make_ing_form(verb):
    '''Heuristic methods to conjugate infinitive verbs into present participle form.
    
    Takes string input and returns string. Only works on words'''
    vowels = ["a", "e", "i", "o", "u"]        #Define vowels in list
    if verb[-1:] == "e":                      #If last letter is e,
        if verb[-2:] == "ee" or verb == "be":  #and if the last two letters are e or if the verb is be,
            verb += "ing"                       #then just add ing.
        else:                                  #and the above is not true,
            verb = verb[:-1] + "ing"            #then update verb by taking all but the last letter (i.e., deleting e), and add ing.
    elif verb[-2:] == "ie":                   #If the last two letters are ie,
        verb = verb[:-2] + "ying"              #then update verb by taking all but the last 2 letters (i.e., deleting ie), and add ing.
    elif verb[-3:-2] not in vowels and verb[-2:-1] in vowels and verb[-1:] not in vowels: #If last letter is not in vowels (i.e., consonant) and second last letter is a vowel and last letter is not a vowel, 
        verb += verb[-1:] + "ing"              #then update verb with the last letter (consonant) and add ing. 
    else:                                     #Otherwise, 
        verb += "ing"                          #update verb with ing.
    return verb 
        

##Test Cases
help(histogram)
help(make_ing_form)

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", mapping(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_word(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", palindrome2("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", bottles())

print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", ROT13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')



