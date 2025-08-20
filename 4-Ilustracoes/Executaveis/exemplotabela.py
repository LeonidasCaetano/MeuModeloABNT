import pandas as pd
import long
import time

try:
    plania = pd.read_excel("../Planilhas/Tabelas.xlsx", sheet_name = "Tab", na_values="~")
    
    sty = plania.style
    
    sty.to_tex("../Tabelas/Tab.tex",
               environment = "table",
               hrules = True,
               caption = "Exemplo de tab",
               position = "!h"
               )
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}")

time.sleep(3)