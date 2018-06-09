from hashedlinkedlist import HLinkedList

print("Hashed LinkedList Test")

Mblock = HLinkedList()
Mblock.addNode("Hello World")
Mblock.printList()
Mblock.printListWithHash()
Mblock.verifyChain()

print("\n\nperform malicious act!")
Mblock.lastnode.prev.data = "hohoho"
print("modified data")
print("\n")

Mblock.verifyChain()
