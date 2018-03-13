"""
Project name: Formula Calculator

Desciption  : A task assignment by SIT for Robu Python Developer position, The App takes a string of numbers based on the number of literation the user wants to loop over calculates the numbers and returns the output as a string

Author      : Thamudi
Name        : Tamim Hamoudi
Git Repo    : https://github.com/thamudi/formula_calculator.git

"""
class Formula:

    """ A global variable that holds the input string """
    data_string = ""
    parent_list = []
    total_list = []

    def __init__(self):

        """
        constructor
        Does nothing
        """
        pass


    def _validate_input(self, data_list):

        """ Validation function for the splited string to check if the list values are according to critira """
        if len(data_list) != 3:
            raise IndexError
        else:
            for x in data_list:
                if isinstance(x, float) or isinstance(float(x), float):
                    pass
                else:
                    raise ValueError

    def _split(self,data_string):

        """ Split function that returns the passed string as a list """

        return data_string.split(',')

    def _stringify_list(self, total_list):

        string_output = ""

        for x in range(len(total_list)):
            string_output += str(total_list[x])

            if  x == (len(total_list) - 1):
                pass
            else:
                string_output +=' , '

        print("Your calulated input = "+string_output)

    def _calculate_formula_one(self,data_list):

        calculated_data = float(data_list[0])*( float(data_list[1]) + float(data_list[2]) ) - float(data_list[0])/2
        total_list.append(str(calculated_data))

    def input_function(self):

        valid = False
        while not valid:
            try:
                input_literation = int(input('Enter the number of times you want to run the process: '))
                if input_literation > 0:
                    pass
                    valid = True
                else:
                    raise ValueError
            except ValueError:
                print("Please enter Natural Numbers larger than zero")
        else:

            i = 0
            global parent_list
            parent_list = []
            while i < input_literation:

                child_list= []

                input_value = input("Please enter your numbers separated by a , and no more than 3 values : ")

                child_list.append(input_value)
                parent_list.append(child_list)
                i+=1


    def error_handeler(self):
        global total_list
        total_list = []
        """ Calculation Formula for the data that was inputed by the user """
        try:
            """ split the string """
            for x in range(len(parent_list)):
                try:
                    data_list = self._split(parent_list[x][0])
                except NameError:
                    print("ERROR: Please enter your values before calculating them")
                else:
                    try:
                        """" Validate the input data """
                        self._validate_input(data_list)
                    except ValueError:
                        print("ERROR: The values that were entered does not match the critira of being numeric or not empty ")
                    except IndexError:
                        print("ERROR: The values entered was out of range ")
                    else:
                        self._calculate_formula_one(data_list)
        except NameError:
            print("ERROR: Please enter your values before calculating them")

        else:
            self._stringify_list(total_list)



"""
End Formula Class
"""

def display_menu():

    """
    Display Menu Options Content
    """

    print('1. Enter your number of literation')
    print('2. Calculate the input using Formula one')
    print('0. Exit program')
    print()
    print('Please select an option by entering a number from the above menu')

def get_menu_choice():

    """
    Validated the Use input for the menu option choices
    """
    option_valid = False

    while not option_valid:
        try:
            choice = int (input("Option Selected: "))
            if 0 <= choice <= 2:
                option_valid = True
            else:
                print("Please enter a valid Option")

        except ValueError:
            print("Please enter a valid Option")

    return choice


def manage_menu(self):

    """
    Welcome Menu for the program interface
    """

    print("Welcome to the Formula Calculation program")
    print()

    exit = False

    while not exit:

        print("##################")
        display_menu()
        print("##################")
        option = get_menu_choice()
        print()

        if option == 1:
             self.input_function()
             print()

        elif option == 2:
            self.error_handeler()
            print()

        elif option == 0:
            exit = True
            print()

    print('Thank you for using our Formula Calculation program')


def main():

    new_data = Formula()
    manage_menu(new_data)

""" Starts the program """

if __name__ == "__main__":

    main()
