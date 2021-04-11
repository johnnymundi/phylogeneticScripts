import sys

def cria_numeros(number):
    arquivo = ''
    output = open(sys.argv[1], 'w')

    for i in range(number):
        arquivo = '>' + str(i + 1) + '\n' + '\n'

        output.write(str(arquivo))


number = int(input("Digite a quantidade de sequências que terá o arquivo fasta: "))
cria_numeros(number)
