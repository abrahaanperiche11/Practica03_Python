class Producto:
    
    def __init__(self, nombre, marca, cede, precio, anio):
        self.nombre=nombre
        self.marca=marca
        self.cede=cede
        self.precio=precio
        self.anio=anio
        
class Catalogo:
    
    def __init__(self):
        self.productos=[]
        
    def agregar_producto(self,producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        for producto in self.productos:
            print('Nombre: ', producto.nombre)
            print('Marca: ', producto.marca)
            print('Precio: ', producto.precio)
            print('Cede: ', producto.cede)
            print('Anio: ', producto.anio)
            print('-----------------------------------------------')
    def filtrar_por_anio(self, anio):
        productos_filtrados = [producto for producto in self.productos if producto.anio == anio]
        return productos_filtrados
    def filtrar_por_cede(self, cede:str):
        productos_filtrados = [producto for producto in self.productos if producto.cede == cede]
        return productos_filtrados
    
# Ejemplo 
catalogo = Catalogo()

producto1 = Producto("Llanta", "Michelin",'Lima',60.99, 2022)
producto2 = Producto("Luces delanteras", "Philips", 'Lima',50.15, 2023)
producto3 = Producto("Cadena", "Zilxiao", 'Piura', 20.66, 2022)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Productos del catalago:")
catalogo.mostrar_productos()

print("Productos comprados el año 2022:")
productos_filtrados = catalogo.filtrar_por_anio(2022)
for producto in productos_filtrados:
    print(producto.nombre)
    
print("Productos comprados en cede Lima:")
productos_filtrados_cede = catalogo.filtrar_por_cede('Lima')
for producto in productos_filtrados_cede:
    print(producto.nombre)