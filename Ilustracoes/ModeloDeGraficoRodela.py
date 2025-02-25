import matplotlib.pyplot as plt
import pandas as pd

planilha = pd.read_excel('Questionário - Fliperama Blast Zone (respostas).xlsx',
                         engine='openpyxl',
                         
                         )
print("Planilha aberta")

def filtro_local(i):
    bairro_que_mora=1
    return (((planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("pinhais") != -1) and ((planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("dos pinhais") == -1)) or (planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("curitiba") != -1 or (planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("colombo") != -1 or (planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("piraquara") != -1

def filtro_bairro(i):
    return ((planilha["Em qual bairro você mora? (ex: Vila Amélia)"])[i].lower().find("cristo Rei" or "alto da xv" or "capão da Imbuia" or "bairro alto" or "tarumã" or "cajuru" or "atuba" or "maracanã" or "atuba" or "guarani" or "centro" or "jardim primavera" or "planta santa" or "guarituba" 
) != -1) or (((planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("pinhais") != -1) and ((planilha["Em qual cidade você mora? (ex: Pinhais)"])[i].lower().find("dos pinhais") == -1))

def like(i):
    return str((planilha["Por quais motivos você não está satisfeito?"])[i]).lower().find("não gosto de jogar")==-1

nome_da_coluna="Você está satisfeito com a frequência com que joga jogos eletrônicos durante o seu dia a dia?"

nome_da_col="Por quais motivos você não está satisfeito?"

um=0
dois=0
tres=0
quatro=0
cinco=0
        
for i in range(0,len(planilha[nome_da_coluna])):
    if ((planilha[nome_da_coluna])[i] == 1) and filtro_local(i) and filtro_bairro(i) and like(i):
        um+=1
    if ((planilha[nome_da_coluna])[i] == 2) and filtro_local(i) and filtro_bairro(i) and like(i):
        dois+=1
    if ((planilha[nome_da_coluna])[i] == 3) and filtro_local(i) and filtro_bairro(i) and like(i):
        tres+=1
    if ((planilha[nome_da_coluna])[i]== 4) and filtro_local(i) and filtro_bairro(i) and like(i):
        quatro+=1
    if ((planilha[nome_da_coluna])[i] == 5) and filtro_local(i) and filtro_bairro(i) and like(i):
        cinco+=1


print(um+dois+tres+quatro+cinco)

nombres = "Muito insatisfeito","Insatisfeito", "Neutro","Satisfeito","Muito satisfeito"
quantidade=[um,dois,tres,quatro,cinco]
print(quantidade)
print("foi")


figl, axl=plt.subplots()

axl.pie(quantidade, autopct="%1.2f%%",)

axl.axis("equal")

axl.legend(labels=nombres,loc='best', bbox_to_anchor=(1, 1))

print("Gerando grafico")
plt.savefig("Graficos/satisfação.pdf",bbox_inches='tight')
plt.show()

