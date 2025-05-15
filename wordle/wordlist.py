"""
Wordle word lists
"""

# sample list
POSSIBLE_ANSWERS = [
    "crane", "slate", "sauce", "slice", "shale",
    "about", "above", "abuse", "actor", "acute"
]

VALID_GUESSES = POSSIBLE_ANSWERS  # same for now

def load_wordlist():
    """Load full word list"""
    return POSSIBLE_ANSWERS