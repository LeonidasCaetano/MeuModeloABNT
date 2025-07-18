import pandas as pd
import sys

plania = "../Planilhas/" + (sys.argv[1] if len(sys.argv) > 1 else input("Insira o nome da planilha: "))
pagina = (sys.argv[2] if len(sys.argv) > 2 else input("Insira o nome da página: "))
dest = "../DumbVars/" + (sys.argv[3] if len(sys.argv) > 3 else input("Insira o arquivo de destino: "))

try:
    planilha = pd.read_excel(plania, sheet_name = pagina)
    lista = planilha.values.tolist()
    with open(dest, "w") as vars:
        for i in lista:
            tmplst = ["",""]
            for k in i:
                if str(k) != "nan":
                    tmplst[0] += ("." if tmplst[0] != "" else "") + str(tmplst[1])
                    tmplst[1] = k
            vars.write(tmplst[0] + " = " + str(tmplst[1]) + "\n")
            print(tmplst[0] + " = " + str(tmplst[1]))
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho e o nome da planilha.")
except PermissionError:
    print("Permissão negada. Feche a planilha se ela estiver aberta em outro programa.")
except ValueError as e:
    print(f"Erro de valor: {e}")
except KeyError:
    print("A aba especificada não foi encontrada.")
except ImportError as e:
    print(f"Erro ao importar bibliotecas necessárias: {e}")
except pd.errors.EmptyDataError:
    print("A planilha está vazia.")
except Exception as e:
    print(f"Erro inesperado: {e}")