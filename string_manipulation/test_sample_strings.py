from sample_strings import *


def test_should_remove_spaces_from_a_string():
	assert remove_spaces("I have spaces") == "Ihavespaces"

def test_should_not_remove_underscores_from_a_string():
	assert remove_spaces("I_have_spaces") == "I_have_spaces"

def test_has_letter_should_tell_if_i_have_an_a_in_thhe_string():
	assert has_letter("this has the letter a", "a")

def test_has_letter_should_tell_if_i_do_not_have_an_x_in_thhe_string():
	assert not has_letter("this has the letter a", "x")

def test_censor_inappropriate_language_should_block_some_offensive_words():
	original_string = "I'm the fucking lizard king"
	censored_string = censor_innapropriate_language(original_string)
	assert "fuck" not in original_string.lower()

	original_string = "holy shit"
	censored_string = censor_innapropriate_language(original_string)
	assert "shit" not in original_string.lower()
	
