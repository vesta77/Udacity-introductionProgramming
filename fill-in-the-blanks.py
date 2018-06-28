ls_categories = ['FIFA', 'Travel', 'Internet']

#The text for the questions and list containing the answeres
FIFA_Text = '''The Federation Internationale de Football Association (short FIFA) is an association responsible for the organization of footballs major international tournaments. The most important tournament is the World Cup, which is currently taking place in __1__. __2__ teams compete against each other in order to win the title. The last World Cup in 2014 was won by __3__ and __4__ is the team with the most wins in total. The World Cup is hosted in a different country every __5__ years.'''
FIFA_Answeres = ['Russia', '32', 'Germany', 'Brazil', '4']
Travel_Text = '''To explore the world is the desire of a great number of people. They want to see all __1__ continents and travel the __2__ seas of the world. The largest ocean is the __3__. The big cities are in particular interesting to visit. The most visited city in 2017 was __4__. The most visited country was __5__.'''
Travel_Answeres = ['7', '7', 'Pacific', 'Bangkok', 'France']
Internet_Text = '''The World Wide Web (short __1__ ) influences the modern world like no other invention did before. The most popular website is __2__ , which was founded in 1998 by __3__. The most popular social media network is __4__.'''
Internet_Answeres =['www', 'Google', 'Larry Page', 'Facebook' ]

#To keep track which answeres belong to which text and category a allocation list is beeing used
allocation = [['FIFA', FIFA_Text, FIFA_Answeres],['Travel', Travel_Text, Travel_Answeres],['Internet', Internet_Text, Internet_Answeres]]

#The function lists all available categories and asks the user to select one
#It returns the index of the choosen category in the allocation list
def selectCategory():
    print 'Select one of the possible categories: \n'
    for category in ls_categories:
        print '- ' + category
    print ''
    userChoice=raw_input('choose a category from the list above: ')
    while userChoice not in ls_categories:
        #Test whether the choosen category is valid
        userChoice=raw_input('please enter a valid category: ')
    print 'ok'
    counter = 0
    for i in allocation:
        if i[0]==userChoice:
            return counter
        counter+=1

#Lets the user choose the difficulty of the game
#The difficulty is defined by the number of lives
#The return is the number of lives correlated with the difficulty
def selectDifficulty():
    difficulties = ['easy', 'medium', 'hard']
    lives=0
    print 'select a difficulty\n'
    for options in difficulties:
        print '- ' + options
    choosenDifficulty=raw_input('\nchoose a difficulty from the list above: ')
    while choosenDifficulty not in difficulties:
        #Test whether the choosen difficulty is valid
        choosenDifficulty=raw_input('please enter a valid difficulty: ')
    print 'ok'
    if choosenDifficulty == 'easy':
        lives=5
    if choosenDifficulty == 'medium':
        lives=3
    if choosenDifficulty == 'hard':
        lives=1
    print 'You have choosen ' + choosenDifficulty + ' and will have ' + str(lives) + ' lives'
    return lives


#The function tests whether the answere given bby the user is correct and askes him to
#enter another answere if it is not. It keeps track of the lives and returns the remaining number of lifes
def checkAnswere(userAnswere, correctAnswere, index, lives):
        if userAnswere != correctAnswere:
            while userAnswere != correctAnswere:
                if lives >1:
                    lives -=1
                    print '\nincorrect'
                    print 'You have ' + str(lives) + ' left'
                    userAnswere = raw_input ('enter another answere for __' + str(index) + '__ : ')
                else:
                    lives = 0
                    return lives
        return lives

#the running version of the quiz
#takes the category index and number of lives as parameters
#takes the answere list and tests the user imput accordingly
def runQuiz (categoryIndex, lives):
    answeres = allocation [categoryIndex][2]
    index=1
    text = allocation [categoryIndex][1]
    for correctAnswere in answeres:
        print '\n' + text + '\n'
        userAnswere = raw_input ('what is the answere for __' + str(index) + '__ : ')
        lives=checkAnswere(userAnswere, correctAnswere, index, lives)
        if lives == 0:
            print '\nGAME OVER'
            return
        text=text.replace('__'+str(index)+'__', userAnswere)
        index+=1
        print 'correct'
    print '\n' + text
    print '\nCongratulations! You won!'

#running code
print '\nHello Player, welcome to the quiz!\n'
runQuiz(selectCategory(),selectDifficulty())
