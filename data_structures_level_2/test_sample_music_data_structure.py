from sample_music_data_structure import *


def test_should_recognize_a_major_chord():
	chord = Chord(["G", "B", "D"])
	assert chord.sonority() == "Major"
def test_should_recognize_a_minor_chord():
	chord = Chord(["G", "Bb", "D"])
	assert chord.sonority() == "Minor"
def test_should_transpose_a_chord():
	chord = Chord(["G", "B", "D"])
	chord.transpose(2)
	assert "A" in chord.notes
	assert "C#" in chord.notes
	assert "E" in chord.notes
	assert chord.sonority() == "Major"

def test_should_make_a_chord_progression_with_some_chords():
	A_Major = Chord(["A", "C#", "E"])
	E_Major = Chord(["E", "G#", "B"])
	Fsharp_Minor = Chord(["F#", "A", "C#"])
	D_Major = Chord(["D", "F#", "A"])
	chord_progression = ChordProgression([A_Major, E_Major, Fsharp_Minor, D_Major])
	'''This is another one of those container style objects'''
	chord_progression.key = "A"
	assert chord_progression.numbers == ["I", "V", "vi", "IV"]
	'''Analysis changes withh the key changing'''
	chord_progression.key = "D"
	assert chord_progression.numbers == ["V", "II", "iii", "I"]
	
	