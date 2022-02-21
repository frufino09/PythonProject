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
    #
    # def mostrar_nombreprovesor_menorprecio:
    #     primerProveedor = list.index(list, 0,0,1)
    #     nombre = primerProveedor
    #     for nombre in list:
    #         menor =
