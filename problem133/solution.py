# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] # <- this is prone to FoxtrotUniforms. Could be an empty list, but locked to list type such as self.neighbors: list = neighbors. AAAND could be done with a for copy of values, since it might simply create pointes and stuff. Very not cool nor friendly :>. Tango Alpha Code.


from typing import Optional
class Solution:
    def __init__(self):
        self.visited = []
    """
    #approach 1: recursive generation of nodes.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #case 1: node is None, no processing required.
        if node == None:
            print("No node!")
            return
        print("accessed node", node.val)
        print("address id:",hex(id(node))) #verification of actual class structure.
        self.visited.append(node)
        #case 2: neighbors are None, simply copy value, return that.
        try:
            access = node.neighbors[0]
        except:
            return Node(node.val)
        #case 3: neighbors exists, activate recursion.
        neighbors: list = []
        for neighbor in node.neighbors:
            if neighbor not in self.visited: #this guy prevents infinite loops.
                print("running for neighbour with memory index:", hex(id(neighbor)))
                self.visited.append(neighbor.val)
                neighbors.append(self.cloneGraph(neighbor))
        return Node(node.val, neighbors)
    """
    #approach 2: generate as needed.
    def pointerfinder(self, node: Node) -> list:
        """
            node -> the starting point of this search
            self.visited.clear() must be runned before running this method.
            also, assumes node passed got neighbors! Else caller function could simply
            return a bloody node with no neighbors and be done with it!

            Will save all pointers found inside self.visited
        """
        #print("DEBUG!-> VISITING ", node.val, "with ID", hex(id(node)))
        self.visited.append(node) #already assumes node passed was NOT visited.
        for neighbor in node.neighbors: #also assumes neighbors not empty nor NULL/None
            if neighbor not in self.visited:
                self.pointerfinder(neighbor)
        return

        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
            limitations: 
                this uses direct access pattern to create the neighbors and store, which
                can use more memory than expected.
        """
        #these initial checks seem to work, so we'll keep them as is.
        #CASE 0: no node, no processing, return nothing!
        if node == None:
            print("No node!")
            return
        #CASE 1: node with no neighbors, return node initialized with node.val.
        try:
            access = node.neighbors[0]
        except:
            return Node(node.val)
        #CASE ACTUAL: actual graph, processing required.
        #1ST PHASE: find all the unique nodes.
        self.visited.clear()
        self.pointerfinder(node)
        #STARTDEBUG :>
        #print("DEBUG! -> FOUND THE FOLLOWING NODES:")
        #for found in self.visited:
            #print("NODEVAL: ", found.val)
            #print("NODEID: ", hex(id(found)))
        #ENDDEBUG
        #2ND PHASE: for all the nodes found, create a new node and find connections.
        #made like this for direct access.
        theNodes: list = [0 for i in range(len(self.visited) + 1)]
        connections: list = [0 for i in range(len(self.visited) +  1)]
        for found in self.visited:
            theNodes[found.val] = Node(found.val, [])
            this = []
            for neighbor in found.neighbors:
                this.append(neighbor.val)
            #print("DEBUG! -> found the following connections:", this)
            connections[found.val] = this #creating a direct access list.
        
        #print("DEBUG!")
        #print("NODES:", theNodes)
        #print("CONNECTIONS:", connections)
        #3RD PHASE: assemble neighbors
        for found in self.visited:
            index = found.val
            #print("DEBUG! -> running neighbor assembly for node index", index)
            this = []
            for connection in connections[index]:
                theNodes[index].neighbors.append(theNodes[connection])
        return theNodes[1] #return the first node created, seems to be enough for leetcode.