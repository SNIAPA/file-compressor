import sys 
sys.path.append('../file-compressor')

from encode import Encoder 



def test_empty():

    test_string = ''

    e = Encoder(test_string)
    assert e._char_count == None

def test_random_1():

    test_string = 'awdaxfpsldpojwpmo21341'
    
    e = Encoder(test_string)
    assert e._char_count == {'x': 1, 'f': 1, 's': 1, 'l': 1, 'j': 1, 'm': 1, '2': 1, '3': 1, '4': 1, 'a': 2, 'w': 2, 'd': 2, 'o': 2, '1': 2, 'p': 3}

def test_random_2():

    test_string = 'awc.@0224__)+'
    
    e = Encoder(test_string)
    assert e._char_count == {'a': 1, 'w': 1, 'c': 1, '.': 1, '@': 1, '0': 1, '4': 1, ')': 1, '+': 1, '2': 2, '_': 2}
