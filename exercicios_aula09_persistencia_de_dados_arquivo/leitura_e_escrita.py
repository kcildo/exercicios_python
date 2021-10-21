dados = open(input(),"r")
nome_aluno = open("nomes.txt","a")
linha = dados.readline()
while (linha!=""):
  nome_aluno.write(linha.split("-")[0]+"\n")
  linha = dados.readline()
dados.close()
nome_aluno.close()

insercao = input().lower()
if (insercao == "s"):
  dados = open("dados.txt","a")
  dados.write(input()+"\n")
  dados.close()