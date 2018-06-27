# Claire Leblanc
# Movie List
# Program Description - User is able to View, Add, Remove from the list of movies.
#                     - User is able to retrieve a Summary - TotalNumber of movies, A - Z Sorting, Z - A Sorting

movieList = list(["Game Night", "The Great Mouse Detective", "Coco", "It"])
movieYear = list(["2018", "1986", "2017", "1960"])
global userOption

#---- CHECK IF LIST IS EMPTY
def listChecks():
    global userOption
    if len(movieList) > 0:
        {"1":viewList,"3":removingList,"4":movieSummary}[userOption]()
    else:
        print("You have an empty list. Try adding to it.")

#-------------------------------- VIEW LIST --------------------------------
def viewList():
    i = 0
    # will validate that there is something in the list to display
    print("This is the current list")
    while i < len(movieList):
        print(movieList[i],"(" + movieYear[i] +")", end=", ")
        i += 1
    print()

#-------------------------------- ADD LIST --------------------------------
def addingList():
    userAdd = ""
    while len(userAdd) < 1:
        userAdd = input("Please enter the title of the movie you wish to add\n")
        i = 0
        while len(userAdd) < i:
            if userAdd == " ":
                userAdd=""
    validYearAdd = True
    while validYearAdd:
        userYear = input("Please enter the year of the movie\n")
        newYear = int(userYear)
        # First motion picture movie was created in 1888
        if newYear >= 1888:
            validYearAdd = False
       
    i = 0 #20
    nonDuplicate = True
    # This loop will go through the list and puts it all upper case to verify that the user input is not a double
    while i < len(movieList):
        #Able to cycle through the index
        newList = list(movieList)
        if userAdd.upper() in newList[i].upper() and movieYear[i] == userYear:
            nonDuplicate = False
        i += 1
    # If the previous loop passes as a true it will add it in the list
    if nonDuplicate == True:
        print("Movie was added")
        movieList.append(userAdd)
        movieYear.append(userYear)
    else:
        print("Movie is a duplicate")

#-------------------------------- REMOVE LIST --------------------------------
def removingList():
    userRemove = input("Please enter the title of the movie you wish to remove\n")
    titleInList = False
    i = 0
    indexList = list()
    # While loop verifies that the title exist within the list
    while i < len(movieList):
        newList = list(movieList)
        if userRemove.upper() == newList[i].upper():
            titleInList = True
            indexList.append(i)
        i += 1
    yearInList = False
    # if statement that if the title does exist in the list it will continue to ask for the year
    j = 0
    if titleInList == True:
        userYearRemove = input("Please enter the year of the movie\n")
    while j < len(indexList):
        f = indexList[j]        
        if userYearRemove == movieYear[f]:
            del movieList[f]
            del movieYear[f]
            yearInList = True
            break
        j += 1
    # if both the title and year exist within the list they are removed 
    if titleInList == True and yearInList == True:
        print(userRemove, userYearRemove, "has been removed")
    else:
        print("This movie does not exist within the list")

#-------------------------------- SUMMARY LIST --------------------------------
def movieSummary():
    print("Summary menu screen")
    return totalNumber(),"\n", longestList(), "\n", shortestList()
#-------------------------------- TOTAL NUMBER IN LIST --------------------------------
def totalNumber():
    print("You have", len(movieList), "movies in the list")

#-------------------------------- LONGEST TITLE --------------------------------
def longestList():
    longest = max(movieList, key=len)
    longestIndex = movieList.index(longest)
    print("Longest title movie is", longest , movieYear[longestIndex])

#-------------------------------- SHORTEST TITLE --------------------------------
def shortestList():
    shortest = min(movieList, key=len)
    shortestIndex = movieList.index(shortest)
    print("Shortest title movie is", shortest, movieYear[shortestIndex])

def main():
    validChoices = True
    while validChoices:
        try:
            global userOption
            # userOption is a global for easy access in other function
            userOption = input("What would you like to do?\n\t1 - View list of movie\n\t2 - Add a movie\n\t3 - Remove a movie\n\t4 - Summary\n") #\tQ - Quit\n")
            if userOption > "0" and userOption < "5":
                {"1":listChecks,"2":addingList,"3":listChecks,"4":listChecks}[userOption]()
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
        except Exception:
            print("Invalid entry")
main() # lines