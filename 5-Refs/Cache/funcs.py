from prompt_toolkit import prompt

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

def visualizarref(ref, tipo, data, config):
    print(f"\t{' ' * 4}>>{ref}")
    for k in config[tipo][1]:
        if k in data[tipo][ref]:
            print(f"\t\t{k}: {data[tipo][ref][k]}")

def visualizardata(data, config, opt):
    match str(opt):
        case 'todos':
            for tipo in data:
                print(f"\t>{tipo}:")
                for ref in data[tipo]:
                    visualizarref(ref, tipo, data, config)
        case _:
            if not (opt in data):
                print(f"{opt} type is not in data")
                return
            print(f"\t>{opt}:")
            for ref in data[opt]:
                visualizarref(ref, opt, data, config)

def getfields_edit(ref, tipo, data, config):
    listofchange = {}
    for field in config[tipo][1]:
        defau = data[tipo][ref][field] if field in data[tipo][ref] else ""
        listofchange = getfield(field, listofchange, defau)
    for groupofF in config[tipo][0]:
        if input("Prosseguir com campos opcionais?\n 1 - Sim\n 2 - Não\n") == "1":
            for field in groupofF:
                listofchange = getfield(field, listofchange)
    return listofchange

def getfields_insert(ref, tipo, data, config):
    listofchange = {}
    for field in config[tipo][1]:
        listofchange = getfield(field, listofchange)
    for groupofF in config[tipo][0]:
        if input("Prosseguir com campos opcionais?\n 1 - Sim\n 2 - Não\n") == "1":
            for field in groupofF:
                listofchange = getfield(field, listofchange)
    return listofchange

def getfield(field, listofchange, defau = ""):
    tmp = prompt(f"{" "*4}{field}: ", default = defau)
    if tmp not in ["", defau]:
        listofchange[field] = tmp
    return listofchange

#Interação

def Visualizarref(data, config):
    entrada = prompt("Deseja visualizar qual tipo de referência? ", default = "todos")
    visualizardata(data, config, entrada)

def EditarRef(data, config):
    try:
        tipo = input("Qual o tipo da referência que deseja editar? ")
        if tipo not in data:
            raise IndexError(f"{tipo} type not in data")
        visualizardata(data, config, tipo)
        ref = input("Qual a chave dela? ")
        if ref not in data[tipo]:
            raise IndexError(f"{ref} not in data")
        listofchange = getfields_edit(ref, tipo, data, config)
        return editref(listofchange, ref, tipo, data)
    except Exception as e:
        print(e)
        return data

def RemoverRef(data, config):
    tipo = input("Qual o tipo da referência que deseja remover? ")
    visualizardata(data, config, tipo)
    ref = input("Qual a chave dela? ")
    return removeref(ref, tipo, data)

def InsertRef(data, config):
    try:
        tipo = input("Qual o tipo da referência que deseja inserir? ")
        if tipo not in config:
            raise IndexError(f"Error! {tipo} not defined for Gerenciator")
        ref = input("Qual a chave dela? ")
        listoffields = getfields_insert(ref, tipo, data, config)
        return insertref(listoffields, ref, tipo, data)
    except Exception as e:
        print(e)
        return data

def Exportar2Bib(data, arquivo):
    if data == {}:
        print("Theres no data in storge to save")
        return
    if arquivo == "":
        arq = prompt("Insira o nome do arquivo no qual as referencias serão exportadas (sem extensão): ", 
                default = "referencias") + ".bib"
    else:
        arq = ".".join(arquivo.split(".")[:-1]) + ".bib"
    data2bib(data, arq)

def Exportar2Db(data, arquivo):
    if data == {}:
        print("Theres no data in storge to export")
        return 
    if arquivo == "":
        arquivo = "Cache/" + prompt("Insira o nome do arquivo no qual as referencias serão armazenadas (sem extensão): ", 
                default = "referencias") + ".refdb"
    data2db(data, arquivo)

def ImportarData():
    arquivo = prompt("Insira o nome do arquivo no qual as referencias serão armazenadas (sem extensão): ", 
                default = "referencias") + ".refdb"
    data = db2data("Cache/" + arquivo, {})
    morearq = False
    while True:
        arq = input("Pegar dados de algum outro arquivo? ")
        if arq == "":
            break
        data = db2data("Cache/" + arq + ".refdb", data)
        morearq = True
    if morearq:
        arquivo = ""
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
                    data = RemoverRef(data, config)
                case "4":
                    Visualizarref(data, config)
                case "5":
                    break
                case _  :
                    print("Insira uma opção válida!")
    except Exception as e:
        print("Something went wrong")
        print(e)
    return data

#Leitura

def importbibconfig():
    config = {}
    with open("Cache/tipos.config","r") as basic:
        for linha in basic:
            config = line2bibconfig(linha, config)
    return config

def line2bibconfig(linha, config):
    partes = linha.strip().split(" --required-- ")
    grupo1 = [parte.split() for parte in partes[0].split(" --part-- ")]
    grupo2 = partes[1].split()
    tipo = grupo2.pop()
    config[tipo] = [grupo1, grupo2]
    return config

def db2data(db, data):
    try:
        with open(db, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                newref = line2ref(linha)
                data = insertref(newref[0], newref[1], newref[2], data)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)
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
