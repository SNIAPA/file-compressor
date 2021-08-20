from typing import Union
from random import randint

class Encoder:
    class Binary_Heap:

        class test:
            pass

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

    _huffmans_root = None
    _node_dict = {}
    _bin_dict = {}
    __input_string = None
    __encoded_string = None
    _char_count = None
    
    def __count_chars(self,s:str) -> dict:
        
        seen_chars = {}

        for char in s:

            if char in seen_chars.keys():
                seen_chars[char] += 1
                continue

            seen_chars[char] = 1

        return dict(sorted(seen_chars.items(), key=lambda item: item[1]))

    def get_encoded_string(self) -> None:
        return self.__encoded_string
    
    def get_tree(self) -> None:

        
        ans = []
        queue = [self._huffmans_root]


        while queue:
            
            if queue[0] == None:
                ans.append(None)
                print(ans[-1])
                continue
            elif queue[0].val == None:
                ans.append('Node')
            else:
                ans.append(queue[0].val)
            print(ans[-1])

            if queue[0].l:
                queue.append(queue[0].l)
            else:
                queue.append(None)

            if queue[0].r:
                queue.append(queue[0].r)
            else:
                queue.append(None)

            queue.pop(0)
        
        return ans

    def __init__(self,input_string: str) -> None:
        if input_string == '':
            return 


        self.__input_string = input_string
        self._char_count = self.__count_chars(input_string)
        self._huffmans_root = self.__create_huffmans_encoding(self._char_count)
        self._bin_dict = self.__create_bin_map(self._node_dict)
        self.__encoded_string = ''.join([self._bin_dict[x] for x in self.__input_string])

    def __create_huffmans_encoding(self,s:dict) -> str:

        q = self.Binary_Heap(s)
        i = 0
        print(q.length)
        while q.length > 1 :

            l = q.next()
            r = q.next()
            
            root = self.Node(None,None)


            if type(l.val) == str:
                root.l = self.Node(l.val,root)
                self._node_dict[root.l.val] = root.l
            else:
                root.l = l.val
                root.l.parrent = root

            if type(r.val) == str:
                root.r = self.Node(r.val,root)
                self._node_dict[root.r.val] = root.r
            else:
                root.r = r.val
                root.r.parrent = root

            q.add_node(root,l.freq + r.freq)
            i+=1

        last = q.next()

        print(self._node_dict)

        if type(last.val) == str:
            
            ans =  self.Node(None)
            ans.l = self.Node(last.val,ans)
            self._node_dict[ans.l.val] = ans.l
            return ans

        else:
            return last.val

    def __create_bin_map(self,__node_dict:dict):
        bin_dict = {}
        keys = list(__node_dict.keys())
        nodes = list(__node_dict.values())
        for i in range(len(__node_dict)):
            key = keys[i]
            node = nodes[i]
            bin_repr = ''
            while node.parrent:
                if node.parrent.l:
                    if node.val == node.parrent.l.val:
                        bin_repr+='0'
                if node.parrent.r:
                    if node.val == node.parrent.r.val:
                        bin_repr+='1'

                node = node.parrent

            bin_dict[key] = bin_repr
        return bin_dict

    def _encode_string(self) -> str:
        
        ans = ''.join([self._bin_dict[x] for x in self.__input_string])

        return ans
    
if __name__ == "__main__":
    e = Encoder(input('Input string: '))
    print(e.get_encoded_string())
    print(e.get_tree())



