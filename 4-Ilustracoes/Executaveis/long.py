import re 
import pandas
from pandas.io.formats.style import Styler

def get_columns(table: str):
    return table[ 18 : table[18:].find("\n") + 17]

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

def get_header(table: str):
    firsthead_match = re.search(r"\\begin\{longtable\}\{.*?\}(.*?)\\endfirsthead", table, re.DOTALL)
    head_match = re.search(r"\\endfirsthead(.*?)\\endhead", table, re.DOTALL)
    firsthead = firsthead_match.group(1).strip() if firsthead_match else ""
    head = head_match.group(1).strip() if head_match else ""
    return f"{firsthead}\n\\endfirsthead\n{head}\n\\endhead"
    
def get_length(table: str):
    match = re.search(r"\\endhead.*?\\multicolumn\{(\d+)\}", table, re.DOTALL)
    return  match.group(1).strip() if match else "1"

def makefoot(fonte: str| None, continue_phrase: str| None, cols: int, hlines):
    rules = ("\\midrule", "\\bottomrule") if hlines else ("\\hline", "\\hline")
    foot = f"{rules[0]}\n{f"\\multicolumn{{{cols}}}{{r}}{{{continue_phrase}}}\n" if continue_phrase else ""}\\endfoot\n"
    lastfoot = f"{rules[1]}\n\\multicolumn{{{cols}}}{{c}}{{\\fonte{"["+fonte+"]" if fonte else ""}}}\n\\endlastfoot\n"
    return foot + lastfoot

def makestring(content: str, env: tuple, header: tuple):
    head = f"\\begin{{{env[0]}}}{{{env[1]}}}\n{header[0]}\n{header[1]}" if env[0] and header[0] else ""
    lastline = f"\n\\end{{{env[0]}}}" if env[0] and header[0] else ""
    return f"{head}{content}{lastline}"

def exportTeX(buf: str, table: str):
  with open(buf, "w", encoding = "utf-8") as tex:
        tex.write(table)

def long(self: Styler, buf = None, environment = None, 
         column_format = None, caption = None, label = None,
         fonte = None, continue_phrase = "Continua na próxima página", 
         **kwargs):
    longstr = self.to_latex(environment="longtable", caption = caption, label = label, hrules = True, **kwargs)
    if not column_format:
        column_format = get_columns(longstr)
    headers = get_header(longstr)
    num_colunas = get_length(longstr)
    foot = makefoot(fonte, continue_phrase, num_colunas, environment == "longtable")
    tablecontent = get_content(longstr)
    tablestr = makestring(tablecontent, (environment, column_format), (headers, foot))
    if not buf:
        return tablestr
    exportTeX(buf, tablestr)

def tex(self: Styler, buf = None, environment = None, 
         column_format = None, caption = None, label = None,
         fonte = None, **kwargs):
    tablestr = self.to_latex(environment = environment, column_format = column_format, caption = caption, label = label, **kwargs)
    tablelist = tablestr.splitlines()
    tablelist.insert(-1, "\\fonte" + (f"[{fonte}]" if fonte else ""))
    tablestr = "\n".join(tablelist)
    if not buf:
        return tablestr
    exportTeX(buf, tablestr)
    
Styler.long_to_latex = long
Styler.to_tex = tex