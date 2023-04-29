#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like vehicles, 
#and then assign import to vehicles.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 Ch11 Inheritance + class exercise #10-2_#6a")
vehicles = __import__("m13 Ch11 Inheritance + class exercise #10-2_#6a")

#start the main function
def main():
    used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0)
    used_car1 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0)

    #Display the results of used car/used car1.
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_mileage())
    print("Price: ", used_car.get_price())
    print("\n")
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())

    print("\n")
    truck = vehicles.Truck('Toyota', 'Tacoma', 4000,12000.0)
    suv = vehicles.SUV('Volvo','SE', 30000, 18500.0)
    ev = vehicles.EV('Tesla', 'EV', 2000, 100000.0)

    #display the truck's data
    print("The following truck is in inventory:")
    print("Make: ", truck.get_make())
    print("Model: ", truck.get_model())
    print("Mileage: ", truck.get_mileage())
    print("Price: ", truck.get_price())
    print("\n")

    #display the SUV's data
    print("The following SUV is in inventory:")
    print("Make: ", suv.get_make())
    print("Model: ", suv.get_model())
    print("Mileage: ", suv.get_mileage())
    print("Price: ", suv.get_price())
    print("\n")

    #display the EV's data
    print("The following electric vehicle is in inventory:")
    print("Make: ", ev.get_make())
    print("Model: ", ev.get_model())
    print("Mileage: ", ev.get_mileage())
    print("Price: ", ev.get_price())
    print("\n")


main()