
import sys

def main(s,l):
    tree = l.replace('[','').replace(']','').replace("'",'').replace('"','').replace(',','').split(' ')
    print(tree)

    ans = ''
    i = 0
    counter = 0
    for x in s:
        index = (2**(i+1))-2 + ((counter)*2) + int(x)
        if tree[index] == 'Branch':
            i+=1
            counter = (counter*2) + int(x)
            continue
        i = 0
        counter = 0
        ans+=tree[index]
    return(ans)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(main(input('Input encoded string: '),input("input tree list: ")))
    else:    
        print(main(sys.argv[1],sys.argv[2]))