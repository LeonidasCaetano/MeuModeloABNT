import time

try:
    plania = pd.read_excel("../Planilhas/Quadros.xlsx",
                           sheet_name="Quadro", na_values="~")

    sty = plania.style

    lg.tex(sty, "../Quadros/Quadro.tex",
           environment="quadro",
           hrules=True,
           caption="Exemplo de quadro",
           position="!h"
           )
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}")

time.sleep(3)
