import time

try:
    plania = pd.read_excel("../Planilhas/Tabelas.xlsx",
                           sheet_name="LongTab", na_values="~")

    sty = plania.style

    lg.long(sty, "../Tabelas/LongTab.tex",
            environment="longtable",
            caption="Exemplo de longtab"
            )
except FileNotFoundError as e:
    print(f"Arquivo não encontrado!\n{e}")

time.sleep(3)
