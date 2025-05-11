# Работа со стеком (LIFO)
#push — добавление элемента в стек,
#pop — удаление верхнего элемента,
#peek — получение верхнего элемента без удаления,
#is_empty — проверка, пуст ли стек.
class Stack:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())


# Работа с очередью (FIFO)

# добавление элемента в конец очереди;
# удаление элемента из начала очереди;
# проверка на пустоту очереди.

class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())

# Работа с деревом -  используется для поиска и сортировок
#Бинарное дерево — это вид дерева, в котором каждый узел имеет не более двух потомков.
#Если же корневой узел есть, мы можем работать с его сторонами, правой и левой.
# Если значение нового узла больше корневого значения, добавляем его в правую ветвь дерева.
# Если значение меньше или равно, добавляем в левую ветвь.

#Сравнение значений: Определяем, в какую сторону дерева пойдёт новый узел,
# сравнивая его значение с корневым узлом.

#Добавление в правую ветвь: Если значение нового узла больше корневого,
# вставляем его в правую сторону. Если правая ветвь пуста, начинаем её заполнять,
# иначе продолжаем вставку в правую ветвь.

#Добавление в левую ветвь: Если значение нового узла меньше или равно корневому,
# вставляем его в левую сторону. Если левая ветвь пуста, начинаем её заполнять,
# иначе продолжаем вставку в левую ветвь.

#Возврат корня дерева: В конце функции возвращаем текущий корень дерева,
# чтобы сохранять его структуру и продолжать с ним работать после каждой вставки нового узла.

class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key

# Функция для добавления нового узла
def insert(root, key):
   if root is None:
       return Node(key)
   else:
       if root.val < key:
           root.right = insert(root.right, key)
       else:
           root.left = insert(root.left, key)
   return root

# Пример использования
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)


# Работа с Графом

class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()

class Graph:
   def __init__(self):
       self.graph = {}
   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)
   def print_graph(self):
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()