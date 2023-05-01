#3. Word Separator
#Write a program that accepts as input a sentence in which all 
#of the words are run together, but the first character of each 
#word is uppercase. Convert the sentence to a string in which
#the words are separated by spaces, and only the first word starts
#with an uppercase letter. For example the string 
#“StopAndSmellTheRoses.” would be converted to “Stop and smell
#the roses.”

def main():
    #Get a string from the user.
    user_string = input('Enter a sentence in which all of the words run together, but the first character of each word is uppercase: ')

    #Call the vowel_count function.
    word_separator(user_string)

#The word_separator function converts the string into a sentence
#that is separated by spaces, and only the first word starts with
#an uppercase.
def word_separator(user_string):
    #Initialize a variable that will count the number of uppercase letters.
    upper = 0

    #Create a variable that looks for non spaces.
    result = ""

    #Create a loop that looks for uppercase letters in the user's string.
    for char in user_string:
        if char.isupper() and upper > 0:
            result += " "
            result += char.lower()
        else:
            result += char
        upper += 1
    #This is what will be displayed after the word_separator function 
    #is called in the main function.
    print(f'The updated sentence is: {result}.')
    print('\n')

main()

