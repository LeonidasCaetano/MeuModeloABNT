import sqlite3
import time
import Funcs

#========================================================================

print("Bem-vindo ao gerenciador de referências!")

print("Abrindo banco de dados...")
conexao = sqlite3.connect('bibliografia.db')
print("Banco de dados aberto com sucesso!")

cursor = conexao.cursor()

#========================================================================

quebra_de_loop = 0

while True:
    quebra_de_loop += 1
    if quebra_de_loop >= 50:
        print(
            "\nPor favor, execute novamente o arquivo\nLimite de processos atingido (",
            str(quebra_de_loop), ")")
        print("Aproveite e tome um cházinho\n")
        break
    print("\nO que gostaria de fazer?")
    print("1 - Criar nova tabela de referências")
    print("2 - Excluir tabela de referências")
    print("3 - Editar tabela de referências")
    print("4 - Adicionar material utilizado")
    print("5 - Remover material utilizado")
    print("6 - Editar material utilizado")
    print("7 - Visualizar Material das tabelas")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Por favor, insira um valor válido.")
        continue

    try:
        match int(opcao):
            case 1:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Criar_Tabela(cursor)
            case 2:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Excluir_Tabela(cursor)
            case 3:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Editar_Tabela(cursor)
            case 4:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Adicionar_ref(cursor)
            case 5:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Remover_Ref(cursor)
            case 6:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Editar_Ref(cursor)
            case 7:
                Funcs.Visualizar_Tab(cursor)
                Funcs.Visualizar_Ref(cursor)
            case 8:
                print("Saindo")
                break
    except sqlite3.OperationalError:
        print("Problema operacional")
    except sqlite3.InternalError:
        print("Problema interno")
    except sqlite3.ProgrammingError:
        print("problema no programa")
    except sqlite3.IntegrityError:
        print("problema de integridade")
    except ValueError:
        print("Insira um valor válido!")

#========================================================================
print("Base de dados atualizada com sucesso!")

print(
    "Deseja exportar para um arquivo .bib (1), para word (2), para ambos (3) ou não atualizar (4)?"
)

exportar = input()
if exportar not in ["1","2","3","4"]:
    print("Execute o arquivo novamente e insira um valor válido!")
    exportar = 4
else:
    exportar=int(exportar)
try:
    match exportar:
        case 1:
            Funcs.Atualizar_bib(cursor, conexao)
            print("Atualizado com sucesso!")
        case 2:
            Funcs.Atualizar_word(cursor)
            print("Atualizado com sucesso!")
        case 3:
            Funcs.Atualizar_bib(cursor, conexao)
            Funcs.Atualizar_word(cursor)
            print("Atualizado com sucesso!")
        case 4:
            print("Não atualizado")
except sqlite3.OperationalError:
    print("Problema operacional")
    print("Não atualizado")
except sqlite3.InternalError:
    print("Problema interno")
    print("Não atualizado")
except sqlite3.ProgrammingError:
    print("problema no programa")
    print("Não atualizado")
except sqlite3.IntegrityError:
    print("problema de integridade")
    print("Não atualizado")
#========================================================================

print("Fechando banco de dados...")

conexao.commit()

conexao.close()

print("Banco de dados fechado com sucesso!")

print("Obrigado por usar o gerenciator de referências!")

time.sleep(2)

