from .solver import WordleSolver

def main():
    solver = WordleSolver()
    
    print("Available words:", solver.get_possible_words())
    print(f"Total words: {len(solver.get_possible_words())}\n")
    
    guess = solver.get_best_guess()
    print(f"First guess: {guess}")
    
    # simulate entering "crane" when answer is "slate"
    # c=0 (not in word), r=0 (not in word), a=1 (in word, wrong spot), 
    # n=0 (not in word), e=2 (correct spot)
    solver.update("plate", "02222")
    
    print(f"\nAfter guessing 'plate' with result '02222':")
    print(f"Remaining possible words: {solver.get_possible_words()}")
    print(f"Count: {len(solver.get_possible_words())}")
    
    next_guess = solver.get_best_guess()
    print(f"\nNext guess: {next_guess}")

if __name__ == "__main__":
    main()