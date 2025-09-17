import pkg.refs as fx


def importbibconfig(file: str):
    config: dict[str, tuple[list[str], ...]] = dict()
    with open(file, "r", encoding="utf-8") as conf:
        for linha in conf:
            config = line2bibconfig(linha, config)
    return config


def line2bibconfig(linha: str, config: dict):
    opt, req_and_type = linha.strip().split(" --required-- ")
    optional = [part_o_opt.split() for part_o_opt in opt.split(" --part-- ")]
    required = req_and_type.split()
    tipo = required.pop()
    config[tipo] = (required, *optional)
    return config

# import data


def db2data(db: str, data: dict):
    try:
        with open(db, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                newref = line2ref(linha)
                data = fx.insertref(newref[0], newref[1], newref[2], data)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)
    return data


def line2ref(linha: str):
    contents = linha.strip().split("--+--")
    tipo = contents.pop()
    ref = contents.pop()
    campos = {}
    for campo in contents:
        key, value = campo.split("=", 1)
        campos[key] = value
    return (campos, ref, tipo)

# Escrita


def data2db(data: dict, destino: str):
    with open(destino, "w", encoding="utf-8") as arquivo:
        for tipo, listofrefs in data.items():
            for ref, campos in listofrefs.items():
                ref2db(ref, campos, tipo, arquivo)


def ref2db(ref, campos, tipo, arquivo):
    for field, value in campos.items():
        arquivo.write(f"{field}={value}--+--")
    arquivo.write(f"{ref}--+--{tipo}\n")


def data2bib(data: dict, destino: str):
    with open(destino, "w", encoding="utf-8") as arquivo:
        for tipo, listofrefs in data.items():
            arquivo.write(f"%{tipo}\n")
            for ref, campos in listofrefs.items():
                ref2bib(ref, campos, tipo, arquivo)
                arquivo.write("\n")
            arquivo.write("\n")


def ref2bib(ref: str, campos: dict[str, str], tipo: str, arquivo):
    arquivo.write(f"@{tipo}{{{ref}")
    for field, value in campos.items():
        arquivo.write(f",\n\t{field} = {{{value}}}")
    arquivo.write("\n}\n\n")
