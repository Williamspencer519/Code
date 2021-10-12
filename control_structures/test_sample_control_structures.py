from sample_control_structures import *


def test_can_check_if_a_number_is_prime():
	assert is_prime(5)
	assert is_prime(7)
	assert is_prime(13)
	assert is_prime(97)

def test_can_check_if_a_number_is_not_prime():
	assert not is_prime(4)
	assert not is_prime(70)
	assert not is_prime(120)


def test_if_a_number_is_the_same_forward_as_it_is_back():
	assert is_palindrome(101)
	assert is_palindrome(141)
	assert is_palindrome(55)
	assert is_palindrome(7)
	assert is_palindrome(200002)


def test_if_a_number_is_NOT_the_same_forward_as_it_is_back():
	assert not is_palindrome(1011)
	assert not is_palindrome(1014)
	assert not is_palindrome(78)
	assert not is_palindrome(7237318455442211373184)

