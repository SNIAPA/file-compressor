from typing import Union
from random import randint

class Queue:

    class Node:
        
        val = None
        freq = None
        l = None
        r = None
        parrent = None

        def __init__(self,val:Union[str,object],freq:float,parrent:object = None) -> None:
            self.val = val
            self.freq = freq
            self.parrent = parrent

    root: Node = None
    length: int = 1

    def __init__(self,char_list:dict) -> None:

        if len(char_list) < 1:
            return

        keys = list(char_list.keys())
        vals = list(char_list.values())

        self.root = self.Node(keys[0],vals[0])

        for i in range(1,len(vals)):
            self.add_node(keys[i],vals[i])

    def find_first_empty(self) -> Node:

        check_queue = [self.root]

        if self.root == None:
            self.root = self.Node(None,None,None)
            return self.root

        while check_queue:

            if check_queue[0].l:
                check_queue.append(check_queue[0].l)
            else:
                check_queue[0].l = self.Node(None,None,check_queue[0])
                return check_queue[0].l 

            if check_queue[0].r:
                check_queue.append(check_queue[0].r)
            else:
                check_queue[0].r = self.Node(None,None,check_queue[0])
                return check_queue[0].r
            check_queue.pop(0)

    def find_last_node(self) -> Union[Node,None]:
        
        if not self.root:
            return None

        check_queue = [self.root]

        if self.root.l:
            check_queue.append(self.root.l)
        if self.root.r:
            check_queue.append(self.root.r)

        while check_queue:
            
            if len(check_queue) < 2:
                return check_queue[0]

            if check_queue[1].l:
                check_queue.append(check_queue[1].l)

            if check_queue[1].r:
                check_queue.append(check_queue[1].r)


            check_queue.pop(0)

    def add_node(self,val:Union[int,object],freq:float) -> None:

        self.length += 1

        new_node = self.find_first_empty()
        new_node.val = val
        new_node.freq = freq

        while new_node.parrent:
            if new_node.parrent.freq < new_node.freq:
                break

            new_node.freq,new_node.parrent.freq =new_node.parrent.freq,new_node.freq
            new_node.val,new_node.parrent.val =new_node.parrent.val,new_node.val

            new_node = new_node.parrent

    def sort_one_node_from_top(self,root:Node) -> Node:


        r = 0
        l = 0

        if root.l:
            l = root.l.freq

        if root.r:
            r = root.r.freq
        
        if (root.freq > l and l > 0) and (r > l or r == 0):
            root.freq,root.l.freq = root.l.freq,root.freq
            root.val,root.l.val = root.l.val,root.val
        elif r > 0:
            root.freq,root.l.freq = root.l.freq,root.freq
            root.val,root.r.val = root.r.val,root.val
        
        if root.l:
            root.l = self.sort_one_node_from_top(root.l)
        
        if root.r:

            root.r = self.sort_one_node_from_top(root.r)

        return root

    def next(self) -> object:

        self.length -= 1

        if self.root == None:
            return None
        
        temp = self.root

        pushed_node = self.find_last_node()
        
        if self.root == pushed_node:
            self.root = None
            return temp

        if pushed_node.parrent.l.val == pushed_node.val:
            pushed_node.parrent.l = None
        else:
            pushed_node.parrent.r = None
        

        self.root = pushed_node

        if temp.l:
            if temp.l != self.root:
                self.root.l = temp.l

        if temp.r:
            if temp.r != self.root:
                self.root.r = temp.r
        self.root.parrent = None

        

        self.root = self.sort_one_node_from_top(self.root)


        return temp

def count_chars(s:str) -> dict:
    
    seen_chars = {}

    for char in s:

        if char in seen_chars.keys():
            seen_chars[char] += 1
            continue

        seen_chars[char] = 1

    return dict(sorted(seen_chars.items(), key=lambda item: item[1]))

class Node:
    
    val = None
    l = None
    r = None
    parrent = None

    def __init__(self,val:str,parrent:object = None) -> None:
        self.val = val
        self.parrent = parrent
    def repr(self,tabs = 0) -> str:
        return_str = f'val:{self.val}\n{"  "*(tabs)}{"{"}'

        if self.l:
            return_str+=f'\n {"  "*(tabs+1)}L: {self.l.repr(tabs=tabs+1)}'

        if self.r:
            return_str+=f'\n {"  "*(tabs+1)}R: {self.r.repr(tabs=tabs+1)}'

        return return_str+f'\n{"  "*(tabs)}{"}"}'
    
    def __repr__(self) -> str:
        return self.repr()


def create_huffmans_encoding(s:str) -> str:

    q = Queue(count_chars(s))
    i = 0

    while q.length > 1:

        print('i: ',i)

        l = q.next()
        r = q.next()
        
        temp_root = Node(None,None)


        if type(l.val) == str:
            temp_root.l = Node(l.val,temp_root)
        else:
            temp_root.l = l.val

        if type(r.val) == str:
            temp_root.r = Node(r.val,temp_root)
        else:
            temp_root.r = r.val

        q.add_node(temp_root,l.freq + r.freq)
        i+=1

    main_root = q.next().val


    return main_root


    
if __name__ == "__main__":
    print(create_huffmans_encoding(input('-> ')))



