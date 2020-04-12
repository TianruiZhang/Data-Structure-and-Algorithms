from collections import Counter
from heapq import heapify, heappush, heappop
from operator import add
from sys import getsizeof


def huffman_encoding(data):
    tree = _create_tree(data)
    codebook = _create_codebook(tree)
    encoded_data = ""
    if not data:
        return "0", tree
    else:
        for char in data:
            encoded_data += codebook[char]
    return encoded_data, tree


def huffman_decoding(encoded_data, tree):
    if len(set(encoded_data)) == 1:
        if tree.data[1]:
            decoded_data = tree.data[1] * len(encoded_data)
        else:
            decoded_data = tree.data[1]
        return decoded_data
    else:
        current_node = tree
        decoded_data = ""
        while True:
            try:
                direction = encoded_data[0]
            except IndexError:
                decoded_data += current_node.data[1]
                break
            if direction == "0" and current_node.left_child:
                current_node = current_node.left_child
                encoded_data = encoded_data[1:]
            elif direction == "1" and current_node.right_child:
                current_node = current_node.right_child
                encoded_data = encoded_data[1:]
            else:
                decoded_data += current_node.data[1]
                current_node = tree
        return decoded_data


def _create_tree(text):
    heap_queue = [_Tree((value, key)) for key, value in Counter(text).items()]
    heapify(heap_queue)
    if len(heap_queue) == 0:
        return _Tree((1, text))
    elif len(heap_queue) == 1:
        return _Tree((1, str(text)[0]))
    else:
        while len(heap_queue) >= 2:
            left_child = heappop(heap_queue)
            right_child = heappop(heap_queue)
            tree = left_child + right_child
            heappush(heap_queue, tree)
        return tree


def _create_codebook(tree):
    codebook = {}
    visits = ""
    stack = []
    current_node = tree
    stack.append(current_node)
    while True:
        if current_node.left_child and current_node.left_child.data[1] not in codebook:
            current_node = current_node.left_child
            stack.append(current_node)
            visits += "0"
        elif current_node.right_child and current_node.right_child.data[1] not in codebook:
            current_node = current_node.right_child
            stack.append(current_node)
            visits += "1"
        else:
            if visits == "":
                codebook[current_node.data[1]] = "0"
                return codebook
            codebook[current_node.data[1]] = visits
            visits = visits[:-1]
            stack.pop()
            try:
                current_node = stack[-1]
            except IndexError:
                break
    codebook = {k: v for k, v in codebook.items() if len(k) == 1}
    return codebook


class _Tree:

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.cache = {}
    
    def __lt__(self, other):
        return self.data < other.data
    
    def __gt__(self, other):
        return self.data > other.data
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __add__(self, other):
        aggregation = _Tree()
        aggregation.data = tuple(map(add, self.data, other.data))
        aggregation.left_child = self
        aggregation.right_child = other
        return aggregation
        
    def __repr__(self):
        return str(f"Tree({self.data})")

    
if __name__ == "__main__":
    print("Test Case 1 - Normal Case")
    data = "Hello World!"
    print(f"The content of the data is: {data}.")
    print(f"The size of the data is: {getsizeof(data)}.")
    encoded_data, tree = huffman_encoding(data)
    print(f"The content of the encoded data is: {encoded_data}.")
    print(f"The size of the encoded data is: {getsizeof(int(encoded_data, base=2))}.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The size of the decoded data is: {getsizeof(decoded_data)}.")
    print(f"The content of the decoded data is: {decoded_data}.")
    assert decoded_data == data
    print("Test Case 2 - Edge Case 1")
    data = "!"
    print(f"The content of the data is: {data}.")
    print(f"The size of the data is: {getsizeof(data)}.")
    encoded_data, tree = huffman_encoding(data)
    print(f"The content of the encoded data is: {encoded_data}.")
    print(f"The size of the encoded data is: {getsizeof(int(encoded_data, base=2))}.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The size of the decoded data is: {getsizeof(decoded_data)}.")
    print(f"The content of the decoded data is: {decoded_data}.")
    assert decoded_data == data
    print("Test Case 3 - Edge Case 2")
    data = "aaaaaa"
    print(f"The content of the data is: {data}.")
    print(f"The size of the data is: {getsizeof(data)}.")
    encoded_data, tree = huffman_encoding(data)
    print(f"The content of the encoded data is: {encoded_data}.")
    print(f"The size of the encoded data is: {getsizeof(int(encoded_data, base=2))}.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The size of the decoded data is: {getsizeof(decoded_data)}.")
    print(f"The content of the decoded data is: {decoded_data}.")
    assert decoded_data == data
    print("Test Case 4 - Edge Case 3")
    data = ""
    print(f"The content of the data is: {data}.")
    print(f"The size of the data is: {getsizeof(data)}.")
    encoded_data, tree = huffman_encoding(data)
    print(f"The content of the encoded data is: {encoded_data}.")
    print(f"The size of the encoded data is: {getsizeof(int(encoded_data, base=2))}.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The size of the decoded data is: {getsizeof(decoded_data)}.")
    print(f"The content of the decoded data is: {decoded_data}.")
    assert decoded_data == data
    print("Test Case 5 - Edge Case 4")
    data = None
    print(f"The content of the data is: {data}.")
    print(f"The size of the data is: {getsizeof(data)}.")
    encoded_data, tree = huffman_encoding(data)
    print(f"The content of the encoded data is: {encoded_data}.")
    print(f"The size of the encoded data is: {getsizeof(int(encoded_data, base=2))}.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The size of the decoded data is: {getsizeof(decoded_data)}.")
    print(f"The content of the decoded data is: {decoded_data}.")
    assert decoded_data == data