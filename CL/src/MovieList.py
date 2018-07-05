# Claire Leblanc
# Movie List
# Program Description - User is able to add in the list, remove from the list, view the list, have a summary of the list
#                     - User is now able to access Shortest to Longest, Longest to Shortest, A - Z, Z - A
#                     - User is not able to add actors and assign them to a movie also remove them 


movieList = list(["Game Night", "The Great Mouse Detective", "Coco"])
movieYear = list(["2018", "1986", "2017"])
newList = list()
actorList = {}
actorName = list()

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
    if len(movieList) > 0:
        print("------ Movie List ------")
    else:
        print("------ Empty List ------")
    while j < len(movieList):
        print(count, ":",movieList[j], movieYear[j])
        count += 1
        j += 1
    userAdd = ""
    userValid = True
    # As long the user doesn't put blanks at the begining of the title it will go through
    while len(userAdd) < 1:
        userAdd1 = input("Please enter the title of the movie you wish to add\n")
        # THIS IS TO REMOVE ANY LEADING WHITE SPACE
        userAdd = str(userAdd1.strip(' '))
        #userAdd = str(userAdd1)
    validYearAdd = True
    # Verification of the user input of year
    while validYearAdd:
        userYear = input("Please enter the year of the movie\n")
        newYear = int(userYear)
        # First motion picture movie was created in 1888 and 9999
        if newYear >= 1888 and newYear <= 9999:
            validYearAdd = False       
    i = 0 
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
    newList = list(sorted(listYear(), key=lambda v: (v.upper(), v[0].islower())))
    print("------ A - Z ------")
    displayList()
#-------------------------------- Z - A List --------------------------------
def zaView():
    # Temporary list that has the current list
    global newList
    newList = list(sorted(listYear(), reverse=True, key=lambda v: (v.upper(), v[0].islower())))
    print("------ Z - A ------")
    displayList()
#------------ View actor
def viewActorList():
    j = 0    
    while j < len(actorName):
        if actorName[j] in actorList:
            temp = actorName[j]
            print(j + 1, "-", actorName[j], ', '.join(actorList[temp]))
        else:
            print(j + 1, "-", actorName[j])
        #print(j + 1, "-", actorName[j])
        j += 1
#-------------------------------- ADD ACTOR --------------------------------
def addActor():
    viewActorList()
    while True:
        # As long the actor has a correct first and last name that's alpha it will go pass
        actorFirstName = input("Actor first name: ")
        if actorFirstName.isalpha():
            break
    while True:
        actorLastName = input("Actor last name: ")    
        if actorLastName.isalpha():
            break
    actorFullName = actorFirstName + " " + actorLastName
    actorName.append(actorFullName)
    viewActorList()
#-------------------------------- LINK ACTOR --------------------------------
def linkActor():
    if len(actorName) > 0:
        viewActorList()
        validChoice = True
        # Once the user selects a valid choice of actor they will proceed if not they will be stuck in the loop 
        while validChoice:
            userSelection = input("Which actor do you want to link: ")
            userSelection = int(userSelection)
            if userSelection < len(actorName) + 1 and userSelection != 0:
                validChoice = False
    
        actorFullName = actorName[userSelection - 1]
        i = 0
        while i < len(movieList):
            print(i + 1, "-", movieList[i])
            i += 1
        userMovie = 0

        while userMovie < len(movieList):
            userMovie = input("Which movie were they in: ")
            userMovie = int(userMovie)
            if userMovie < len(movieList) + 1 and userMovie > 0:
                movieLocation = movieList[userMovie - 1] + " (" + movieYear[userMovie -1] + ")"
                # Even if the actor is in multiple movies as long the name is correct it will go to it's assigned actor
                j = 0
                exist = False

                if actorFullName not in actorList:
                    #print("Hello")
                    actorList.setdefault(actorFullName, []).append(movieLocation)
                else:
                    print("Actor is already in this movie")
                if userMovie < len(movieList):
                    break
            else:
                print("Keep in range")
        viewActorList()
    else:
        print("You have no actor in the list to link with")    
#-------------------------------- REMOVE ACTOR --------------------------------
def remActor():
    inList = False
    if len(actorList) >= 0:
        i = 0
        viewActorList()
        while inList == False:
            actorRemove = input("Who do you want to remove: ")
            actorRemove = int(actorRemove)
            # If the actor is within the list it will remove it as welle in the list for link 
            actor = actorName[actorRemove - 1]
            if actorRemove - 1 < len(actorName):
                del actorName[actorRemove - 1]
                if actor in actorList:
                    actorList.pop(actor)
                break
    else:
        # Displays the list is empty
        print("You have no actor in the list to remove")
    viewActorList()
#----------------------------- MAIN --------------------------------
def main():
    validChoices = True
    while validChoices:
        try:
            userOption = input("What would you like to do?\n\t1 - View list of movie\n\t2 - Add a movie\n\t3 - Remove a movie\n\t4 - Summary\n\t5 - Short to Long\n"
                                "\t6 - Long to Short\n\t7 - A - Z\n\t8 - Z - A\n\t9 - Add Actor\n\t10 - Remove Actor\n\t11 - Link Actor\n")
            if userOption > "0" and userOption <= "9" or userOption == "10" or userOption == "11":
                # if the length of the list is more than 0 or 2 it will go to it's proper function if not it will print the else statement
                if len(movieList) > 0 or userOption == "2":
                        {"1":viewList,"2":addingList,"3":removingList,"4":movieSummary,"5":shortToLong,"6":longToShort,"7":azView,"8":zaView,"9":addActor,"10":remActor,"11":linkActor}[userOption]()
                else:
                    print("------ Empty List ------")
            else:
                raise Exception
            # Loop to go through the yes or no continue part
            while validChoices:
                userContinue = input("Do you wish to continue? Y - N :")
                if userContinue.upper() == "Y":
                    validChoices = True
                    break
                elif userContinue.upper() == "N":
                    validChoices = False
                else:
                    print("Please use Y or N")
        # If there's anything that throws off the code it will go to the exception
        except Exception:
            print("Invalid Entry")
main()