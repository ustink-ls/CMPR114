#Caesar Cipher

#A “Caesar Cipher” is a simple way of encrypting a message 
#by replacing each letter with a letter a certain number of 
#spaces up the alphabet. For example, if shifting the message by
#13, an A would become an N, while an S would wrap around to the
#start of the alphabet to become an F.
#Write a program that asks the user for a message (a string) and 
#a shift amount (an integer). The values should be passed to a 
#function that accepts a string and an integer as arguments, and 
#returns a string representing the original string encrypted by 
#shifting the letters by the integer. For example, a string of 
#“BEWARE THE IDES OF MARCH” and an integer of 13 should result in 
#a string of “ORJNER GUR VQRF BS ZNEPU”.


user_string = input("enter your message: ")
shift_amount = int(input("enter the number to shift your message: "))
caesar_cypher = ""
for char in user_string:
    if char.isalpha():
        #shift the character by shift amount/uppercase letters
        char_code = ord(char.upper())
        shifted_code = (char_code - 65 + shift_amount) % 26 + 65
        shifted_char = chr(shifted_code)

        #lower case letters
        if char.islower():
            shifted_char = shifted_char.lower()

        caesar_cypher += shifted_char
    else: 
        caesar_cypher += char

print(caesar_cypher)


