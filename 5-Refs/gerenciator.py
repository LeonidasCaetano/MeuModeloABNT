import Funcs as fx

try:
    data = fx.importdata()
except FileNotFoundError:
    data = ###???
except Exception:
    print("Something went wrong")

try: 
    print("Bem vindo ao gerenciator!")
    for i in range(1, 50):
        match input("Escolha o que deseja fazer: "):
            case 1:
                #
            case 2:
                #
            case 3:
                #
            case 4:
                #
            case 5:
                #
            case 6:
                #
            case 7:
                #
            case 8:
                #
            case _:
                #