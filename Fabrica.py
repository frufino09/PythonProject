import Proveedor

class Fabrica():

    def __init__(self):
        list= []
        list.append(Proveedor("Emil",12))
        list.append(Proveedor("juanito",15))
        list.append(Proveedor("pablito",10))

    def mostrar_precio_promedio(self):
        suma = 0
        for proveedor in list:
            suma += proveedor.precio_unidad
        promedio = suma / list.count()
        return promedio

    def mostrar_nombreprovesor_menorprecio(self):
        menor_precio = 9999999999
        nombre = ""
        for proveedor in list:
            if menor_precio > proveedor.precio_unidad:
                menor_precio = proveedor.precio_unidad
                nombre = proveedor.nombre

        return nombre
