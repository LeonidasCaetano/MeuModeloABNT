#========================================================================
#Funções base
#============================================
#Visualizar tabelas
def Visualizar_Tab(cursor):
    tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print("Tabelas no banco de dados:")
    lista=[]
    for tabela in tabelas:
        if tabela[0]=="sqlite_sequence":
            continue
        print(tabela[0])
        lista.append(tabela[0])
    return lista
#============================================
#Existe?
def Tab_Existe(cursor,nome):
    return cursor.execute("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table' AND name=?
    """, (nome,)).fetchone() is not None
#============================================
#Visualizar material de 1 tabela
def Visualizar_Referencia(cursor,tabela):
    if Tab_Existe(cursor,tabela):
        tabela_para_ver = cursor.execute(f"SELECT * FROM {tabela}").fetchall()
        print("Lista das referencias:")
        print(Colunas_Tab(cursor,tabela))
        referencias=[]
        for ref in tabela_para_ver:
            print(ref)
            referencias.append(ref)
        return referencias
    else:
        print("Tabela não existe! Crie a tabela primeiro!")
#============================================
#Colunas de 1 tabela
def Colunas_Tab(cursor,tabela):
    colunas_vector = []
    for coluna in cursor.execute(f"PRAGMA table_info({tabela})").fetchall():
        colunas_vector.append(coluna[1])
    return colunas_vector
#========================================================================
#Funções de interação com o usuário
#============================================
#Adicionar Tabela
def Criar_Tabela(cursor):
    Nome_da_tabela = str(input("Insira o nome para a tabela\n"))
    campos_padronizados = int(input("Campos padronizados?\n1 - Não\n2 - Livro\n3 - Artigo\n4 - Online\n5 - Legislação\n"))
    if campos_padronizados not in [1,2,3,4,5]:
        campos_padronizados = 2
    if campos_padronizados == 1:
        campos = []
        while True:
            apend = input("Insira o campo que aparece nas referências\n")
            if apend == "":
                break
            campos.append(apend)
        campos_str = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ref_key TEXT NOT NULL,
                                ''' + ", ".join(campos)
    else:
        match campos_padronizados:
            case 2:
                campos_str = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ref_key TEXT NOT NULL,
                                author TEXT,
                                title TEXT,
                                subtitle TEXT,
                                date TEXT,
                                location TEXT,
                                publisher TEXT,
                                edition TEXT,
                                url TEXT,
                                urldate TEXT,
                                note TEXT'''
            case 3:
                campos_str = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ref_key TEXT NOT NULL,
                                author TEXT,
                                title TEXT,
                                subtitle TEXT,
                                date TEXT,
                                location TEXT,
                                journaltitle TEXT,
                                edition TEXT,
                                url TEXT,
                                urldate TEXT,
                                note TEXT'''
            case 4:
                campos_str = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ref_key TEXT NOT NULL,
                                author TEXT,
                                title TEXT,
                                subtitle TEXT,
                                date TEXT,
                                location TEXT,
                                publisher TEXT,
                                edition TEXT,
                                url TEXT,
                                urldate TEXT,
                                note TEXT'''
            case 5:
                campos_str = '''id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ref_key TEXT NOT NULL,
                                author TEXT,
                                title TEXT,
                                subtitle TEXT,
                                date TEXT,
                                location TEXT,
                                journaltile TEXT,
                                edition TEXT,
                                url TEXT,
                                urldate TEXT,
                                note TEXT'''
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {Nome_da_tabela} ({campos_str})")
    print("Tabela criada com sucesso!")
#============================================
#Excluir Tabela
def Excluir_Tabela(cursor):
    tabela=input("Deseja excluir qual?\nSe não deseja, insira um número: ")
    try:
        int(tabela)
        print("UFA!\nNada excluido!")
    except ValueError:
        cursor.execute(f"DROP TABLE IF EXISTS {tabela}")
        print("Excluida com sucesso!")
#============================================
#Editar Tabela
def Editar_Tabela(cursor):
    tabela=input("Deseja editar qual?\n")
#============================================
#Adicionar ref
def Adicionar_ref(cursor):
    tabela = str(input("Deseja adicionar a qual?\n"))
    Visualizar_Referencia(cursor,tabela)
    if Tab_Existe(cursor,tabela):
        print("Insira o valor de cada campo a seguir")
        colunas = cursor.execute(f"PRAGMA table_info({tabela})").fetchall()
        colunas_vector = [[], []]
        for coluna in colunas:
            if coluna[1]=="id":
                continue
            entrada = input(f"Insira o valor do campo {coluna[1]} ({coluna[2]}): ")
            colunas_vector[0].append(coluna[1])
            colunas_vector[1].append(entrada)
        valores = [entrada for entrada in colunas_vector[1]]
        string_SQL_Insert = f"INSERT INTO {tabela} (" + ", ".join(colunas_vector[0]) + ") VALUES (" + ", ".join(["?"] * len(valores)) + ")"
        cursor.execute(string_SQL_Insert, valores)
        print("Adicionado com sucesso!")
    else:
        print("Tabela não existe! Crie a tabela primeiro!")
#============================================
#Remover ref
def Remover_Ref(cursor):
    tabela=input("Deseja remover de qual?\n")
    Visualizar_Referencia(cursor,tabela)
    if Tab_Existe(cursor,tabela):
        print("A remoção do conteúdo é irreversivel!")
        print("Esse gerenciador remove por meio das chaves únicas (id e chave de referência)")
        id=(input("Insira o id da referência: "))
        chave=str(input("Insira a chave de referência: "))
        cursor.execute(f"DELETE FROM {tabela} WHERE id=? AND ref_key=?",(id,chave))
        print("Removido com sucesso!")
    else:
        print("Tabela não existe! Crie a tabela primeiro!")
#============================================
#Editar ref
def Editar_Ref(cursor):
    tabela=input("Editar material de qual tabela?\n")
    Visualizar_Referencia(cursor,tabela)
    if Tab_Existe(cursor,tabela):
        print("Insira o valor do id e da chave")
        id=int(input("Insira o id da referência: "))
        chave=str(input("Insira a chave de referência: "))
        print("Insira os campos que deseja editar e os novos valores\n(Insira '' para parar de editar)")
        array_de_sub=[]
        array_valores=[]
        while True:
            campo_local=input("Campo: ")
            if (campo_local==""):
                break
            valor_local=input("Novo valor: ")
            array_de_sub.append(f"{campo_local} = ?")
            array_valores.append(valor_local)
        string_de_sub=", ".join(array_de_sub)
        cursor.execute(f"UPDATE {tabela} SET {string_de_sub} WHERE id={id} AND ref_key='{chave}'",array_valores)
        print("Editado com sucesso!")
    else:
        print("Tabela não existe! Crie a tabela primeiro!")
#============================================
#Visualizar material de 1 tabela
def Visualizar_Ref(cursor):
    Tabela_Visualizar = str(input("Deseja visualizar qual?\n"))
    Visualizar_Referencia(cursor,Tabela_Visualizar)
#============================================
#Atualizar o arquivo bib
def Atualizar_bib(cursor,conexao):
    print("Carregando tabelas")
    tabelas = Visualizar_Tab(cursor)
    with open("referencias.bib", "w", encoding="utf-8") as arquivo:
        for tabela in tabelas:
            if tabela=="sqlite_sequence":
                continue
            arquivo.write("%")
            arquivo.write("="*100)
            arquivo.write(f"\n%{tabela}s\n")
            todas_referencias = Visualizar_Referencia(cursor, tabela)
            for ref in range(0,len(todas_referencias)):
                arquivo.write(f"@{tabela}"+"{"+f"{todas_referencias[ref][1]}")
                for numb_item in range(2,len(Colunas_Tab(cursor,tabela))):
                    if todas_referencias[ref][numb_item]=="":
                        continue
                    arquivo.write(f",\n\t{(Colunas_Tab(cursor,tabela))[numb_item]}"+" = {"+f"{todas_referencias[ref][numb_item]}"+"}")
                arquivo.write("\n}\n\n")
    arquivo.close()
#============================================
#Atualizar word
def Atualizar_word(cursor):
    return None
#========================================================================
