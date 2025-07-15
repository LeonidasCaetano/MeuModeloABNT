import pandas as pd
import sys

plania = "../Planilhas/" + (sys.argv[1] if len(sys.argv) > 1 else input("Insira o nome da planilha: "))
pagina = (sys.argv[2] if len(sys.argv) > 2 else input("Insira o nome da página: "))

try:
    planilha = pd.read_excel(plania, sheet_name = pagina, na_values = "<NULL>")
    lista = planilha.values.tolist()
    for i in lista:
        for k in i:
            print(k)
        print("\n\n")
    """with open("Vars.lua") as lua:
        for i in planilha.index:
            value = recursive(planilha, )
            lua.write(value)"""

except Exception:
    print("Algo deu errado")