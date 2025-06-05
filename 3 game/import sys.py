import random
import time


NUM_PEGS = 4
NUM_COLORS = 6
MAX_TURNS = 10



def generateSecretCode():
    
    secret_code = [random.randint(0, NUM_COLORS - 1) for _ in range(NUM_PEGS)]
    return secret_code

def getGuess():
    
    while True:
        try:
            guess_str = input("Enter your guess (4 values between 0 and 5, separated by space): ")
            guess_list = [int(x) for x in guess_str.split()]
            if len(guess_list) == NUM_PEGS and all(0 <= x < NUM_COLORS for x in guess_list):
                return guess_list
            else:
                print(f"Invalid format. Please enter {NUM_PEGS} numbers between 0 and {NUM_COLORS - 1}.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def numPerfectMatches(secret, guess):
    
    perfect_matches = 0
    secret_temp = []
    guess_temp = []

    for i in range(NUM_PEGS):
        if secret[i] == guess[i]:
            perfect_matches += 1
        else:
            secret_temp.append(secret[i])
            guess_temp.append(guess[i])
    return perfect_matches, secret_temp, guess_temp

def numWrongPlaceMatches(secret_remaining, guess_remaining):
    
    imperfect_matches = 0
   
    secret_counts = {}
    for peg in secret_remaining:
        secret_counts[peg] = secret_counts.get(peg, 0) + 1

    
    for peg in guess_remaining:
        
        if peg in secret_counts and secret_counts[peg] > 0:
            imperfect_matches += 1
            secret_counts[peg] -= 1 

    return imperfect_matches

def checkWin(perfect_matches):
    
    return perfect_matches == NUM_PEGS

def formatTime(seconds):

    minutes = int(seconds // 60)
    seconds_remainder = int(seconds % 60)
    return f"{minutes:02d}:{seconds_remainder:02d}"

def displayWelcome():
  
    print("Welcome to MasterMind!!!")
    print("\nAt each turn, you will enter your guess for the playing board.")
    print(f"A valid guess has {NUM_PEGS} values in between 0 and {NUM_COLORS - 1}.")
    print("Each guess will have each number within the guess separated by a space.")
    print("When you are ready, enter your first guess.")
    print("From that point on, you will be told how many perfect and imperfect matches you have.")
    print(f"After this message, you should guess again. You have {MAX_TURNS} chances, good luck!")

def displayWin(turns, time_taken):
    
    print(f"\nYou have won the game in {turns} turns and {formatTime(time_taken)}!!!")

def displayLose(secret_code):
    
    print(f"\nSorry, you have exceeded the maximum number of turns. You lose.")
    print("Here is the winning board: " + " ".join(map(str, secret_code)))


def main():
    displayWelcome()
    secret_code = generateSecretCode()
    
    

    start_time = time.time()
    turns_taken = 0
    game_won = False

    while turns_taken < MAX_TURNS:
        turns_taken += 1
        print(f"\nTurn {turns_taken}/{MAX_TURNS}")
        guess = getGuess()

        perfect_matches, secret_remaining, guess_remaining = numPerfectMatches(secret_code, guess)
        imperfect_matches = numWrongPlaceMatches(secret_remaining, guess_remaining)

        print(f"You have {perfect_matches} perfect matches and {imperfect_matches} imperfect matches.")

        if checkWin(perfect_matches):
            game_won = True
            break
    
    end_time = time.time()
    time_taken = end_time - start_time

    if game_won:
        displayWin(turns_taken, time_taken)
    else:
        displayLose(secret_code)

if __name__ == "__main__":
    main()


