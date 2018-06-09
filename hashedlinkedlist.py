import nacl.encoding
import nacl.hash

# Practice 2
# Hashed LinkedList

class Node:
    def __init__(self, prev, data):
        self.data = data
        self.prev = prev

        if prev == None: # This is the genesis block
            byte_prevHash = "GENESIS".encode()
        else:
            byte_prevHash = bytes(prev.hash)

        hashMe = byte_prevHash + bytes(data)  + bytes(nonce)
        self.hash = nacl.hash.sha256(hashMe, encoder=nacl.encoding.RawEncoder)


class HLinkedList:
    def __init__(self):
        self.root = Node(None, "This is genesis")
        self.lastnode = self.root

    def addNode(self, node_data):
        self.lastnode = Node(self.lastnode, node_data)

    def printList(self):
        curNode = self.lastnode
        while curNode != None:
            print(curNode.data)
            curNode = curNode.prev

    def printListWithHash(self):
        curNode = self.lastnode
        while curNode != None:
            print(curNode.data, " / " , curNode.hash)
            curNode = curNode.prev


