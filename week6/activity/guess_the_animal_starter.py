import pickle

class GuessTheAnimal:
    """
    A simple "Guess the animal" game where a player plays against the computer, which learns
    about animals as it goes along. 
    
    Every time the computer fails to guess the animal, it will
    ask the player what animal they thought of. 
    
    If it needs to distinguish between animals,it will ask for a y/n question
    to make that distinction. At first, the computer doesn't know
    any animals, so it gives up immediately.
    """

    SAVE_GAME_FILENAME = 'guess_the_animal_save_game.bin'

    def __init__(self):
        # Initialise binary tree with an "empty" node
        # Boolean to determine whether the data has changed (for game save purposes)
        # Boolean to determine whether a round was played (for "play again" purposes)


    def init(self):
        """
        Basically reinitialise the game.
        Create the root, set the changed or played booleans to False
        """
        pass


    @staticmethod
    def __input(prompt='> ', yes_no=False):
        """
        A helper function that asks for user input. It allows for a special prompt (the default
        is '> ') and to force the user to answer a yes/no question (yes_no=True). 

        :param prompt: A prompt to show to the user
        :param yes_no: If True, only accepts yes/no answers (yes/Yes/y/Y or no/No/n/N)
        :return: if yes_no is True, return True for yes, False for no, otherwise just return
        the actual response
        """
        while True:
            response = input(prompt)
            if response == '':
                continue

            if yes_no:
                response = response.lower()
                if response[0] == 'y':
                    return True
                elif response[0] == 'n':
                    return False
            else:
                return response

    # A bunch of helper functions for player interaction that are pretty self-explanatory
    def __get_animal():
        print('You win. I give up. What animal were you thinking of?')
        return self.__input()

    def __get_differentiating_question():
        print('What y/n question would you ask to tell the difference between a {0} and a {1}?'.format())
        return self.__input()

    def __get_differentiating_answer():
        print('And what would your answer be for a {0}? (y/n)'.format())
        return self.__input(yes_no=True)

    def __ask_differentiating_question():
        print('{0} (y/n)'.format())
        return self.__input(yes_no=True)

    def __guess_animal(self, animal):
        print('Is it a {0}? (y/n)'.format())
        return self.__input(yes_no=True)

    def __play_again(self):
        print('Do you want to play again? (y/n)')
        return self.__input(yes_no=True)

    # End of helper functions
    def save(self):
        """
        Save game to a file. It dumps the pickled binary tree.
        """
        with open(self.SAVE_GAME_FILENAME, 'wb') as saved_game:
            pickle.dump(self.__root, saved_game)

    def load(self):
        """
        Load game from a file. It loads the pickled binary tree.
        """
        try:
            with open(self.SAVE_GAME_FILENAME, 'rb') as saved_game:
                # Game and tree reloading
                pass
        except FileNotFoundError:
            print('Oops. No saved game found.')

    @staticmethod
    def __update_current_node(current_node, animal, question, answer_is_yes):
        """
        Use the  information to update the current node and connect to the next node/leaf
        Ref: slide 19
        """
        pass
     

    def play_round(self):
        """
        Play a single round. This means asking questions (if any are available) until a leaf node
        is reached starting from the root. Then, the computer will guess, which ends the round.
        """
        self.__has_played_round = True

        # This loops context is from the computers perspective
        has_guessed = False
        while not has_guessed:
            # At this point we need to DFS until we run out of leaves 
            # and need to make some sort of guess
            pass


    def __menu(self):
        """
        Show player menu.
        :return: The selected menu item.
        """
        print('What would you like to do?')
        # if has playedround
        print('   [P] Play again')

        print('   [N] Start a new game')
        print('   [L] Load previously saved game')
        # if tree has changed:
        print('   [S] Save game')

        print('   [Q] Quit game')
        return self.__input().upper()[0]

    def play(self):
        """
        Play rounds until the player quits the game.
        """
        print("+-----------------------------------------+")
        print("|                Animal                   |")
        print("|                                         |")
        print("|               Guessing                  |")
        print("|                                         |")
        print("|                 Game                    |")
        print("+-----------------------------------------+")
        print("")

        while True:
            choice = self.__menu()
            # A new unsaved game
            if choice == 'N':
                self.init()
                self.play_round()
            # Play the game
            elif choice == 'P':
                self.play_round()
            # Load the binary file with our tree
            elif choice == 'L':
                self.load()
            # Save the existing binary tree
            elif choice == 'S':
                self.save()
            # Quit the game
            elif choice == 'Q':
                break

        print("+-----------------------------------------+")
        print('|           Thanks for playing.           |')
        print("+-----------------------------------------+")
