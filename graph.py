# requirements.txt
import matplotlib.pyplot as plt
import numpy as np

# Notas dos alunos e total de questões
notas = [34, 42, 31, 33, 39, 50, 37, 35, 32, 32, 35, 31, 40, 35, 54, 40, 37, 39, 40, 42, 27, 36, 27, 27]
total_questoes = 60

# Nomes dos alunos
nomes = ["Camila", "Marçal", "Paulo Vinicius", "João Willy", "Lucas Mendes", "Rodrigo", "William", "Veronica", "Sofia", "Davi Willian", "Deivison Costa", "Igor Lucena", "Alice", "Shay", "Breno", "Flavianny", "Vinicius", "Davi", "Osiel", "Eloísa", "Mauro", "Amanda", "Jeiel"]

# Define a nota de corte
nota_corte = 35

# Cria uma lista de cores com base na nota de corte
cores = ['green' if nota >= nota_corte else 'red' for nota in notas]

# Ordena as notas e nomes correspondentes
notas, nomes, cores = zip(*sorted(zip(notas, nomes, cores), reverse=True))

# Cria o gráfico de barras
plt.bar(range(len(notas)), notas, color=cores)
plt.xticks(range(len(notas)), nomes, rotation=90)
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.title("Notas dos Alunos")

# Exibe as notas acima das barras
for i in range(len(notas)):
    plt.text(i, notas[i] + 1, str(notas[i]), ha='center')

# Calcula a média das notas
media = np.mean(notas)

# Mostra o Gráfico e o Corte
plt.show()
print(f"A nota de corte é: {media}")

# https://is.gd/JeielMiranda
