from enum import Enum

class Estado_Pedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "Cancelado"


### Clase que representa un pedido
class Pedido:
    def __init__(self, identificador):
        self.identificador = identificador
        self.estado = Estado_Pedido.PENDIENTE

    # Método para marcar el pedido como enviado
    def enviar(self):
        if self.estado == Estado_Pedido.PENDIENTE:
            self.estado = Estado_Pedido.ENVIADO
            print(f"Pedido {self.identificador}: ha sido marcado como ENVIADO.")
        else:
            print(f"Pedido {self.identificador}: no se puede enviar. Estado actual: {self.estado.name}.")

    # Método para marcar el pedido como entregado
    def entregar(self):
        if self.estado == Estado_Pedido.ENVIADO:
            self.estado = Estado_Pedido.ENTREGADO
            print(f"Pedido {self.identificador}: ha sido marcado como ENTREGADO.")
        else:
            print(f"Pedido {self.identificador}: no se puede entregar. Estado actual: {self.estado.name}.")

    # Método para cancelar el pedido
    def cancelar(self):
        if self.estado in [Estado_Pedido.PENDIENTE, Estado_Pedido.ENVIADO]:
            self.estado = Estado_Pedido.CANCELADO
            print(f"Pedido {self.identificador}: ha sido CANCELADO.")
        else:
            print(f"Pedido {self.identificador}: no se puede cancelar. Estado actual: {self.estado.name}.")

    # Método para mostrar el estado actual del pedido
    def mostrar_estado(self):
        print(f"Pedido {self.identificador}: Estado actual - {self.estado.value}.")

# Creación de pedidos y demostración de su gestión
pedido1 = Pedido(1)
pedido2 = Pedido(2)
pedido3 = Pedido(3)

# Interacción con los pedidos
pedido1.mostrar_estado()  # Muestra: Pendiente
pedido1.enviar()          # Cambia estado a ENVIADO
pedido1.entregar()        # Cambia estado a ENTREGADO
pedido1.cancelar()        # No se puede cancelar porque ya está entregado

pedido2.mostrar_estado()  # Muestra: Pendiente
pedido2.cancelar()        # Cambia estado a CANCELADO

pedido3.mostrar_estado()  # Muestra: Pendiente
pedido3.enviar()          # Cambia estado a ENVIADO
pedido3.cancelar()        # Cambia estado a CANCELADO (porque fue enviado pero no entregado)
pedido3.entregar()        # No se puede entregar porque fue cancelado