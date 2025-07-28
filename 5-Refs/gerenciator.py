import Cache.funcs as fx

try:
    data, arquivo = fx.ImportarData()
    config = fx.importbibconfig()
except Exception as e:
    print("Something went wrong during data import:")
    print(e)

data = fx.Interface(data, config)

try:
    fx.Exportar2Db(data, arquivo)
    fx.Exportar2Bib(data, arquivo)
except Exception as e:
    print("Couldn't export data:")
    print(e)
