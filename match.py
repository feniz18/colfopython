opcion = input("ingresa tu opción: ")

match opcion:
    case 'fruta':
        print("selecionaste fruta")
    case 'sopa':
        print("Selecionaste sopa")
    case _:
        print("selececcionaste una opción incorrecta")