## phylogeneticScripts

Simples *scripts* para facilitar a vida de quem trabalha com muitas sequências gênicas

É composto por:

### get_fasta_from_Genomes.py 

Usando o resultado de um BLAST em .txt com formatação default (-outfmt "6), é possível extrair do genoma correspondente .fna as sequências

Para usar, certifique-se de que tenha Python instalado e digite no terminal:

python get_fasta_from_Genomes.py genoma.fna resultadoBLAST.txt escolha_um_nome_para_output.fas


### criaNumerosFasta.py

Cria um arquivo .fas simples com a quantidade de sequências desejadas em ordem crescente. Exemplo:
- Digite a quantidade de sequências: 10
- Digite o nome do output: sequencias.fas

Resultado: um arquivo .fas com 10 vagas para sequências com numeração:
>1

>2

>3
.
.
.
>10





Enjoy
