
class LinkedList(object):

    def __init__(self, *args):
        self.list = args
        self.index = 0


    def add(self, value):
        self.list = self.list + (value,)


    def insert(self, index, value):
        self.list = self.list[:index] + (value,) + self.list[index:]


    def get(self, index):
        if index >= len(self.list):
            raise IndexError
        return self.list[index]


    def remove(self, value):
        n = 0
        for i in self.list:
            if i == value:
                break
            n += 1
        if n < len(self.list):
            self.list = self.list[:n] + self.list[n+1:]


    def remove_at(self, index):
        if index >= len(self.list):
            raise IndexError
        element = self.list[index]
        self.list = self.list[:index] + self.list[index + 1:]
        return element


    def clear(self):
        self.list = ()


    def contains(self, value):
        if value in self.list:
            return True
        else: return False


    def len(self):
        return len(self.list)


    def is_empty(self):
        if self.len() == 0:
            return True
        else: return False


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration

        element = self.list[self.index]
        self.index += 1
        return element


# if __name__ == '__main__':
#     ll = LinkedList(1, 2, 3, 4, 5)
#     ll.add(9)
#     ll.insert(5, 111)
#     print(ll.get(5))
#     ll.remove(1)
#     print(ll.remove_at(2))
#     ll.clear()
#     print(ll.contains(44))
#     print(ll.is_empty())

    #simple_iter = LinkedList(1,2,2,4,5,77,8,99,9887)
    #for i in simple_iter:
    #    print(str(i))


