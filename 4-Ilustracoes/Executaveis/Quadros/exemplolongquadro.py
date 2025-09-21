import time

try:
    plania = pd.read_excel("../Planilhas/Quadros.xlsx",
                           sheet_name="LongQuadro", na_values="~")

    sty = plania.style

    sty.set_table_styles([
        {'selector': 'toprule', 'props': ':hline;'},
        {'selector': 'midrule', 'props': ':hline;'},
        {'selector': 'bottomrule', 'props': ':hline;'},
    ], overwrite=True)

    lg.long(sty, "../Quadros/LongQuadro.tex",
            environment="longquadro",
            caption="Exemplo de longquadro"
            )

except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}\n")
except Exception as e:
    print(f"Error\n{e}")

time.sleep(3)
