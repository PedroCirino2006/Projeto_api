distancia = float(input("Insira a distância do percurso (em km): "))
velocidade = float(input("Insira a velocidade do veículo (em km/h): "))

tempo_viagem = distancia / velocidade

print(f"O tempo de viagem será de aproximadamente {tempo_viagem:.2f} horas.")