"""

Author:         Silvana Cardenas Rico
Date:           April 23, 2024
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    01

"""
#palmetto cluster

#________________________________________________________________________________________________________
# import random
# # Open the file in read mode
# with open('file_name.txt', 'r') as file:
#     # Iterate over each line in the file
#     for line in file:
#         # Split the line by the semicolon
#         question, answer = line.strip().split(';')
        
#         # Print the question and answer
#         print("Question:", question)
#         print("Answer:", answer)
#         print() # Add an empty line for better readability




# import random

# # Open the file in read mode
# with open('file_name.txt', 'r') as file:
#     # Read all lines from the file
#     lines = file.readlines()

# # Shuffle the lines randomly
# random.shuffle(lines)

# # Iterate over each line and print a random question-answer pair
# for line in lines:
#     # Split the line by the semicolon
#     question, answer = line.strip().split(';')
    
#     # Print the question and answer
#     print("Question:", question)
#     print("Answer:", answer)
#     print() # Add an empty line for better readability
    
#     # Break the loop after printing one question-answer pair
#     break





import random

class QuestionAnswerPair:
    def __init__(self, file_path):
        self.file_path = file_path
        self.question_answer_pairs = []
        self.load_pairs()

    def load_pairs(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    question, answer = parts
                    self.question_answer_pairs.append((question, answer))
                else:
                    print(f"{line.strip()}")

    def get_random_pair(self):
        if not self.question_answer_pairs:
            return None
        random_pair = random.choice(self.question_answer_pairs)
        return random_pair

# Example usage
# qa_pair = QuestionAnswerPair('file_name.txt')
# random_pair = qa_pair.get_random_pair()
# if random_pair:
#     question, answer = random_pair
#     # print("Question:", question)
#     # print("Answer:", answer)
# else:
#     print("No question-answer pairs found in the file.")


# m = Map()
# m.choose_question(file_name)

# class Map:
#     #m: Map = Map()
#     def __init__(self):
#         pass

#     def choose_question(self, filename: str) -> list:
#         with open(filename, 'r') as file:
#             lines = file.readlines()#.strip()
#             #random_line = random.choice(lines).strip() 
#             random_line = random.choice(lines).strip() 
#             random_line.split(';')
#             random_str: list = choose_question("file_name.txt")
#         return random_str
#         #return random_line.split(";")

# # m: Map = Map()
# # random_str: list = m.choose_question("file_name.txt")
# # print(random_str)

# # file_name = 'file_name.txt'
# # question, answer = m.choose_question(file_name)
# # print("Question:", question)
# # print("Answer:", answer)


# introduction to the game 
class Game:
    def intro(self):
        print("\tWelcome to the Saw-themed RPG game!")
        print("___________________________________________________________________________________")
        print()
        print("You wake up in the kitchen room of a house you've never seen, unsure of how you got there.")
        print("Everything is closed, not a single way outside")
        print("Your only clue is a note on the table in front of you.")

#_______________________________________________
# first selection of questions at the start of the game (in the kitchen)
class Selections:
    def kitchen_options(action):
        print("\nWhat do you want to do?")
        print("1. Read the note")
        print("2. Try to open the door")
        print("Enter the number of the action:")
        action = int(input().strip())
        return action 
    
    def master_options(action):
        print("You are now in the Master Room")
        print("\nWhat do you want to do?")
        print("1. Read the note")
        print("2. Try to open the door")
        print("Enter the number of the action:")
        action = int(input().strip())
        return action
    
    def living_room_options(action):
        print("You are now in the Living Room")
        print("\nWhat do you want to do?")
        print("1. Read the note")
        print("2. Try to open the door")
        print("Enter the number of the action:")
        action = int(input().strip())
        return action

#_______________________________________________
# prints out the questions from the file and return the answer to the questions
class Questions:

    # qa_pair = QuestionAnswerPair('file_name.txt')
    # random_pair = qa_pair.get_random_pair()
    # if random_pair:
    #     question, answer = random_pair

    def kitchen_questions(self, random_pair):
        print("\nThe note reads: You will have to play the Word Riddle Game before going to the next room.")
        print("'To escape, you must solve a series of games in each room.'" )
        print("It's signed, 'Jigsaw'")
        qa_pair = QuestionAnswerPair('file_name.txt')
        random_pair = qa_pair.get_random_pair()
        if random_pair:
            question, answer = random_pair
        #print(f"\nBelow the message is a riddle: {m.random_line.split(';')[0]}") # how to separate the question with the answer
        print(f"\nBelow the message is a riddle: {question}")
        
        print("Enter your answer:")
        your_answer = input().lower().strip()
        return your_answer, answer
        
    def master_questions():
        print(f"\nBelow the message is a riddle: {question}")
        print("Enter your answer:")
        answer = input().lower().strip()
#_______________________________________________

# contains the object the player will interact when they reach the last room
# class Objects():
    # def keys():
    
    # def lever():
#_______________________________________________

# contains the answers to the question from the file
class Answers:
    fingers = 5

    def riddle_answer(fingers, your_answer, answer):
        if your_answer == answer:
            print("Correct! You hear a click as the door unlocks, you move on to the next room.")
            return True

        else:
            print("Incorrect. You loose a finger.")
            fingers -= 1
            return False, fingers

    # def qa_answer():

#_______________________________________________

# main where everything is print out
def main():
    random_line = random.randint(0, 7)
    tries = 5
    question = Questions()
    select = Selections()
    game = Game()
    ans = Answers
    qa_pair = QuestionAnswerPair('file_name.txt')
    # m: Map = Map()

# prints out the introduction to the game 
    game.intro()
    # m.choose_question(filename)
    fingers = 5
    room_locked = True
    while room_locked:
        action = select.kitchen_options()

        if action == 1:
            qa_pair.load_pairs()
            random_pair = qa_pair.get_random_pair()
            question.kitchen_questions(random_pair)
            ####
            ans.riddle_answer(fingers, your_answer, answer)

        elif action == 2:
            # if "key" in globals():
            #     open_door()
            #     room_locked = False

            # else:

            print("\nThe door is locked, you won't be able to get out until you solve the riddle.")
            question.kitchen_questions(random_str)

        else:
            print("Invalid choice. Please enter a number.")
            action = input()

if __name__ == "__main__":
    main()