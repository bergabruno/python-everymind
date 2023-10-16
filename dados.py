import random
import csv

#gerando data para analise

with open('dados.csv', 'w', newline='') as file:
    output = csv.writer(file)

    cidades = ['Sao Paulo', 'Rio de Janeiro', 'Brasilia', 'Porto Alegre', 'Salvador', 'Recife']
    pcds = ['0', '1']
    rendas = ['0', '1']
    racas = ['0', '1', '2', '3', '4']
    generos = ['0', '1', '2']
    idades = ['0', '1']
    cursos = ['Administracao', 'Engenharia Civil', 'Ciencia da Computacao', 'Direito', 'Medicina']
    experiencias = ['0', '1']
    linguas = ['portugues', 'ingles', 'espanhol', 'frances', 'mandarim']
    modalidades = ['presencial', 'EaD', 'semipresencial']

    for _ in range(500):
        cidade = random.choice(cidades)
        pcd = random.choice(pcds)
        renda = random.choice(rendas)
        raca = random.choice(racas)
        genero = random.choice(generos)
        idade = random.choice(idades)
        curso = random.choice(cursos)
        experiencia = random.choice(experiencias)
        lingua = random.choice(linguas)
        modalidade = random.choice(modalidades)


        output.writerow([cidade, pcd, renda, raca, genero, idade, curso, experiencia, lingua, modalidade])


