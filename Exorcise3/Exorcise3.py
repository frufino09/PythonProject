from Series import Series


def show_menu():
    print("1. El nombre de pelotero de más veces a bateado.")
    print("2. Los datos del pelotero de mayor average. ")
    print("3. lista de los jugadores del equipo ganador")
    print("4. salir")


series = Series()

while True:
    show_menu()
    value = int(input("Selccione una opcion: "))

    if value == 1:
        name_player = series.name_player_more_batted()
        print("El jugador que mas a bateado es: ", name_player,"\n")

    elif value == 2:
        data_player = series.data_the_player_highest_average()
        print("El jugador con mejor promedio es:  ", data_player,"\n")

    elif value == 3:
        lits_player = series.list_of_players_of_the_winning_team()
        print("La lista de jugadores del equipo ganador de esta semana es: ", lits_player)
        count = 1
        for equipament in lits_player:
            print(str(count) + "->", equipament)
            count += 1
        print("\n")

    elif value == 4:
        print("Salir, Gracias por utilizar nuestro programa")
        break
