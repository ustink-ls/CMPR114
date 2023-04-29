#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like vehicles, 
#and then assign import to vehicles.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 Ch11 Inheritance + class exercise #10-2_#4a")
vehicles = __import__("m13 Ch11 Inheritance + class exercise #10-2_#4a")

#start the main function
def main():
    #first car
    used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0,2)

    #second car
    used_car2 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0,4)
   
    #Display the results of first car.
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_mileage())
    print("Doors: ", used_car.get_door())

    #Display the results of second car.
    print("\n")
    print("Make: ", used_car2.get_make())
    print("Model: ", used_car2.get_model())
    print("Mileage: ", used_car2.get_mileage())
    print("Price: ", used_car2.get_price())
    print("Doors: ", used_car2.get_door())

main()