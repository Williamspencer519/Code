from sample_control_structures import *
from math import sqrt

def test_sin_of_pi_is_close_to_0():
	PI = 3.1415
	assert sin(PI) < .08

def test_sin_of_pi_over_2_is_close_to_one():
	PI = 3.1415
	assert sin(PI/2) > .9
	assert sin(PI/2) < 1.1

def test_the_recurrence_relation_of_fib_numbers():
	assert fib(8) == 21
	for n in range(5,11):
		assert fib(n) == fib(n-1) + fib(n-2)
def test_the_ratio_property_of_fib_numbers():
	PHI = (1 + sqrt(5))/2
	test_ratio =  float(fib(20))/float(fib(19))
	assert abs(test_ratio - PHI) < .3
