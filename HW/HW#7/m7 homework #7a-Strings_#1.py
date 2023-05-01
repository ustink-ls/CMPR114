#1. Vowels and Consonants
#Write a program with a function that accepts a string as 
#an argument and returns the number of vowels that the 
#string contains. The application should have another function 
#that accepts a string as an argument and returns the number 
#of consonants that the string contains. The application should 
#let the user enter a string, and should display the number of 
#vowels and the number of consonants it contains.

def main():
    #Create the list of vowels.
    vowels = ["a", "e", "i", "o", "u"]

    #Create the list of consonants.
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    #Get a string from the user.
    user_string = input('Enter a string: ')

    #Make the user's string lower case so the functions match
    #the lowercase arrays.
    user_string = user_string.lower()
    print('\n')

    #Call the vowel_count function.
    vowel_count(user_string,vowels)

    #Call the consonant_count function.
    consonant_count (user_string, consonants)
    
#The vowel_count function counts the number of vowels in the 
#user's string.
def vowel_count(user_string,vowels):
    #Initialize a count variable.
    vowel = 0
    
    #Count the vowels.
    for i in range(len(user_string)):
        if user_string[i] in vowels:
            vowel += 1

    #This is what will be displayed after the vowels function is called
    #in the main function.
    print(f'The number of vowels contained in the string is {vowel}.')
    print('\n')

#The consonants function counts the number of consonants in the
#user's string.
def consonant_count (user_string, consonants):
    #Initialize a count variable.
    consonant = 0

    #Count the alphabetical values in the user's string.
    for j in range(len(user_string)):
        if user_string[j] in consonants:
                consonant+=1
    
    #This is what will be displayed after the main function calls 
    #vowels function, which then calls the consonants function.
    print(f'The number of consonants contained in the string is {consonant}.')

main()

