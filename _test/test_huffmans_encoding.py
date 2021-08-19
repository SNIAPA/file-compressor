import sys 
sys.path.append('../file compressor')
from main import create_huffmans_encoding


def test_1():
    root = create_huffmans_encoding('caabbb')

    assert root.r.val == 'b'

    assert root.l.l.val == 'c'

    assert root.l.r.val == 'a'

    print(root)

    assert False

    