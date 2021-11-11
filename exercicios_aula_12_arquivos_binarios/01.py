# Exemplos de Leitura de Arquivo Binário

#Subprogramas
# Leitura de todos os bytes contidos em um arquivo
def leTudo():
    try:
        with open('arquivo.bin', 'rb') as arq:
            byte = arq.read(1)
            while byte != b'':
                # Faça alguma coisa com o byte lido
                byte = arq.read(1)
                print(byte, end='')
            print()
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')
    return None

# Leitura de um valor inteiro e um ponto flutuante com precisão dupla
def leInteReal():
    import struct
    try:
        with open('arquivo2.bin', 'rb') as arq:
            inteiro = struct.unpack('i', arq.read(4))[0] # Note o acesso “[0]”
            real = struct.unpack('d', arq.read(8))[0]
            print(f'Valor inteiro: {inteiro} Valor real: {real}')
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')
    print()
    return None

# Leitura de um string binarizado que ocupa 16 bytes no arquivo
def leString():
    try:
        with open('arquivo3.bin', 'rb') as arq:
            bloco = arq.read(16)
            texto = bloco.decode('utf-8') # Conversão do bloco em String
            print(texto)
    except IOError:
        print('Erro ao abrir ou ao  manipular o arquivo.')
    return None

#Programa Principal
leTudo()
leInteReal()
leString()