#Author: Shanielle Haynes
#Date Created: December 8, 2023
#Course: ITT103
#Purpose: The provided Python code creates a simple reservation system for different travel classes (First, Business, Economy) with
#seat availability displayed in a menu. Users can reserve seats, and the program runs until the user chooses to quit, providing a user-friendly interface for seat selection.


def quit():
    print("You have chosen to quit")
    print("Thank you for choosing UCC Signature Express Limited!")


def business_class():
    row, column, seats = reserve_seat(class_seats['B']) #reserve_seat is called to indicate which row and column was chosen by the user
    print("You have chosen Business class, as your reservation type \n")


def first_class():
    row, column, seats = reserve_seat(class_seats['F']) #'F' is used to access the number of seats in the First class from the dictionary
    print("You have chosen First class, as your reservation type \n")


def economy_class():
    row, column, seats = reserve_seat(class_seats['E'])
    print("You have chosen Economy class, as your reservation type \n")


def reserve_seat(total_seats): #user input to take their prefered row and column
    global seats# The global seats statement indicates that the variable seats is a global variable, that can be used outside this function.
    row = int(input("Please enter your desired row number: "))
    column = int(input("Please enter your desired column number: "))

    if row <= 0: #this section of code is to validate whether the number users put in are positive
        print("Catching Errors: Number must be positive or greater than zero!")
        return reserve_seat(total_seats) #if the row number is positive then row and column will print. if not then error statement will print then



    print(f"Reserving seat: row {row} and column {column}")
    print("You have reserved 1 seat")

    return row, column, 1 #this line of code is apart of the reserve_seat function and it will return the three values of row, column and 1


def show_seats(total_seats): # seats: This is a parameter representing the total number of seats in a class.
    for i in range(total_seats): # The outer loop (for i in range(seats)) iterates over each row.
        for j in range(4): # The inner loop (for j in range(4)) iterates over each column in a row.
            print(f"row {i + 1}, column {j + 1}", end='\t')
        print() #Prints a newline after each row


# Initialize seats
class_seats = {'F': 27, 'B': 38, 'E': 56} #this is a dictionary that maps the class options to the number of seats in each class


while True: #a while true loop was used to ensure that the menu is displayed repeatedly until the user chooses to quit.
    print("Welcome to UCC Signature Express Limited, The Best for traveling over the island\n" #the menu that will be displayed to users
          "Please select your option:\n"
          "1. First class (F/f)\n"
          "2. Business class (B/b)\n"
          "3. Economy class (E/e)\n"
          "4. Quit (Q/q)\n")

    option = input()  #users will input their option in this box

#The If statements below are to go to the function that was entered by the user
    if option == 'F' or option == 'f':
        first_class()

    elif option == 'b' or option == 'B':
        business_class()

    elif option == 'E' or option == 'e':
        economy_class()

    elif option == 'Q' or option == 'q':
        quit()
        break  # break is use to exit the loop if the user enter 'q' or 'Q'

    else:
        print("Invalid choice! Please try again.")#this is an error statement that will print if the user has entered anything other than what was in the menu

