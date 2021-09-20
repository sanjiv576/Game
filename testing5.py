"""
This module tests high score by using pytest.
"""
import pytest

def score_obtained(score):
    return score

def testing_highscore():
    high_score = 27
    assert (score_obtained(23) < high_score) is True == True

