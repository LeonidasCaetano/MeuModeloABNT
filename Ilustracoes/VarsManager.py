import pandas as pd
import time

def Ler_planilha(xlsx,pagina="Dumb vars"):
        return (pd.read_excel(
        xlsx,
        engine = "openpyxl",
        sheet_name = pagina
        )).sort_values(by='Tabela')

print("Lembre-se de organizar os dados nas colunas 'Tabela', 'Índice' e 'Valor'")
print("Nome do arquivo e a página que estão as variáveis")
xlsx=input("Nome da planilha (Com extensão): ")
pagina=input("Nome da página que contém as variáveis: ")
export=input("Arquivo para exportar a base: ")

try:
        plania=Ler_planilha(xlsx,pagina)
        
        to_apend=plania["Tabela"]
        
        Tabelas = list(to_apend.unique())
        
        print("\nTabelas a serem criadas: ",Tabelas,"\n")
        
        with open(export, "w") as Lua:
                for k, group in plania.groupby("Tabela"):
                        Lua.write(k + "={")
                        print(k + "={")
                        for _, row in group.iterrows():
                                b = row["Índice"]
                                c = row["Valor"]
                                print(f"\n\t[\"{b}\"] = {c},")
                                Lua.write(f"\n\t[\"{b}\"] = {c},")
                        Lua.write("\n}\n")
                        print("\n}\n")
        Lua.close()
        
        print(f"Arquivo {export} exportado com sucesso!")
        
except FileNotFoundError:
        print("Erro ao ler a planilha")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
time.sleep(5)
