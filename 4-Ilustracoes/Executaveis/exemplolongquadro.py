import pandas as pd
import long as lg
import time

try:
    plania = pd.read_excel("../Planilhas/Quadros.xlsx",
                           sheet_name="LongQuadro", na_values="~")

    sty = plania.style

    sty.to_latex()

    sty.set_table_styles([
        {'selector': 'toprule', 'props': ':hline;'},
        {'selector': 'midrule', 'props': ':hline;'},
        {'selector': 'bottomrule', 'props': ':hline;'},
    ], overwrite=True)

    a = lg.long(sty,  # "../Quadros/LongQuadro.tex",
                environment="longquadro",
                caption="Exemplo de longquadro"
                )
    print(a)
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}\n")
except Exception as e:
    print(f"Error\n{e}")

time.sleep(3)
