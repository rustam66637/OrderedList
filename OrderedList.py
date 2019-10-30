class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2: return -1 # -1 если v1 < v2
        elif v1 == v2: return 0 # 0 если v1 == v2
        elif v1 > v2: return 1 # +1 если v1 > v2

    def add(self, value):
        '''
        автоматическая вставка value
        в нужную позицию
        '''
        node = self.head

        while node != None:
            # Первый элемент в списке!
            if self.head == None:
                self.head = self.tail = value # Начало = Конец = value
                value.prev = None # Пред.элемент отсутствует
                value.next = None # След.элемент отсутствует

            # Число меньше тек. узла
            if self.compare(value, node.value) == -1:
                if node.prev == None: # Когда был единственный элемент!
                    self.head = value # Начало = value
                    value.prev = None # Нет предыдущего элемента
                    value.next = node # След. элемент = тек.элемент(node)
                    node.prev = value # value -> пред. элемент node
                    self.tail = node # node -> Конец
                else:
                    value.prev = node.prev # Ссылка на пред.элем. = пред.node
                    value.next = node # Ссылка на след. элемент = тек.node

            # Число равно текущему
            if self.compare(value, node.value) == 0:
                if node == self.tail:# Если элемент последний
                    self.tail = value # value -> хвост
                    value.prev = node # пред.элемент = node
                    value.next = None # След. элем. = None
                    node.next = value # след. элем node = value
                else:
                    node.next = value # node след.элем = value
                    value.prev = node # пред.элем value = node

            # Число больше узла
            if self.compare(value, node.value) == 1:
                if node == self.head or node == self.tail:
                    # Если элемент единственный или последний
                    node.next = value # node.next -> value
                    value.prev = node # value.prev -> node
                    value.next = None # value.next -> None
                    self.tail = value # tail -> value
                else:
                    node.next = value
                    value.prev = node
            node = node.next

    def find(self, val):
        '''
        Поиск по значению
        Возвращает узел либо None
        '''
        node = self.head
        while node != None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node != None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
        return None

    def clean(self, asc):
        self.__ascending = asc
        pass # здесь будет ваш код

    def len(self):
        node = self.head
        len = 0
        while node != None:
            len += 1
            node = node.next
        return len # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

s = OrderedList()
s.add(Node(12))
