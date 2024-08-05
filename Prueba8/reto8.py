class Empleado:
    def __init__(self,nombre, apellido, edad, profesion):
        #Constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion

    def imprimir_empleado(self):
        #Metodo para obtener(imprimir) los datos del empleado
        print(f"Nombre del empleado: {self.nombre.title()}")
        print(f"Apellido del empleado: {self.apellido.title()}")
        print(f"Edad del empleado: {self.edad}")
        print(f"profesion del empleado: {self.profesion.title()}")

# Instanciar de la clase Empleado
empleado1 = Empleado("jaime antonio", "gonzalez castellanos", 59, "Ingeniero Electricista")

#empleado1.imprimir_empleado()
print("\n*******Informacion del Empleado***************")
Empleado.imprimir_empleado(empleado1)
print("*************************************************")


#Modificacion de datos

empleado1.nombre ="carlos"
empleado1.apellido = "Sanchez"
empleado1.edad = 35

print("\n*******Modificacion del Empleado***************")
Empleado.imprimir_empleado(empleado1)
print("*************************************************")




###Extra!!!!
# Colas

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == 0
    
    def push(self, item):
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("pop from empty stack")
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
print("longitud de la Pila:", stack.size())


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
print("longitud de la cola:", queue.size())
        

