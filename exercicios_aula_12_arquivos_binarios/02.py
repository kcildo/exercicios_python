# Exemplos de Escrita em Arquivo Binário

#Subprogramas
# Cópia do conteúdo de um arquivo binário para outro
def copia():
    with open('origem.bin', 'rb') as entrada:
        with open('destino.bin', 'wb') as saida:
            byte = entrada.read(1)
            while byte != b'':
                saida.write(byte)
                byte = entrada.read(1)
    return None


# Escrita de um valor inteiro e um ponto flutuante com precisão dupla
def escreveInteReal():
    import struct
    try:
        with open('arquivo4.bin', 'wb') as arq:
            bloco = struct.pack('i', 10)
            arq.write(bloco)
            bloco = struct.pack('d', 99.5)
            arq.write(bloco)
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')

# Escrita de um string binarizado no arquivo
def escreveBin():
    try:
        with open('arquivo5.bin', 'wb') as arq:
            texto = 'Sou aluno do CEDERJ'
            bloco = texto.encode('utf-8') # Conversão do String em bloco de bytes
            arq.write(bloco)
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')
    return None

#Programa Principal
copia()
escreveInteReal()
escreveBin()