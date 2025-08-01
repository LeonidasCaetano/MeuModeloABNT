import pandas
from pandas.io.formats.style import Styler

def get_columns(table: str):
    return table[ 17 : table[17:].find("\n") + 17]

def get_content(table: str):
    listofcont = []
    insidecontent = False
    for i in table.splitlines():
        if i == "\\end{longtable}":
            break
        if insidecontent:
            listofcont.append(i)
        if i == "\\endlastfoot":
            insidecontent = True
    return "\n".join(listofcont)

def exportTeX(buf, content, environment, columns, caption, label, head, foot, lastfoot):
    with open(buf, "w", encoding = "utf-8") as tex:
        tex.write(f"\\begin{{{environment}}}{columns}\n")
        tex.write(caption)
        tex.write(label)
        tex.write("\\endfirsthead\n")
        tex.write(head)
        tex.write("\\endhead\n")
        tex.write(foot)
        tex.write("\\endfoot\n")
        tex.write(lastfoot)
        tex.write("\\endlastfoot\n")
        tex.write(f"{content}\n")
        tex.write(f"\\end{{{environment}}}")

def long(self, buf = "tmp.tex", environment = "longtable", 
         columns = None, caption = None, label = None,
         fonte = None, continue_phrase = "Continua na próxima página", 
         **kwargs):
    longstr = self.to_latex(environment="longtable", **kwargs)
    if not columns:
        columns = get_columns(longstr)
    num_colunas = self.data.shape[1]
    thecaption = f"\\caption{{{caption}}}" if caption else ""
    thelabel = f"\\label{{{label}}}\n" if label else "\n"
    thehead = f"\\caption*{{{caption}}}\n" if caption else "\n"
    thefoot = f"\\multicolumn{{{num_colunas}}}{{r}}{{{continue_phrase}}}"
    thefonte = f"[{fonte}]" if fonte else ""
    thelastfoot = f"\\multicolumn{{{num_colunas}}}{{r}}{{\\fonte{thefonte}}}"
    tablecontent = get_content(longstr)
    exportTeX(buf, tablecontent, environment, columns, thecaption, 
              thelabel, thehead, thefoot, thelastfoot)
    
Styler.long = long