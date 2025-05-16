"""
Wordle word lists
"""
from pathlib import Path

def load_wordlist():
    """Load Wordle answer list"""
    answers_file = Path(__file__).parent / "answers.txt"
    
    if answers_file.exists():
        with open(answers_file, 'r') as f:
            return [word.strip().lower() for word in f.readlines()]
    else:
        # fallback to sample list if file doesn't exist
        return [
            "crane", "slate", "sauce", "slice", "shale",
            "about", "above", "abuse", "actor", "acute",
            "plate", "later", "water"
        ]

def load_valid_guesses():
    """Load valid Wordle guesses"""
    valid_file = Path(__file__).parent / "valid_guesses.txt"
    
    if valid_file.exists():
        with open(valid_file, 'r') as f:
            return [word.strip().lower() for word in f.readlines()]
    else:
        # fallback to answer list
        return load_wordlist()