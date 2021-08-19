import sys 
sys.path.append('../file compressor')

from main import Encode 



def test_empty():

    test_string = ''

    e = Encode(test_string)
    assert e.count_chars(test_string) == {}

def test_random_1():

    test_string = 'awdaxfpsldpojwpmo21341'
    
    e = Encode('')
    assert e.count_chars(test_string) == {'x': 1, 'f': 1, 's': 1, 'l': 1, 'j': 1, 'm': 1, '2': 1, '3': 1, '4': 1, 'a': 2, 'w': 2, 'd': 2, 'o': 2, '1': 2, 'p': 3}

def test_random_2():

    test_string = 'awc.@0224__)+'
    
    e = Encode('')
    assert e.count_chars(test_string) == {'a': 1, 'w': 1, 'c': 1, '.': 1, '@': 1, '0': 1, '4': 1, ')': 1, '+': 1, '2': 2, '_': 2}
