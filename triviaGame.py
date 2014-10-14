# Trivia Game
# 
# This is a trivia game written in Python.
#
# The player is presented with 10 questions, each with mulitple choice answers. 
# The questions are presented to the player at random. A score is kept, awarding 
# 10 points for each correct answer, and the player is given their score at the 
# end of the game. 

score = 0

questionsAndAnswers = [(("In what city would you find the Eiffel Tower?"), ("a. New York", "b. London", "c. Paris", "d. Amsterdam"), ("c")),
                       (("What famous document begins: 'When in the course of human events...'?"), ("a. The US Constitution", "b. The US Declaration of Independence", "c. Magna Carta", "d. The Communist Manifesto"), ("b")),
                       (("Who was the last president of the Soviet Union?"), ("a. Mikail Gorbachev", "b. Nikita Khrushchev", "c. Vladimir Lenin", "d. Joseph Stalin"), ("a")),
                       (("According to the nursery rhyme, what were Jack and Jill fetching?"), ("a. Milk", "b. Water", "c. Orange Juice", "d. Apple Juice"), ("b")),
                       (("Which fruit inspired Sir Isaac Newton?", ("a. Orange", "b. Kiwi", "c. Banana" "d. Apple"), ("d")),
                       (("What 1975 blockbuster sees Roy Scheider utter: 'We need a bigger boat'?"), ("a. Jaws", "b. Apocalypse Now", "c. Titanic", "d. Das Boot"), ("a")),
                       (("What movie has Bob Hoskins seething: 'A toon killed my brother'?"), ("a. Space Jam", "b. Toy Story", "c. Who Framed Roger Rabbit?", "d. Cool World"), ("c")),
                       (("What kind of animal is the emblem of the US Democratic political party?"), ("a. Donkey", "b. Elephant", "c. Wolverine", "d. Honey Badger"), ("a")),
                       (("What breakfast cereal was Sonny the Cuckoo Bird 'cuckoo for'?"), ("a. Cocoa Puffs", "b. Count Chocula", "c. Coco Pebbles", "d. Kix"), ("a")),
                       (("John Davidson Rockefeller got rich in what industry?"), ("a. Coal", "b. Oil", "c. Steel", "d. Logging"), ("b"))]

print "\n"
print "*****************************************************"
print "*                                                   *"
print "*                    Trivia Game                    *"
print "*                                                   *"
print "*****************************************************"
print "\n"

print "This is a general triva game. You will be presented with"
print "10 questions. Each question is multiple choice. Enter the"
print "letter of the answer you think is correct. For each correct"
print "answer, will receive 10 points."
print "\n"
print "Let's get started!"
print "\n"

for (question, choices, answer) in questionsAndAnswers:
    random.choice(questionsAndAnswers)
    print question
    print choices[0] "\t" choices[1]
    print choices[2] "\t" choices[3]
    response = raw_input("Your answer:  ")
    if response != answer:
        print "I'm sorry, that's not correct. The correct answer is '" + answer + "'.\n\n"
    else:
        print "That's correct!\n\n"
        score += 10
