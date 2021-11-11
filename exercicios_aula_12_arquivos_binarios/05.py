import struct
Aluno = struct.Struct('9s 30s f') # Criar Struct com o formato do registro
#Subprogramas
def escrever(arq, matricula, nome, cr):
	bloco = Aluno.pack(matricula.encode('utf-8'), nome.encode('utf-8'), cr)
	arq.write(bloco)
def ler(arq):
	bloco = arq.read(Aluno.size)
	campos = Aluno.unpack(bloco)
	return campos[0], campos[1].decode('utf-8').rstrip(chr(0)), campos[2]
# Programa Principal
with open('arquivo.bin', 'w+b') as arq:
	escrever(arq, '213031001', 'Alessandro', 5.4) # chave 0
	escrever(arq, '114031012', 'Dayana', 8.3) # chave 1
	escrever(arq, '214031173', 'Gustavo', 7.2) # chave 2
	arq.seek(2 * Aluno.size)
	matricula, nome, cr = ler(arq)
	print(f'Matricula: {matricula} Nome: {nome} CR: {cr:.1f}')
