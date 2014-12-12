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

# Import csv in order to read the comma separated value files that hold
# the trivia data.
# Import os in order to read from the current directory to find the csv
# files that contain the question data.

import csv
import os
import sys

# Initialize two variables to start: player score, and the question
# number.

# Initialize a list, csvFiles, to hold all of the names of the csv
# files in the current directory that hold the trivia data.

# Initialize a list, questionList, to hold the Trivia objects created
# from the csv files.

score = 0
questNum = 1
csvFiles = []
questionList = []


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
    """
    strippedName = inputName[:-4]
    secondWord = strippedName.find("Trivia")
    splitWords = strippedName[:secondWord] + " " + strippedName[secondWord:]
    return splitWords


def finalScore(score):
    """Tell the player the final score, with some encouragement
    or admonition.
    """
    if score == 100:
        return "*** Great job! Perfect score! ***"
    elif score >= 80 and score < 100:
        return "*** Not bad!. Your score was: " + str(score) + " ***"
    elif score >= 50 and score < 80:
        return "*** Need more studying. Your score was: " + str(score) + " ***"
    else:
        return "*** Better luck next time. Your score was: " + str(score) + " ***"

# Create the list of csv files

listCSVfiles()

print "\n"
print "************************************************************"
print "*                                                          *"
print "*                       Trivia Game                        *"
print "*                                                          *"
print "************************************************************"
print "\n"

print "Welcome to the triva game. You will choose a category, and"
print "you will be asked 10 questions. Each question is multiple"
print "choice. Enter the letter of the answer you think is correct"
print "For each correct answer, you will receive 10 points."
print "\n"
print "Choose a category:"
print "\n"

# Print out a list of the cateories as a menu for the user to select.
# The menu displays a number and a category name. The number is 
# printed with the counter variable, and the category name is printed
# by taking the names of the csv files and making the file name pretty
# with the makeMenuListing function. The user selects a number that
# corresponds to the category they would like to play.

counter = 1
for csvfile in csvFiles:
    print str(counter) + ". " + makeMenuListing(csvfile)
    counter += 1

print "\n"

# Ask for the user's choice and assign that choice to the
# menuChoice variable.

menuChoice = raw_input("Category selection: ")

print "\n"
print "******************"
print "*                *"
print "*   LET'S PLAY   *"
print "*                *"
print "******************"
print "\n"

# Create the variable categoryChoice by choosing from the csvFiles list
# the menuChoice - 1 (to get the proper index from the list).

categoryChoice = csvFiles[int(menuChoice) - 1]

# Take the categoryChoice and use it to read the selected csv file, and
# instantiate Trivia objects from the file, and append them to the
# questionList.

with open(categoryChoice, 'rb') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(fileReader, None)
    for question, answer, choiceA, choiceB, choiceC, choiceD in fileReader:
        questionList.append(Trivia(question,
                                   answer,
                                   choiceA,
                                   choiceB,
                                   choiceC,
                                   choiceD))

# Print out the questions and multiple choices.

for item in questionList:

    # First, we print out the question number, then the question,
    # followed by the answer 4 choices, presented by the 
    # askQuestion method.

    print "Question " + str(questNum) + ": "
    item.askQuestion()
    print "\n"

    # Next, we ask for the player's response, and only allow them
    # to enter a, b, c, or d.

    response = raw_input("Your answer: ")
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
        score += 10

    # Increment the question number

    questNum += 1

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n"

# This is where we tell the player their final score.

print finalScore(score)

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n\n"
