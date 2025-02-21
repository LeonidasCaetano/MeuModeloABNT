import matplotlib.pyplot as plt
import pandas as pd

planilha = pd.read_excel('Questionário - Fliperama Blast Zone (respostas).xlsx',
                         engine='openpyxl',
                         )
print("Planilha aberta")

dadosfem=len(planilha.loc[planilha["Qual seu sexo?"]=="Feminino"])

dadosmasc=len(planilha.loc[planilha["Qual seu sexo?"]=="Masculino"])



sexo = "Masculino","Feminino"
quantidade=[dadosmasc,dadosfem]

print("foi")

figl, axl=plt.subplots()

axl.pie(quantidade, labels=sexo,autopct="%1.2f%%",)

axl.axis("equal")

print("Gerando grafico")
plt.savefig("Graficos/Qual seu sexo.png")
plt.show()

