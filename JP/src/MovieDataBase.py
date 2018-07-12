#Name: Potter Nerdling
# Date: 07/05/18
#Movie Data Base

def DisplayMovieList(MovieList):# Displays Movie Titles in list
    MovieNum = 1
    if len(MovieList) > 0:
        print(" Movies in your collection:")
        for i in MovieList: # loop to display each movie in the list
            print(" ", MovieNum,")", " ", i)
            MovieNum += 1 # numbers the movies
    else:
        print(" .....No Movies in Data Base.....") 
def AddtoMovieList(MovieList): # adding movie to list
     Year = 0
     i = 0
     DisplayMovieList(MovieList)
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
        MovieTitle = input(" Enter the Movie Title: ")
        if len(MovieTitle.strip()) > 0:
            MovieEntry = (str(Year) +": "+ MovieTitle.title()) # Title function for Movie Title
            UCMovieEntry = MovieEntry.upper()
            MovieTitleValid = True  
        else:
            print(" .....Invalid Entry, Please try again.....")
            MovieTitleValid = False

     if MovieTitleValid == True:
         while i < len(MovieList): # converts everything to upper case to ensure it is not already in list
            UCMovieList.append(MovieList[i].upper())
            i += 1
         if UCMovieEntry in UCMovieList:
            print(".....Movie already added to List.....")
         else:
            MovieList.append(MovieEntry)
            print(" .....Movie Added.....") 
def DisplayMovieListStats(MovieList): # Displays Movie List Stats
     num = 1
     if len(MovieList) <= 0: # insures if there is movies in the DB the stats will be displayed, if not no stats will be displayed. 
        print(" .....No movie stats to display.....")
     else:
        print(" Movie Data Base Stats:")
        print(" Total amount of Movies in List: ", len(MovieList))
        print(" The longest Title is as follows:",max(MovieList, key=len))
        print(" The shortest Title is as Follows:", min(MovieList, key=len))
        print(" List from Oldest to Newest is as follows:")
        MovieList.sort()
        for i in MovieList:
            print(" ",str(num) + ")", i)
            num += 1
def AddActor(Actors): # Add Actor to a specific Movie
    ValidActor = False
    UCActorEntry = ""
    UCActorEntryList = list()
    i = 0
    
    while ValidActor == False:
           try:
               ActorEntry = input(" Enter an Actors Name: ")

               if len(ActorEntry) <= 0:
                   print(" .....Invalid Entry.....")
                   ValidActor = False
               elif len(ActorEntry.strip()) > 0:
                   ValidActor = True
               else:
                   print(" .....Invalid Entry.....")
           except TypeError:
               print(" .....Invalid Entry.....")
               ValidActor = False
    if ValidActor == True:
            Actors.update({ActorEntry:list()})
            print(" .....Actor Added.....")
            DisplayActors(Actors)      
def RemoveActor(MovieList): # Remove an Actor from a specific Movie
    ActorList = list()
    ActorRemoved = False
    DisplayActors(Actors)
    while ActorRemoved == False:
        if len(Actors) <= 0:
            print(" .....No Actors in Data Base.....")
        else:
            try:
                ActorSelection = int(input(" Enter the number for the Actor you would like to have removed: "))
                if ActorSelection < len(MovieList) and ActorSelection > len(MovieList) or ActorSelection == 0:
                    print(" .....Invalid Entry.....") 
                    ActorRemoved = False
                else:
                    for key in Actors:
                        ActorList.append(key)
                        choice = ActorList[ActorSelection - 1]
                    if choice in Actors:
                        del Actors[choice]
                        print(" .....Actor Removed.....")
                    ActorRemoved = True
            except Exception:
                print(" .....Invalid Entry.....")
def RemoveMovieFromMovieList(MovieList, Actors): # Removes from list
    Removed = False
    if len(MovieList) <= 0:
        print(" .....No Movies in the Database.....")
    elif len(MovieList) > 0:
        DisplayMovieList(MovieList)
        while Removed == False:
            try:
                removeTitle = int(input(" Enter the number for the title you would like to have removed: "))
                if removeTitle < len(MovieList) and removeTitle > len(MovieList) or removeTitle == 0:
                    print(" .....Invalid Entry.....")
                    Removed = False

                else:
                    for Actor in Actors:
                        if MovieList[removeTitle - 1] in Actors[Actor]:
                            Actors[Actor].remove(MovieList[removeTitle - 1])
                    MovieList.remove(MovieList[removeTitle - 1]) # taking away from the list
                    Removed = True
                    print(" .....Movie has been Removed.....")
                    
                    if len(MovieList) > 0: 
                        DisplayMovieList(MovieList) 
                    else:
                        print(" .....No more Movies in Data Base.....")
            except Exception:
                print(" .....Invalid Entry.....")
def SwapMovieTitleandYear(MovieList): # swaps movie title and year
    i = 0
    SwapList = list()
    while i < len(MovieList): # loop to display each movie in the list
        SwapList.append(MovieList[i][6:] +" :" + MovieList[i][:4:] )
        i += 1
    return SwapList
def Linking(Actors, MovieList): # Links a movie to an Actor
    ActorList = list()
    ValidActor = False
    ValidMovie = False
    if len(Actors) <= 0:
        print(" .....No Actors in Data Base.....")
    elif len(MovieList) <= 0:
        print(" .....No Movies in Data Base.....")
    else:
        for key in Actors:
            ActorList.append(key)

        DisplayActors(Actors)
        while ValidActor == False:
            try:
                ActorChoice = int(input(" Which Actor would you like to add a Movie to? "))
                if ActorChoice == 0:
                    print(" .....Invalid Entry.....")
                    ValidActor = False
                else:
                    ActorChoice = ActorList[ActorChoice - 1]
                    DisplayMovieList(MovieList)
                    ValidActor = True
            except Exception:
                print(" .....Invalid Entry.....")
        while ValidMovie == False:
            try:
                MovieChoice = int(input(" Which Movie would you like to connect the Actor to? "))
                if MovieChoice == 0:
                    print(" .....Invalid Entry.....")
                    ValidMovie = False
                else:
                    MovieChoice = MovieList[MovieChoice - 1]
                    Actors[ActorChoice].append(MovieChoice)
                    print(" .....LINKED!.....") 
                    ValidMovie = True
            except Exception:
                print(" .....Invalid Entry.....")              
def DisplayActorsandMovies(Actors): # prints actors and their movies 
    totallengths = 0
    lengths = [len(v) for v in Actors.values()]
    for i in lengths:
        totallengths += i
     
    if totallengths <= 0:
        print(" .....No Actors Linked with a Movie.....")
    else:
        counter = 1
        number = 1
        print(" Actors: ")
        for key in Actors:
            print(" ", counter,")",key)
            counter += 1
            print("   Movie Title(s):")
            for i in Actors[key]:
                print("    ",i)
                number += 1       
def DisplayActors(Actors):# Display List of Actors
    counter = 1
    if len(Actors) > 0:
        print(" Actors:")
        for key in Actors:
            print("  " + str(counter) + ")",key)
            counter += 1
    else:
        print(" .....No Actors in Data Base.....") 
def RemoveMovieFromActor(Actors): #Removes a Movie From a specific Actor
    ActorList = list()
    MovieList = list()
    ValidActor = False
    ValidMovie = False
    counter = 1

    if len(Actors) > 0: # Creates Actor List for options
        for Actor in Actors:
            ActorList.append(Actor)
        while ValidActor == False:
            try:
                DisplayActors(Actors)
                ActorChosen = int(input(" Which Actor would you like to remove a movie from? "))
                if ActorChosen < len(ActorList) or ActorChosen > len(ActorList) or ActorChosen == 0:
                    print(" .....Invalid Entry.....")
                    ValidActor = False
                else:
                    ActorChosen = ActorList[ActorChosen - 1]
                    #print(ActorChosen)
                    ValidActor = True
            except ValueError:
                print(" .....Invalid Entry.....")
                ValidActor = False
        if len(Actors[ActorChosen]) <= 0:
            print(" .....Actor is not linked to any Movies.....")
        else:
           while ValidMovie == False:
               print(" List of Movies for", ActorChosen + ": ")
               for Movie in Actors[ActorChosen]:
                   print(" " + str(counter) + ")", Movie)
                   MovieList.append(Movie) # Appends movie to MovieList for options

               MovieChosen = int(input(" Which Movie would you like to have removed? "))
               if MovieChosen < len(MovieList) or MovieChosen > len(MovieList) or MovieChosen == 0:
                   print(" .....Invalid Entry.....")
                   ValidMovie = False
               else:
                   MovieChosen = MovieList[MovieChosen - 1] # Checks to ensure movie is in the list for the specified Actor
                   if MovieChosen in Actors[ActorChosen]:
                       Actors[ActorChosen].remove(MovieChosen)
                       print(" .....Movie has been Removed.....") 
                       ValidMovie = True   
    else:
        print(" .....No Actors in Data Base.....")
    
    

        
MovieList = (["2010: Alice in Wonderland","1988: Beetlejuice","1994: Ace Ventura: Pet Detective"])
Quit = False
Actors = dict()
ValidActor = False

while Quit == False:
    print(" Movie Data Base choices: ") # Displays choices that can modify the list for Movies
    print("     1) Add a Movie")
    print("     2) Add an Actor")
    print("     3) Remove a Movie")
    print("     4) Remove an Actor")
    print("     5) Display Movie List")
    print("     6) Display Actors")
    print("     7) Display Movie List Stats")
    print("     8) Display Movie List Shortest to Longest")
    print("     9) Display Movie List Longest to Shortest")
    print("     10) Display Movie List A to Z")
    print("     11) Display Movie List Z to A")
    print("     12) Link Movie to an Actor")
    print("     13) View Actors with their Movie Titles")
    print("     14) Remove Movie From Actor")
    print("     15) Or you can Quit! ")
    

    choice = str(input("    Enter your choice:")) # takes the users input
    print("")
    if choice == "1": 
        AddtoMovieList(MovieList) 
        DisplayMovieList(MovieList)
    elif choice == "2":
        AddActor(Actors)
    elif choice == "3":
        RemoveMovieFromMovieList(MovieList, Actors)   
    elif choice == "4":
        RemoveActor(Actors)  
    elif choice == "5":
        DisplayMovieList(MovieList)
    elif choice == "6":
        DisplayActors(Actors) 
    elif choice == "7":
        DisplayMovieListStats(MovieList)
    elif choice == "8":
        MovieList.sort(key = len)
        DisplayMovieList(MovieList)
    elif choice == "9":
        MovieList.sort(key = len, reverse = True)
        DisplayMovieList(MovieList) 
    elif choice == "10":
        AtoZ = SwapMovieTitleandYear(MovieList)
        AtoZ.sort()
        DisplayMovieList(AtoZ)
    elif choice == "11":
        ZtoA= SwapMovieTitleandYear(MovieList)
        ZtoA.sort(reverse = True)
        DisplayMovieList(ZtoA)
    elif choice == "12":
        Linking(Actors, MovieList)
    elif choice == "13":
        DisplayActorsandMovies(Actors)
    elif choice == "14":
        RemoveMovieFromActor(Actors)
    elif choice == "15":
        Quit = True
    else:
        print(" .....Invalid Option, plese try again!.....") # if no valid option is chosen the user will be advised. 
        print("")