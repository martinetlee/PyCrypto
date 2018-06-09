import nacl.encoding
import nacl.hash

# Practice 2
# Hashed LinkedList

class Node:
    def __init__(self, prev, data):
        self.data = data
        self.prev = prev

        byte_prevHash = self.prevHash()

        hashMe = byte_prevHash + bytes(data.encode())
        self.hash = nacl.hash.sha256(hashMe, encoder=nacl.encoding.HexEncoder)

    def prevHash(self):
        if self.prev == None: # This is the genesis block
            return "GENESIS".encode()
        else:
            return bytes(self.prev.hash)

class HLinkedList:
    def __init__(self):
        self.root = Node(None, "This is genesis")
        self.lastnode = self.root

    def addNode(self, node_data):
        self.lastnode = Node(self.lastnode, node_data)

    def printList(self):
        print("###############################")
        print("           printList")
        print("###############################")
        curNode = self.lastnode
        while curNode != None:
            print(curNode.data)
            curNode = curNode.prev

    def printListWithHash(self):
        print("###############################")
        print("       printListWithHash")
        print("###############################")
        curNode = self.lastnode
        while curNode != None:
            print(curNode.data, " / " , curNode.hash)
            curNode = curNode.prev


    def verifyChain(self):
        print("###############################")
        print("         Verify Chain")
        print("###############################")
        curNode = self.lastnode
        while curNode != None:
            print("curNode Hash : \n" , curNode.hash)

            byte_prevHash = curNode.prevHash()
            hashMe = byte_prevHash + bytes(curNode.data.encode())
            calHash = nacl.hash.sha256(hashMe, encoder=nacl.encoding.HexEncoder)

            print("calculated Hash : \n", calHash)

            if curNode.hash != calHash:
                print("ERROR: This hashed linkedlist is not valid")

            curNode = curNode.prev