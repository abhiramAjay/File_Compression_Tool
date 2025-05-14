import heapq

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Required for heapq to sort nodes
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0] if heap else None
