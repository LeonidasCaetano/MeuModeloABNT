import os
import time

Arquivo="Main"
Arquivos_a_excluir = []

Arquivos_a_excluir.append(Arquivo+".aux")
Arquivos_a_excluir.append(Arquivo+".bbl")
Arquivos_a_excluir.append(Arquivo+".bcf")
Arquivos_a_excluir.append(Arquivo+".blg")
Arquivos_a_excluir.append(Arquivo+".idx")
Arquivos_a_excluir.append(Arquivo+".ilg")
Arquivos_a_excluir.append(Arquivo+".ind")
Arquivos_a_excluir.append(Arquivo+".log")
Arquivos_a_excluir.append(Arquivo+".lol")
Arquivos_a_excluir.append(Arquivo+".lua")
Arquivos_a_excluir.append(Arquivo+".out")
Arquivos_a_excluir.append(Arquivo+".run.xml")
Arquivos_a_excluir.append(Arquivo+".synctex.gz")
Arquivos_a_excluir.append(Arquivo+".synctex(busy)")
Arquivos_a_excluir.append(Arquivo+".toc")
Arquivos_a_excluir.append(Arquivo+".lof")
Arquivos_a_excluir.append(Arquivo+".lot")
Arquivos_a_excluir.append(Arquivo+".loq")
Arquivos_a_excluir.append(Arquivo+".ldg")
Arquivos_a_excluir.append(Arquivo+".loe")
Arquivos_a_excluir.append(Arquivo+".lop")
Arquivos_a_excluir.append(Arquivo+".tdo")

Arquivos_a_excluir.append("Glossario_Ordenada.tex")
Arquivos_a_excluir.append("Lista_de_Abreviaturas_Ordenada.tex")
Arquivos_a_excluir.append("Lista_de_Siglas_Ordenada.tex")
Arquivos_a_excluir.append("Lista_de_Simbolos_Ordenada.tex")

Arquivos_a_excluir.append("palavras.low")

for arquivo in Arquivos_a_excluir:
    if os.path.exists(arquivo):
        os.unlink(arquivo)
        print(arquivo+" foi excluido")

time.sleep(3)
