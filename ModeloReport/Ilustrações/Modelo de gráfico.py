import pandas as pd
import matplotlib.pyplot as plt
import time

nome="Detalhada"

path="Graficos/"+nome+".png"

planilha = pd.read_excel(
    'Análise financeira Blast Zone.xlsm',
    engine='openpyxl',
    sheet_name=nome,
    index_col=0
    )

planilha=planilha.rename_axis(index=None,columns="Mês")

custos=planilha["Custos e descontos"]
despesas=planilha["Despesas"]
faturamento=planilha["Financiamento"]
meses=planilha.index

plt.style.use('dark_background')
#plt.style.use('default')  # Voltar ao estilo padrão para evitar fundos automáticos
plt.figure(facecolor='none')  # Fundo transparente para a figura

plt.plot(meses, despesas, label="Despesas", color="yellow")
plt.plot(meses, custos, label="Custos e descontos", color="magenta")
plt.plot(meses, faturamento, label="Financiamento", color="cyan")

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.ylabel("Gasto (R$)")
plt.xlabel("Meses")

plt.savefig(path, bbox_inches='tight', dpi=300)
path="Graficos/"+nome+".pdf"
plt.savefig(path, bbox_inches='tight', dpi=300)
plt.show()

print()

print("Gráfico "+nome+" Feito")

print()

time.sleep(5)
