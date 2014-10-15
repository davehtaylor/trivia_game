# Trivia Game
# 
# This is a trivia game written in Python.
#
# The player is presented with 10 questions, each with mulitple choice answers. 
# A score is kept, awarding 10 points for each correct answer, and the player 
# is given their score at the end of the game. 

score = 0             # Initialize Player's score
questNum = 1          # Initialize variable to show the question number as the game goes on

# The following lists are sets of nested tuples inside the list. Inside a larger tuple, 
# you find three tuples, like this: [ ( (foo), (bar), (baz) ) ]. One is for the question, 
# one is for the multiple choice answers for the quesition and the other is for the answer 
# to the question. The answer references the letter of the correct answer in the multiple 
# choice answers. Here we have 4 lists: generalTriva[], movieTrivia[], musicTrivia[], and 
# eightiesTrivia[]. The user is presented with a menu to decide which category they want 
# to play in. 

generalTrivia = [(("In what city would you find the Eiffel Tower?"), ("a. New York", "b. London", "c. Paris", "d. Amsterdam"), ("c")), 
                 (("What famous document begins: 'When in the course of human events...'?"), ("a. The US Constitution", "b. The US Declaration of Independence", "c. Magna Carta", "d. The Communist Manifesto"), ("b")), 
                 (("Who was the last president of the Soviet Union?"), ("a. Mikail Gorbachev", "b. Nikita Khrushchev", "c. Vladimir Lenin", "d. Joseph Stalin"), ("a")), 
                 (("According to the nursery rhyme, what were Jack and Jill fetching?"), ("a. Milk", "b. Water", "c. Orange Juice", "d. Apple Juice"), ("b")), 
                 (("Which fruit inspired Sir Isaac Newton?"), ("a. Orange", "b. Kiwi", "c. Banana", "d. Apple"), ("d")), 
                 (("What 1975 blockbuster sees Roy Scheider utter: 'We need a bigger boat'?"), ("a. Jaws", "b. Apocalypse Now", "c. Titanic", "d. Das Boot"), ("a")), 
                 (("What movie has Bob Hoskins seething: 'A toon killed my brother'?"), ("a. Space Jam", "b. Toy Story", "c. Who Framed Roger Rabbit?", "d. Cool World"), ("c")), 
                 (("What kind of animal is the emblem of the US Democratic political party?"), ("a. Donkey", "b. Elephant", "c. Wolverine", "d. Honey Badger"), ("a")), 
                 (("What breakfast cereal was Sonny the Cuckoo Bird 'cuckoo for'?"), ("a. Cocoa Puffs", "b. Count Chocula", "c. Coco Pebbles", "d. Kix"), ("a")), 
                 (("John Davidson Rockefeller got rich in what industry?"), ("a. Coal", "b. Oil", "c. Steel", "d. Logging"), ("b"))]

movieTrivia = [(("Which working hours were a hit for Dolly Parton?"), ("a. 10 to 7", "b. 9 to 5", "c. 8 to 4", "d. 6 to 2"), ("b")),
               (("Which plant was Uma Thurman named after in Batman & Robin?"), ("a. Fern", "b. Pothos", "c. Boxwood", "d. Ivy"), ("d")),
               (("Who was Elwood's brother in The Blues Brothers?"), ("a. Jake", "b. Jerry", "c. Jonathan", "d. Jim"), ("a")),
               (("Which Oscar-winning actress played the medium Oda Mae Brown in Ghost?"), ("a. Angela Basset", "b. Oprah Winfrey", "c. Whoopi Goldberg", "d. Pam Grier"), ("c")),
               (("Which star of Three Men and a Baby had appeared in Cheers?"), ("a. Ted Danson", "b. Woody Harrelson", "c. Kelsey Grammer", "d. George Wendt"), ("a")),
               (("In which 1979 film with Bo Derek was the title simply a number?"), ("a. 1942", "b. 10", "c. 21", "d. 300"), ("b")),
               (("In which 80s film did Arnold Schwarzenegger play Danny De Vito's brother?"), ("a. Predator", "b. Commando", "c. The Terminator", "d. Twins"), ("d")),
               (("In the first Pink Panther movie, what is the Pink Panther?"), ("a. Diamond", "b. Cat", "c. Person", "d. Car"), ("a")),
               (("Who  was the voice behind Woody, the cowboy doll in Toy Story?"), ("a. Tim Allen", "b. Don Rickles", "c. Tom Hanks", "d. Wallace Shawn"), ("c")),
               (("What sci-fi thriller set attendance records during the Fourth of July weekend in 1996?"), ("a. Independence Day", "b. The Net", "c. Hackers", "d. Terminator 2"), ("a"))]

musicTrivia = [(("What video, the first to cost over $150,000, helped Michael Jackson's Thriller soar?"), ("a. Thriller", "b. Beat It", "c. Billie Jean", "d. The Girl is Mine"), ("b")),
               (("What did Def Leppard drummer Rick Allen lose in a 1984 auto accident?"), ("a. Wallet", "b. Song Lyrics", "c. Rolex Watch", "d. Arm"), ("d")),
               (("What Kiss star sported the longest tongue in rock?"), ("a. Gene Simmons", "b. Paul Stanley", "c. Ace Freeley", "d. Peter Criss"), ("a")),
               (("Who adorned his last piano with 350 pounds of rhinestones?"), ("a. Elton John", "b. Billy Joel", "c. Liberace", "d. Barry Mantilow"), ("c")),
               (("What sitcom spawned the hit song I'll Be There for You?"), ("a. Seinfeld", "b. Seinfeld", "c. 3rd Rock from the Sun", "d. Friends"), ("d")),
               (("What countdown deejay intones: 'keep your feet to the ground, and keep reaching for the stars'?"), ("a. Casey Kasem", "b. John Tesh", "c. Wolfman Jack", "d. Rick Dees"), ("a")),
               (("Who recorded the album Nevermind?"), ("a. Soundgarden", "b. Pearl Jam", "c. Alice in Chains", "d. Nirvana"), ("d")),
               (("Who had 90s hits with 'You Oughta Know' and 'Ironic'?"), ("a, Liz Phair", "b. Lisa Loeb", "c. Alanis Morissette", "d. Fiona Apple"), ("c")),
               (("In which US state was Elvis Presley's mansion?"), ("a. Tennessee", "b. Mississippi", "c. Kentucky", "d. Alabama"), ("a")),
               (("Who had No 1s with 'Pappa Don't Preach' and 'Open Your Heart'?"), ("a. Tiffany", "b. Madonna", "c. Belinda Carlisle", "d. Debbie Gibson"), ("b"))]

eightiesTrivia = [(("What Peter Gabriel song did John Cusack play in the iconic scene in 'Say Anything'?"), ("a. Big Time", "b. In Your Eyes", "c. Shock the Monkey", "d. Sledgehammer"), ("b")),
                  (("Which Tom starred in the TV hit 'Magnum P.I.'?"), ("a. Hanks", "b. Cruise", "c. Selleck", "d. Arnold"), ("c")),
                  (("What video game saw a round, yellow 'man' attempting to eat ghosts and various fruits?"), ("a. Pac-Man", "b. Pong", "c. Galaga", "d. Centipede"), ("a")),
                  (("What sketch comedy show gave birth to 'The Simpsons'?"), ("a. Saturday Night Live", "b. Kids in the Hall", "c. In Living Color", "d. The Tracey Ullman Show"), ("d")),
                  (("The TV hit 'Knight Rider' featured a talking car named K.I.T.T. What did the initials K.I.T.T. stand for?"), ("a. Knight Industries Two Thousand", "b. Knight Incorporated Two Thousand", "c. Knight Intelligence Two Thousand", "d. Knight Investments Two Thousand"), ("a")),
                  (("Which space shuttle exploded just moments after launching in January of 1986?"), ("a. Atlantis", "b. Challenger", "c. Discovery", "d. Columbia"), ("b")),
                  (("What type of candy did the alien enjoy in film 'E.T.'?"), ("a. M&Ms", "b. Skittles", "c. Reece's Pieces", "d. Mike and Ike"), ("c")),
                  (("What 1982 music video starred a popular singer and a troupe of dancing zombies?"), ("a. Thriller", "b. Bad", "c. Beat It", "d. Man in the Mirror"), ("a")),
                  (("This popular toy was first called Little People:"), ("a. Baby Alive", "b. Cabbage Patch Kids", "c. Barbie", "d. Strawberry Shortcake"), ("b")),
                  (("Which type of car played a major role in the film 'Back to the Future'?"), ("a. Trans Am", "b. Mustang", "c. Jeep", "d. DeLorean"), ("d"))]

print "\n"
print "*****************************************************"          # Pretty title banner when game starts
print "*                                                   *"
print "*                    Trivia Game                    *"
print "*                                                   *"
print "*****************************************************"
print "\n"

print "Welcome to the triva game. You will choose a category, and"     # Game instructions
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

menuChoice = raw_input("Category selection: ")                          # Ask for the user's choice and assign that choice to the menuChoice variable
while menuChoice not in ['1', '2', '3', '4']:                           # Only allow the user to enter '1', '2', '3', or '4'
    print "I'm sorry, I don't understand. Please type the number of the category you would like to play."
    categoryChoice = raw_input("Category selection: ")

if menuChoice == '1':                                                   # Create the variable categoryChoice and assign it the name of the questions list
    categoryChoice = generalTrivia                                      # based on the user's choice from the menu. 
elif menuChoice == '2':
    categoryChoice = movieTrivia
elif menuChoice == '3':
    categoryChoice = musicTrivia
elif menuChoice == '4':
    categoryChoice = eightiesTrivia

print "\n"
print "******************"
print "*                *"
print "*   LET'S PLAY   *"
print "*                *"
print "******************"
print "\n"

for (question, choices, answer) in categoryChoice:                     # Loop through the question list assigned to the categoryChoice variable. Apply the variable names 'question', 'choices', and 'answer' to the tuples.
    print "Question " + str(questNum) + ": "                           # Print out the question
    print question
    print choices[0]                                                   # Print out the choices
    print choices[1]
    print choices[2] 
    print choices[3]
    print "\n"
    response = raw_input("Your answer: ")                              # Get the players response
    while response not in ['a','b','c','d']:                           # Only allow the player to enter 'a', 'b', 'c', or 'd'
        print "I'm sorry, I don't understand. Please type 'a', 'b', 'c', or 'd'."
        response = raw_input("Your answer: ")
    if response != answer:                                             # Test if the player's response matches the answer        
        print "\n\n*** I'm sorry, that's not correct. The correct answer is '" + answer + "'. ***\n\n"    # If the player gets it wrong, tell them so, and then tell them the correct answer
    else:
        print "\n\n*** That's correct! ***\n\n"                        # If their reponse is correct, tell them so
        score += 10                                                    # And if correct, add 10 points to the score. 
    questNum +=1                                                       # Increment the question number

print "\n"
print "*****************************************************"
print "*****************************************************"
print "\n"

if score == 100:                                                       # This is where we tell the player their final score. 
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
