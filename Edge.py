class Edge:
    def __init__(self, tail, head, length):
        self.tail = tail
        self.head = head
        self.length = length

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def get_length(self):
        return self.length
