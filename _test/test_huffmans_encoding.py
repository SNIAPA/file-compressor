import sys 
sys.path.append('../file compressor')
from main import Encode


def test_tree():
    e = Encode('caabbb')

    assert  e.huffmans_root.r.val == 'b'

    assert  e.huffmans_root.l.l.val == 'c'

    assert  e.huffmans_root.l.r.val == 'a'

def test_node_dict():
    e = Encode('caabbb')

    assert e.node_dict['a'].val == 'a'
    
    assert e.node_dict['b'].val == 'b'
    
    assert e.node_dict['c'].val == 'c'

def test_bin_dict():
    e = Encode('caabbb')

    assert e.bin_dict['a'] == '10'
    
    assert e.bin_dict['b'] == '1'
    
    assert e.bin_dict['c'] == '00'


def test_encode_SNIAPA():
    e = Encode('SNIAPA')

    print(e.huffmans_root)

    assert e.encode_string() == '00111011010010101001'




    
    


    