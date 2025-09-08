import re
from pandas.io.formats.style import Styler


def get_columns(table: str):
    return table[18: table[18:].find("\n") + 17]


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

# ==============================================================================


def get_header(table: str) -> str:
    frst_head_str = r"\\begin\{longtable\}\{.*?\}(.*?)\\endfirsthead"
    firsthead_match = re.search(frst_head_str, table, re.DOTALL)
    head_str = r"\\endfirsthead(.*?)\\endhead"
    head_match = re.search(head_str, table, re.DOTALL)
    firsthead = firsthead_match.group(1).strip() if firsthead_match else ""
    head = head_match.group(1).strip() if head_match else ""
    head = head.replace("\\toprule", "\\midrule", 1)
    return f"{firsthead}\n\\endfirsthead\n{head}\n\\endhead"


def get_length(table: str) -> str:
    match = re.search(r"\\endhead.*?\\multicolumn\{(\d+)\}", table, re.DOTALL)
    return match.group(1).strip() if match else "1"


def getrules(self: Styler) -> tuple[str, str]:
    details = self.table_styles
    bottom = "\\bottomrule"
    mid = "\\midrule"
    if not details:
        return (mid, bottom)
    for i in details:
        if i["selector"] == "bottomrule":
            bottom = "\\" + i["props"][0][1]
        if i["selector"] == "midrule":
            mid = "\\" + i["props"][0][1]
    return (mid, bottom)


def makefoot(fonte: str | None, c_phrase: str | None, c: str, rules: tuple) -> str:
    parc_foot = f"\\multicolumn{{{c}}}{{r}}{{{c_phrase}}}\n" if c_phrase else ""
    foot = f"{rules[0]}\n{parc_foot}\\endfoot\n"
    parc_lst_foot = "{\\fonte" + ("["+fonte+"]"if fonte else "") + "}"
    lastfoot = f"{rules[1]}\n\\multicolumn{{{c}}}{{c}}{parc_lst_foot}\n\\endlastfoot\n"
    return foot + lastfoot

# ==============================================================================


def makestring(content: str, env: tuple, header: tuple) -> str:
    head = f"\\begin{{{env[0]}}}{{{env[1]}}}\n{header[0]}\n{header[1]}"\
        if env[0] and header[0] else ""
    lastline = f"\n\\end{{{env[0]}}}" if env[0] and header[0] else ""
    return f"{head}{content}{lastline}"


def exportTeX(buf: str, table: str) -> None:
    with open(buf, "w", encoding="utf-8") as tex:
        tex.write(table)


def long(
    self: Styler, buf: str | None = None,
    environment: str | None = None,
    column_format: str | None = None,
    caption: str | None = None,
    label: str | None = None,
    fonte: str | None = None,
    continue_phrase: str = "Continua na próxima página",
    **kwargs
) -> str | None:
    """
    Converte uma tabela Styler em uma tabela longtable ou similar;

    Parameters
    ----------
        self: Objeto Styler
        buf: Caminho para exportar, se não informado será retornado 
        environment: tipo da tabela, se não informado será exportado somente o conteúdo
        columns_format: formatação das colunas
        caption: Titulo da tabela
        label: Nome usado para referenciar a tabela (hyperref)
        fonte: Referência utilizada na fonte
        continue_phrase: Frase utilizada no fim de uma página quando a ilustração ainda não acabou
        **kwargs: Outros comandos usados na função Styler.to_latex
    examples
    --------
        >>> sim
    """
    longstr = self.to_latex(environment="longtable", caption=caption,
                            label=label, hrules=True, **kwargs)
    if not column_format:
        column_format = get_columns(longstr)
    headers = get_header(longstr)
    num_colunas = get_length(longstr)
    ruletype = getrules(self)
    foot = makefoot(fonte, continue_phrase, num_colunas, ruletype)
    tablecontent = get_content(longstr)
    tablestr = makestring(
        tablecontent, (environment, column_format), (headers, foot))
    if not buf:
        return tablestr
    exportTeX(buf, tablestr)
    return None


def tex(
    self: Styler,
    buf: str | None,
    environment: str | None,
    column_format: str | None,
    caption: str | None,
    label: str | None,
    fonte: str | None,
    position: str | None,
    **kwargs
):
    tablestr = self.to_latex(environment=environment,
                             column_format=column_format,
                             caption=caption,
                             label=label, position=position, **kwargs)
    tablelist = tablestr.splitlines()
    tablelist.insert(-1, "\n\\fonte" + (f"[{fonte}]" if fonte else ""))
    tablestr = "\n".join(tablelist)
    if not buf:
        return tablestr
    exportTeX(buf, tablestr)
