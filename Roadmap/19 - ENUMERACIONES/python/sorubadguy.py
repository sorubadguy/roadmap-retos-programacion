from enum import Enum
from random import randint

#? Enumeradores

class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def mostrarDia(numero: int):
    print(DiasSemana(numero).name)
    
mostrarDia(1)
mostrarDia(2)
mostrarDia(3)

#! Extra

class Estados(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4
    
class pedido():
    
    def __init__(self) -> None:
        self.estado = Estados.PENDIENTE.name
        self.id = randint(1000, 1000000)
    
    def estadoActual(self):
        print(f"El estado actual del pedido n°:{self.id} es {self.estado}")
    
    def enviarProducto(self):
        if(self.estado == Estados.PENDIENTE.name):
            self.estado = Estados.ENVIADO.name
            print(f"El pedido n°:{self.id} ah sido {Estados.ENVIADO.name}")
        else:
            print(f"El pedido n°:{self.id} no puede ser enviado, actualmente se encuentra: {self.estado}")
        
    def entregarProducto(self):
        if(self.estado == Estados.ENVIADO.name):
            self.estado = Estados.ENTREGADO.name
            print(f"El pedido n°:{self.id} ah sido {Estados.ENTREGADO.name}")
        else:
            print(f"El pedido n°:{self.id} no puede ser entregado, actualmente se encuentra: {self.estado}")
            
    def cancelar(self):
        self.estado = Estados.CANCELADO.name
        print(f"El pedido n°{self.id} ah sido {self.estado}")
            
nuevo_pedido = pedido()
nuevo_pedido.estadoActual()
nuevo_pedido.entregarProducto()
nuevo_pedido.enviarProducto()
nuevo_pedido.entregarProducto()
nuevo_pedido.enviarProducto()
nuevo_pedido.cancelar()
nuevo_pedido.enviarProducto()