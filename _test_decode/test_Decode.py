import sys 
sys.path.append('../file-compressor')

from decode import Decoder
 
def test_decode_SNIAPA():
   Decoder.decode('00011111001010','x0x0x53x0x41x49x50x4e') 

def test_normalized_string():
   assert Decoder._normalize_string('x0x0x53x0x41x49x50x4e') == ['','','S','','A','I','P','N']