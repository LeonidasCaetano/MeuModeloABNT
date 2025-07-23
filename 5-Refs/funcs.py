from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

#Gerenciamento

def insertref(ref, data):
    if not (ref[2] in data):
        data[ref[2]] = {}
    data[ref[2]][ref[1]] = ref[0]
    return data

def removeref(tipo, ref, data):
    if tipo in data and ref in data[tipo]:
        del data[tipo][ref]
    return data

def editref(tipo, ref, listofchange, data):
    if tipo in data and ref in data[tipo]:
        for k, v in listofchange.items():
            data[tipo][ref][k] = v
    return data

def append2ref(tipo, ref, listofapend, data)
    
#Interação

def visualizardata(opt = "a")
def visualizarref(ref, tipo, data):

def Visualizar()
def EditarRef()
def RemoverRef()
def InsertRef()

def Exportar2Bib(arq = "referencias.bib", tipo = "a")
def Exportar2Db(arq = "referencias")

def Interface()

#Leitura

def importbibconfig():
    config = {}
    with open("tipos.config","r") as basic:
        for linha in basic:
            config = line2bibconfig(linha, config)
    return config
        
def line2bibconfig(linha, data):
    contents = linha.strip().split(" required ")
    contents = [contents[0].split(), contents[1].split()]
    tipo = contents[1].pop()
    data[tipo] = (contents[0], contents[1])
    return data

def db2data(db, data):
    with open(db, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            newref = line2ref(linha)
            data = insertref(newref, data)
    return data

def line2ref(linha):
    contents = linha.strip().split()
    tipo = contents.pop()
    ref = contents.pop()
    campos = {}
    for campo in contents:
        key, value = campo.split("=",1)
        campos[key] = value
    return (campos, ref, tipo)

#Escrita

def data2db(db, destino):
    with open(destino, "w", encoding="utf-8") as arquivo:
        for tipo, listofrefs in db.items():
            for ref, campos in listofrefs.items():
                ref2db(ref, campos, tipo, arquivo)

def ref2db(ref, campos, tipo, arquivo):
    for field, value in campos.items():
        arquivo.write(f"{field}={value} ")
    arquivo.write(f"{ref} {tipo}\n")

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
