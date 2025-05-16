"""
Interactive Wordle helper to use while playing Wordle
"""
from .solver import WordleSolver


def get_result_from_user():
    """Get result string from user"""
    print("\nEnter the result using:")
    print("  0 = gray (letter not in word)")
    print("  1 = yellow (letter in word, wrong spot)")
    print("  2 = green (letter in correct spot)")
    print("Example: 01200")
    
    while True:
        result = input("Result: ").strip()
        if len(result) == 5 and all(c in '012' for c in result):
            return result
        print("Invalid. Must be 5 characters using only 0, 1, and 2.")


def main():
    """Run Wordle helper"""
    print("=" * 50)
    print("Wordle Helper")
    print("=" * 50)
    print("\nI'll suggest guesses while you play Wordle.")
    print("After each guess, tell me about your result.\n")
    
    solver = WordleSolver()
    attempt = 0
    max_attempts = 6
    
    while attempt < max_attempts:
        attempt += 1
        
        # get suggestion
        guess = solver.get_best_guess()
        
        if guess is None:
            print("\nNo valid words remaining. Double check your inputs.")
            break
        
        print(f"\n{'='*50}")
        print(f"Attempt {attempt}/6")
        print(f"{'='*50}")
        print(f"Suggested guess: {guess.upper()}")
        print(f"({len(solver.get_possible_words())} possible words remaining)")
        
        # show alternatives if there are few words left
        if len(solver.get_possible_words()) <= 10:
            print(f"\nPossible answers: {', '.join(solver.get_possible_words())}")
        
        # get result from user
        result = get_result_from_user()
        
        # check if won
        if result == "22222":
            print(f"\n🎉 Congratulations! Solved in {attempt} guesses.")
            break
        
        # update solver
        solver.update(guess, result)
        
        if len(solver.get_possible_words()) == 0:
            print("\nNo words match those constraints. Check your results.")
            break
    else:
        print(f"\nDidn't solve in {max_attempts} attempts.")
        if len(solver.get_possible_words()) > 0:
            print(f"Remaining possibilities: {solver.get_possible_words()[:10]}")
    
    print(f"\n{'='*50}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()