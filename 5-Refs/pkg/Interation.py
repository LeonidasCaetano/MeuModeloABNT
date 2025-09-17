from prompt_toolkit import prompt
import pkg.refs as ref
import pkg.database as db

config: dict[str, tuple] = {}
config_path = "tipos.config"

bib_path = ""
db_path = ""
file_src: list[str] = []


class InterationError(Exception):
    pass


# =============================================================================


def error_block(f):
    def wrapper(l, v):
        try:
            return f(l, v), True
        except FileNotFoundError:
            print(f"Erro em {v}: Arquivo não encontrado")
        return v, False
    return wrapper


# =============================================================================


def ImportConfig():
    global config
    config = db.importbibconfig(config_path)


def get_option(
    part_config: tuple[tuple[str, ...], ...],
    ref: dict = {}
) -> dict[str, str]:
    contents: dict[str, str] = dict()
    for campo in part_config[0]:
        contents[campo] = prompt(campo, default=ref.get(campo, ""))
    opt = input("Deseja verificar campos opcionais? Y/n\n")
    if opt == "Y":
        for campos in part_config[1:]:
            for campo in campos:
                contents[campo] = prompt(
                    f"{campo}: ", default=ref.get(campo, ""))
    return contents


# =============================================================================


def InsertRef(data: dict = {}):
    tipo = prompt("Insira o tipo da referencia: ", default="book")
    if tipo not in config:
        raise InterationError("Tipo de referência não definido")
    chave = prompt("Insira a chave da referência: ")
    change = get_option(config[tipo], {})
    data = ref.insertref(change, chave, tipo, data)
    return data


def EditarRef(data: dict):
    tipo = prompt("Insira o tipo da referencia: ", default="book")
    if tipo not in config:
        raise InterationError("Tipo de referência não definido")
    chave = prompt("Insira a chave da referência: ")
    if tipo not in data or chave not in data[tipo]:
        raise InterationError("Referência não existe!")
    change = get_option(config[tipo], data[tipo][chave])
    data = ref.editref(change, chave, tipo, data)
    return data


def RemoverRef(data: dict):
    tipo = prompt("Insira o tipo da referencia: ", default="book")
    if tipo not in config:
        raise InterationError("Tipo de referência não definido")
    chave = prompt("Insira a chave da referência: ")
    data = ref.removeref(chave, tipo, data)
    return data


def Visualizarref(data: dict) -> None:
    tipo = prompt(
        "Insira o tipo da referencia a ser visualizado: ", default="todos")
    ref.visualizardata(data, config, tipo)


# =============================================================================


def ImportarData(data: dict = {}):
    global file_src
    print("Insira o nome dos arquivos que estão as referencias um a um (somente nome)")
    print("Se não existir mais, insira um espaço em branco")
    while True:
        newfile = input(f"1º arquivo: ")
        if newfile.strip() == "":
            break

        if newfile in file_src:
            print("Arquivo já carregado")
            continue

        data, scss = error_block(db.db2data)(newfile, data)
        if scss:
            file_src.append(newfile.strip())
    return data


def Exportar2Bib(data: dict):
    bib_arq = file_src[0] if len(file_src) == 1 else input(
        "Para qual arquivo deve-se exportar as referências feitas? ")
    dest_bib = f"{bib_path}{bib_arq}.bib"
    db.data2bib(data, dest_bib)


def Exportar2Db(data: dict):
    db_arq = file_src[0] if len(file_src) == 1 else input(
        "Para qual arquivo deve-se exportar os dados? ")
    dest_db = f"{db_path}{db_arq}.refdb"
    db.data2db(data, dest_db)


# =============================================================================


def Get_entrada_opt():
    print("""
\t1 - Inserir Referência
\t2 - Editar Referência
\t3 - Remover Referência
\t4 - Visualizar
\t5 - Prosseguir""")
    return input("Opção: ")


def Interface(data):
    try:
        while True:
            entrada = Get_entrada_opt()
            match entrada:
                case "1":
                    data = InsertRef(data)
                case "2":
                    data = EditarRef(data)
                case "3":
                    data = RemoverRef(data)
                case "4":
                    Visualizarref(data)
                case "5":
                    break
                case _:
                    print("Insira uma opção válida!")
    except InterationError as e:
        print("Something went wrong")
        print(e)
    except Exception as e:
        print("Something went wrong")
        print(e)
    return data
