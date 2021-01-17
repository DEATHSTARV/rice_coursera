import simplegui
import random
import math



def new_game(fl=0):
   
    global secret_number
    global f
    f = fl
    global n
    if f == 0:
        secret_number = random.randrange(0, 100)
        n = math.ceil(math.log(101, 2))
        print "range[0,100)"
    else:
        secret_number = random.randrange(0, 1000)
        n = math.ceil(math.log(1001, 2))
        print "range[0,1000)"
    global c
    c = 0
    
    print "remain:", n
    
    
def range100():
    print '\n'
    new_game()
    
def range1000():
    print '\n'
    new_game(1)

def input_guess(guess):
    global n
    global c
    if c < n:
        global secret_number
        c = c + 1

        n_guess = int(guess)
        print "Guess was", n_guess
        if secret_number < n_guess:
            print "Lower"
            print "remain:", n-c 
            print '\n'
        if secret_number > n_guess:
            print "Higher"
            print "remain:", n-c
            print '\n'
        if secret_number == n_guess:
            print "Correct"
            print "remain:", n-c 
            print "You win! start new game!"
            print '\n'
            new_game(f)
            
        if c == n:
            print "You run out ot times! start new game! correct is", secret_number
            print '\n'
            new_game(f)
        
frame = simplegui.create_frame('Guess the number!', 200, 200)

inp = frame.add_input('My Guess', input_guess, 100)
range100 = frame.add_button('range100', range100, 100)
range1000 = frame.add_button('range1000', range1000, 100)


new_game()


