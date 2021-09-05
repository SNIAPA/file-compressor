import sys 
sys.path.append('../file-compressor')

from encode import Encoder 
def test_empty():
    
    e = Encoder('')
    test_dict = {}

    assert e.Binary_Heap(test_dict).next() == None

def test_next_1():
    
    e = Encoder('')

    test_dict = {'a':1}

    q = e.Binary_Heap(test_dict)

    one = q.next()

    assert one.val == 'a'
    assert one.freq == 1

    two = q.next()

    assert two == None

def test_next_2():
    
    e = Encoder('')

    test_dict = {'a':1,'b':2}

    q = e.Binary_Heap(test_dict)

    one = q.next()

    assert one.val == 'a'
    assert one.freq == 1

    two = q.next()

    assert two.val == 'b'
    assert two.freq == 2

    three = q.next()

    assert three == None


def test_add_node():
    
    e = Encoder('')

    test_dict = {'b':3,'a':2,'c':1}

    q = e.Binary_Heap(test_dict)


    assert q.root.val == 'c'


    q.add_node('d',9)


    assert q.root.val == 'c'



def test_find_last_node():
    
    e = Encoder('')

    test_dict = {'a':3,'b':2,'c':1}

    q = e.Binary_Heap(test_dict)

    assert q.find_last_node().val == 'c'

def test_sort_one_node_from_top():
    
    e = Encoder('')
    
    test_dict = {'a':3,'b':2,'c':1}

    q = e.Binary_Heap(test_dict)

def test_find_last_node():
    
    e = Encoder('')
    
    test_dict = {'a':1,'b':2,'c':3}

    q = e.Binary_Heap(test_dict)
    assert q.find_last_node().val == 'c'

def test_add_and_next():
    
    e = Encoder('')
    
    
    test_dict = {'a':1,'b':2,'c':3}

    q = e.Binary_Heap(test_dict)

    assert q.next().val == 'a'

    q.add_node('a',1)     
    assert q.next().val == 'a'


def test_first_two():
    
    e = Encoder('')

    test_dict = {'a':1,'b':2,'c':3}

    q = e.Binary_Heap(test_dict)


    assert q.next().val == 'a'

    assert q.next().val == 'b'
