#include <iostream>
#include <string>   // std::string
#include <sstream>  // std::istringstream
#include <fstream>  // std::ifstream
#include <vector>   // std::vector


// Struct to hold player score
struct Player {
    int score = 0;
};


// Function to take the file needed for the questions, open it, add the
// info to a vector, then close the file. 
//
// Arguments taken: the file to be used as input, and a reference to 
// the vector where the information will be stored.
//
// Returns: no return value. Function will write the file data to a
// vector, questions_and_answers
void get_questions(std::string file, 
                   std::vector< std::vector<std::string> >& 
                   questions_and_answers) {
    
    std::ifstream category_file;
    std::string line;
    std::string tok;

    category_file.open(file, std::ios::in);

    if (category_file.is_open()) {

        while (std::getline(category_file, line)) {

            std::vector<std::string> row;
            std::istringstream iss (line);
            
            while (std::getline(iss, tok, '|')) {
                row.push_back(tok);
            } 

            questions_and_answers.push_back(row);
        }
    } else {
        std::cout << "Error opening data file" << std::endl;
        std::exit(0); 
    }

    category_file.close();
}


// Function to test if the player response is correct.
//
// Arguments taken: a string of the vector element holding the 
// correct answer, and player response. 
//
// Returns: correct or incorrect.
std::string test_response(std::string correct_answer, 
                          std::string player_response) {
    
    if (player_response == "q") {
        std::exit(0);
    } else if (player_response == correct_answer) {
        return "correct";
    } else {
        return "incorrect";
    }

}


// Function to present the questions to the player.
//
// Arguments taken: category data vector, reference to player struct
//
// Returns: no return value
void ask_questions(std::vector< std::vector<std::string> > q_and_a,
                   Player& player) {

    int i = 0;
    int rows = q_and_a.size();
    std::string player_response;
    std::string clear_screen(50, '\n');

    while (i < rows) {
        std::cout << "Current score: " << player.score << std::endl;
        std::cout << std::endl;

        std::cout << q_and_a[i][0] << std::endl;
        std::cout << q_and_a[i][2] << std::endl;
        std::cout << q_and_a[i][3] << std::endl;
        std::cout << q_and_a[i][4] << std::endl;
        std::cout << q_and_a[i][5] << std::endl;

        std::cout << std::endl;

        std::cout << "Response: ";
        std::cin >> player_response;

        if (player_response == "q") {
            std::exit(0);
        } else if (q_and_a[i][1] == player_response) {
            std::cout << "*That's correct!*" << std::endl;
            player.score += 10;
        } else {
            std::cout << "*Sorry, that's incorrect*" << std::endl;
        }

        std::cout << std::endl;
        std::cout << "Press enter to continue" << std::endl;
        std::getchar();
        std::cin.get();
        std::cout << clear_screen;
        i++;
    }
}


// Function to give the player their score and appropriate congratulations
//
// Arguments taken: a reference to the player struct
//
// Return value: No return value, just prints layer score and congratulations
void congrats(Player& player) {

    if (player.score == 100) {
        std::cout << "Congratulations! Perfect score!" << std::endl;
    } else if (player.score >= 80) {
        std::cout << "Great score!" << std::endl;
    } else if (player.score >= 60) {
        std::cout << "Could be better. Maybe next time." << std::endl;
    } else if (player.score >= 50) {
        std::cout << "Might need a bit of studying." << std::endl;
    } else {
        std::cout << "Hit the books and try again later." << std::endl;
    }

    std::cout << std::endl;
}


// MAIN 
int main() {

    struct Player Player1;
    int menu_choice;

    // Variables for the banner and menu borders
    std::string stars(31, '*');
    std::string spaces(10, ' ');
    std::string border(9, '*');
    std::string clear_screen(50, '\n');

    // Multidimensional vector to hold the trivia category data
    // Each row will be the question, correct answer, and answer choices
    // for each question presented to the user.
    std::vector< std::vector<std::string> > questions_and_answers;

    // Clear the screen then print a pretty banner
    std::cout << clear_screen << std::endl;
    std::cout << stars << std::endl;
    std::cout << spaces << "TRIVIA GAME" << spaces << std::endl;
    std::cout << stars << std::endl;
    std::cout << std::endl;

    // Print the main menu
    std::cout << "MAIN MENU" << std::endl;
    std::cout << border << std::endl; 

    std::cout << "1. General Trivia" << std::endl;
    std::cout << "2. Eighties Trivia" << std::endl;
    std::cout << "3. Movie Trivia" << std::endl;
    std::cout << "4. Music Trivia" << std::endl;
    std::cout << "5. Quit" << std::endl;

    std::cout << std::endl;

    std::cout << "Selection: ";

    // Make sure the player can only enter choices presented on the menu.
    // The user will choose the category of trivia they want to play.
    // For each category option, the category questions and answers file
    // will be passed to the get_questions function, along with the vector
    // in which the data will be stored. 
    while (menu_choice < 1 || menu_choice > 5) {

        std::cin >> menu_choice;

        switch (menu_choice) {
            case 1:
                std::cout << std::endl;
                std::cout << "*GENERAL TRIVIA*" << std::endl;
                std::cout << std::endl;
                get_questions("GeneralTrivia.csv", questions_and_answers);
                break;
            case 2:
                std::cout << std::endl;
                std::cout << "*EIGHTIES TRIVIA*" << std::endl;
                std::cout << std::endl;
                get_questions("EightiesTrivia.csv", questions_and_answers);
                break;
            case 3:
                std::cout << std::endl;
                std::cout << "*MOVIE TRIVIA*" << std::endl;
                std::cout << std::endl;
                get_questions("MovieTrivia.csv", questions_and_answers);
                break;
            case 4:
                std::cout << std::endl;
                std::cout << "*MUSIC TRIVIA*" << std::endl;
                std::cout << std::endl;
                get_questions("MusicTrivia.csv", questions_and_answers);
                break;
            case 5:
                std::exit(0);
                break;
            default:
                std::cout << "Sorry, please enter your choice again: ";
        }
    }

    std::cout << "Type 'q' at any time to quit" << std::endl;
    std::cout << std::endl;
    std::cout << "Press enter to continue" << std::endl;
    std::getchar();
    std::cin.get();
    std::cout << clear_screen;

    // Ask the questions
    ask_questions(questions_and_answers, Player1);
    
    // Give the player their score and an appropriate congratulations
    std::cout << "Thanks for playing! " << std::endl;
    std::cout << "Your final score: " << Player1.score << std::endl;
    congrats(Player1);    

    return 0;
}
