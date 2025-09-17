# Gerenciamento


def insertref(fields, ref, tipo, data):
    if not (tipo in data):
        data[tipo] = {}
    if ref in data[tipo]:
        raise Exception("Referência já existe")
    data[tipo][ref] = fields
    return data


def removeref(ref, tipo, data):
    try:
        del data[tipo][ref]
    except IndexError:
        raise Exception("Referência não existe")
    return data


def editref(listofchange, ref, tipo, data):
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


def getfield(field, listofchange, defau=""):
    tmp = prompt(f"{" "*4}{field}: ", default=defau)
    if tmp not in ["", defau]:
        listofchange[field] = tmp
    return listofchange
