# Claire Leblanc
# Movie List
# Program Description - User is able to add in the list, remove from the list, view the list, have a summary of the list
#                     - User is now able to access Shortest to Longest, Longest to Shortest, A - Z, Z - A
#                     - User is not able to add actors and assign them to a movie also remove them

# All the functions for Movie Add a movie, Remove a movie, View movie(s), A - Z movies, Z - A movies, Shortest to longest movie titles, Long to short movie titles, movie summary
#-------------------------------- VIEW MOVIE LIST --------------------------------
def viewList(movieList, movieYear):
    i = 0
    count = 1
    # will validate that there is something in the list to display
    print("This is the current list")
    while i < len(movieList):
        print(count, ":" ,movieList[i],"(" + movieYear[i] +")")
        count += 1
        i += 1
#-------------------------------- ADD MOVIE --------------------------------
def addingList(movieList, movieYear):
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
##-------------------------------- REMOVE MOVIE --------------------------------
def removingList(movieList, movieYear,actorList):
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
    if userRemove < len(movieList) + 1 and userRemove != 0:
        # If the actor is in the movie it will remove the title out of the list
        titleRemoveList = movieList[userRemove - 1] + " (" + movieYear[userRemove - 1] + ")"
        for v in actorList.values():
            if titleRemoveList in v:
                v.remove(titleRemoveList)
        #print(actorList)
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
#-------------------------------- SUMMARY MOVIE --------------------------------
def movieSummary(movieList, movieYear):
    print("------ Summary menu screen ------")
    # This goes through the functions to get the results
    return totalNumber(movieList, movieYear),"\n", longestList(movieList, movieYear), "\n", shortestList(movieList, movieYear), "\n", oldestYear(movieList, movieYear), "\n", newestYear(movieList, movieYear)
#-------------------------------- TOTAL MOVIE IN LIST --------------------------------
def totalNumber(movieList, movieYear):
    print("You have", len(movieList), "movies in the list")
#-------------------------------- LONGEST MOVIE TITLE --------------------------------
def longestList(movieList, movieYear):
    # Max for the length 
    longest = max(movieList, key=len)
    longestIndex = movieList.index(longest)
    print("Longest title movie is:", longest , movieYear[longestIndex])
#-------------------------------- SHORTEST MOVIE TITLE --------------------------------
def shortestList(movieList, movieYear):
    # Min for the length
    shortest = min(movieList, key=len)
    shortestIndex = movieList.index(shortest)
    print("Shortest title movie is:", shortest, movieYear[shortestIndex])
#-------------------------------- OLDEST MOVIE YEAR --------------------------------
def oldestYear(movieList, movieYear):
    # Oldest year
    oldest = min(movieYear)
    oldestTitle = movieYear.index(oldest)
    print("Oldest movie year:", oldest, movieList[oldestTitle])
#-------------------------------- OLDEST MOVIE YEAR --------------------------------
def newestYear(movieList, movieYear):
    # Newest year
    newest = max(movieYear)
    newestTitle = movieYear.index(newest)
    print("Newest movie year:", newest, movieList[newestTitle])
#------------------------------- MOVIE LIST AND YEAR ------------------------------------
def listYear(movieList, movieYear, newList):
    newList = list()
    j = 0
    while j < len(movieList):
        titleYear = movieList[j] + " (" + movieYear[j] + ")"
        newList.append(titleYear)
        j += 1
    return newList
#-------------------------------- DISPLAY MOVIE --------------------------------
def displayList(movieList, movieYear, newList):
    i = 0
    count = 1
    while i < len(movieList):
        print(count,":", newList[i])
        count += 1
        i += 1
#-------------------------------- SHORTEST TO LONGEST - MOVIE --------------------------------
def shortToLong(movieList, movieYear, newList):
    newList = list(sorted(movieList, key=len))
    #--- Getting the proper year
    newList = list(sorted(listYear(movieList, movieYear, newList), key=len))
    print("------ Shortest to Longest ------")
    displayList(movieList, movieYear, newList)
#-------------------------------- LONGEST TO SHORTEST - MOVIE --------------------------------
def longToShort(movieList, movieYear, newList):
    newList = list(sorted(listYear(movieList, movieYear, newList), key=len, reverse=True))
    print("------ Longest to Shortest ------")
    displayList(movieList, movieYear, newList)
#-------------------------------- A - Z List - MOVIE --------------------------------
def azView(movieList, movieYear, newList):
    # Creating a temporary list with the current list sorted
    newList = list(sorted(listYear(movieList, movieYear, newList), key=lambda v: (v.upper(), v[0].islower())))
    print("------ A - Z ------")
    displayList(movieList, movieYear, newList)
#-------------------------------- Z - A List - MOVIE --------------------------------
def zaView(movieList, movieYear, newList):
    # Temporary list that has the current list
    newList = list(sorted(listYear(movieList, movieYear, newList), reverse=True, key=lambda v: (v.upper(), v[0].islower())))
    print("------ Z - A ------")
    displayList(movieList, movieYear, newList)
# All the functions for Actor that is used - Add an actor, Remove an actor, Remove a movie from the actor, Link actor to movie, View actor(s), View actor(s) in movie
#-------------------------------- VIEW ACTOR LIST --------------------------------
def viewActorList(actorName, actorList):
    j = 0
    empty = True
    while j < len(actorName):
        if actorName[j] in actorList:
            temp = actorName[j]
            print(j + 1, ":", actorName[j], ', '.join(actorList[temp]))
            empty = False
        else:
            print(j + 1, ":", actorName[j])
            empty = False 
        j += 1  
    if empty == True:
        print("------ NO ACTOR IN LIST ------")
#-------------------------------- ADD ACTOR --------------------------------
def addActor(actorName, actorList):
    viewActorList(actorName, actorList)
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
    # If the actor is already in the actor list name it will print duplicate
    if actorFullName in actorName:
        print("Duplicate name entry")
    else:
        #print("Single")
        actorName.append(actorFullName)
    #actorName.append(actorFullName)
    viewActorList(actorName, actorList)
#-------------------------------- LINK ACTOR --------------------------------
def linkActorMovie(movieList, movieYear, actorList, actorName):
    if len(actorName) > 0:
        viewActorList(actorName, actorList)
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
            movieLocation = movieList[i] + " (" + movieYear[i] + ")"
            print(i + 1, ":", movieLocation)
            i += 1
        userMovie = 0
        # This is to assign the actor in the movie they were in
        while userMovie < len(movieList):
            userMovie = input("Which movie were they in: ")
            userMovie = int(userMovie)
            if userMovie < len(movieList) + 1 and userMovie > 0:
                movieLocation = movieList[userMovie - 1] + " (" + movieYear[userMovie -1] + ")"
                # Even if the actor is in multiple movies as long the name is correct it will go to it's assigned actor
                j = 0
                exist = False
                #print(type(movieLocation), type(isinstance(actorList.values(), str)))
                for key, value in actorList.items():
                     test1 = ''.join(value)
                     if actorFullName in key:
                        if test1 == movieLocation:
                            exist = True
                # If the actor isn't already link it will link it         
                if exist == False:
                    actorList.setdefault(actorFullName, []).append(movieLocation)
                else:
                    print("They are already in the movie")
                if userMovie < len(movieList):
                    break
            else:
                print("Keep in range")
        viewActorList(actorName, actorList)
    else:   
        print("You have no actor in the list to link with")
#-------------------------------- REMOVE MOVIE FROM ACTOR --------------------------------
def removeMoviefromActor(actorName, actorList):
    if len(actorList) > 0:
        actorKeyList = list(actorList.keys())
        actorSpacingKey = ','.join(actorKeyList)
        actorKey = actorSpacingKey.split(',')
        j = 0
        for temp in actorKey:
            print(j + 1, temp)
            j += 1
        userSelection = input("Which actor would you like to remove from?")
        k = 0
        nameOfActor = ""
        for temp in actorKey:
            #print(temp)
            if int(userSelection) == k + 1:
                nameOfActor = temp
            k += 1
        tempMovieList = list(actorList.get(nameOfActor))
        i = 0
        movieListStrip = ','.join(str(e) for e in tempMovieList)
        movieListTemp = movieListStrip.split(',')
        #print(movieListTemp)
        j = 0
        for temp in movieListTemp:
            print(j + 1, temp.strip("['']"))
            j += 1
        userMovieSelection = input("Which movie would you like to remove?")
        l = 0
        for temp in movieListTemp:
            if int(userMovieSelection) == l +1:
                newMovie = temp
            l += 1
        actorList[nameOfActor].remove(newMovie)
        if len(actorList[nameOfActor]) == 0:
            actorList.pop(nameOfActor)
        viewActorList(actorName, actorList)
    else:
        print("You have no actor in the list link with a movie")    
#-------------------------------- REMOVE ACTOR --------------------------------
def removeActor(actorName, actorList):
    if len(actorName) > 0:
        inList = False
        if len(actorName) > 0:
            i = 0
            viewActorList(actorName, actorList)
            while inList == False:
                actorRemove = input("Who do you want to remove: ")
                actorRemove = int(actorRemove)
                # If the actor is within the list it will remove it as well what is link to this Actor
                if actorRemove - 1 < len(actorName) and actorRemove > 0:
                    actor = actorName[actorRemove - 1]
                    del actorName[actorRemove - 1]
                    if actor in actorList:
                        actorList.pop(actor)
                    break
                else:
                    print("Not in range")
        else:
            # Displays the list is empty
            print("You have no actor in the list to remove")
        viewActorList(actorName, actorList)
    else:
        print("You have no actor in the list to link with")
#-------------------------------- VIEW ACTORS IN MOVIE --------------------------------
def viewMovieActor(movieList, actorName, actorList, movieYear):
    if len(actorList) > 0: 
        i = 0
        while i < len(movieList):
            print( i + 1,":", movieList[i])
            i += 1
        userChoice = input("Choose a movie you want to view the actor(s) ")
        # Making sure that the movie selected is the correct one
        #print(movieList[int(userChoice) - 1])
        test1 = movieList[int(userChoice) - 1] + " (" + movieYear[int(userChoice) - 1] +")"
        i = 1
        for key, value in actorList.items():
            if test1 in value:
                print(i, ":", key)
                i += 1
            else:
                print("There are no actor in that movie")
    else:
        print("Try adding actor(s) and linking them to a movie")
#----------------------------- MAIN --------------------------------
def main():
    # These are the list that will be in use
    movieList = list(["Game Night", "The Great Mouse Detective", "Coco"])
    movieYear = list(["2018", "1986", "2017"])
    newList = list()
    actorList = {}
    actorName = list()
    validChoices = True
    while validChoices:
        try:
            # Input the menu list for the option
            userOption = input("What would you like to do?\n\t1 - Add a movie\n\t2 - Add an actor\n\t3 - Remove a movie\n\t"
                                "4 - Remove an actor\n\t5 - Remove a movie from the actor\n\t6 - Link actor to movie\n\t7 - View movie(s)\n\t8 - View actor(s)\n\t9 - View actor(s) in movie\n\t"
                                "10 - A - Z movies\n\t11 - Z - A movies\n\t12 - Short to long movie titles\n\t13 - Long to short movie titles\n\t14 - Movie Summary\n")
            userOption = int(userOption)
            if userOption > 0 and userOption < 15:
                # If the movie length is greater than 0 it will go through the statement if not you don't have a movie list
                if len(movieList) > 0 or userOption == 1:
                    if userOption == 1:
                        addingList(movieList, movieYear)
                    elif userOption == 2:
                        addActor(actorName, actorList)
                    elif userOption == 3:
                        removingList(movieList, movieYear,actorList)
                    elif userOption == 4:
                        removeActor(actorName, actorList)
                    elif userOption == 5:
                        removeMoviefromActor(actorName, actorList)
                    elif userOption == 6:
                        linkActorMovie(movieList, movieYear, actorList, actorName)   
                    elif userOption == 7:
                        viewList(movieList, movieYear)
                    elif userOption == 8:
                        viewActorList(actorName, actorList)
                    elif userOption == 9:
                        viewMovieActor(movieList, actorName, actorList, movieYear)
                    elif userOption == 10:
                        azView(movieList, movieYear, newList)            
                    elif userOption == 11:
                        zaView(movieList, movieYear, newList)
                    elif userOption == 12:
                        shortToLong(movieList, movieYear, newList)
                    elif userOption == 13:
                        longToShort(movieList, movieYear, newList)
                    elif userOption == 14:
                        movieSummary(movieList, movieYear)
                else:
                    print("------ Empty List ------")
            else:
                print("Not within the valid range 1 - 15")
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
        except SyntaxError:
            print("Invalid Entry")
        except ValueError:
            print("Invalid Entry")
main()