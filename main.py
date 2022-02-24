from Fabric import Fabric


def show_menu():
    print("----- welcome to the buy from supplier Provider -----")
    print("1. Mostrar el precio promedio de una unidad de materia prima.")
    print("2. Mostrar el nombre del proveedor que vende a menor precio.")
    print("3. Mostrar el precio al que vende un proveedor si se conoce su nombre.")
    print("4. Salir.")


fabric = Fabric()

while True:
    show_menu()
    value = int(input("Seleccione una opcion: "))
    if value == 1:
        average = fabric.show_average_unit_value()
        print(" >> El promedio del valor por unidad es de: ", average, "\n")
    elif value == 2:
        name_provider = fabric.show_name_provider_low_unit_value()
        print(" >> El nombre del proveedor que vende a menor precio es: " + name_provider, "\n")
    elif value == 3:
        name_provider = input("Entre el nombre del proveedor: ")
        unit_value = fabric.show_unit_value_by_name_provider(name_provider)
        if unit_value == -1:
            print(" >> No existe un proveedor con el nombre", name_provider, "\n")
        else:
            print(" >> El precio al que vende el proveedor", name_provider, "es de:", unit_value, "\n")
    elif value == 4:
        print(" >> Gracias por utilizar nuesto sistema....")
        break
    else:
        print(" >> Opcion invalida.\n")


