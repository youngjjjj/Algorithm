def swap(tree, idx1, idx2):
    tree[idx1], tree[idx2] = tree[idx2], tree[idx1]


def heapify(tree, idx):
    parent = idx // 2

    if 0 < parent < len(tree) and tree[idx] > tree[parent]:
        swap(tree, idx, parent)
        heapify(tree, parent)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        heapify(self.heap, len(self.heap) - 1)


priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)
