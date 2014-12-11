########################################################################
#                                                                      #
#                            Trivia Game                               #
#                                                                      #
########################################################################
#                                                                      #
# This is a trivia game written in Python, and licensed under          #
# the GPLv3. See LICENSE.txt for more information.                     #
#                                                                      #
# The player is presented with 4 categories of trivia to choose from   #
# each with 10 questions, each with mulitple choice answers. Score is  #
# kept, awarding 10 points for each correct answer, and the player is  #
# given their score at the end of the game.                            #
#                                                                      #
########################################################################

# Import csv in order to read the comma separated value files that hold
# the trivia data.

import csv

# Initialize two variables to start: player score, and the question
# number.

score = 0
questNum = 1

# Initialize a list to hold all of the trivia categories, which is
# created by reading all of the csv files in the current directory.

categories = []

for file in os.listdir("."):
    if file.endswith(".csv"):
        categories.append(file)


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

# Read the csv files and instantiate list of objects from the data

with open('generalTrivia.csv', 'rb') as csvfile:
    generalTriviaReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(generalTriviaReader, None)
    for question, answer, choiceA, choiceB, choiceC, choiceD in generalTriviaReader:
        generalTriviaList.append(Trivia(question, answer, choiceA, choiceB, choiceC, choiceD))

with open('movieTrivia.csv', 'rb') as csvfile:
    movieTriviaReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(movieTriviaReader, None)
    for question, answer, choiceA, choiceB, choiceC, choiceD in movieTriviaReader:
        movieTriviaList.append(Trivia(question, answer, choiceA, choiceB, choiceC, choiceD))

with open('musicTrivia.csv', 'rb') as csvfile:
    musicTriviaReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(musicTriviaReader, None)
    for question, answer, choiceA, choiceB, choiceC, choiceD in musicTriviaReader:
        musicTriviaList.append(Trivia(question, answer, choiceA, choiceB, choiceC, choiceD))

with open('eightiesTrivia.csv', 'rb') as csvfile:
    eightiesTriviaReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(eightiesTriviaReader, None)
    for question, answer, choiceA, choiceB, choiceC, choiceD in eightiesTriviaReader:
        eightiesTriviaList.append(Trivia(question, answer, choiceA, choiceB, choiceC, choiceD))

print "\n"
print "*****************************************************"
print "*                                                   *"
print "*                    Trivia Game                    *"
print "*                                                   *"
print "*****************************************************"
print "\n"

print "Welcome to the triva game. You will choose a category, and"
print "you will be asked 10 questions. Each question is multiple"
print "choice. Enter the letter of the answer you think is correct"
print "For each correct answer, you will receive 10 points."
print "\n"
print "Let's get started!"
print "\n"
print "What trivia category do you prefer:"
print "\n"
print "1. General Trivia"
print "2. Movie Trivia"
print "3. Music Trivia"
print "4. 80s Trivia"
print "\n"

# Ask for the user's choice and assign that choice to the
# menuChoice variable.

menuChoice = raw_input("Category selection: ")

# Only allow the user to enter '1', '2', '3', or '4'

while menuChoice not in ['1', '2', '3', '4']:
    print "I'm sorry, I don't understand. Please type the number of the " \
          "category you would like to play."
    menuChoice = raw_input("Category selection: ")

# Create the variable categoryChoice and assign it the name of the
# questions list based on the user's choice from the menu.

if menuChoice == '1':
    categoryChoice = generalTriviaList
elif menuChoice == '2':
    categoryChoice = movieTriviaList
elif menuChoice == '3':
    categoryChoice = musicTriviaList
elif menuChoice == '4':
    categoryChoice = eightiesTriviaList

print "\n"
print "******************"
print "*                *"
print "*   LET'S PLAY   *"
print "*                *"
print "******************"
print "\n"

# Loop through the question list assigned to the categoryChoice
# variable. Apply the variable names 'question', 'choices', and
# 'answer' to the tuples.

for item in categoryChoice:

    # First, we print out the question number, then the question,
    # followed by the answer 4 choices.

    print "Question " + str(questNum) + ": "
    print item.question
    print item.choiceA
    print item.choiceB
    print item.choiceC
    print item.choiceD
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

if score == 100:
    print "*** Great job! Perfect score! ***"
elif score >= 80 and score < 100:
    print "*** Not bad!. Your score was: " + str(score) + " ***"
elif score >= 50 and score < 80:
    print "*** Need more studying. Your score was: " + str(score) + " ***"
else:
    print "*** Better luck next time. Your score was: " + str(score) + " ***"

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n\n"
