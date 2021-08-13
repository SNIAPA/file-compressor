from typing import Union




def compress(s:str) -> str:
    
 
    def count_chars(s:str) -> dict:
       
        seen_chars = {}

        for char in s:

            if char in seen_chars.keys():
                seen_chars[char] += 1
                continue

            seen_chars[char] = 1

        return dict(sorted(seen_chars.items(), key=lambda item: item[1]))

    class Queue:

        class Node:

            
            val = None
            freq = None
            l = None
            r = None
            parrent = None


            def __init__(self,val:Union[int,object],freq:float,parrent:object = None) -> None:
                self.val = val
                self.freq = freq
                self.parrent = parrent

        root: Node
        
        def __init__(self,char_list:dict) -> None:

            self.root = self.Node(list(char_list.keys())[0],list(char_list.values())[0])

            for char in list(char_list.keys())[1:]:
                self.add_node(char,char_list[char])

        def find_first_empty(self) -> Node:

            check_queue = [self.root]

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

        def add_node(self,val:Union[int,object],freq:float) -> None:
            
            
            new_node = self.find_first_empty()

            new_node.val = val
            new_node.freq = freq

            while new_node.parrent.freq > new_node.freq:
                print(new_node.parrent.freq ,new_node.freq)
                temp = new_node
                new_node.freq,new_node.val = new_node.parrent.freq,new_node.parrent.val
                new_node.parrent.freq,new_node.parrent.val = temp.freq, temp.val

                new_node = new_node.parrent


        def next(self) -> object:
            return self.root


    q = Queue(count_chars(s))
    print(q.root.val,q.root.freq)    

if __name__ == "__main__":
    compress('aswdwasdawdawdadfgesewaioljcdkauhbd')




