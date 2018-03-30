"""
Project name: Formula Calculator

Desciption  : A task assignment by SIT for Robu Python Developer position, The App takes a string of numbers based on the number of literation the user wants to loop over calculates the numbers and returns the output as a string

Author      : Thamudi
Name        : Tamim Hamoudi
Git Repo    : https://github.com/thamudi/formula_calculator.git

"""
class Formula:

    """ A global variable that holds the input string """

    string_list = []
    nested_list = []
    return_list  = []

    def __init__(self):

        """
        constructor
        Does nothing
        """
        pass


    def _validate_input(self, nested_list):

        """ Validation function for the splited string to check if the list values are according to critira """

        if ( len(nested_list[0]) != 3 ) or (len(nested_list[1]) != 3 ) or (len(nested_list[2]) != 3 )  :
            raise IndexError
        else:
            for x in range(len(nested_list)):
                for y in range(len(nested_list[x])):
                    if isinstance(nested_list[x][y],float) or isinstance(float(nested_list[x][y]),float):
                        pass
                    else:
                        raise ValueError

    def _split(self,data_string,nested_list):

        """ Split function that returns the passed string as a list """
        nested_list.append(data_string.split(','))

    def _calculate_formula_one(self,nested_list):
        count = 0
        for x in range(len(nested_list)):
            calculated_data = float(nested_list[0][count])*( float(nested_list[1][count]) + float(nested_list[2][count]) ) - float(nested_list[0][count])/2
            count += 1
            return_list.append(str(calculated_data))

    def input_function(self):

        global string_list
        string_list = []
        list_length = ['x','y','z']
        for x in list_length:
            input_value = input("list: "+x+" | Please enter your three numbers separated by a ',': ")
            string_list.append(input_value)

    def error_handeler(self):
        global return_list
        global nested_list
        nested_list  = []
        return_list   = []

        try:
            """ split the string """
            for x in range(len(string_list)):
                self._split(string_list[x],nested_list)
            try:
                """" Validate the input data """
                self._validate_input(nested_list)
            except ValueError:
                return print("ERROR: The values that were entered does not match the critira of being numeric or not empty ")
            except IndexError:
                return print("ERROR: The values entered was out of range ")
            else:
                self._calculate_formula_one(nested_list)
        except NameError:
            return print("ERROR: Please enter your values before calculating them")
        else:
            print(','.join(return_list))



"""
End Formula Class
"""

def display_menu():

    """
    Display Menu Options Content
    """

    print('1. Input the values')
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
