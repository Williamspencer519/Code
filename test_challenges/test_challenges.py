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


def test_bridges():
	islands = ['a', 'b', 'c', 'd']
	bridges = [ ('a','b'), ('a', 'b'), ('a','c'), ('a','c'), ('a','d'), ('b','d'), ('c','d')]
	# Note that there are duplicates in the edges, there are some islands that have 2 distinct bridges 
	# between them.  If you look here it's this setup https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
	# though don't read too much, because it contains the very clever answer!
	assert not bridges(islands, bridges) #Spoiler, you can't!

