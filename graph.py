# requirements.txt
import matplotlib.pyplot as plt
import numpy as np

# Notas dos alunos e total de questões
notas = [34, 42, 31, 33, 39, 50, 37, 35, 32, 32, 35, 31, 40, 35, 54, 40, 37, 39, 40, 42, 27, 36, 26, 27]
total_questoes = 60

# Nomes dos alunos
nomes = ["Camila", "Marçal", "Paulo Vinicius", "João Willy", "Lucas Mendes", "Rodrigo", "William", "Veronica", "Sofia", "Davi Willian", "Deivison Costa", "Igor Lucena", "Alice", "Shay", "Breno", "Flavianny", "Vinicius", "Davi", "Osiel", "Eloísa", "Mauro", "Amanda", "Herik", "Jeiel"]

# Define a nota de corte
nota_corte = 35

# Cria uma lista de cores com base na nota de corte
cores = ['green' if nota >= nota_corte else 'red' for nota in notas]

# Ordena as notas e nomes correspondentes
notas_ordenadas, nomes_ordenados, cores_ordenadas = zip(*sorted(zip(notas, nomes, cores), reverse=True))

# Cria o gráfico de barras
plt.bar(range(len(nomes)), notas_ordenadas, color=cores_ordenadas)
plt.xticks(range(len(nomes)), nomes_ordenados, rotation=90)
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.title("Notas dos Alunos")

# Exibe as notas originais acima das barras
for i in range(len(nomes)):
    plt.text(i, notas_ordenadas[i] + 1, str(notas_ordenadas[i]), ha='center')

# Calcula a média das notas
media = np.mean(notas)

# Mostra o Gráfico
plt.show()
print(f"A nota de corte é: {media}")

# https://is.gd/JeielMiranda
