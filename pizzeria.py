'''
Pizzeria papa yon, no queda papa queda puro yon.

Un menú principal:
    • Registrar nuevas pizzas disponibles para la venta.
    • Ver el catálogo de pizzas.
    • Realizar un pedido, ingresando nombre del cliente, pizza seleccionada y cantidad.
    • Ver los pedidos realizados.
    • Salir del sistema.
Cada pizza tendrá:
    • código
    • nombre
    • tipo de masa
    • precio unitario
    • stock disponible.
    
Las compras deberán descontar stock y calcular el total a pagar según la cantidad pedida.

Los pedidos realizados por los clientes se almacenan también en una lista y deben incluir el
nombre del cliente, la pizza comprada, la cantidad y el total pagado.
'''

import os, time
clean = 'clear'
#clean = 'cls'
Pizza = [nombre, codigo, tipo_de_masa, precio_u, stock]
Pizzas = []

menu = """
+---------PIZZERIA EL PAPA YON---------+
| 1) Agregar pizzas al catálogo actual.|
| 2) Ver el catálogo.                  |
| 3) Realizar un pedido.               |
| 4) Ver los pedidos del dia.          |
| 5) Salir.                            |
+--------------------------------------+
"""

while True:
    os.system(clean)
    print(menu)
    page = input("- ")

    if page == '1':
        os.system(clean)
        Pizza[Nombre]= input("Nombre de la Pizza: ")
        Pizza[codigo]= input("Código de la Pizza: ")
        Pizza[tipo_de_masa]= input("Tipo de masa de la Pizza: ")
        Pizza[precio_u]= input("Precio unitario de la Pizza: ")
        Pizza[stock]= input("Stock disponible de la Pizza: ")
        Pizzas.append(Pizza)
        os.system(clean)
        print("Listo!")
        time.sleep(1.5)
        
    elif page == '2':
        pass
    elif page == '3':
        pass
    elif page == '4':
        pass
    elif page == '5':
        print("Saliendo...")
        break
    else:
        print("Error, la opcion ingresada no existe.")
