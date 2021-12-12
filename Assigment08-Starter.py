# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kathleen Wong,12.08.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kathleen Wong,12.08.2021,Modified code to complete assignment 8
    """
    # -- Constructor -- #
    def __init__(self, product_name: str, product_price: float):
        # 	   -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties -- #
    # product_name
    @property
    def product_name(self): # getter or accessor
        """
        property: gets product_name
        setter: validates product_name. if product_name is numeric, script will tell user to try again
        return: product_name
        """
        # gets product name
        return str(self.__product_name)

    @product_name.setter # setter
    def product_name(self, value):
        if value.isnumeric() == True:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # product_price
    @property
    def product_price(self):  # getter or accessor
        """
        getter: get product price
        #setter: set price value to product_price if numeric. else, raise error message
        :return: product_price
        """
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Not numeric. Try again.")

    # -- Methods --
    def to_string(self):
        # convert results into string
        return self.__str__()

    def __str__(self):
        # formats product name and string as: name, price
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects)
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kathleen Wong, 01.09.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_rows: list):
        """
        :param file_name:
        :param list_of_rows (list):
        :return: list_of_rows (list) of data
        """
        try:
            file_obj = open(file_name, "w") # opens file to write in
            for product in list_of_rows:
                file_obj.write(str(product) + "\n")
            file_obj.close()
            print("File saved successfully!")
        except:
            print("File did not save successfully. Try adding some data and try again!")
        return list_of_rows

    @staticmethod
    def read_data_from_file(file_name: str):
        """
        :param file_name:
        :return: list_of_rows (list) containing all items in file
        """
        list_of_rows = []
        try:
            # reads file and writes data from file into list_of_rows
            file_obj = open(file_name, "r")
            for line in file_obj:
                product = line.split(",")
                row = Product(product[0], product[1])
                list_of_rows.append(row)
            file_obj.close()
        except:
            print("There is an error! Try adding some data first")
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    a class to perform input and output

    methods:
    print_options(): prints options available to user
    get_option(): asks which option the user wants to select
    show_current_data(list_of_rows): rows of data already inputted
    add_product_data(): vet data and add to list

    changelog:
        RRoot, 1.1.2030, Created Class
        Kathleen Wong, 12.10.2021, finished class to complete Assignment 08
    """

    @staticmethod
    def print_options():
        # prints options
        print("""
        Menu of options:
        1. Show current data in list of product objects
        2. Add to list
        3. Save current data to file    
        4. Exit    
        """)

    @staticmethod
    def get_option():
        # Asks which option the user wants to select
        option = str(input("Which option would you like to select? Pick from 1-4. "))
        return option

    @staticmethod
    def show_current_data(list_of_rows: list):
        # prints current data
        print("******* The current items are: *******")
        for row in list_of_rows:
            print(row.product_name, ",", str(row.product_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def add_product_data():
        """ asks for product name and price and calls for class to vet the entry
        :return: vetted product name and price
        """
        try:
            str_name = str(input("What product do you want to add? ")).strip()
            float_price = float(input("How much is the product? "))
            product = Product(product_name = str_name, product_price = float_price)
        except Exception as e:
            print(e)
        return product

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# # Main Body of Script  ---------------------------------------------------- #
try:
    """"
    actions taken:
    1. prints options
    2. loops through file and saves it to list
    3. asks for option
    4. loops through options until 4 is selected
    """
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
    while True:
        # printing options
        IO.print_options()
        # printing items already in list
        IO.show_current_data(lstOfProductObjects)
        # getting option
        option = IO.get_option()

        if option == "1":
            # shows current data
            IO.show_current_data(lstOfProductObjects)
            continue

        elif option == "2":
            # adds data after going through Product class
            lstOfProductObjects.append(IO.add_product_data())

        elif option == "3":
            # saves data to file
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)

        elif option == "4":
            # ends
            break
except Exception as e:
    # prints error message
    print(e)
    print("Error in file. Check for mistake")

# Test ------------------------------------- #
# item_1 = Product(product_name = "Egg Nog", product_price=5.5)
# save_data_to_file(strFileName, )
# print(item_1)
# FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
