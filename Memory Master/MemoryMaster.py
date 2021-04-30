from tkinter import * # IMPORT ALL TKINTER FUNCITONALITIES AND WIDGETS
from tkinter import messagebox
import random # For random integers
from time import sleep # for sleeping

# GLOBAL VARIABLES AND CONFIGURATIONS
    # MAIN SCREEN
DIMENSIONS_MAIN_SCREEN = "1000x800"
WIDTH_MAIN_SCREEN = 1000
HEIGHT_MAIN_SCREEN = 800
root = None  # MASTER WINDOWS, THE MAIN WINDOW
    # MEMORY MASTER LABEL
nameOfTheGameLabel = None
    # START GAME
theStartButton = None
TEXT_START_GAME = "Start the Game!"
WIDTH_START_BUTTON = 300
HEIGHT_START_BUTTON = 150
    # GAME SCREEN
WIDTH_GAME_SCREEN = 920
HEIGHT_GAME_SCREEN = 500
gameScreenFrame = None  # GAME SCREEN FRAME itself
RANDOM_NUMBERS_PADDING = 50
CONGRATS_MESSAGE = "You were RIGHT! Congratulations:)"
MESSAGE_YOU_ARE_WRONG = "You've failed :("
QUESTION_PLAY_AGAIN = "Do you want to play again ?"

    # USER INPUT SCREEN
userInputScreen = None
WIDTH_USER_INPUT = 520
HEIGHT_USER_INPUT = 120
userEntryBox: Entry # The input the user has entered
tryButton = None # The TRY button to check game
TEXT_TRY = "Try"
    # GAME LOGIC
randomlyGeneratedNumbers = [] # randomly generated numbers will be stored in here
givenNumbersFromUser = [] # the numbers user gave us will be stored here
    # COLORS
YELLOW = "yellow"
NAVY_BLUE = "navy blue"
WHITE = "white"
    # FONTS
MEDIUM = 20
BIG = 28
FONT_COMIC_SANS_MEDIUM = ("Comic Sans MS", MEDIUM)
FONT_COMIC_SANS_BIG = ("Comic Sans MS", BIG)

    # INFORMATION
NAME_OF_THE_GAME = "Memory Master"
    # CONFIGURATIONS
SEED_THE_RANDOM = 1 # this will seed the random number generator
GAME_LEVEL = 1 # How many numbers to generate?




def InitializeGameScreen():
    # This function will initialize Game Screen once start button is pressed
    # INITIALIZE GAME SCREEN
        # NAME OF THE GAME WILL APPEAR ON THE SCREEN 
    nameOfTheGameLabel = Label(root, 
                                text  = NAME_OF_THE_GAME,
                                fg = NAVY_BLUE,
                                bg = YELLOW,
                                font = 30 )
    nameOfTheGameLabel.configure(font=("Comic Sans MS", 39))
    nameOfTheGameLabel.grid(row=0, column=0, padx = 40, pady = 20)

     # RENDER Game Screen 
    gameScreenFrame = LabelFrame(root, text = "Game Screen", 
                                        width = WIDTH_GAME_SCREEN, 
                                        height = HEIGHT_GAME_SCREEN, 
                                        font= FONT_COMIC_SANS_MEDIUM)
    gameScreenFrame.configure(bg = YELLOW) # Background color
    gameScreenFrame.configure(fg = NAVY_BLUE) # Color of the title
    gameScreenFrame.grid(row=1, column=0, padx = 40, pady = 10)

     # RENDER User Input Screen
    userInputScreen = LabelFrame(root, 
                                text = "User Input",
                                width = WIDTH_USER_INPUT,
                                height = HEIGHT_USER_INPUT,
                                bg = YELLOW,
                                fg = NAVY_BLUE,
                                font = FONT_COMIC_SANS_MEDIUM)
    userInputScreen.grid(row = 2, column = 0, padx = 5, pady = 5)
    
    # Render Entry Box
    
    userEntryBox = Entry(userInputScreen,
                        bd = 3,
                        bg = YELLOW,
                        fg = NAVY_BLUE,
                        font = FONT_COMIC_SANS_MEDIUM)
    tryButton = Button(userInputScreen,
                        text = TEXT_TRY,
                        bg = NAVY_BLUE,
                        fg = WHITE,
                        font = FONT_COMIC_SANS_MEDIUM)

    userEntryBox.pack() # Pack this editText feature into the user input area
    tryButton.pack() # Pack this button into the user input area

    def controlTheGame():
    # The function will control whether
    # the user has guessed correctly or not
        theInputText = userEntryBox.get() # get the text in the edit text box
        
        givenNumbersFromUserAsCharacters = theInputText.split(" ") # split the string based on " "
        # convert string or characters to integers
        for Element in givenNumbersFromUserAsCharacters:
            global givenNumbersFromUser
            givenNumbersFromUser.append(int(Element))
        
        # NOW COMPARISON
        FLAG_SAME = True # assume that they are the same
        
        global randomlyGeneratedNumbers
        for index in range(0, len(randomlyGeneratedNumbers)):
            if(givenNumbersFromUser[index] == randomlyGeneratedNumbers[index]):
                continue
            else:
                FLAG_SAME = FALSE
                break
        
        if(FLAG_SAME):
            # If the user has entered the right numbers
            messagebox.showinfo("Level Up", CONGRATS_MESSAGE)
            # Refresh the seeds
            global SEED_THE_RANDOM
            SEED_THE_RANDOM = 1

            # Level Up
            global GAME_LEVEL
            GAME_LEVEL += 1

            # Remove the lists
            randomlyGeneratedNumbers = []
            givenNumbersFromUser = []

            # Call InitializeGameScreen function again
            startGameSession() # New Game

        else:
            # If the user was wrong
            # First ask whether he/she would play again or not
            theResponse = messagebox.askquestion(MESSAGE_YOU_ARE_WRONG, QUESTION_PLAY_AGAIN)
            if(theResponse == "yes"):
                # Refresh LEVEL and Numbers Information
                GAME_LEVEL = 1

                #global givenNumbersFromUser
                givenNumbersFromUser = []

                #global randomlyGeneratedNumbers
                randomlyGeneratedNumbers = []


                startGameSession() # New Game
            else:
                global root
                root.destroy() # Release memory allocated for GUI Components
                exit()


    tryButton.configure(command = controlTheGame) # When clicked perform control game action


def startGameSession():
    # This function will start each game session
    InitializeGameScreen()

    # First generate Random Numbers for Game
    for aNumber in range(GAME_LEVEL):
        oneTimeRandomNumber = random.randint(0, 9) # generate numbers between 0 - 10 included
        randomlyGeneratedNumbers.append(oneTimeRandomNumber)
        # Seed the random number generator
        global SEED_THE_RANDOM
        SEED_THE_RANDOM += 1
        random.seed(SEED_THE_RANDOM)

    # Now Draw Game Screen 
    for eachNumber in randomlyGeneratedNumbers:
        # for each number in randomly generated numbers
        # FIRST DRAW THE NUMBER TO THE SCREEN
        DrawGameScreen(eachNumber)
    



#1. INITIALIZE WINDOW
root = Tk() # create Tk root widget
root.geometry(DIMENSIONS_MAIN_SCREEN) # dimensions of the canvas
root.title(NAME_OF_THE_GAME) # Name of the Game
root.configure(bg = YELLOW) # Change background color to yellow



#2. PUT START BUTTON and Listen to It
theStartButton = Button(root, 
                        text = TEXT_START_GAME,
                        font = FONT_COMIC_SANS_MEDIUM,
                        fg = WHITE,
                        bg = NAVY_BLUE,
                        command = startGameSession)
theStartButton.place(x = (WIDTH_MAIN_SCREEN - WIDTH_START_BUTTON) / 2, y = (HEIGHT_MAIN_SCREEN - HEIGHT_START_BUTTON) / 2)


def DrawGameScreen(numberToBeDisplayed):
    # This function will draw game screen with the given number
    # First Game Screen Frame
    gameScreenFrame = LabelFrame(root, text = "Game Screen", 
                                        width = WIDTH_GAME_SCREEN, 
                                        height = HEIGHT_GAME_SCREEN, 
                                        font= FONT_COMIC_SANS_MEDIUM)
    gameScreenFrame.configure(bg = YELLOW) # Background color
    gameScreenFrame.configure(fg = NAVY_BLUE) # Color of the title
    # Second Render The Number on the Screen
    theNumber = Label(gameScreenFrame,
                           text = numberToBeDisplayed,
                           font = FONT_COMIC_SANS_BIG,
                           fg = NAVY_BLUE,
                           bg = YELLOW)
    # Place the number randomly on the screen
    randomlyChosenX = random.randint(RANDOM_NUMBERS_PADDING, WIDTH_GAME_SCREEN - RANDOM_NUMBERS_PADDING * 2)
    randomlyChosenY = random.randint(RANDOM_NUMBERS_PADDING, HEIGHT_GAME_SCREEN - RANDOM_NUMBERS_PADDING)
    theNumber.place(x = randomlyChosenX, y = randomlyChosenY)

    # Seed the random number algorithm
    global SEED_THE_RANDOM
    SEED_THE_RANDOM += 1 # new seed
    random.seed(SEED_THE_RANDOM);

    # Render Whole GameScreen to the Screen
    gameScreenFrame.grid(row=1, column=0, padx = 40, pady = 10)

    # Update The Root
    root.update()
    # Wait for 2 seconds
    sleep(2)

    # Destroy this frame from memory
    gameScreenFrame.destroy()
    

    return



def main():
    # MAIN FUNCTION
    root.mainloop() # enter the Tkinter event loop


if __name__ == "__main__":
    main() # CALL MAIN FUNCTION INITIALLY

