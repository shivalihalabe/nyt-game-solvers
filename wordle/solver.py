"""
Wordle solver
"""
from .wordlist import load_wordlist


class WordleSolver:
    def __init__(self, wordlist=None):
        """Initialize solver"""
        self.wordlist = wordlist or load_wordlist()
        self.possible_words = self.wordlist.copy()
        self.guesses = []
        
    def update(self, guess, result):
        """
        Update possible words based on guess result
        
        Parameters:
            guess: The guessed word (e.g., "plate")
            result: Result string using 0, 1, 2
                    0 = letter not in word (gray)
                    1 = letter in word, wrong position (yellow)
                    2 = letter in correct position (green)
        """
        self.guesses.append((guess, result))
        self.possible_words = self._filter_words(guess, result)
        
    def _filter_words(self, guess, result):
        """Filter words based on the result"""
        filtered = []
        
        for word in self.possible_words:
            if self._matches_pattern(word, guess, result):
                filtered.append(word)
                
        return filtered
    
    def _matches_pattern(self, word, guess, result):
        """Check if a word matches the guess pattern"""
        # TODO: implement the matching logic
        return True  # placeholder
    
    def get_best_guess(self):
        """Get the best next guess"""
        if not self.guesses:
            return "plate"  # best starting word
        
        if len(self.possible_words) == 1:
            return self.possible_words[0]
        
        if len(self.possible_words) == 0:
            return None
            
        # right now, just returning the first possible word
        return self.possible_words[0]
    
    def get_possible_words(self):
        """Return remaining possible words"""
        return self.possible_words