"""
Wordle solver
"""
from .wordlist import load_wordlist, load_valid_guesses
from collections import Counter
import math


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
        """Get the best next guess using entropy"""
        if not self.guesses:
            return "plate"  # Wordle Bot's starting word
        
        if len(self.possible_words) == 1:
            return self.possible_words[0]
        
        if len(self.possible_words) == 0:
            return None
        
        # if very few words left, just guess one of them
        if len(self.possible_words) <= 2:
            return self.possible_words[0]
        
        # calculate entropy for each possible guess
        best_guess = None
        best_entropy = -1
        
        # limit candidates to check for performance
        candidates = self.possible_words[:100] if len(self.possible_words) > 100 else self.possible_words
        
        for guess in candidates:
            entropy = self._calculate_entropy(guess)
            if entropy > best_entropy:
                best_entropy = entropy
                best_guess = guess
        
        return best_guess
    
    def _calculate_entropy(self, guess):
        """Calculate expected information gain from a guess"""
        # count how many words would give each pattern
        pattern_counts = Counter()
        
        for word in self.possible_words:
            pattern = self._get_pattern(guess, word)
            pattern_counts[pattern] += 1
        
        # calculate entropy
        total = len(self.possible_words)
        entropy = 0
        
        for count in pattern_counts.values():
            if count > 0:
                probability = count / total
                entropy -= probability * math.log2(probability)
        
        return entropy
    
    def _get_pattern(self, guess, answer):
        """Get pattern that would result from guessing 'guess' when answer is 'answer'"""
        result = ['0'] * 5
        answer_letters = list(answer)
        
        # first pass: mark greens
        for i in range(5):
            if guess[i] == answer[i]:
                result[i] = '2'
                answer_letters[i] = None  # Mark as used
        
        # second pass: mark yellows
        for i in range(5):
            if result[i] == '0' and guess[i] in answer_letters:
                result[i] = '1'
                # Remove first occurrence
                answer_letters[answer_letters.index(guess[i])] = None
        
        return ''.join(result)
    
    def get_possible_words(self):
        """Return remaining possible words"""
        return self.possible_words