def main():
    while True:
        print_menu()
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                enter_score_and_comment()
            elif num == 2:
                check_results()
            elif num == 3:
                end_program()
                break
            else:
                print("Introduzca un número del 1 al 3")
        else:
            print("Introduzca un número del 1 al 3")


def print_menu():
    print("Seleccione el proceso que desea aplicar")
    print("1: Ingresar puntuación y comentario")
    print("2: Comprueba los resultados obtenidos hasta ahora.")
    print("3: Finalizar")


def enter_score_and_comment():
    while True:
        print("Por favor, introduzca una puntuación en una escala de 1 a 5")
        point = input()

        if point.isdecimal():
            point = int(point)

            if point <= 0 or point > 5:
                print("Por favor, introduzca un valor entre el 1 y 5")
            else:
                comment = input("Por favor, introduzca un comentario: ")
                save_to_file(point, comment)
                break
        else:
            print("Por favor, introduzca la puntuación en números")


def save_to_file(point, comment):
    post = f"punto: {point} comentario: {comment}"
    with open("data.txt", 'a') as file:
        file.write(f"{post}\n")


def check_results():
    print("Resultados hasta la fecha.")
    try:
        with open("data.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No hay resultados guardados aún.")


def end_program():
    print("Finalizando")


# Ejecutar el programa
if __name__ == "__main__":
    main()
