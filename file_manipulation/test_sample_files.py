from sample_files import *
import os
def test_should_create_a_text_file_with_the_name_test():
	new_file = create_file("test.txt")
	assert os.path.exists("test.txt")
def test_should_not_create_a_text_file_with_spaces_in_its_name():
	new_file = create_file("I have spaces.txt")
	assert not os.path.exists("I have spaces.txt")
def test_when_creating_a_new_text_file_there_should_not_already_exist_a_file_of_that_name():
	'''clean up files with that name before making them'''
	assert not os.path.exists("test.txt")
	new_file = create_file("test.txt")
	assert os.path.exists("test.txt")
def test_should_be_able_to_rename_a_file():
	source_file = create_file("test.txt")
	target_name = "renamed_test.txt"
	rename_file("test.txt", "renamed_test.txt")
	assert os.path.exists("renamed_test.txt")
def test_should_write_a_string_into_a_file():
	assert False
	'''I am asserting false here.  This will never pass.  Change this test and write a good one yourself, 
	read the file after you make it and check that it has a string you put in it'''