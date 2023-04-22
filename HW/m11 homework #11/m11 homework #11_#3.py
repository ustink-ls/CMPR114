#3. RetailItem Class
#Write a class named RetailItem that holds data about an item in a 
#retail store. The class should store the following data in attributes: item description, units in inventory, and price.
#Once you have written the class, write a program that creates 
#three RetailItem objects and stores the following date in them:

class RetailItem:
    #the keyword(self)
    #it is used to access variables that belong to the class.
    def GetInformation(self):
        print("description: " + self.description)
        print("units in inventory: " + self.units)
        print("price: " + self.price)

#RetailItem1 Object
RetailItem1 = RetailItem()
RetailItem1.description = "Jacket"
RetailItem1.units = "12"
RetailItem1.price = "59.95\n"

#RetailItem2 Object
RetailItem2 = RetailItem()
RetailItem2.description = "Designer Jeans"
RetailItem2.units = "40"
RetailItem2.price = "34.95\n"

#RetailItem3 Object
RetailItem3 = RetailItem()
RetailItem3.description = "Shirt"
RetailItem3.units = "20"
RetailItem3.price = "24.95\n"

#display the results.
print('Item #1:')
RetailItem1.GetInformation()
print('Item #2:')
RetailItem2.GetInformation()
print('Item #3:')
RetailItem3.GetInformation()