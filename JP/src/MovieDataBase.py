# Name: Potter Nerdling
# Date: 06/14/18
# Project: Modifiable List of Movies

def DisplayList(MovieList):
    i = 0
    MovieNum = 1

    print(" Here is the list of Movies in your collection: ")

    while i < len(MovieList): # loop to display each movie in the list
        print(" ", MovieNum, " ", MovieList[i])
        i += 1 # indexes through the list
        MovieNum += 1 # numbers the movies

def DisplayAtoZ(MovieList): # function to sort list from A-Z
    MovieList.sort()
    i = 0
    MovieNum = 1

    print(" Here is the list of Movies in your collection: ")

    while i < len(MovieList): # loop to display each movie in the list
        print(" ", MovieNum, " ", MovieList[i])
        i += 1 # indexes through the list
        MovieNum += 1 # numbers the movies

def DisplayZtoA(MovieList): #Display Alphabetical order in reverse
    MovieList.sort()
    MovieList.reverse()
    
    i = 0
    MovieNum = 1

    print(" Here is the list of Movies in your collection: ")

    while i < len(MovieList): # loop to display each movie in the list
        print(" ", MovieNum, " ", MovieList[i])
        i += 1 # indexes through the list
        MovieNum += 1 # numbers the movies

#####################################################################################################################
MovieList =(["Alice in Wonderland", "Beetlejuice", "Ace Ventura: Pet Detective"])
Valid = False
PrintOC = False
#DisplayList(MovieList)
print("                     MOvIeS")
print("")
# Confirms if they would like to modify the list
while Valid == False:

    Modify = str(input(" Would you like to Modify your list? Y = Yes, N = No: ")) # asking user if they would like to modify the list
    print("")
   
    if Modify.upper() == "Y": # If user would like to modify the program
        print("   How would you like to Modify the list: ") 
        print("")
        print(" A) Add to the List.  B) Take away from the List.") # option to modify list
        print("")
        choice = str(input(" Please enter your choice: ")) # asking for the choice
        if choice.upper() == "A":
            addTitle = input(" Please enter the Title you would like to add: ")
            MovieList.append(str(addTitle)) # adding to the list
            DisplayList(MovieList) # function call
            Valid = True
            
        elif choice.upper() == "B":
            DisplayList(MovieList) # function call

            removeTitle = int(input(" Enter the number for the title you would like to have removed: "))
            MovieList.remove(MovieList[removeTitle - 1]) # taking away from the list
            DisplayList(MovieList) # function call
            Valid = True
    elif Modify.upper() == "N":
        Valid = True
        Display = str(input(" Would you like to display the list of Movies in your Collection? Y = Yes, N = No: ")) # if user does not wish to modify they have the chice to display the list
        while PrintOC == False: # loop for list display
            if Display.upper() == "Y":
                print(" Would you like to: ")
                print(" A) Sort A - Z ")
                print(" B) Sort Z - A")
                
                SChoice = str(input(" Please enter your choice:"))

                if SChoice.upper() == "A":
                    DisplayAtoZ(MovieList) # function call
                    PrintOC = True
                elif SChoice.upper() == "B":
                    DisplayZtoA(MovieList)
                    PrintOC = True

            if Display.upper() == "N":
                print(" .........Have a Red Carpet Day!........")
                PrintOC  = True
            else:
                print("..........Invalid Entry, please try again.......")
    else:
        print(".....Invalid Entry, please try again.....")
        Valid == False






