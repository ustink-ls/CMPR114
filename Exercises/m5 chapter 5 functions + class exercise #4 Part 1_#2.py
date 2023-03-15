#This program demonstrates passing two string arguments to a function.

def main ():
    first_name = input('Enter your first name: ')
    last_name = input ('Enter your last name: ')
    complete_address = input('Enter your complete address: ')
    print ('Your name reversed is ')
    reverse_name(first_name, last_name)
    address(complete_address)
    

def reverse_name(first, last):
    print(last, first)

def address (user_address):
    print (f'Your full address is {user_address}.')

#Call the main function.
main()
