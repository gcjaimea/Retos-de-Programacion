
#Pila
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0  
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError ("peek from empty stack")
    
    def size(self):
        return len(self.items)
    

#Correr el codigo
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)

print("Pila actual:", stack.items)
print("Elemento superior:", stack.peek())
print("Retirar elemento:", stack.pop())
print("Pila después de retirar:", stack.items)
print(f"longitud de la Pila:", stack.size())


# Colas

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from empty queue")

    def size(self):
        return len(self.items)

# Ejemplo de uso
queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
print("Cola actual:", queue.items)
print("Elemento al frente:", queue.front())
print("Retirar elemento:", queue.dequeue())
print("Cola después de retirar:", queue.items)
print(f"longitud de la cola:", queue.size())
        

