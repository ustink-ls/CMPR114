#Project #1 (based on Chapter 5 functions) for the program below
#be sure to use functions.

def main():
    #Ask the user for the number of fat/carbohydrate grams
    #consumed in a day.
    fats = float(input('Enter the number of fat grams consumed in a day: '))
    carbohydrates = float(input('Enter the number of carbohydrate grams consumed in a day: '))
    print('\n')
    #Call the functions.
    calories_from_fat(fats)
    calories_from_carbohydrates(carbohydrates)

def calories_from_fat(fats):
    #Calculate the calories from fat.
    caloriesF = fats * 9
    print(f'The number of calories that result from fat is {caloriesF:,.2f}.')

def calories_from_carbohydrates(carbohydrates):
    #Calculate the calories from carbohydrates.
    caloriesC = carbohydrates * 4
    print(f'The number of calories that result from carbohydrates is {caloriesC:,.2f}.')

main()