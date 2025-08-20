import pandas as pd
import long
import time

try:
    plania = pd.read_excel("../Planilhas/Quadros.xlsx", sheet_name = "LongQuadro", na_values="~")
    
    sty = plania.style
    
    sty.to_longtex("../Quadros/LongQuadro.tex",
               environment = "longquadro",
               caption = "Exemplo de longquadro"
               )
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}")
except Exception as e:
    print("Error")
    print(e)

time.sleep(3)