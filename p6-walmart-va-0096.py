import matplotlib.pyplot as plt
import numpy as np
# Samuel Martinez NC 0096

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()

# Perzonalizar grafica
plt.plot(cant_productos, precio, color = 'yellow', marker= '*', linestyle= 'dashed', linewidth=2, markersize=12)
plt.title("Ventas de Walmart 0096")
plt.xlabel("cantidad productos")
plt.ylabel("precios")
plt.show()
