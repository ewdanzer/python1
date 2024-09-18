#1. Contagem de Nucleotídeos
# Escreva um programa que leia um arquivo contendo uma sequência de DNA de até 1000 nucleotídeos.
# O programa deve contar e exibir, em uma única linha, o número de ocorrências das letras 'A', 'C', 'G' e 'T', separadas por espaços.

# Exemplo de entrada:
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Exemplo de saída:
# 20 12 17 21


#2. Transcrição de DNA para RNA
# Implemente um programa que leia um arquivo contendo uma sequência de DNA e retorne a versão transcrita para RNA, substituindo todas as ocorrências da base 'T' pela base 'U'.

# Exemplo de entrada:
# GATGGAACTTGACTACGTAAATT
# Exemplo de saída:
# GAUGGAACUUGACUACGUAAAUU



#3. DNA Complementar
# Crie um programa que leia uma sequência de DNA a partir de um arquivo e gere o DNA complementar (fita cDNA), onde as bases 'A' são complementadas por 'T', 'C' por 'G', e vice-versa. A sequência retornada deve ser a inversa da original.

# Exemplo de entrada:
# AAAACCCGGT
# Exemplo de saída:
# ACCGGGTTTT



#4. População de Coelhos
# Desenvolva um programa para calcular o crescimento de uma população de coelhos, usando uma variação da sequência de Fibonacci.
# O programa deve ler um arquivo contendo dois números inteiros: n, o número de meses, e k, o número de pares de filhotes gerados por cada par adulto de coelhos por mês.
# Retorne o número total de pares de coelhos após n meses.

# Exemplo de entrada:
# 5 3
# Exemplo de saída:
# 19



#5. Conteúdo GC em Sequências FASTA
# Faça um programa que leia um arquivo FASTA contendo várias sequências de DNA.
# O programa deve calcular o conteúdo de GC (a porcentagem de bases 'G' e 'C') para cada sequência e retornar o identificador da sequência com o maior conteúdo de GC, seguido pela porcentagem.

# Exemplo de entrada:
# >Sequencia1
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
# >Sequencia2
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
# >Sequencia3
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT

# Exemplo de saída:
# Sequencia3 60.919540



#6. Distância de Hamming
# Escreva um programa que leia um arquivo contendo duas sequências de DNA de mesmo tamanho e retorne a distância de Hamming, que é o número de posições nas quais as sequências diferem.

# Exemplo de entrada:
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Exemplo de saída:
# 7



#7. Tradução de RNA para Proteína
# Crie um programa que leia um arquivo contendo uma sequência de RNA e retorne a sequência de aminoácidos correspondente, de acordo com a tabela de CODONS.

# Exemplo de entrada:
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Exemplo de saída:
# MAMAPRTEINSTRING



#8. Localizando Substrings em DNA
# Escreva um programa que leia um arquivo contendo duas strings de DNA: uma sequência s e um padrão p.
# O programa deve retornar todas as posições (iniciando em 0) onde o padrão ocorre na sequência, separadas por espaços.

# Exemplo de entrada:
# GATATATGCATATACTT
# ATAT
# Exemplo de saída:
# 1 3 9



#9. Splicing de RNA e Tradução
# Desenvolva um programa que leia um arquivo FASTA contendo uma sequência de DNA e várias subsequências que representam introns.
# O programa deve remover os introns e concatenar os exons restantes, retornando a sequência de aminoácidos resultante da tradução da nova sequência.

# Exemplo de entrada:
# >Sequencia4
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Sequencia5
# ATCGGTCGAA
# >Sequencia6
# ATCGGTCGAGCGTGT
# Exemplo de saída:
# MVYIADKQHVASREAYGHMFKVCA