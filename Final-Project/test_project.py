from project import guess_limit, generate_integer, user_guess
import pytest

def test_guess_limit():
    # assert lower and upper-bound to test limitation
    assert guess_limit(10,1) == 3
    assert guess_limit(100,23) == 6

def test_generate_integer():
    # generate a random integer between 1 and 10
    integer = generate_integer(1, 10)
    # assert that the integer is between 1 and 10
    assert 1 <= integer <= 10

def test_user_guess():
    # test if the function returns a string
    assert isinstance(user_guess(10, 20, 1, 3), str)
    # test if the function returns the correct string
    assert user_guess(10, 20, 1, 3) == "It's too low! Try again..."
    # test if the function returns the correct string when the guess is too high
    assert user_guess(30, 20, 1, 3) == "It's too much! Try again..."
    # test if the function returns the correct string when the guess counter is equal to the guess limit
    assert user_guess(10, 20, 3, 3) == "Sorry, but the answer was: 20"