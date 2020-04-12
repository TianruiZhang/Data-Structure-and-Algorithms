from datetime import datetime
from hashlib import sha256


class BlockChain:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_block(self, new_block):
        if not self.head:
            self.head = Block(new_block.data, 0)
            self.tail = self.head
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = Block(new_block.data, head.hash)
            self.tail = Block(new_block.data, head.hash)
                
    def print_blockchain(self):
        head = self.head
        if not head:
            print(f"""
            The blockchain is empty!"""
            )
        else:
            while head:
                print(head)
                head = head.next
        
            
class Block:

    def __init__(self, data=None, previous_hash=None):
        self.timestamp = datetime.utcnow().timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data, self.timestamp)
        self.next = None

    def calc_hash(self, data, timestamp):
        sha = sha256()
        hash_str = str(timestamp).encode("utf-8") + str(data).encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"""
        Timestamp: {self.timestamp}
        Data: {self.data}
        SHA256 Hash: {self.hash}
        Prev_Hash: {self.previous_hash}
        """
    
    
if __name__ == "__main__":
    print("Test Case 1")
    blockchain = BlockChain()
    first_block = Block("The First Block")
    blockchain.append_block(first_block)
    second_block = Block("The Second Block")
    blockchain.append_block(second_block)
    third_block = Block("The Third Block")
    blockchain.append_block(third_block)
    blockchain.print_blockchain()
    print("Test Case 2")
    blockchain = BlockChain()
    first_block = Block()
    blockchain.append_block(first_block)
    second_block = Block()
    blockchain.append_block(second_block)
    blockchain.print_blockchain()
    print("Test Case 3")
    blockchain = BlockChain()
    blockchain.print_blockchain()