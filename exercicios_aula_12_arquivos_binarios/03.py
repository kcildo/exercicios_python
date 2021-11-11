# Exemplos de Navegação em Arquivo Binário

#Subprogramas
 # Verificando o avanço do cursor de leitura/escrita
def verificaAvancoCursor():
    import struct
    try:
        with open('arquivo.bin', 'rb') as arq:
            pos = arq.tell()
            print('O cursor está no endereço', pos)
            x = struct.unpack('i', arq.read(4))[0]
            pos = arq.tell()
            print('Após ler 4 bytes, ele foi para o endereço', pos)
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')

def verificaTamanho():
    # Verificando o tamanho do arquivo
    try:
        with open('arquivo.bin', 'rb') as arq:
            arq.seek(0, 2)
            tam = arq.tell()
            print(f'O arquivo possui {tam} bytes')
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')

def acessRandominco():
    import struct
    # Acesso randômico para leitura do conteúdo do arquivo
    try:
        with open('arquivo6.bin', 'rb') as arq:
            print('Os 10 primeiros valores inteiros armazenados são')
            for x in range(0, 10):
                print(struct.unpack('i', arq.read(4))[0])
            print('Da posição atual, voltarei o cursor para reler os 5 últimos valores')
            arq.seek(-(4 * 5), 1)
            for x in range(0, 5):
                print(struct.unpack('i', arq.read(4))[0])
            print('Agora voltei para o início do arquivo para reler o primeiro valor')
            arq.seek(0)
            print(struct.unpack('i', arq.read(4))[0])
    except IOError:
        print('Erro ao abrir ou ao manipular o arquivo.')

#Programa Principal
verificaAvancoCursor()
verificaTamanho()
acessRandominco()