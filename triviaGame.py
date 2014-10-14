# Trivia Game
# 
# This is a trivia game written in Python.
#
# The player is presented with 10 questions, each with mulitple choice answers. 
# The questions are presented to the player at random. A score is kept, awarding 
# 10 points for each correct answer, and the player is given their score at the 
# end of the game. 

import random                                                                                   # Import random so we can choose from the questionsAndAnswers[] list at random

score = 0                                                                                       # Initialize Player's score
questNum = 1                                                                                    # Initialize variable to show the question number as the game goes on

questionsAndAnswers = [(("In what city would you find the Eiffel Tower?"), ("a. New York", "b. London", "c. Paris", "d. Amsterdam"), ("c")), 
                       (("What famous document begins: 'When in the course of human events...'?"), ("a. The US Constitution", "b. The US Declaration of Independence", "c. Magna Carta", "d. The Communist Manifesto"), ("b")), 
                       (("Who was the last president of the Soviet Union?"), ("a. Mikail Gorbachev", "b. Nikita Khrushchev", "c. Vladimir Lenin", "d. Joseph Stalin"), ("a")), 
                       (("According to the nursery rhyme, what were Jack and Jill fetching?"), ("a. Milk", "b. Water", "c. Orange Juice", "d. Apple Juice"), ("b")), 
                       (("Which fruit inspired Sir Isaac Newton?"), ("a. Orange", "b. Kiwi", "c. Banana", "d. Apple"), ("d")), 
                       (("What 1975 blockbuster sees Roy Scheider utter: 'We need a bigger boat'?"), ("a. Jaws", "b. Apocalypse Now", "c. Titanic", "d. Das Boot"), ("a")), 
                       (("What movie has Bob Hoskins seething: 'A toon killed my brother'?"), ("a. Space Jam", "b. Toy Story", "c. Who Framed Roger Rabbit?", "d. Cool World"), ("c")), 
                       (("What kind of animal is the emblem of the US Democratic political party?"), ("a. Donkey", "b. Elephant", "c. Wolverine", "d. Honey Badger"), ("a")), 
                       (("What breakfast cereal was Sonny the Cuckoo Bird 'cuckoo for'?"), ("a. Cocoa Puffs", "b. Count Chocula", "c. Coco Pebbles", "d. Kix"), ("a")), 
                       (("John Davidson Rockefeller got rich in what industry?"), ("a. Coal", "b. Oil", "c. Steel", "d. Logging"), ("b"))]

# The questionsAndAnswers[] list is sets of nested tuples inside the list. Inside a larger tuple, you find three tuples. One is for the question, one is for the multiple choice answers for the quesition
# and the other is for the answer to the question. The answer references the letter of the correct answer in the multiple choice answers.

print "\n"
print "*****************************************************"                                   # Pretty title banner when game starts
print "*                                                   *"
print "*                    Trivia Game                    *"
print "*                                                   *"
print "*****************************************************"
print "\n"

print "This is a general triva game. You will be presented with"                                # Game instructions
print "10 questions. Each question is multiple choice. Enter the"
print "letter of the answer you think is correct. For each correct"
print "answer, will receive 10 points."
print "\n"
print "Let's get started!"
print "\n"

for (question, choices, answer) in questionsAndAnswers:                                         # Loop through the questionsAndAnswers[] list. Apply the variable names 'question', 'choices', and 'answer' to the tuples.
    random.choice(questionsAndAnswers)                                                          # Choose a question set at random
    print "Question " + str(questNum) + ": "                                                    # Print out the question
    print question
    print choices[0]                                                                            # Print out the choices
    print choices[1]
    print choices[2] 
    print choices[3]
    print "\n"
    response = raw_input("Your answer: ")                                                       # Get the players response
    if response != answer:                                                                      # Test if the player's response matches the answer        
        print "\n\n*** I'm sorry, that's not correct. The correct answer is '" + answer + "'. ***\n\n"    # If the player gets it wrong, tell them so, and then tell them the correct answer
    else:
        print "\n\n*** That's correct! ***\n\n"                                                   # If their reponse is correct, tell them so
        score += 10                                                                             # Also, if it were correct, add 10 points to their score. And then the loop continues going to the next question.
    questNum +=1                                                                                # Increment the question number

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n"

if score == 100:                                                                                # This is where we tell the player their final score. 
    print "*** Great job! Perfect score! ***"
elif score >= 80 and score < 100:
    print "*** Not bad!. Your score was: " + str(score) + " ***"
elif score >=50 and score < 80:
    print "*** Need to do some studying. Your score was: " + str(score) + " ***"
else:
    print "*** Better luck next time. Your score was: " + str(score) + " ***"

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n\n"
