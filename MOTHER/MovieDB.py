#   Name:       Mother Murray
#   Date:       06/25/2018
#   Purpose:    Reference Implementation for Movie DB Project

#   Version History:
#   v0.1:   (06/25/2018) Initial Version (Movies)
#   v0.2:   (06/30/2018) Adding Year Support for Movies (Name/Year Composite Key)


menuFilter = None

def displayMainMenu():
    print('1: View Movie List')
    print('2: Add a Movie')
    print('3: Remove a Movie')
    print('Q: Quit')

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

def showMovieList(mList):

    print('\n','----- Movies -----')
    if len(mList) > 0:
        for i,v in enumerate(mList):
            print(i+1,': ',v['name'],' (', v['year'],')',sep='')
    else:
        print("**** NO MOVIES ****")

    print()
    return

def addMovie(mList):

    print('----- Add Movies -----')

    showMovieList(mList)
    newMovieName = input("Enter Movie name to add:")
    newMovieYear = input("Enter Movie year")

    if len(newMovieName) > 0:

        for movieEntry in mList:
            if movieEntry['year'] == int(newMovieYear) and movieEntry['name'] == newMovieName:
                print('Sorry, Movie exists!')
                break
        else:
            mList.append({'name':newMovieName,'year':newMovieYear})

def removeMovie(mList):

    print('----- Remove Movies -----')

    showMovieList(mList)
    
    if len(mList) > 0:
        try:
            delMovie = int(input("Select Movie # to remove:"))
            if delMovie > 0 and delMovie <= len(mList):
                mList.remove(mList[delMovie-1])
            else:
                raise Exception
        except:
            print('Invalid Option!')
            pass

#   -------------------------------------------------

movieList = []
#   Default Movie Information
movieList.append({'name':'Serenity','year':2005})
movieList.append({'name':'Predator','year':1987})
movieList.append({'name':'Salton Sea','year':2002})

menuOptions = {'1':showMovieList,'2':addMovie,'3':removeMovie,'Q':exit,' ':print}

menuFilter = ''
for i in menuOptions:
    menuFilter += i

while True:
    choice = displayMainMenu()

    if choice == 'Q':
        break ;    

    menuOptions[choice](movieList)