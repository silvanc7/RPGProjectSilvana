"""

Author:         Silvana Cardenas Rico
Date:           April 30, 2024
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    Section 01

CODE DESCRIPTION: The user will be kidnapped by jigsaw, they will wake up in a unfamiliar house. This program will make the user follow jigsaw's game with 
randomized riddle question from the file_name.txt. The user will have 5 tries on each riddle question found in each room. Once the user solves each riddle 
question without using all the tries they will be free to go, however if the user uses up all their tries in one riddle they will be killed by jigsaw. The
user will have two outcomes, to come out alive or be trapped in the house forever.

"""

import random

class QuestionAnswerPair():

    def __init__(self, file_path):
        """
        A class that manages a collection of question-answer pairs loaded from a file.

        Attributes:
            file_path (str): The file path where the question-answer pairs are stored.
            question_answer_pairs (list): A list of tuples, where each tuple contains a question and its corresponding answer.
        """
        self.file_path = file_path
        self.question_answer_pairs = []
        self.load_pairs()

    # opens the file 'file_name.txt'
    def load_pairs(self):
        """
        Loads the question-answer pairs from the file and stores them in the `question_answer_pairs` list.

        The file is expected to have one question-answer pair per line, separated by a semicolon (;).

        """
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split(';')
                
                # separates the question and the answer
                if len(parts) == 2:
                    question, answer = parts
                    self.question_answer_pairs.append((question, answer))

                else:
                    print(f"{line.strip()}")

    # generates random questions for the riddles
    def get_random_pair(self):
        """
        Returns a random question-answer pair from the `question_answer_pairs` list.

        Returns:
            tuple or None: A tuple containing a random question and its corresponding answer, or None if the list is empty.
        """
        if not self.question_answer_pairs:
            return None

        random_pair = random.choice(self.question_answer_pairs)

        return random_pair

# introduction to the game 
class Game():
    def intro(self):
        print("\n\n\t\tWelcome to the Saw-themed RPG game!")
        print("_______________________________________________________________________")
        print()
        print("You wake up in the kitchen room of a house you've never seen, unsure of how you got there.")
        print("Everything is closed, not a single way outside.")
        print("Your only clue is a note on the table in front of you.")

class Room():
    def __init__(self, room_type):
        """
        Initializes the Room object with the specified room type.

        Args:
            room_type (str): The type of the room.
        """
        self.room_type = room_type

class Selections(Room):

    # prints an introduction message based on the current room type
    def room_intro(self):
        if self.room_type == "kitchen":
            pass

        elif self.room_type == "master":
            print('_______________________________________________')
            print("\nYou are in the Master Room")
            print("There is another note.")
            
        elif self.room_type == "living":
            print('_______________________________________________')
            print("\nYou are in the Living Room")
            print("There is another note.")

    # prints the available options for the user to choose from
    def print_options(self):
        self.room_intro()
        print("\nWhat do you want to do?")
        print("1. Read the note")
        print("2. Try to open the door")
        print("Enter the number of the action:")

    # prompts the user to enter an action and validates the input.
    def get_user_action(self):

        action = input().strip()

        # validates that the user input
        while action not in ['1','2']:
            print("Invalid option. Please enter a number: ")
            action = input().strip()

        # returns the user's selected action (1 or 2).
        return int(action)

class Questions():

    # handles the game's starting plot in the kitchen room.
    def kitchen_questions(self, random_pair, your_answer, answer):
        print("\nThe note reads: \n\n\t\t\t'You will have to play the Word Riddle Game in each room.'")
        print(f"\t\t\t'To escape, you must solve all the riddles in each room.'" )
        print("\t\t\t'However you will only have 5 tries for each room.'")
        print("'Each error will bring you closer to Jigsaw... so think carefully before answering, or else you could die.'")
        print("It's signed, 'Jigsaw'")

        # retrieves a random question answer pair from the file
        qa_pair = QuestionAnswerPair('file_name.txt')
        random_pair = qa_pair.get_random_pair()

        if random_pair:
            question, answer = random_pair

        # prints the riddle question 
        print(f"\nBelow the message is a riddle: {question}")
        print("Enter your answer:")
        your_answer = input().lower().strip()

        # returns the user's answer and correct answer
        return your_answer, answer

    # handles the game's question in the master room.
    def master_questions(self, random_pair, your_answer, answer):

        # retrieves a random question answer pair from the file
        qa_pair = QuestionAnswerPair('file_name.txt')
        random_pair = qa_pair.get_random_pair()

        if random_pair:
            question, answer = random_pair

        # prints the riddle question 
        print(f"\nBelow the message is a riddle: {question}")
        print("Enter your answer:")
        your_answer = input().lower().strip()

        # returns the user's answer and correct answer
        return your_answer, answer

    # contains the riddle question for when the user gets to the living room
    def living_room_questions(self, random_pair, your_answer, answer):

        # retrieves a random question answer pair from the file
        qa_pair = QuestionAnswerPair('file_name.txt')
        random_pair = qa_pair.get_random_pair()

        if random_pair:
            question, answer = random_pair

        # prints the riddle question 
        print(f"\nBelow the message is a riddle: {question}")
        print("Enter your answer:")
        your_answer = input().lower().strip()

        # returns the user's answer and correct answer
        return your_answer, answer
        
class Answers():

    # checks the user's answer to a riddle and manages the number of tries.
    def riddle_answer(tries, your_answer, answer):

        # checks if the user's answer is correct
        while your_answer != answer:

            # if the answer is incorrect, subtract the number of tries left
            tries -= 1
            print("\nIncorrect.")

            # if the tries is 0, the user dies and the game ends.
            if tries == 0:
                print("You lost all your tries, Jigsaw comes out of the door with a knife.\nHe stabs you, you bled out.\nYou died from hemorrhage.\nJigsaw won.\n")
                print("Do you want to play again?(Yes or No)")
                play_again = input().lower().strip()

                # validate the user's input for playing again
                while play_again not in ['yes', 'no']:
                    print('Please enter Yes or No')
                    play_again = input().lower().strip()

                # if the user wants to play again, call the main function
                if play_again == 'yes':
                    main()

                # if the user doesn't want to play again, exit the program
                elif play_again == 'no':
                    exit()

            # if the user has tries left, inform them of the remaining tries
            else:
                if tries == 1:
                    print(f'You got {tries} try left out of 5.')

                else:
                    print(f'You got {tries} tries left out of 5.')

                print('Try again:')
                your_answer = input().lower().strip()
        
        # if the user's answer is correct, the following will print and will continue to the next room
        print()
        print("Correct! You hear a click as the door unlocks, you move on to the next room.")
        print()

        # return the updated number of tries
        return tries

def main():

    # initialize variables
    random_line = random.randint(0, 15)
    your_answer = ""
    answer = ""

    # creating instances of the classes
    question = Questions()
    game = Game()
    ans = Answers
    qa_pair = QuestionAnswerPair('file_name.txt')

    # prints the introduction to the game 
    game.intro()

    # initial game state
    tries = 5
    room_locked = True

    while room_locked:

        # user enters the kitchen room
        kitchen_room_selections = Selections("kitchen")
        kitchen_room_selections.print_options()
        action = kitchen_room_selections.get_user_action()

        if action == 1:
            qa_pair.load_pairs()
            random_pair = qa_pair.get_random_pair()
            your_answer, answer = question.kitchen_questions(random_pair, your_answer, answer)
            ans.riddle_answer(tries, your_answer, answer)

            while True:

            # user enters the master room
                master_room_selections = Selections("master") 
                master_room_selections.print_options()
                action = master_room_selections.get_user_action()

                if action == 1:
                    qa_pair.load_pairs()
                    random_pair = qa_pair.get_random_pair()
                    your_answer, answer = question.master_questions(random_pair, your_answer, answer)
                    ans.riddle_answer(tries, your_answer, answer)
                    
                    while True:

                        # user enters the living room
                        living_room_selections = Selections("living")
                        living_room_selections.print_options()
                        action = living_room_selections.get_user_action()

                        if action == 1:
                            qa_pair.load_pairs()
                            random_pair = qa_pair.get_random_pair()
                            your_answer, answer = question.living_room_questions(random_pair, your_answer, answer)
                            ans.riddle_answer(tries, your_answer, answer)

                            # prints out the end/outcome of the game
                            print("\nCongrats!")
                            print("You made it out of the House!")
                            print("You made Jigsaw mad, he will come for you again in the future")
                            print()
                            print("6 days since your kidnapping")
                            print("Time passed since your kidnapping from Jigsaw, you are now back to your daily life")
                            print("You see in the news that another person was also missing during the same timeline as you.")
                            print("The police found the body of the missing person in an abandoned house.")
                            print("It's the same house you escaped...")
                            print()
                            print("Do you want to play again?(Yes or No)")
                            play_again = input().lower().strip()

                            while play_again not in ['yes', 'no']:
                                print('Please enter Yes or No')
                                play_again = input().lower().strip()

                            # if the user wants to play again, call the main function
                            if play_again == 'yes':
                                main()

                            # if the user doesn't want to play again, exit the program
                            elif play_again == 'no':
                                exit()

                        # the following will print and take the use back to the starting menu
                        elif action == 2:
                            print("\nThe door is locked, you won't be able to get out until you solve the riddle.")
                            continue

                elif action == 2:
                    print("\nThe door is locked, you won't be able to get out until you solve the riddle.")
                    continue

        elif action == 2:
            print("\nThe door is locked, you won't be able to get out until you solve the riddle.")
            continue

if __name__ == "__main__":
    main()