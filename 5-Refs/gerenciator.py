import pkg.Interation as rel

rel.config_path = "pkg/tipos.config"
rel.bib_path = "bib/"
rel.db_path = "db/"


def main():
    rel.ImportConfig()
    print(rel.config["book"][0])
    data = rel.ImportarData()
    data = rel.Interface(data)
    rel.Exportar2Bib(data)
    rel.Exportar2Db(data)


main()
