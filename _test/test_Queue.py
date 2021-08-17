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

    test_dict = {'a':1,'b':2}

    q = Queue(test_dict)

    one = q.next()

    assert one.val == 'b'
    assert one.freq == 2

    two = q.next()

    assert two.val == 'a'
    assert two.freq == 1

    three = q.next()

    assert three == None


def test_add_node():

    test_dict = {'b':123,'a':8,'c':7}

    q = Queue(test_dict)

    
    assert q.root.l.val == 'a'


    q.add_node('d',9)


    assert q.root.l.val == 'd'



def est_find_last_node():

    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)

    assert q.find_last_node().val == 'c'

def test_sort_one_node_from_top():
    
    test_dict = {'a':3,'b':2,'c':1}

    q = Queue(test_dict)

    