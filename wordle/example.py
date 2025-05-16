from wordle.solver import WordleSolver

def simulate_game(answer):
    """Simulate solving a Wordle game"""
    solver = WordleSolver()
    
    print(f"Solving for answer: {answer}")
    print(f"Starting with {len(solver.get_possible_words())} possible words\n")
    
    attempts = 0
    max_attempts = 6
    
    while attempts < max_attempts:
        attempts += 1
        guess = solver.get_best_guess()
        
        if guess is None:
            print("No valid guesses remaining")
            return False
        
        # simulate result
        result = solver._get_pattern(guess, answer)
        
        print(f"Attempt {attempts}: {guess}")
        print(f"Result: {result}")
        
        if result == "22222":
            print(f"\nSolved in {attempts} guesses")
            return True
        
        solver.update(guess, result)
        print(f"Remaining possibilities: {len(solver.get_possible_words())}")
        
        if len(solver.get_possible_words()) <= 10:
            print(f"Options: {solver.get_possible_words()}")
        print()
    
    print(f"Failed to solve. Answer was: {answer}")
    return False

def main():
    # test with different words
    test_words = ["slate", "audio", "crisp", "match", "flame"]
    
    for word in test_words:
        print("=" * 50)
        simulate_game(word)
        print()

if __name__ == "__main__":
    main()