# Claire Leblanc
# Movie List

movieList = list(['Coco', 'Justice League', 'Great mouse detective'])
#-------------------------------- VIEW LIST --------------------------------
def viewList():
    i = 0
    # will validate that there is something in the list to display
    if len(movieList) > 0:
        print("This is the current list")
        while i < len(movieList):
            print(movieList[i], end=", ")
            i += 1
        print()
    else:
        print("Empty list")

#-------------------------------- ADD LIST --------------------------------
def addingList():
    userAdd = input("Please enter the title of the movie you wish to add\n")
    i = 0
    nonDuplicate = True
    # This loop will go through the list and puts it all upper case to verify that the user input is not a double
    while i < len(movieList):
        #Able to cycle through the index
        newList = list(movieList)
        if userAdd.upper() in newList[i].upper():
            nonDuplicate = False
        i += 1
    # If the previous loop passes as a true it will add it in the list
    if nonDuplicate == True:
        print("Movie was added")
        movieList.append(userAdd)
    else:
        print("Movie is a duplicate")

#-------------------------------- REMOVE LIST --------------------------------
def removingList():
    userRemove = input("Please enter the title of the movie you wish to remove\n")
    i = 0
    nonDuplicate = False
    test1 = ""
    while i < len(movieList):
        #Able to cycle through the index
        newList = list(movieList)
        # This will remove the title that is in the list
        if userRemove.upper() == newList[i].upper():
            nonDuplicate = True
            removedWord = newList[i]
            movieList.remove(removedWord)
            print("Title was removed")
        i += 1
    if nonDuplicate == False:
        raise ex1

def main():
    validChoices = True
    while validChoices:
        try:
            userOption = input("What would you like to do?\n\t1 - View list of movie\n\t2 - Add a movie\n\t3 - Remove a movie\n")
            userOption = int(userOption)
            if userOption > 0 and userOption < 4:
                # Prints the current list
                if userOption == 1:
                    viewList()
                elif userOption == 2:
                    addingList()
                elif userOption == 3:
                    removingList()
            else:
                raise Exception
            # Loop to go through the yes or no continue part
            while validChoices:
                userContinue = input("Do you wish to continue? Y - N :")
                if userContinue.upper() == "Y" or userContinue.upper() == "YES":
                    validChoices = True
                    break
                elif userContinue.upper() == "N" or userContinue.upper() == "NO":
                    validChoices = False
                else:
                    print("Please use Y or N")
        except Exception:
            print("Invalid entry")
main()