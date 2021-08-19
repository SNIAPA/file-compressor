import sys 
sys.path.append('../file compressor')
from main import create_huffmans_encoding


def test_1():
    root = create_huffmans_encoding('caabbb')

    assert root.r == 123

    assert root.r.l.val == 'c'

    assert root.r.r.val == 'a'

    