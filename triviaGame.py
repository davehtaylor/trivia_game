########################################################################
#                                                                      #
#                            Trivia Game                               #
#                                                                      #
########################################################################
#                                                                      #
# This is a trivia game written in Python, and licensed under          #
# the GPLv3. See LICENSE.txt for more information.                     #
#                                                                      #
# The player is presented with different categories of trivia to       #
# choose from, each displaying 10 questions with mulitple choice       #
# answers. Score is kept, awarding 10 points for each correct answer,  #
# and the player is given their score at the end of the game.          #
#                                                                      #
########################################################################

# Import csv in order to use csv.reader to read the comma separated
# value files that hold the trivia data.

# Import os in order to use os.listdir to read from the current
# directory to find the csv files that contain the question data, and
# to use the os.system command to clear the screen. 

import csv
import os

# Initialize two variables to start: player score, and the question
# number.

# Initialize a list, csvFiles, to hold all of the names of the csv
# files in the current directory that hold the trivia data.

# Initialize a list, questionList, to hold the Trivia objects created
# from the csv files.

questNum = 1
csvFiles = []
questionList = []


class Player:
    """A class to create a player object, in order to hold the player's
    category choice, score, and response the player is given regarding
    their final score, 

    The category choice is printed out while the questions are being
    asked, so the player can always see the current category.The
    makeMenuListing function is used to format the output, just as
    it is when the game menu is displayed, so the category choice is
    readble.

    The score is tallied as the game goes, based on the player's
    responses, and printed out at the end to show the player's final
    score.

    The scoreResponse is initialized as an empty
    string. The finalScore function will define it later on.
    """

    def __init__(self, categoryChoice, score, scoreResponse = ""):
        self.categoryChoice = makeMenuListing(categoryChoice)
        self.score = score
        self.scoreResponse = scoreResponse


class Trivia:
    """A class to create objects from the trivia data in the csv files.
    Take in the question, the answer, and four multiple choice answers.
    """

    def __init__(self, question, answer, choiceA, choiceB, choiceC, choiceD):
        self.question = question
        self.answer = answer
        self.choiceA = choiceA
        self.choiceB = choiceB
        self.choiceC = choiceC
        self.choiceD = choiceD

    def askQuestion(self):
        print self.question
        print self.choiceA
        print self.choiceB
        print self.choiceC
        print self.choiceD
       

def listCSVfiles():
    """Create a list to hold all of the names of the csv files to in
    the current directory.
    """
    for file in os.listdir("."):
        if file.endswith(".csv"):
            csvFiles.append(file)


def makeMenuListing(inputName):
    """Take the name of the csv file that holds the question data, and
    make it pretty for the user category selection menu. The csv
    filenames follow the form "CategoryTrivia.csv". This function takes
    the name, removes the file extension, inserts a space between the
    category name and the word "Trivia". So that instead of
    "CategoryTrivia.csv", in the menu you see "Category Trivia".

    This is also used in the Player class to display the current
    category to the player during the game. 
    """
    strippedName = inputName[:-4]
    secondWord = strippedName.find("Trivia")
    splitWords = strippedName[:secondWord] + " " + strippedName[secondWord:]
    return splitWords


def printPlayerMenu():
    """Prints out the menu that they player is presented with when
    they first launch the game. The menu displays a number and a
    category name. The number is  printed with the counter variable,
    and the category name is printed by taking the names of the csv
    files and making the file name pretty with the makeMenuListing
    function. The user selects a number that corresponds to the
    category they would like to play.
    """
    counter = 1
    for csvfile in csvFiles:
        print str(counter) + ". " + makeMenuListing(csvfile)
        counter += 1
    print "\n"


def instantiateQuestionObjects(categoryChoice):
    """Take the categoryChoice and use it to read the selected csv file,
    and instantiate Trivia objects from the file, and append them to the
    questionList. 
    """
    with open(categoryChoice, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)
        for question, answer, choiceA, choiceB, choiceC, choiceD in reader:
            questionList.append(Trivia(question,
                                       answer,
                                       choiceA,
                                       choiceB,
                                       choiceC,
                                       choiceD))


def testPlayerResponse(response):
    """Test the player's response to see if it's correct."""

    # Only allow the user to repsond with a, b, c, or d.

    while response not in ['a', 'b', 'c', 'd']:
            print "I'm sorry, I don't understand. " \
                  "Please type 'a', 'b', 'c', or 'd'."
            response = raw_input("Your answer: ")

    # Test if the player's response is the correct answer. If not, tell
    # them the correct answer. If correct, add 10 points to their score.

    if response != item.answer:
        print "\n\n*** I'm sorry, that's not correct. " \
              "The correct answer is '" + item.answer + "'. ***\n\n"
    else:
        print "\n\n*** That's correct! ***\n\n"
        player.score += 10


def printSeparator():
    """Print out a pretty separator around the final score.
    """
    print "\n"
    print "*****************************************************"
    print "*****************************************************"
    print "\n"


def finalScore(score):
    """Tell the player the final score, with some encouragement
    or admonition.
    """
    if score == 100:
        player.scoreResponse = "*** Great job! Perfect score! ***"
    elif score >= 80 and score < 100:
        player.scoreResponse = "*** Not bad!. Your score was: " + str(score) + " ***"
    elif score >= 50 and score < 80:
        player.scoreResposne = "*** Need more studying. Your score was: " + str(score) + " ***"
    else:
        player.scoreResponse = "*** Better luck next time. Your score was: " + str(score) + " ***"

    return player.scoreResponse

# Create the list of csv files

listCSVfiles()

# Clear the screen to get started

os.system('clear')

print "\n"
print "************************************************************"
print "*                                                          *"
print "*                       Trivia Game                        *"
print "*                                                          *"
print "************************************************************"
print "\n"

print "Choose a category. Each category will present 10 questions."
print "Each correct answer will receive 10 points."
print "\n"
print "Choose a category:"
print "\n"

# Print out the player menu with the printPlayerMenu funtion

printPlayerMenu()

# Ask for the user's choice and assign that choice to the
# menuChoice variable.

menuChoice = raw_input("Category selection: ")

# Create the variable categoryChoice by choosing from the csvFiles list
# the menuChoice - 1 (to get the proper index from the list).

categoryChoice = csvFiles[int(menuChoice) - 1]

# Take the categoryChoice and use it to read the selected csv file, and
# instantiate Trivia objects from the file, and append them to the
# questionList.

instantiateQuestionObjects(categoryChoice)

# Initialize the player object. Give it the category choice, and 
# start the score off at 0.

player = Player(categoryChoice, score = 0)

# Clear the screen to begin the questions

os.system('clear')

# Print out the questions and multiple choices.

for item in questionList:

    # First, we print out the question number, then the question,
    # followed by the answer 4 choices, presented by the 
    # askQuestion method.

    print "Category: " + player.categoryChoice
    print "\n"
    print "Question " + str(questNum) + ": "
    item.askQuestion()
    print "\n"

    # Next, ask for the player's response, and use the 
    # testPlayerResponse to check if the answer is correct.

    response = raw_input("Your answer: ")

    # Check the player's response

    testPlayerResponse(response)

    # Pause so the player can see if their answer was
    # correct. 

    raw_input("Press enter to continue...")

    # Increment the question number

    questNum += 1
    
    # Clear the screen for the next question

    os.system('clear')

# This is where we tell the player their final score.

printSeparator()

print finalScore(player.score)

printSeparator()
