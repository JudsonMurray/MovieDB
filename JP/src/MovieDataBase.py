#Name: Potter Nerdling
# Date: 06/29/18
#Movie Data Base

def DisplayList(MovieList):# Displays Movie Titles in list
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection:")
        for i in MovieList: # loop to display each movie in the list
            print(" ", MovieNum,")", " ", i)
            MovieNum += 1 # numbers the movies
    else:
        print(" ........No Movies in Data Base.......") 
def AddtoList(MovieList): # adding movie to list
     Year = 0
     i = 0
     DisplayList(MovieList)
     MovieTitle = ""
     UCMovieList = list() # UC = Upper case
     UCMovieEntry = ""
     MovieEntry = ""
     MovieTitleValid = False
     
     
     while len(str(Year)) != 4 or Year < 1895 and Exception != True: # checks the length of the year and there is no exception. 
        try:
            Year = int(input(" Enter in the year of the Movie Title:"))
            if len(str(Year)) != 4 or Year < 1895:
                print(" Invalid Entry, please try again!")
        except Exception:
            print(" Invalid Entry, please try again!")

     while len(MovieTitle) <= 0 or MovieTitleValid == False: # Verifies there is a valid entry for Movie title, not just white spaces
        MovieTitle = str(input(" Enter the Movie Title: "))
        if len(MovieTitle.strip()) > 0:
            MovieEntry = (str(Year) +": "+ MovieTitle.title()) # Title function for Movie Title
            UCMovieEntry = MovieEntry.upper()
            MovieTitleValid = True  
        else:
            print("......Invalid Entry, Please try again......")
            MovieTitleValid = False

     if MovieTitleValid == True:
         while i < len(MovieList): # converts everything to upper case to ensure it is not already in list
            UCMovieList.append(MovieList[i].upper())
            i += 1
         if UCMovieEntry in UCMovieList:
            print(".....Movie already added to List....")
         else:
            MovieList.append(MovieEntry)
            print(" .............Movie Added...............") 
def DisplayStats(MovieList): # Displays Movie List Stats
     if len(MovieList) <= 0: # insures if there is movies in the DB the stats will be displayed, if not no stats will be displayed. 
        print(" ......No movie stats to display.....")
     else:
        print(" Movie Data Base Stats:")
        print(" Total amount of Movies in List: ", len(MovieList))
        print(" The longest Title is as follows:",max(MovieList, key=len))
        print(" The shortest Title is as Follows:", min(MovieList, key=len))
        print(" List from Oldest to Newest is as follows:")
        OldtoNew(MovieList)
def AddActor(MovieList): # Add Actor to a specific Movie
    ValidActorEntry = False
    ValidMovieChoice = False
    try:
        if len(MovieList) > 0:
            while ValidMovieChoice == False: # Ensure the choice for film to add to is valid. 
                try:
                    moviechoice = int(input(" Enter the number for which movie you would like to add actors too?"))
                    if moviechoice < len(MovieList) and moviechoice > len(MovieList) or moviechoice == 0:
                        print(" ......Invalid Entry.....")
                        ValidMovieChoice = False
                    else:
                        MovieKey = MovieList[moviechoice - 1]
                        print(" Movie Chosen:",MovieKey)
                        ValidMovieChoice = True
                except Exception:
                    print(" .......Invalid Entry.....")
            
            while ValidActorEntry == False: # Checks to ensure Actor name is valid and not just blank
                ActorEntry = str(input(" Enter Actors Name: "))
                if len(ActorEntry) <= 0 or len(ActorEntry.strip()) <= 0:
                    print(" .......Invalid Entry.....")
                    ValidActorEntry = False
                else:
                    ValidActorEntry = True
            
            if  MovieKey not in Actors:
                Actors.update({MovieKey: [ActorEntry] })
                print("........Actor Added.......")
                DisplayActors(Actors) # Shows List of Movies with Actors
        
            elif MovieKey in Actors and len(ActorEntry.strip()) > 0:
                Actors[MovieKey].append(ActorEntry)
                print("........Actor Added.......")
                DisplayActors(Actors) 
        
    except Exception:
        print(" ......Invalid Entry......")
def RemoveActor(MovieList): # Remove an Actor from a specific Movie
    Numbered = 0
    ChosenTitle = ""
    if len(Actors) > 0:
        for key in Actors:
            MoviewithActors.append(key) # Create a list with movies that has actors in it
            #print(MoviewithActors)
        if len(MoviewithActors) > 0: # ensure the list of actors is not empty
            print(" List Of Movie(s) to Choose from with Actors: ")
            for i in MoviewithActors:
                print(" ",str(Numbered + 1) + ")",i) # prints list of movies with Actors
                Numbered += 1
        MovieChoice = int(input("Enter the number for the Movie title to remove actors from: ")) # asks which movie to remove an actor from
        ChosenTitle =  MoviewithActors[MovieChoice - 1]
        print("Length of vals =", len(Actors[ChosenTitle]))

        if ChosenTitle in Actors:
            for i in Actors[key]:
                print(" ",Actors[ChosenTitle].index(i) + 1,")",i) # Displays actors per movie
            RemoveActor = int(input(" Enter the number for the actor you would like removed: "))
            if len(Actors[ChosenTitle]) >= 2:
                del Actors[ChosenTitle][RemoveActor - 1]
                print(" .......Actor Removed.....")
                DisplayActors(Actors)
            elif len(Actors[ChosenTitle]) <= 1:
                del Actors[ChosenTitle]
                print(" .......Actor Removed.....")
                DisplayActors(Actors)

           
    else:
        print(" .......No Actors in Data Base......")
def DisplayActors(Actors):  #Displays Movie with Actors in List
    MovieNum = 1
    
    if len(Actors) > 0:
        print(" Movies with Actors are as follows: ")
        for key in Actors:
            print("",MovieNum,")"," Movie Title:",key)
            MovieNum += 1
            print("  Actors:")
            for i in Actors[key]:
                print(" ",Actors[key].index(i) + 1,")",i) # Displays actors per movie
    else:
        print(" .........No Actors in Database.........")
def RemoveFrList(MovieList): # Removes from list
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
def OldtoNew(MovieList):  # Sorts and displays Movie Oldest to Newest
    MovieList.sort()
    MovieNum = 1
    if len(MovieList) > 0:
        for i in MovieList: # loop to display each movie in the list
            print(" ", MovieNum,")", " ", i)
            MovieNum += 1 # numbers the movies
    else:
        print(" .......No Movies in the Database......")
def ShorttoLong(MovieList): # Sorts movie title shortest to longest
    MovieList.sort(key = len) # sorts list based on length
   
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection Shortest to Longest: ")
        DisplayList(MovieList)
    else:
        print(" .......No Movies in the Database......") 
def LongtoShort(MovieList): # Sorts movie title longest to shortest
    MovieList.sort(key = len, reverse = True) # sorts list based on length then reverses list
   
    if len(MovieList) > 0:
        print(" Here is the list of Movies in your collection Longest to Shortest: ")
        DisplayList(MovieList)
    else:
        print(" .......No Movies in the Database......")
def SwapMovieTitleandYear(MovieList): # swaps movie title and year
    i = 0
    SwapList = list()
    while i < len(MovieList): # loop to display each movie in the list
        SwapList.append(MovieList[i][6:] +" :" + MovieList[i][:4:] )
        i += 1
    return SwapList
def AtoZ(MovieList): # function to sort list and display aplhabetically
    AtoZList = SwapMovieTitleandYear(MovieList)
    AtoZList.sort()
    DisplayList(AtoZList)         
def ZtoA(MovieList):  # function to sort list and display aplhabetically in reverse
    ZtoAList = SwapMovieTitleandYear(MovieList)
    ZtoAList.sort(reverse = True)
    DisplayList(ZtoAList) 
           
MovieList = (["2010: Alice in Wonderland","1988: Beetlejuice","1994: Ace Ventura: Pet Detective"])
Quit = False
Actors = dict()
MoviewithActors = list()

while Quit == False:
    print(" Here are some Movie Data Base choices: ") # Displays choices that can modify the list for Movies
    print("     1) Add a Movie")
    print("     2) Add Actor to Movie")
    print("     3) Remove a Movie")
    print("     4) Remove an Actor")
    print("     5) Display Movie List")
    print("     6) Display Actors")
    print("     7) Display Movie List Stats")
    print("     8) Display Movie List Shortest to Longest")
    print("     9) Display Movie List Longest to Shortest")
    print("     10) Display Movie List A to Z")
    print("     11) Display Movie List Z to A")
    print("     12) Or you can Quit! ")

    choice = str(input("    Enter your choice:")) # takes the users input
    print("")
    if choice == "1": 
        AddtoList(MovieList) #Function Call
        DisplayList(MovieList)#Function Call
    elif choice == "2":
        DisplayList(MovieList)#Function Call
        AddActor(MovieList)   #Function Call
    elif choice == "3":
        RemoveFrList(MovieList) #Function Call
        if len(MovieList) > 0: 
            DisplayList(MovieList) #Function Call
    elif choice == "4":
        RemoveActor(MovieList) # Function Call
    elif choice == "5":
        DisplayList(MovieList)#Function Call
    elif choice == "6":
        DisplayActors(Actors) # Function Call
    elif choice == "7":
        DisplayStats(MovieList)#Function Call
    elif choice == "8":
        ShorttoLong(MovieList) #Function Call
    elif choice == "9":
        LongtoShort(MovieList) #Function Call
    elif choice == "10":
        AtoZ(MovieList) #Function Call
    elif choice == "11":
        ZtoA(MovieList) # Function Call
    elif choice == "12":
        Quit = True
    else:
        print(" .....Invalid Option, plese try again!.....") # if no valid option is chosen the user will be advised. 
        print("")