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
        # green letters (2) - must be in exact position
        for i, (g_letter, r) in enumerate(zip(guess, result)):
            if r == '2':
                if word[i] != g_letter:
                    return False
        
        # yellow letters (1) - must be in word but in different position
        for i, (g_letter, r) in enumerate(zip(guess, result)):
            if r == '1':
                if g_letter not in word:
                    return False
                if word[i] == g_letter:
                    return False
        
        # gray letters (0) - must not be in word unless they appear elsewhere as yellow or green
        for i, (g_letter, r) in enumerate(zip(guess, result)):
            if r == '0':
                # count how many times letter appears as yellow or green
                required_count = sum(1 for j, r2 in enumerate(result) 
                                    if guess[j] == g_letter and r2 in ['1', '2'])
                # count how many times letter appears in candidate word
                actual_count = word.count(g_letter)
                
                if actual_count > required_count:
                    return False
    
        return True
    
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