# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Erik Duong>,<11/20/2024>,<Assignment 06>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Processing --------------------------------------- #
class FileProcessor:
    """
     A collection of processing layer functions that work with json files

     ChangeLog: (Who, When, What)
    """

    def read_data_from_file(file_name:str, student_data:list):
        """This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        :return: list
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    def write_data_to_file(file_name: str, student_data: list):
        """This function writes data from a json file and loads it into a list of dictionary rows

               ChangeLog: (Who, When, What)
               """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_name(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file. "
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    """

    @staticmethod
    def output_error_messages(message: str, error = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_name(student_data: list):
        print("-" * 50)
        if student_data:
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                    f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        else:
            print('No student data available')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ").strip()
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message=e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
        return str


    # When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(students)
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_name(students)
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
    # Stop the loop
    elif menu_choice == "4":
        print("Exiting the program. Goodbye!")
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

