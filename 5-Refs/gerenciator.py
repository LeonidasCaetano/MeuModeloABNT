import traceback
import funcs as fx

try:
    data, arquivo = fx.ImportarData()
    config = fx.importbibconfig()
except Exception as e:
    print("Something went wrong during data import:")
    traceback.print_exc()

try: 
    data = fx.Interface(data, config)
except Exception as e:
    print("Error during interface interaction:")
    traceback.print_exc()

try:
    fx.Exportar2Db(data, arquivo)
    fx.Exportar2Bib(data, arquivo)
except Exception as e:
    print("Couldn't export data:")
    traceback.print_exc()
