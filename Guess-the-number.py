# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

try_count = 0
range_limit = 100
secret_number = 0
guess_limit = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print ""
    print "Guess-the-number new game"
    print "Select values within [0, %d) range" %range_limit
    print "Remaining guesses: %d" %(guess_limit - try_count)
    global secret_number
    secret_number = random.randrange(0, range_limit)
    global try_count
    try_count = 0
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global guess_limit
    guess_limit = 7
    global range_limit
    range_limit = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global guess_limit
    guess_limit = 10
    global range_limit
    range_limit = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    global try_count
    print ""
    print "Your guess: %d" %guess
    if guess == secret_number:
        "You win!"
        new_game()
    else:
        if try_count == guess_limit - 1:
            print "You reached guess limit."
            print "Secret number was %d." %secret_number
            new_game()
        else:
            try_count +=1
            print "Remaining guesses: %d" %(guess_limit - try_count)
            if guess < secret_number:
                print "Higher"            
            else:
                print "Lower"
        

# create frame
frame = simplegui.create_frame("Guess the Number", 100, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
frame.add_input("Guess:", input_guess, 100)
frame.start()

# call new_game 
new_game()
