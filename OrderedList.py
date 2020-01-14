class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
class OrderedList:
    def __init__(self, asc = True):
        self.head = None
        self.tail = None
        self.__ascending = asc
    def print_all_nodes(self): #метод отладочного вывода списка
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
    def compare(self, v1, v2):
        '''
        Сравнение значений node с value
        '''
        if self.__ascending:
            if v1 < v2: return -1
            elif v1 == v2: return 0
            elif v1 > v2: return 1
        else:
            if v1 < v2: return 1
            elif v1 == v2: return 0
            elif v1 > v2: return -1

    def add(self, value):
        '''
        Автоматическая вставка value
        в нужную позицию
        '''
        value = Node(value)
        node = self.head
        if self.head == None: # Первый элемент в списке!
            self.head = self.tail = value # Начало = Конец = value
            value.prev = None # Пред.элемент отсутствует
            value.next = None # След.элемент отсутствует
        else:
            while node != None:
                if self.compare(value.value, node.value) <= 0:
                    if self.head == self.tail or self.head == node:
                        #первый или единственный элемент
                        value.next = node
                        value.prev = node.prev
                        node.prev = self.head = value
                        break
                    else:
                        break

                if self.compare(value.value, node.value) == 1:
                    if self.head == self.tail:#единствен
                        value.prev = node
                        node.next = value
                        self.tail = value
                        break
                    elif self.head == node: #первый
                        value.prev = node
                        value.next = node.next
                        value.next.prev = value
                        node.next = value
                    elif self.tail == node: #послед
                        node.prev = value.prev
                        value.prev.next = node
                        value.prev = node
                        value.next = None
                        node.next = value
                        self.tail = value
                        break
                    else:
                        node.prev = value.prev
                        value.prev.next = node
                        value.prev = node
                        value.next = node.next
                        value.next.prev = value
                        node.next = value
                node = value.next

    def find(self, val):
        '''
        Поиск по значению
        Возвращает узел, либо None
        '''
        node = self.head
        if self.__ascending:
            while node != None:
                if node.value == val: return node
                elif node.value > val: return None
                elif node.value < val: node = node.next
        if not self.__ascending:
            while node != None:
                if node.value == val: return node
                elif node.value < val: return None
                elif node.value > val: node = node.next

    def delete(self, val):
        '''
        Удаление узла по значению
        '''
        search = self.find(val)
        if search != None:
            if self.head == self.tail == search:
                self.head = self.tail = None
                return None
            elif self.head == search:
                self.head = search.next
                search.next.prev = None
                search.next = None
                return None
            elif self.tail == search:
                self.tail = search.prev
                search.prev.next = None
                search.prev = None
                return None
            search.next.prev = search.prev
            search.prev.next = search.next
            search.next = None
            search.prev = None
        return None

    def len(self):
        '''
        Длина списка
        '''
        node = self.head
        len = 0
        while node != None:
            len += 1
            node = node.next
        return len

    def clean(self, asc = True):
        '''
        Метод очистки списка
        '''
        self.__ascending = asc
        self.head = None
        self.tail = None

    def get_all(self):
        '''
        Список всех элементов
        '''
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc = True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):# переопределённая версия для строк
        '''
        Сравнение значений node с value
        '''
        if self.__ascending:
            if v1 < v2: return -1
            elif v1 == v2: return 0
            elif v1 > v2: return 1
        else:
            if v1 < v2: return 1
            elif v1 == v2: return 0
            elif v1 > v2: return -1
