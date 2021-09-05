import sys

class Decoder():
    
    @staticmethod
    def _normalize_string(s:str) -> list[str]:
        splited_string = [x for x in s.split('x')][1:]

        return [chr(int(x,16)) if x != '0' else '' for x in splited_string]


    @staticmethod
    def decode(s:str,l:str) -> str:
        
        normalized_string = Decoder._normalize_string(l)

        tree = Decoder.Tree(normalized_string)

        i = 0 
        ans = ''
        
        while i <len(s):
            current_node = tree.root


            while current_node.val == None:
                if s[i] == '1':
                    current_node = current_node.r
                else:
                    current_node = current_node.l

                i+=1
            ans += current_node.val
        return ans

    class Tree():

        class Node():

            l = None
            r = None
            val = None

            def __init__(self,val:str) -> None:
                self.val = val
        

        root = Node(None)

        def __init__(self,node_list:list[str]) -> None:

            empty_node_queue = [self.root]

            node_list = ['']+node_list

            for x in node_list:
                empty_node_queue[0]
                if not x:
                    empty_node_queue[0].l = self.Node(None)
                    empty_node_queue[0].r = self.Node(None)
                    empty_node_queue.extend([empty_node_queue[0].l,empty_node_queue[0].r])
                else:
                    empty_node_queue[0].val = x

                empty_node_queue.pop(0)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(Decoder.decode(input('Input encoded string: '),input("input node list: ")))
    else:    
        print(Decoder.decode(sys.argv[1],sys.argv[2]))