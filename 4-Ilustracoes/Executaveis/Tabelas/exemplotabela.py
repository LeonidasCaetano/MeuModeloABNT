import time

try:
    plania = pd.read_excel("../Planilhas/Tabelas.xlsx",
                           sheet_name="Tab", na_values="~")

    sty = plania.style

    lg.tex(sty, "../Tabelas/Tab.tex",
           environment="table",
           hrules=True,
           caption="Exemplo de tab",
           position="!h"
           )
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}")

time.sleep(3)
