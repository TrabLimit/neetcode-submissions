
class Node:


    def __init__(self, key=None, val=None, pr=None, nx=None):
        self.key = key
        self.val = val
        self.pr = pr
        self.nx = nx
        

class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node()
        self.end = Node()
        self.start.nx = self.end
        self.end.pr = self.start
        self.nodes = {}
        self.capacity = capacity
        
    def moveToFront(self, node: Node) -> None:

        oldNext = node.nx
        oldPrev = node.pr

        # unlink the node first
        oldNext.pr = oldPrev
        oldPrev.nx = oldNext

        oldTop = self.start.nx

        self.start.nx = node
        node.pr = self.start

        oldTop.pr = node
        node.nx = oldTop



    def get(self, key: int) -> int:
        if key in self.nodes.keys():
            # don't forget that now that we accessed this node, this must be placed in front
            self.moveToFront(self.nodes[key])

            return self.nodes[key].val
        
        return -1
        


    def add(self, key: int, value: int) -> None:
        newNode = Node()
        newNode.key = key
        newNode.val = value

        oldTop = self.start.nx

        self.start.nx = newNode
        newNode.pr = self.start

        oldTop.pr = newNode
        newNode.nx = oldTop

        self.nodes[key] = newNode
        self.capacity -= 1
        

    
    def evict(self) -> None:
        evicted = self.end.pr
        nextEvict = evicted.pr

        nextEvict.nx = self.end
        self.end.pr = nextEvict

        self.nodes.pop(evicted.key)
        self.capacity += 1



        

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1: # not found
            self.add(key,value)
            
            if self.capacity < 0 : 
                self.evict()
                
        else:
            self.nodes[key].val = value
        



        

