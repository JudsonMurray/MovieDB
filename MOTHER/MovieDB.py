#   Name:       Mother Murray
#   Date:       06/25/2018
#   Purpose:    Reference Implementation for Movie DB Project

#   Version History:
#   v0.1:   Initial Version (Movies)


menuFilter = None

def displayMainMenu():
    print('1: View Movie List')
    print('2: Add a Movie')
    print('3: Remove a Movie')
    print('Q: Quit')

    print('Select a choice:',end='')

    #ui = input().capitalize()                  #   Previous implementation of Menu Filter
    #while len(ui) != 1 or ui not in '123Q ':
    #    print('Try again: ',end='')
    #    ui = input().capitalize()
    
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
        for i in mList:
            print(mList.index(i)+1,': ',i)
    else:
        print("**** NO MOVIES ****")

    print()
    return

def addMovie(mList):

    print('----- Add Movies -----')

    showMovieList(mList)
    newMovie = input("Enter Movie to add:")
    if len(newMovie) > 0:
        mList.append(newMovie)

def removeMovie(mList):

    print('----- Remove Movies -----')

    showMovieList(mList)
    
    if len(mList) > 0:
        try:
            delMovie = int(input("Select Movie # to remove:"))
            if delMovie >= 0 and delMovie < len(mList):
                mList.remove(mList[delMovie])
        except:
            pass

#   -------------------------------------------------

movieList = []
movieList.append('Serenity')
movieList.append('Predator')
movieList.append('Salton Sea')

menuOptions = {'1':showMovieList,'2':addMovie,'3':removeMovie,'Q':exit,' ':print}

menuFilter = ''
for i in menuOptions:
    menuFilter += i

#print(menuFilter)

while True:
    choice = displayMainMenu()

    if choice == 'Q':
        break ;    

    menuOptions[choice](movieList)