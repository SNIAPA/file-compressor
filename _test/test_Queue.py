import sys 
sys.path.append('../file compressor')

from main import Queue 

def test_empty():

    test_dict = {}

    assert Queue(test_dict).next() == None

def test_next_1():

    test_dict = {'a':1}

    q = Queue(test_dict)

    one = q.next()

    assert one.val == 'a'
    assert one.freq == 1

    two = q.next()

    assert two == None

def test_next_2():

    test_dict = {'a':2,'b':1}

    q = Queue(test_dict)

    one = q.next()

    assert one.val == 'a'
    assert one.freq == 2

    two = q.next()

    assert two.val == 'b'
    assert two.freq == 1

    three = q.next()

    assert three == None


def test_add_node():

    test_dict = {'b':3,'a':2,'c':1}

    q = Queue(test_dict)


    assert q.root.val == 'b'


    q.add_node('d',9)


    assert q.root.val == 'd'



def test_find_last_node():

    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)

    assert q.find_last_node().val == 'c'

def test_sort_one_node_from_top():
    
    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)

def test_find_last_node():
    
    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)
    assert q.find_last_node().val == 'c'

def test_add_and_next():
    
    
    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)

    assert q.next().val == 'a'

    q.add_node('a',1)     
    assert q.next().val == 'b'