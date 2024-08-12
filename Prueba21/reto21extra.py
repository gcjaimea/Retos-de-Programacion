import time
import random

# Función callback para confirmar el pedido
def confirm_order(dish_name):
    print(f"Pedido confirmado: {dish_name}")

# Función callback para notificar que el pedido está listo
def order_ready(dish_name):
    print(f"Pedido listo: {dish_name}")

# Función callback para notificar que el pedido ha sido entregado
def deliver_order(dish_name):
    print(f"Pedido entregado: {dish_name}")

# Función que simula el procesamiento del pedido
def process_order(dish_name, on_confirm, on_ready, on_deliver):
    # Confirmación del pedido
    on_confirm(dish_name)
    
    # Simula el tiempo de preparación del plato
    preparation_time = random.randint(1, 10)
    print(f"Preparando {dish_name}... Tiempo estimado: {preparation_time} segundos.")
    time.sleep(preparation_time)
    
    # Notificación de que el pedido está listo
    on_ready(dish_name)
    
    # Simula el tiempo de entrega del plato
    delivery_time = random.randint(1, 10)
    print(f"Entregando {dish_name}... Tiempo estimado: {delivery_time} segundos.")
    time.sleep(delivery_time)
    
    # Notificación de que el pedido ha sido entregado
    on_deliver(dish_name)

# Ejemplo de uso
if __name__ == "__main__":
    dish = "Restaurante Palace"
    process_order(dish, confirm_order, order_ready, deliver_order)