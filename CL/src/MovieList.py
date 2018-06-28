# Claire Leblanc
# Movie List
# Program Description - User is able to add in the list, remove from the list, view the list, have a summary of the list
#                     - User is now able to access Shortest to Longest, Longest to Shortest, A - Z, Z - A

movieList = list(["Game Night", "The Great Mouse Detective", "Coco"])
movieYear = list(["2018", "1986", "2017"])
newList = list()
global userOption

#---- CHECK IF LIST IS EMPTY
def listChecks():
    global userOption
    if len(movieList) > 0:
        {"1":viewList,"3":removingList,"4":movieSummary,"5":shortToLong,"6":longToShort,"7":azView,"8":zaView}[userOption]()
    else:
        print("------ Empty List ------")
#-------------------------------- VIEW LIST --------------------------------
def viewList():
    i = 0
    count = 1
    # will validate that there is something in the list to display
    print("This is the current list")
    while i < len(movieList):
        print(count, ":" ,movieList[i],"(" + movieYear[i] +")")
        count += 1
        i += 1
#-------------------------------- ADD LIST --------------------------------
def addingList():
    j = 0
    count = 1
    # Having the movie list display before it's executed
    print("------ Movie List ------")
    while j < len(movieList):
        print(count, ":",movieList[j], movieYear[j])
        count += 1
        j += 1
    userAdd = ""
    userValid = True
    # As long the user doesn't put blanks at the begining of the title it will go through
    while len(userAdd) < 1:
        userAdd = input("Please enter the title of the movie you wish to add\n")
        i = 0
        # Verification of the spaces in the string
        while len(userAdd) > i and userValid == True:
            if userAdd[0] == " " and userAdd[i] == " ":
                userAdd=""
            else:
                userValid = False
            i += 1
    validYearAdd = True
    # Verification of the user input of year
    while validYearAdd:
        userYear = input("Please enter the year of the movie\n")
        newYear = int(userYear)
        # First motion picture movie was created in 1888 and 9999
        if newYear >= 1888 and newYear <= 9999:
            validYearAdd = False       
    i = 0 #20
    nonDuplicate = True
    # This loop will go through the list and puts it all upper case to verify that the user input is not a double
    while i < len(movieList):
        # Able to cycle through the index
        newList = list(movieList)
        if userAdd.upper() in newList[i].upper() and movieYear[i] == userYear:
            nonDuplicate = False
        i += 1
    # If the previous loop passes as a true it will add it in the list
    if nonDuplicate == True:
        print("Movie was added")
        movieList.append(userAdd)
        movieYear.append(userYear)
        j = 0
        count = 1
        # Displaying final result of the new list
        print("------ Movie List ------")
        while j < len(movieList):
            print(count, ":",movieList[j], movieYear[j])
            count += 1
            j += 1
    # If the movie is a duplicate
    else:
        print("Movie is a duplicate")
##-------------------------------- REMOVE LIST --------------------------------
def removingList():
    j = 0
    count = 1
    # Having the list display before
    print("------ Movie List ------")
    while j < len(movieList):
        print(count, ":",movieList[j], movieYear[j])
        count += 1
        j += 1
    # Which number does the user which to remove
    userRemove = input("Which one do you want to remove\n")
    userRemove = int(userRemove)
    # If the number is between the lenght of the list it will go through
    if userRemove < len(movieList) + 1 and userRemove > 0 :
        del movieList[userRemove - 1]
        del movieYear[userRemove - 1]
        j = 0
        count = 1
        # Printing the new list
        if len(movieList) > 0:
            print("------ Movie List ------")
            while j < len(movieList):
                print(count, ":", movieList[j], movieYear[j])
                count += 1
                j += 1
        # Once the user removes everything it will display empty list
        else:
            print("------ Empty List ------")
    else:
        print("Not within the range of movies.")
#-------------------------------- SUMMARY LIST --------------------------------
def movieSummary():
    print("------ Summary menu screen ------")
    # This goes through the functions to get the results
    return totalNumber(),"\n", longestList(), "\n", shortestList(), "\n", oldestYear(), "\n", newestYear()
#-------------------------------- TOTAL NUMBER IN LIST --------------------------------
def totalNumber():
    print("You have", len(movieList), "movies in the list")
#-------------------------------- LONGEST TITLE --------------------------------
def longestList():
    # Max for the length 
    longest = max(movieList, key=len)
    longestIndex = movieList.index(longest)
    print("Longest title movie is:", longest , movieYear[longestIndex])
#-------------------------------- SHORTEST TITLE --------------------------------
def shortestList():
    # Min for the length
    shortest = min(movieList, key=len)
    shortestIndex = movieList.index(shortest)
    print("Shortest title movie is:", shortest, movieYear[shortestIndex])
#-------------------------------- OLDEST YEAR --------------------------------
def oldestYear():
    # Oldest year
    oldest = min(movieYear)
    oldestTitle = movieYear.index(oldest)
    print("Oldest movie year:", oldest, movieList[oldestTitle])
#-------------------------------- OLDEST YEAR --------------------------------
def newestYear():
    # Newest year
    newest = max(movieYear)
    newestTitle = movieYear.index(newest)
    print("Newest movie year:", newest, movieList[newestTitle])
#------------------------------- LIST AND YEAR ------------------------------------
def listYear():
    global newList
    newList = list()
    j = 0
    while j < len(movieList):
        titleYear = movieList[j] + " " + movieYear[j]
        newList.append(titleYear)
        j += 1
    return newList
#-------------------------------- DISPLAY THE LIST --------------------------------
def displayList():
    global newList
    i = 0
    count = 1
    while i < len(movieList):
        print(count,":", newList[i])
        count += 1
        i += 1
#-------------------------------- SHORTEST TO LONGEST --------------------------------
def shortToLong():
    global newList
    newList = list(sorted(movieList, key=len))
    #--- Getting the proper year
    newList = list(sorted(listYear(), key=len))
    print("------ Shortest to Longest ------")
    displayList()
#-------------------------------- LONGEST TO SHORTEST --------------------------------
def longToShort():
    global newList
    newList = list(sorted(listYear(), key=len, reverse=True))
    print("------ Longest to Shortest ------")
    displayList()
#-------------------------------- A - Z List --------------------------------
def azView():
    # Creating a temporary list with the current list sorted
    global newList
    newList = list(sorted(listYear()))
    print("------ A - Z ------")
    displayList()
#-------------------------------- Z - A List --------------------------------
def zaView():
    # Temporary list that has the current list
    global newList
    newList = list(sorted(listYear(), reverse=True))
    print("------ Z - A ------")
    displayList()
#----------------------------- MAIN --------------------------------
def main():
    validChoices = True
    while validChoices:
        try:
            global userOption
            # userOption is a global for easy access in other function
            userOption = input("What would you like to do?\n\t1 - View list of movie\n\t2 - Add a movie\n\t3 - Remove a movie\n\t4 - Summary\n\t5 - Short to Long\n"
                                "\t6 - Long to Short\n\t7 - A - Z\n\t8 - Z - A\n") #\tQ - Quit\n")
            if userOption > "0" and userOption < "9":
                {"1":listChecks,"2":addingList,"3":listChecks,"4":listChecks,"5":listChecks,"6":listChecks,"7":listChecks,"8":listChecks}[userOption]()
            #elif userOption.upper() == 'Q':
             #   break
            else:
                raise Exception
            # Loop to go through the yes or no continue part
            while validChoices:
                userContinue = input("Do you wish to continue? Y - N :")
                if userContinue.upper() == "Y":
                    validChoices = True
                    break
                elif userContinue.upper() == "N": #80
                    validChoices = False
                else:
                    print("Please use Y or N")
        # If there's anything that throws off the code it will go to the exception
        except Exception:
            print("Invalid Entry")
main() # lines