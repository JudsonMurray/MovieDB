#Name: Potter Nerdling
# Date: 06/19/2018
#Movie Data Base

def DisplayList(MovieList):
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection:")
        for i in MovieList: # loop to display each movie in the list
            print(" ", MovieNum,")", " ", i)
            MovieNum += 1 # numbers the movies
    else:
        print(" ........No Movies in Data Base.......")
def AddtoList(MovieList):
     Year = 0
     i = 0
     DisplayList(MovieList)
     
     while len(str(Year)) != 4 or Year < 1895 and Exception != True: # checks the length of the year and there is no exception. 
        try:
            Year = int(input(" Enter in the year of the Movie Title:"))
            if len(str(Year)) != 4 or Year < 1895:
                print(" Invalid Entry, please try again!")
        except Exception:
            print(" Invalid Entry, please try again!")

     MovieTitle = str(input(" Enter the Movie Title: "))
     MovieEntry = (str(Year) +": "+ MovieTitle)
     UCMovieEntry = MovieEntry.upper()
     UCMovieList = list()
     while i < len(MovieList): # converts everything to upper case to ensure it is not already in list
         UCMovieList.append(MovieList[i].upper())
         i += 1
     if UCMovieEntry in UCMovieList:
        print(".....Movie already added to List....")
     else:
        MovieList.append(MovieEntry)
        print(" .............Movie Added...............")     
def RemoveFrList(MovieList):
    Removed = False
    if len(MovieList) <= 0:
        print(" .......No Movies in the Database......")
    elif len(MovieList) > 0:
        DisplayList(MovieList)
        while Removed == False:
            try:
                removeTitle = int(input(" Enter the number for the title you would like to have removed: "))
                if removeTitle < len(MovieList) and removeTitle > len(MovieList) or removeTitle == 0:
                    print(" ....Invalid Entry....")
                    Removed = False

                else:
                    MovieList.remove(MovieList[removeTitle - 1]) # taking away from the list
                    Removed = True
                    print(" ....Movie has been Removed....")
                    #DisplayList(MovieList)
            except Exception:
                print(" ....Invalid Entry....")  
def OldtoNew(MovieList):
    MovieList.sort()
    MovieNum = 1
    if len(MovieList) > 0:
        for i in MovieList: # loop to display each movie in the list
            print(" ", MovieNum,")", " ", i)
            MovieNum += 1 # numbers the movies
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
        AtoZList.append(MovieList[i][6:] +" :" + MovieList[i][:4:] )
        i += 1
    AtoZList.sort()  
    for i in AtoZList:
        print("",j,")","",i)
        j += 1
def ZtoA(MovieList):
    i = 0
    j = 1
    MovieNum = 1
    ZtoAList = list() # Creates new list for sorting

    print(" Here is the list of Movies in your collection from A to Z: ")
    while i < len(MovieList): # loop to display each movie in the list
        ZtoAList.append(MovieList[i][6:] +" :" + MovieList[i][:4:] )
        i += 1
    ZtoAList.sort(reverse = True)  
    for i in ZtoAList:
        print("",j,")","",i)
        j += 1
    
    
             
MovieList = (["1951: Alice in Wonderland","1988: Beetlejuice","1994: Ace Ventura: Pet Detective"])
Quit = False
#print(len(MovieList))

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
            print(" List from Oldest to Newest is as follows:")
            OldtoNew(MovieList)
    elif choice == "5":
        ShorttoLong(MovieList) #Function Call
    elif choice == "6":
        LongtoShort(MovieList) #Function Call
    elif choice == "7":
        AtoZ(MovieList) #Function Call
    elif choice == "8":
        ZtoA(MovieList) # Function Call
    elif choice == "9":
        Quit = True
    else:
        print(" .....Invalid Option, plese try again!.....") # if no valid option is chosen the user will be advised. 
        print("")