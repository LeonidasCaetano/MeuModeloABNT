from pathlib import Path
import pandas as pd
import long as lg


def get_option() -> str:
    print("Pastas disponiveis: ")
    diretorio_atual = Path('.')
    for p in diretorio_atual.iterdir():
        if p.is_dir() and not p.name.startswith((".", "_")):
            print(f"\t{p.name}")
    return input("Pasta escolhida: ")


def list_exec(pasta: str) -> list[str]:
    caminho = Path(pasta)
    return [str(arquivo) for arquivo in caminho.glob("*.py") if not arquivo.name.startswith("__")]


def showscripts(executable):
    print("Executáveis na pasta:")
    for script in executable:
        print("\t- ", script)


def get_ridof_opt() -> str:
    print("Options:")
    print("\tall")
    print("\tpart <{n-} with n being a single caracter>")
    print("\tarq <name of the arq>")
    return input("Option: ")


def get_ridof(opt, executable):
    option = opt.split()
    match option[0]:
        case "all":
            return executable
        case "part":
            return [i for i in executable if i[0:1] == option[1][0:1]]
        case "arq":
            return [i for i in executable if i == option[1]]
        case _:
            return []


def get_scripts(executable: list[str]) -> list[str]:
    rid_opt = get_ridof_opt()
    if rid_opt.strip() == "":
        return []
    return get_ridof(rid_opt, executable)


def dofile(arquivo: str, cont: dict = {}) -> bool:
    contexto = cont
    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            exec(arq.read(), contexto)
        return True
    except Exception as e:
        print(f"Error when execting {arquivo}:\n {e}")
        return False


def main():
    pasta = get_option()
    list_of_exec = list_exec(pasta)
    showscripts(list_of_exec)
    list_2_exec = get_scripts(list_of_exec)
    list_of_scss = list()
    for script in list_2_exec:
        longlist = {"lg": lg, "pd": pd} if pasta in (
            "Tabelas", "Quadros") else {}
        list_of_scss.append(dofile(script, longlist))
    for scss, script in zip(list_of_scss, list_2_exec):
        print(f"{script}: {"Sucesso" if scss else "Erro"}")


main()
