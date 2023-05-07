#CMPR 114 Project_Leslye Sirena

#Modules
import openai
import time

#Demonstrate the use of List.
def demonstrate_list_operations():
    print("Demonstrate the use of list in Python:")
    #orignal list of items.
    cities = ["New York", "London", "Paris", "Munich"]
    print("Original list:", cities)
    #add madrid to orignal list.
    cities.append("Madrid")
    print("After append:", cities)
    #remove new york from appended list.
    cities.remove("New York")
    print("After remove:", cities)
    print()

#Demonstrate the use of Tuple.
def demonstrate_tuple_operations():
    print("Demonstrate the use of tuple in Python:")
    #original tupple
    tup = (15, 20, 123, 47, 26, 81)
    print ("Original tupple: ", tup)
    #The max function accepts a sequence, such as a list, 
    #as an argument and returns the item that has the highest 
    #value in the sequence.
    print(f'The largest number in this tuple is {max(tup)}.')
    print()

#Demonstrate the use of Dictionaries.
def demonstrate_dictionaries_operations():
    print("Demonstrate the use of dictionaries in Python:")
    # create a dictionary with some data
    country = {"name": "Italy",
        "capital": "Rome",
        "language": "Italian",
        "currency": "EUR",
        "popular food": "pasta"
    }
    #print the original dictionary.
    print("Original dictionary: ", country)
    #modifying popular food in the dictionary.
    country["popular food"] = "Gelato"
    #print the dictionary after popular food modification.
    print("After pop food update:", country)
    #delete langauge/currency in the dictionary.
    del country['language']
    del country['currency']
    #print the updated dictionary after deleted values.
    print("After removal update:", country)
    print()

#Demonstrate the use of Exception Handling.
def demonstrate_exception_handling_operations():
    print("Demonstrate the use of Exception Handling in Python:")
    #This program calculates gross pay.
    #If this statement raises a ValueError exception...
    #The program jumps to the except ValueError clause 
    #and executes its handler.
    while True:
        try:
            # Get the number of hours worked.
            hours = int(input('How many hours did you work? '))
            # Get the hourly pay rate.
            pay_rate = float(input('Enter your hourly pay rate: '))
            # Calculate the gross pay.
            gross_pay = hours * pay_rate
            # Display the gross pay.
            print(f'Gross pay: ${gross_pay:,.2f}')
            print()
            #exit the loop
            break
        except ValueError:
            #Demonstrate the use of repeat loop.
            print('ERROR: Hours worked and hourly pay rate must be valid integers.')
            retry = input('Do you want to retry? (y/n): ')
            if retry.lower() != 'y':
                #exit the looop
                break

#Demonstrate the use of functions.
#Call the functions to display in terminal:
demonstrate_list_operations()
demonstrate_tuple_operations()
demonstrate_dictionaries_operations()
demonstrate_exception_handling_operations()

#Demonstrate the use of Object Oriented.
class Pet:
    #using init to create a customized constructor
    #here we have three arguments
    def __init__(self, name, animal, size):
        self.name = name
        self.animal = animal
        self.size = size

    def GetPet(self):
        print("Pet name is " + self.name)
        print("Pet is " + self.animal)
        print("Pet size is " + self.size)
#creating the Objects and calling the three arguments
pet1= Pet("Jodie", "cat", "small")
pet2= Pet("Rufus", "dog", "large")
#calling the function
print("Demonstrate the use of Object Oriented in Python:")
pet1.GetPet()
pet2.GetPet()
print()

#Use Python and OpenAPI to implement a ChatGPT session.
#Set up the OpenAI API key
openai.api_key = "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"
#Define a function to generate ChatGPT's response to user's
#question.
def generate_response(prompt):
    response = openai.Completion.create(
        #The Davinci model is one of the natural language processing 
        #models developed by OpenAI. It is known for its ability to 
        #generate high-quality, human-like text in a wide range of 
        #styles and formats.
        engine="davinci",
        prompt=prompt,
        #The maximum number of tokens is set to 1000, which means 
        #that the model will generate text up to a maximum length 
        #of 1000 words.
        max_tokens=50,
        #The parameter n in the OpenAI API's Completion.create() 
        #method specifies the number of text completions to generate 
        #for a given prompt. n is set to 1, which means that the 
        #API will generate a single text completion for the given 
        #prompt. Setting n to a higher value will cause the API to 
        #generate multiple completions for the same prompt, which 
        #can be useful if you want to compare and choose between 
        #different versions of the generated text. 
        n=1,
        #No stop sequence is specified, which means that the model 
        #will continue generating text until it reaches the maximum 
        #number of tokens or runs out of ideas.
        stop=None,
        #The temperature is set to 0.5, which controls the 
        #randomness of the generated text. A temperature of 0.5 
        #means that the model will generate text that is somewhat 
        #random, but still coherent and logical.
        temperature=0.5,
    )
    return(response.choices[0].text.strip())

#Demonstrate the use of repeat loop.
#Ask the user for a question and generate a response
while True:
    user_input = input("Ask ChatGPT a question: ")
    response = generate_response(user_input)
    print(response)
    #The time.sleep(1) line is added to slow down the loop so 
    #that it does not run too quickly and overwhelm the console. 
    #You can adjust the sleep time as needed.
    time.sleep(1)
    #ask the user if they want to continue asking ChatGPT questions.
    while True:
        user_choice = input("\nDo you want to ask another questions? (y/n): ")
        if user_choice.lower() == 'n':
            print("Exiting program.")
            exit()
        elif user_choice.lower() == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

