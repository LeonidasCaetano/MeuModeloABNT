import Funcs as fx

try:
    data = fx.db2data()
    basic_campus = fx.importbibconfig()
except FileNotFoundError:
    data = {}
except Exception:
    print("Something went wrong")

try: 
    data = fx.Interface()
except Exception:
    print("Error")

try:
    Exportar2Db()
    Exportar2Bib()
except Exception:
    print("Couldnt export")