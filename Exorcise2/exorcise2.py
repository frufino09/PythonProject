from CollegeCareer import CollegeCareer


def show_menu():
    print("1. Cantidad de becados")
    print("2. Listado con los alumnos de un grupo dado")
    print("3. Visualizar datos del estudiante")
    print("4. listado ordenado por promedio de todas las mujeres de la carrera")
    print("5. Total de varones de un grupo en específico.")
    print("6. salir")


college = CollegeCareer()

while True:
    show_menu()
    value = int(input("Seleccione una opcion: "))

    if value == 1:
        count_scholarship = college.number_of_scholarship_holders()
        print("** La cantidad de estudiantes becados es ", count_scholarship, "\n")

    elif value == 2:
        group_number = input("Ingrese el numero del grupo que desea visualizar: ")
        list_student = college.list_of_students_in_a_given_group(group_number)
        print("** La lista de estudiantes de el grupo que indico es.")
        count = 1
        for student in list_student:
            print(str(count) + "->", student)
            count += 1
        print("\n")

    elif value == 3:
        code_student = input("Ingrese el codigo del estudiante que decea observas sus datos: ")
        student = college.student_visualization(code_student)
        if student is None:
            print("** No existe ningun estuduante con el codigo ingresado")
        else:
            print("** Los datos del estudiante son ", student, "\n")

    elif value == 4:
        list_female = college.female_average_list()
        print("** La lista de mujeres segun su promedio es")
        count = 1
        for student in list_female:
            print(str(count) + "->",student)
            count += 1
        print("\n")
    elif value == 5:
        group_number = input("Ingrese el grupo de estudiates que decea ver cuantos varones estan registrados: ")
        count_male = college.total_male_group(group_number)
        print("La cantidad de estudiantes varones que hay en el grupo mencionado es", count_male, "\n")

    elif value == 6:
        print("Salir, Gracias por utilizar nuestro programa""\n")
        break

    else:
        print("Opcion no valida")
