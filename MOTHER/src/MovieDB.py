#   Name:       Mother Murray
#   Date:       06/25/2018
#   Purpose:    Reference Implementation for Movie DB Project

#   Version History:
#   v0.1:   (06/25/2018) Initial Version (Movies)
#   v0.2:   (06/30/2018) Adding Year Support for Movies (Name/Year Composite Key)
#   v0.3:   (07/01/2018) Added Movie Summary Info
#   v0.4:   (07/02/2018) Added Sorting options for Viewing Movies
#   v0.5:   (07/17/2018) Adding Actor DB and Linking behaviour to Movies
#                        Refactored Menu Implementation for Maintainability

import uuid
import os
import copy

#   -------------------------------------------------------------------------------------------------------------------
#   Global variable Declaration
menuFilter = None
movieList = []  #   Used to store Movie Info
actorList = []  #   Used to store Actor Info (& Movie Links)

menuDB = {}     #   Used to store Menu Navigation
keyVal = 0      #   Initial Key to use for Movie Keys (Unique Constraint)
#   -------------------------------------------------------------------------------------------------------------------

def showMovieList(mList):

    #   (C) Chronological (DEFAULT)
    #   (S) Shortest - Longest
    #   (L) Longest - Shortest
    #   (A) Alphabetical
    #   (R) Reverse Alphabetical
   
    print('\n','----- Movies -----', currViewOption[0])
    if len(mList) > 0:

        if currViewOption[0] == 'S':
            displayList = sorted(mList, key = lambda k: len(k['name']))
        elif currViewOption[0] == 'L':
            displayList = sorted(mList, key = lambda k: len(k['name']),reverse=True)
        elif currViewOption[0] == 'A':
            displayList = sorted(mList, key = lambda k: k['name'])
        elif currViewOption[0] == 'R':
            displayList = sorted(mList, key = lambda k: k['name'],reverse=True)
        elif currViewOption[0] == 'O':
            displayList = sorted(mList, key = lambda k: k['year'])
        elif currViewOption[0] == 'N':
            displayList = sorted(mList, key = lambda k: k['year'],reverse=True)
        else:
            displayList = mList

        #for i,v in enumerate(mList):
        for i,v in enumerate(displayList):
            print(i+1,': ',v['name'],' (', v['year'],')', ':\t',v['key'],sep='')
    else:
        print("**** NO MOVIES ****")

    print()
    return

#   -------------------------------------------------------

def addMovieDB(mList, newMovieName, newMovieYear):
    mList.append({'name':newMovieName,'year':newMovieYear,'key':getKey()})

#   -------------------------------------------------------

def addMovie(mList):

    print('----- Add Movie -----')

    showMovieList(mList)

    try:
        newMovieName = input("Enter Movie name to add:")
        newMovieYear = int(input("Enter Movie year:"))

        if len(newMovieName) > 0:

            for movieEntry in mList:
                if movieEntry['year'] == newMovieYear and movieEntry['name'] == newMovieName:
                    #print('Sorry, Movie exists!')
                    userChoice = input('Are you sure you want to add a duplicate: (Y/N)')
                    while userChoice.upper() not in 'YN':
                        userChoice = input('Are you sure you want to add a duplicate: (Y/N)')
                    if userChoice.upper() == 'N':
                        break
                    else:
                        #mList.append({'name':newMovieName,'year':newMovieYear,'key':nextKey()})
                        addMovieDB(mList, newMovieName, newMovieYear)
                        break
            else:
                #mList.append({'name':newMovieName,'year':newMovieYear,'key':nextKey()}) #   If Movie does not exist, add to list
                addMovieDB(mList, newMovieName, newMovieYear)
    except:
        pass

#   -------------------------------------------------------

def removeMovie(mList):

    print('----- Remove Movie -----')

    showMovieList(mList)
    
    if len(mList) > 0:
        try:
            delMovie = int(input("Select Movie # to remove:"))
            if delMovie > 0 and delMovie <= len(mList):

                actorKey = mList[delMovie-1]['key']
                for actor in actorList:
                    if actorKey in actor['movieList']:
                        print("Removing Link to ", actor['name'])
                        actor['movieList'].remove(actorKey)

                mList.remove(mList[delMovie-1])
            else:
                raise Exception
        except Exception as e:
            print(e)
            print('Invalid Option!')
            pass


#   -------------------------------------------------------

def movieStats(mList):

    print()
    print('----- Movie Stats -----')

    print('Total Movies:',len(mList))
    print('Oldest Movie:', min(movie['year'] for movie in mList))
    print('Newest Movie:', max(movie['year'] for movie in mList))
    print('Shortest Title:',min(len(movie['name']) for movie in mList))    
    print('Longest Title:',max(len(movie['name']) for movie in mList))
    print()

#   -------------------------------------------------

def changeSortOption(currViewOpt):
    
    print()
    print("Current View Option: ",currViewOpt[0])
    print()
    print(  "Select View Option:",
            "(S) Shortest - Longest",
            "(L) Longest - Shortest",
            "(A) Alphabetical",
            "(R) Reverse Alphabetical",
            "(O) Oldest - Newest",
            "(N) Newest - Oldest",
            "(C) Chronological",
        sep='\n')

    print()
    newOption = input().upper()
    while(newOption not in "SLARCON"):
        print("INVALID OPTION")
        newOption = input().upper()
    
    if len(newOption) > 0:
        currViewOpt[0] = newOption
    return

#   -------------------------------------------------------------------------------------------------------------------

def getKey():

    global keyVal
    keyVal+=1
    return keyVal

#   -------------------------------------------------------------------------------------------------------------------
#   -------------------------------------   Functions for Actor Options     -------------------------------------------
#   -------------------------------------------------------------------------------------------------------------------

def showActorList(actList):

    #   (C) Chronological (DEFAULT)
    #   (S) Shortest - Longest
    #   (L) Longest - Shortest
    #   (A) Alphabetical
    #   (R) Reverse Alphabetical
   
    print('\n','----- Actors -----', currViewOption[0])
    if len(actList) > 0:

        if currViewOption[0] == 'S':
            displayList = sorted(actList, key = lambda k: len(k['name']))
        elif currViewOption[0] == 'L':
            displayList = sorted(actList, key = lambda k: len(k['name']),reverse=True)
        elif currViewOption[0] == 'A':
            displayList = sorted(actList, key = lambda k: k['name'])
        elif currViewOption[0] == 'R':
            displayList = sorted(actList, key = lambda k: k['name'],reverse=True)
        elif currViewOption[0] == 'O':
            displayList = sorted(actList, key = lambda k: k['year'])
        elif currViewOption[0] == 'N':
            displayList = sorted(actList, key = lambda k: k['year'],reverse=True)
        else:
            displayList = actList

        for i,v in enumerate(displayList):
            print(i+1,': ',v['name'],' (', v['year'],'): ',len(v['movieList']),' Movie(s)' ,sep='')
    else:
        print("**** NO ACTORS ****")

    print()
    return

#   -------------------------------------------------------

def addActor(actList):
    print('----- Add Actor -----')

    showActorList(actList)

    try:
        newActorName = input("Enter Actor name to add:")
        newActorYear = int(input("Enter Actor year:"))

        if len(newActorName) > 0:

            for actorEntry in actList:
                if actorEntry['year'] == newActorYear and actorEntry['name'] == newActorName:
                    print('Sorry, Actor exists!')
                    break
            else:
                actList.append({'name':newActorName,'year':newActorYear,'movieList':set()}) #   If Movie does not exist, add to list
    except:
        pass

#   -------------------------------------------------------

def removeActor(actList):

    print('----- Remove Actor -----')
    showActorList(actList)
    
    if len(actList) > 0:
        try:
            delMovie = int(input("Select Movie # to remove:"))
            if delMovie > 0 and delMovie <= len(actList):
                actList.remove(actList[delMovie-1])
            else:
                raise Exception
        except:
            print('Invalid Option!')
            pass

#   -------------------------------------------------------

def linkActor(actList):

    os.system('cls')
    print('----- Link Actor to Movie -----')

    newMovieDB = {m['key']:m for m in movieList}

    #   Show Actors to select from
    #   TODO: I don't like this implementation. It would be possible for the index to get disaccociated from the correct selection
    
    showActorList(actList)
    if len(actList) > 0:
        actSelect = 0
        while actSelect < 1 or actSelect >len(actList) :
            actSelect = int(input("Choose Actor:"))

        #   Show Movie(s) that Actor is currently linked to
        print("Actor:",actList[actSelect-1]['name'])
        for movie in actList[actSelect-1]['movieList']:
                print('\t',newMovieDB[movie]['name'], '(',newMovieDB[movie]['year'], ') -', newMovieDB[movie]['key'])
        else:
                print()
        
        #   Remove Movies the Actor is a current participant within from the list of options for Linking
        for movieKey in actList[actSelect-1]['movieList']:
            newMovieDB.pop(movieKey)
        else:
            
            #   If there are any unlinked movies, offer to link
            if len(newMovieDB) > 0:

                for movie in newMovieDB:
                    print(newMovieDB[movie]['key'], '-', newMovieDB[movie]['name'], newMovieDB[movie]['year'])

                linkSelect = None
                while linkSelect not in newMovieDB:
                    linkSelect = int(input("Choose Movie to Link:"))
        
                #   Add Movie to Actor's List of Movie Referencess
                actList[actSelect-1]['movieList'].add(linkSelect)

#   -------------------------------------------------------

def unlinkActor(actList):

    os.system('cls')
    print('----- UnLink Actor to Movie -----')

    newMovieDB = {m['key']:m for m in movieList}

    showActorList(actList)  #TODO: Show only Actors with 1 or more Movies Linked

    if len(actList) > 0:
        actSelect = 0
        while actSelect < 1 or actSelect >len(actList) :
            actSelect = int(input("Choose Actor:"))
            
        if len(actList[actSelect-1]['movieList']) == 0:
            print("Sorry - No Movies!")
        else:
            for movie in actList[actSelect-1]['movieList']:
                print(newMovieDB[movie]['name'], newMovieDB[movie]['year'], newMovieDB[movie]['key'])

            linkSelect = None
            while linkSelect not in newMovieDB:
                linkSelect = int(input("Choose Movie to UnLink:"))
        
            #   Add Movie to Actor's List of Movie Referencess
            actList[actSelect-1]['movieList'].remove(linkSelect)

#   -------------------------------------------------------------------------------------------------------------------
#   -------------------------------------------------------------------------------------------------------------------

def displayMainMenu():

    for option in menuDB:
        print(option, ':', menuDB[option][0])

    print('Select a choice:',end='')
    
    while True:
        try:
            ui = input().capitalize()
            if len(ui) == 1 and ui in menuFilter:
                break
        except:
            pass

        print('Try again: ',end='')

    return(ui)

#   -------------------------------------------------------


#   Default Movie Information
addMovieDB(movieList, 'Serenity',   2005)
addMovieDB(movieList, 'Predator',   1987)
addMovieDB(movieList, 'Salton Sea', 2002)
addMovieDB(movieList, 'Cube',       1980)

#   Default Actor Information
actorList.append({'name':'Patrick Stewart','year':1940,'movieList':set()})
actorList.append({'name':'Arnold Schwarzenegger','year':1947,'movieList':set()})
actorList.append({'name':'Nathan Fillion','year':1971,'movieList':set()})
actorList.append({'name':'Stana Katic','year':1978,'movieList':set()})

#   Default Sorting Options for Movies/Actors
currViewOption = ['C']

#   Build Menu Options & Function Bindings for 
menuDB['1'] = ['Show Movie List',   showMovieList,movieList]
menuDB['2'] = ['Add Movie',         addMovie,movieList]
menuDB['3'] = ['Remove Movie',      removeMovie,movieList]  #Needs actorList (for Movie Links)
menuDB['4'] = ['Show Movie Stats',  movieStats,movieList]
menuDB['5'] = ['Change Sort Options',changeSortOption,currViewOption]
menuDB['6'] = ['Show Actor',        showActorList,actorList]
menuDB['7'] = ['Add Actor',         addActor,actorList]
menuDB['8'] = ['Link Actor',        linkActor,actorList]    #Needs actorList & movieList
menuDB['9'] = ['Unlink Actor',      unlinkActor,actorList]  #Needs actorList & movieList
menuDB['A'] = ['Remove Actor',      removeActor,actorList]
menuDB['Q'] = ['Quit',None,None]

#   Build Dynamic Filter for Limiting User Input to Correct Choices
menuFilter = ''
for i in menuDB:
    menuFilter += i

#   Run Main Menu Selection until user quits
while True:
    choice = displayMainMenu()
    os.system('cls')
    
    if choice == 'Q':
        break
    else:
        menuDB[choice][1](menuDB[choice][2])    #TODO: Replace List implementation with Dictionary Imp. with titled properties