#Name: Potter Nerdling
# Date: 06/19/2018
#Movie Data Base

def DisplayList(MovieList):
    i = 0
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection:")
        while i < len(MovieList): # loop to display each movie in the list
            print(" ", MovieNum, " ", MovieList[i])
            i += 1 # indexes through the list
            MovieNum += 1 # numbers the movies
    else:
        print(" ........No Movies in Data Base.......")
def AddtoList(MovieList):
     Year = 0
     
     while len(str(Year)) != 4 or Year < 1895 and Exception != True: # checks the length of the year and there is no exception. 
        try:
            Year = int(input(" Enter in the year of the Movie Title:"))
            if len(str(Year)) != 4:
                print(" Invalid Entry, please try again!")
            elif Year < 1895:
                 print(" Invalid Entry, please try again!")
        except Exception:
            print(" Invalid Entry, please try again!")

     MovieTitle = str(input(" Enter the Movie Title: "))
     MovieEntry = (str(Year) +": "+ MovieTitle)
     if MovieEntry in MovieList:
        print(".....Movie already added to List....")
     else:
        MovieList.append(MovieEntry)
        print(" .............Movie Added...............")
def RemoveFrList(MovieList):
     if len(MovieList) <= 0:
            print(" .......No Movies in the Database......")
     elif len(MovieList) > 0:
            DisplayList(MovieList)
            try:
                if len(MovieList) > 0:
                    removeTitle = int(input(" Enter the number for the title you would like to have removed: "))
                    MovieList.remove(MovieList[removeTitle - 1]) # taking away from the list
                else:
                    pass
            except Exception:
                print(" Invalid Entry, please try again!")
def OldtoNew(MovieList):
    MovieList.sort()
    i = 0
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Here is the list of Movies Oldest to Newest:")
        DisplayList(MovieList) # Function Call
    else:
        print(" .......No Movies in the Database......")

def ShorttoLong(MovieList):
    MovieList.sort(key = len) # sorts list based on length
    i = 0
    MovieNum = 1
    length = len(MovieList)
    if length > 0:
        print(" Here is the list of Movies in your collection Shortest to Longest: ")
        DisplayList(MovieList)
    elif length == 0:
        print(" .......No Movies in the Database......")
def LongtoShort(MovieList):
    MovieList.sort(key = len, reverse = True) # sorts list based on length then reverses list
    i = 0
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection Longest to Shortest: ")
        DisplayList(MovieList)
    else:
        print(" .......No Movies in the Database......")
def AtoZ(MovieList):
    i = 0
    j = 1
    MovieNum = 1
    AtoZList = list() # Creates new list for sorting

    print(" Here is the list of Movies in your collection from A to Z: ")
    while i < len(MovieList): # loop to display each movie in the list
        AtoZList.append(MovieList[i][6:])
        i += 1
    AtoZList = sorted(AtoZList) # sorts the list
    for i in AtoZList:
        print(j,"",i)
        j += 1
def ZtoA(MovieList):
    i = 0
    j = 1
    MovieNum = 1
    AtoZList = list() # Creates new list for sorting

    print(" Here is the list of Movies in your collection from Z to A: ")

    while i < len(MovieList): # loop to display each movie in the list
        AtoZList.append(MovieList[i][6:])
        i += 1
    AtoZList = sorted(AtoZList, reverse = True) # sorts the list ensure is is reversed
    for i in AtoZList:
         print(j,"",i)
         j += 1
             
MovieList = list() #(["1951: Alice in Wonderland", "1988: Beetlejuice","1994: Ace Ventura: Pet Detective"])
Quit = False

while Quit == False:
    print(" Here are some Movie Data Base choices: ") # Displays choices that can modify the list for Movies
    print("     1) Add a Movie")
    print("     2) Remove a Movie")
    print("     3) Display Movie List")
    print("     4) Display Movie List Stats")
    print("     5) Display Movie List Shortest to Longest")
    print("     6) Display Movie List Longest to Shortest")
    print("     7) Display Movie List A to Z")
    print("     8) Display Movie List Z to A")
    print("     9) Or you can Quit! ")

    choice = str(input("    Enter your choice:")) # takes the users input
    print("")
    if choice == "1": 
        AddtoList(MovieList)
        DisplayList(MovieList)
    elif choice == "2":
        RemoveFrList(MovieList) 
        if len(MovieList) > 0: 
            DisplayList(MovieList) 
    elif choice == "3":
        DisplayList(MovieList)
    elif choice == "4":
        if len(MovieList) <= 0: # insures if there is movies in the DB the stats will be displayed, if not no stats will be displayed. 
            print(" ......No movie stats to display.....")
        else:
            print(" Movie Data Base Stats:")
            print(" Total amount of Movies in List: ", len(MovieList))
            print(" The longest Title is as follows:",max(MovieList, key=len))
            print(" The shortest Title is as Follows:", min(MovieList, key=len))
            OldtoNew(MovieList)
    elif choice == "5":
        ShorttoLong(MovieList) #Function Call
    elif choice == "6":
        LongtoShort(MovieList) #Function Call
    elif choice == "7":
        AtoZ(MovieList) #Function Call
    elif choice == "8":
        ZtoA(MovieList)   
    elif choice == "9":
        Quit = True
    else:
        print("Invalid Option, plese try again!") # if no valid option is chosen the user will be advised. 
        print("")