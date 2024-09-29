# 1. Frequência de k-mers em uma sequência de DNA

# K-mers são subsequências de comprimento fixo "k" extraídas de uma sequência biológica, como DNA ou RNA.
# Eles são amplamente utilizados em bioinformática para análises de padrões, montagem de genomas e identificação de sequências repetitivas ou mutações.

# Desenvolva um programa que receba uma string de DNA e um número inteiro k.
# O objetivo é identificar todos os k-mers mais frequentes, ou seja, as subsequências de tamanho k que aparecem com maior frequência no texto.
# O programa deve retornar esses k-mers separados por espaço.

# Exemplo de entrada:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4

# Exemplo de saída:
# CATG GCAT


# 2. Percentual de identidade em alinhamento BLAST
# Crie um programa que leia o arquivo de saída de um alinhamento BLAST (aqruivo resultado.txt), identifique a linha contendo o valor de identidade e o imprima na tela.

# Exemplo de entrada:
# resultado.txt

# Exemplo de saída:
# Identidade: 21%


# 3. Divisão de arquivo FASTA em múltiplos arquivos
# Escreva um programa que leia um arquivo FASTA contendo vários identificadores e suas respectivas sequências.
# O programa deve criar arquivos separados para cada identificador, nomeando-os como o identificador seguido de .fasta.

# Exemplo de entrada:
# >Sequencia1
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
# >Sequencia2
# ATCGGTCGAA
# >Sequencia3
# ATCGGTCGAGCGTGT

# Exemplo de saída:
# Sequencia1.fasta
# Sequencia2.fasta
# Sequencia3.fasta


# 4. Combinação de arquivos FASTA em um único arquivo
# Faça um programa que receba uma lista de arquivos FASTA e combine todo o conteúdo desses arquivos em um único arquivo de saída chamado all.fasta.
# O novo arquivo deve conter todos os identificadores e suas sequências.

# Exemplo de entrada:
# Sequencia1.fasta
# Sequencia2.fasta
# Sequencia3.fasta

# Exemplo de saída:
# all.fasta


# 5. Conversão de formato de aminoácidos
# Crie um programa que leia um arquivo contendo várias linhas, onde cada linha possui o nome de um aminoácido (no formato "nome", "sigla" ou "letra") e o formato desejado para conversão.
# O programa deve retornar todas as conversões de aminoácidos para o formato solicitado.
# A tabela de aminoácidos pode ser encontrada em: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4665559/table/diagnostics-04-00140-t001/

# Exemplo de entrada:
# ALA nome
# V sigla
# Tirosina letra

# Exemplo de saída:
# Alanina
# Val
# Y


# 6. Conversão de arquivo PDB para FASTA
# Desenvolva um programa que leia um arquivo no formato PDB, extraia as sequências de aminoácidos de cada cadeia polipeptídica e as converta para o formato FASTA.
# O programa deve gerar um arquivo de saída onde cada identificador corresponde ao código da cadeia extraída.

# Exemplo de entrada:
# 6pjv.pdb

# Exemplo de saída:
# >6PJV_1|Chain A|Sonic hedgehog protein|Homo sapiens (9606)
# GFGKRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKISRNSERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNALAISVMNQWPGVKLRVTEGWDEDGHHSEESLHYEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGG
