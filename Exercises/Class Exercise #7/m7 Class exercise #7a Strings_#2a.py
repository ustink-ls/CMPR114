#This program gets a password from the user and validates it.

#import the file that contains the data. Since I cannot import
#a file with a long file name that includes spaces, use the below
#import. Or name module something simple like login, and then use
#import login.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m7 Class exercise #7a Strings_#2")
login = __import__("m7 Class exercise #7a Strings_#2")

#main program
def main():
    #Get a password from the user.
    password = input('Enter your password: ')

    #Validate the password.
    while not login.valid_password(password):
        print ('The password is not valid.')
        password = input('Enter your password: ')

    print ('That is a valid password.')

#call the main function.
if __name__ == '__main__':
    main()

    