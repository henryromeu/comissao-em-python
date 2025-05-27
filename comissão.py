# Importa o módulo 'time' para poder usar a função de pausa (sleep)
import time

# Exibe o título do sistema
print("SISTEMA DE COMISSÃO")

# Solicita ao usuário o nome do vendedor e armazena na variável 'nome'
nome = input("\nDigite o nome do vendedor(a): ")

# Solicita ao usuário o valor da venda (faturamento) e converte para float
faturamento = float(input("\nDigite o valor da venda: "))

# Define a primeira meta de faturamento
meta1 = 5000

# Define a comissão associada à meta1 (2.5%)
comissão1 = 0.025

# Calcula o valor da comissão caso o faturamento atinja meta1
ValorComissão1 = comissão1 * faturamento

# Define a segunda meta de faturamento
meta2 = 10000

# Define a comissão associada à meta2 (6%)
comissão2 = 0.06

# Calcula o valor da comissão caso o faturamento atinja meta2
ValorComissão2 = comissão2 * faturamento

# Define uma terceira meta especial (para bônus extraordinário)
meta3 = 100000  # Aqui não há comissão, mas um bônus de 1% da empresa

# Mensagem de processamento para dar um feedback visual ao usuário
print("\nProcessando...")
time.sleep(3)  # Pausa de 3 segundos

# Estrutura condicional que verifica qual meta o vendedor alcançou

# Se o faturamento for igual ou maior que a meta3
if faturamento >= meta3:
    print(f"\nO funcionario(a) {nome} bateu a meta e ganhou 1% DA EMPRESA")

# Se não atingiu meta3 mas atingiu ou superou meta2
elif faturamento >= meta2:
    print(f"\nO funcionario(a) {nome} bateu a meta e ganhou R${ValorComissão2:.2f}!")

# Se não atingiu meta2 mas atingiu ou superou meta1
elif faturamento >= meta1:
    print(f"\nO funcionario(a) {nome} bateu a meta e ganhou R${ValorComissão1:.2f}")

# Se não atingiu nenhuma das metas
else:
    print(f"\nO funcionario(a) {nome} não bateu a meta \nNão desista! No próximo mês você pode alcançar a meta!")

# Mensagem final de agradecimento
print("\nObrigado por usar nossos serviços!")
