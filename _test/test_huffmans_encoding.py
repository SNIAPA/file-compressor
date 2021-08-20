import sys 
sys.path.append('../file compressor')
from main import Encoder


def test_tree():
    e = Encoder('caabbb')

    assert  e._huffmans_root.r.val == 'b'

    assert  e._huffmans_root.l.l.val == 'c'

    assert  e._huffmans_root.l.r.val == 'a'

def test_node_dict():
    e = Encoder('caabbb')

    assert e._node_dict['a'].val == 'a'
    
    assert e._node_dict['b'].val == 'b'
    
    assert e._node_dict['c'].val == 'c'

def test_bin_dict():
    e = Encoder('caabbb')

    assert e._bin_dict['a'] == '10'
    
    assert e._bin_dict['b'] == '1'
    
    assert e._bin_dict['c'] == '00'


def test_Encoder_one_letter():
    e = Encoder('a')

    assert e.get_encoded_string() == '0'

def test_Encoder_SNIAPA():
    e = Encoder('SNIAPA')

    assert e.get_encoded_string() == '00111011010010101001'





    
    


    