import pandas as pd
import time

nome="DRE"

path="Tabelas/"+nome+".tex"

planilha = pd.read_excel(
    'Análise financeira Blast Zone.xlsm',
    engine='openpyxl',
    sheet_name=nome,
    nrows=9,
    index_col=0
    )

planilhaextra=pd.read_excel(
    'Análise financeira Blast Zone.xlsm',
    engine='openpyxl',
    sheet_name=nome,
    header=0,
    #skiprows=9,
    index_col=0
    )

print(planilha)

planilha=planilha.style.hide(subset=["Taxa","Acumulado","Média mensal"],axis="columns")

planilha=planilha.format(lambda v: "\\formatarduascasas{"+str(v)+"}" if type(v)!="str" else v,na_rep="")

planilha=planilha.format_index(escape="latex",axis="columns")

#

print(planilhaextra)

planilhaextra=planilhaextra.style.hide(subset=["Taxa","Acumulado","Média mensal"],axis="columns")

planilhaextra=planilhaextra.hide(subset=["Faturamento",
                                               "Custos e descontos",
                                               "Margem bruta",
                                               "Despesas",
                                               "Investimentos",
                                               "Resultado operacional",
                                               "Financiamento",
                                               "Depreciação",
                                               "Resultado líquido"],axis="index")

planilhaextra=planilhaextra.format(lambda v: "\\formatarduascasas{"+str(v)+"}" if type(v)!="str" else v,na_rep="")

planilhaextra=planilhaextra.format_index(escape="latex",axis="columns")

#

planilha=planilha.concat(planilhaextra)

#

planilha.to_latex(path,
                        column_format=" >{\\raggedright}m{2.5cm} >{\\raggedleft\\arraybackslash}m{\\widthof{1.000.000,000}} >{\\raggedleft\\arraybackslash}m{\\widthof{1.000.000,000}} >{\\raggedleft\\arraybackslash}m{\\widthof{1.000.000,000}} >{\\raggedleft\\arraybackslash}m{\\widthof{1.000.000,000}} >{\\raggedleft\\arraybackslash}m{\\widthof{1.000.000,000}}",
                        clines= None,
                        hrules=True
                  )
print()

print("Quadro "+nome+" Feita")

print()

print(str(planilha.to_latex(
                        column_format=" >{\\raggedright}m{3cm} >{\\raggedleft\\arraybackslash}m{2cm} >{\\raggedleft\\arraybackslash}m{2cm}>{\\raggedleft\\arraybackslash}m{2cm}>{\\raggedleft\\arraybackslash}m{2cm}>{\\raggedleft\\arraybackslash}m{2cm}",
                        clines= None,
                        hrules=True
                  )))

time.sleep(5)
