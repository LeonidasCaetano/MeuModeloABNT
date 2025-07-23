from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

#Gerenciamento

def insertref(fields, ref, tipo, data):
    if not (tipo in data):
        data[tipo] = {}
    data[tipo][ref] = fields
    return data

def removeref(ref, tipo, data):
    if tipo in data and ref in data[tipo]:
        del data[tipo][ref]
    return data

def editref(listofchange, ref, tipo, data):
    if tipo in data and ref in data[tipo]:
        for k, v in listofchange.items():
            data[tipo][ref][k] = v
    return data
    
#Interação

def visualizardata(data, config, opt = 'Todos'):
    match str(opt):
        case 'todos':
            for tipo in data:
                for ref in data[tipo]:
                    visualizarref(ref, tipo, data, config)
            print("#=======#")
        case _:
            if not (opt in data):
                print(f"{opt} type is not in data")
                return
            for ref in data[opt]:
                visualizarref(ref, opt, data, config)
            print("#=======#")

def visualizarref(ref, tipo, data, config):
    print(f"#=======#{ref}")
    for k in config[tipo][1]:
        if k in data[tipo][ref]:
            print(f"{k}: {data[tipo][ref][k]}")

def Visualizarref(data, config):
    entrada = prompt("Deseja visualizar qual tipo de referência? ", default = "todos")
    visualizardata(data, config, entrada)

def EditarRef(data, config):
    tipo = prompt("Qual o tipo da referência que deseja editar? ", default = "book")
    ref = prompt("Qual a chave dela? ")
    listofchange = getfields_edit(ref, tipo, data, config)
    return editref(listofchange, ref, tipo, data)

def RemoverRef(data):
    tipo = prompt("Qual o tipo da referência que deseja remover? ", default = "book")
    ref = prompt("Qual a chave dela? ")
    return removeref(ref, tipo, data)

def InsertRef(data, config):
    tipo = prompt("Qual o tipo da referência que deseja inserir? ", default = "book")
    ref = input("Qual a chave dela? ")
    listoffields = getfields_insert(ref, tipo, data, config)
    return insertref(listoffields, ref, tipo, data)

def getfields_edit(ref, tipo, data, config):
    if not (tipo in data) or not (ref in data[tipo]):
        raise IndexError("Error! insert existing fields")
    listofchange = {}
    for field in config[tipo][1]:
        defau = data[tipo][ref][field] if field in data[tipo][ref] else ""
        listofchange = getfield(field, listofchange, defau)
    if input("Prosseguir com campos opcionais?\n 1 - Sim\n 2 - Não\n") == "1":
        for field in config[tipo][0]:
            defau = data[tipo][ref][field] if field in data[tipo][ref] else ""
            listofchange = getfield(field, listofchange, defau)
    return listofchange

def getfields_insert(ref, tipo, data, config):
    if tipo not in config:
        raise IndexError(f"Error! {tipo} not defined for Gerenciator")
    listofchange = {}
    for field in config[tipo][1]:
        listofchange = getfield(field, listofchange)
    if input("Prosseguir com campos opcionais?\n 1 - Sim\n 2 - Não\n") == "1":
        for field in config[tipo][0]:
            listofchange = getfield(field, listofchange)
    return listofchange

def getfield(field, listofchange, defau = ""):
    tmp = prompt(f"{" "*4}{field}: ", default = defau)
    if tmp not in ["", defau]:
        listofchange[field] = tmp
    return listofchange

def Exportar2Bib(data, arquivo):
    if data == {}:
        print("Theres no data in storge to save")
        return 
    arq = ".".join(arquivo.split(".")[:-1]) + ".bib"
    data2bib(data, arq)

def Exportar2Db(data, arquivo):
    if data == {}:
        print("Theres no data in storge to export")
        return 
    data2db(data, arquivo)

def ImportarData():
    arquivo = prompt("Insira o nome do arquivo no qual as referencias serão armazenadas (sem extensão): ", 
                    default = "referencias") + ".refdb"
    data = db2data(arquivo)
    return (data, arquivo)

def Interface(data, config):
    try:
        while True:
            print("""\n\t1 - Inserir Ref\n\t2 - Editar Ref\n\t3 - Remover Ref\n\t4 - Visualizar\n\t5 - Prosseguir""")
            entrada = prompt("Opção: ")
            match entrada:
                case "1":
                    data = InsertRef(data, config)
                case "2":   
                    data = EditarRef(data, config)
                case "3":
                    data = RemoverRef(data)
                case "4":
                    Visualizarref(data, config)
                case "5":
                    break
                case _  :
                    print("Insira uma opção válida!")

    except Exception:
        print("Something went wrong")
    return data

#Leitura

def importbibconfig():
    config = {}
    with open("tipos.config","r") as basic:
        for linha in basic:
            config = line2bibconfig(linha, config)
    return config
        
def line2bibconfig(linha, config):
    contents = linha.strip().split(" required ")
    contents = [contents[0].split(), contents[1].split()]
    tipo = contents[1].pop()
    config[tipo] = (contents[0], contents[1])
    return config

def db2data(db):
    data = {}
    try:
        with open(db, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                newref = line2ref(linha)
                data = insertref(newref[0], newref[1], newref[2], data)
    except FileNotFoundError:
        print("File not found, inicialing with no refs")
    return data

def line2ref(linha):
    contents = linha.strip().split("--+--")
    tipo = contents.pop()
    ref = contents.pop()
    campos = {}
    for campo in contents:
        key, value = campo.split("=",1)
        campos[key] = value
    return (campos, ref, tipo)

#Escrita

def data2db(data, destino):
    with open(destino, "w", encoding="utf-8") as arquivo:
        for tipo, listofrefs in data.items():
            for ref, campos in listofrefs.items():
                ref2db(ref, campos, tipo, arquivo)

def ref2db(ref, campos, tipo, arquivo):
    for field, value in campos.items():
        arquivo.write(f"{field}={value}--+--")
    arquivo.write(f"{ref}--+--{tipo}\n")

def data2bib(data, destino):
    with open(destino, "w", encoding="utf-8") as arquivo:
        for tipo, listofrefs in data.items():
            arquivo.write(f"%{tipo}\n")
            for ref, campos in listofrefs.items():
                ref2bib(ref, campos, tipo, arquivo)
                arquivo.write("\n")
            arquivo.write("\n")

def ref2bib(ref, campos, tipo, arquivo):
    arquivo.write(f"@{tipo}{{{ref}")
    for field, value in campos.items():
        arquivo.write(f",\n\t{field} = {{{value}}}")
    arquivo.write("\n}\n\n")
