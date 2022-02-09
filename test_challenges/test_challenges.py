from challenges import *

def test_foobar():
	assert foobar(3) == 'foo'
	assert not foobar(2) 
	assert foobar(5) == 'bar'
	assert foobar(6) == 'foo'
	assert foobar(15) == 'foobar'
	assert foobar(21) == 'foo'
	assert foobar(25) == 'bar'
	assert not foobar(31)
	assert foobar(150) == 'foobar'


