"""
Tests for Wordle solver
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from wordle.solver import WordleSolver


def test_solver_init():
    """Test that solver initializes"""
    solver = WordleSolver()
    assert solver is not None
    assert len(solver.possible_words) > 0


def test_first_guess():
    """Test first guess"""
    solver = WordleSolver()
    guess = solver.get_best_guess()
    assert guess == "crane"


if __name__ == "__main__":
    # manual test
    test_solver_init()
    test_first_guess()
    print("All tests passed")