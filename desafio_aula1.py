nome = input("Digite seu nome: ")
salario_mensal = input("Digite seu salário: ")
bonus = input("Digite o percentual do seu bônus: ")
percentual = 1000 + int(salario_mensal) * float(bonus)

print("Olá, " + nome + ". O seu bônus será de " + str(percentual))

#bugs que podem acontecer

#a pessoa inserir valores com tipos distintos do que se espera