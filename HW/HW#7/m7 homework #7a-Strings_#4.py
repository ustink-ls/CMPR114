#4. Pig Latin
#Write a program that accepts a sentence as input and converts 
#each word to “Pig Latin.” In one version, to convert a word to 
#Pig Latin, you remove the first letter and place that letter
#at the end of the word. Then, you append the string “ay” to the 
#word. Here is an example:
#English: I SLEPT MOST OF THE NIGHT
#Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def main():
    #Request the user's sentence.
    english = input("Enter a sentence that you want converted into pig latin: ")
    
    #call the pig_latin_converter function.
    pig_latin(english)

def pig_latin(english):
    #Split the user's sentence into words.
    word_list = english.split()

    #convert each word to Pig Latin.
    #create a variable that will hold an empty list. 
    #once the words are converted in the for loop,
    #they will be added to the pig_latin_word list.
    pig_latin_words = []
    for word in word_list:
        #remove the first letter and add it to the end of the word
        pig_latin_word = word[1:] + word[0]

        #add "ay" to the end of the word
        pig_latin_word += "ay"

        #add the Pig Latin word to the list
        pig_latin_words.append(pig_latin_word)
    
    #combine tne pig latin words together
    pig_latin = " ".join(pig_latin_words)

    #Display the pig latin translation.
    print("\nHere is the pig latin version of your sentence:", pig_latin)

main()
