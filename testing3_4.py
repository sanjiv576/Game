"""
This module tests name and contact number by using pytest.
"""

import pytest
@pytest.fixture
def tester():
    name = "Bishal"
    contact = 9800000000
    return [name, contact]

def testing_1(tester):
    first_name = "Bishal"
    assert tester[0] == first_name

def testing_2(tester):

    contact_num = 9800000000
    assert tester[1] == contact_num
