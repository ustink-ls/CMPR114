#import the other class file that contains the data. Since I cannot 
#import a file with a long file name that includes spaces, use 
#the below import. Or name module something simple like insects, 
#and then assign import to insects.
import sys
sys.path.append("/Users/leslyesirena/Desktop/Python/m13 Ch11 Inheritance + class exercise #10-2_#5a")
insects = __import__("m13 Ch11 Inheritance + class exercise #10-2_#5a")

#start the main function
def main():
    #create a Bumblebee object.
    bumblebee = insects.Bumblebee('Bumblebee', 'Sting', 'Black and yellow', 'Fuzzy')

    #create a Grasshopper object.
    grasshopper = insects.Grasshopper('Grasshopper', 'Sting', 'Black and yellow', 'Fuzzy')

    #Display the results of bumblebee.
    print("Species: ", bumblebee.get_species())
    print("Ability: ", bumblebee.get_ability())
    print("Color: ", bumblebee.get_color())
    print("Texture: ", bumblebee.get_texture())

    #Display the results of grasshopper.
    print("\n")
    print("Species: ", grasshopper.get_species())
    print("Ability: ", grasshopper.get_ability())
    print("Color: ", grasshopper.get_color())
    print("Body Type: ", grasshopper.get_body_type())

main()