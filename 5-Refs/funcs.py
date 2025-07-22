#Gerenciamento

def insertref(ref, data):
    if not (ref[1] in data):
        data[newref[1]] = []
    return data[newref[1]].append(newref[0])
    
#Interação



#Leitura

def db2data(db, data):
    with open(db, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            newref = line2data(linha)
            data = insertref(newref, data)
    return data

def line2data(linha):
    contents = linha.strip().split()
    tipo = contents.pop()
    newref = ({}, tipo)
    for campo in contents:
        key, value = campo.split("=")
        newref[0][key] = value
    return newref

#Escrita

def data2db(db, destino):
    with open(destino, "w", encoding = "utf-8") as arquivo:
        for tipo, listofrefs in db.items():
            for ref in listofrefs:
                ref2db(ref, tipo, arquivo)

def ref2db(ref, tipo, arquivo):
    for field, value in ref.items():
        arquivo.write(f"{field}={value} ")
    arquivo.write(f"{tipo}\n")

def data2bib(db, destino):
    with open(destino, "w", encoding = "utf-8") as arquivo:
        for tipo, listofrefs in db.items():
            arquivo.write("%" + tipo + "\n")
            for ref in listofrefs:
                ref2bib(ref, tipo, arquivo)
                arquivo.write("\n")
            arquivo.write("\n")

def ref2bib(ref, tipo, arquivo):
    arquivo.write(f"@{tipo}{{{ref['ref']}")
    for field, value in ref.items():
        if field != "ref":
            arquivo.write(f",\n\t{field} = {{{value}}}")
    arquivo.write("\n}\n\n")



    