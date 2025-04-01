import csv
import datetime

# Nome do arquivo CSV onde os registros serão armazenados
FILENAME = "ponto_registro.csv"

# Função para registrar o horário
def registrar_ponto(tipo):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([agora, tipo])
    print(f"{tipo} registrado em {agora}")

# Criando menu
while True:
    print("\n1 - Registrar Entrada")
    print("2 - Registrar Saída")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_ponto("Entrada")
    elif opcao == "2":
        registrar_ponto("Saída")
    elif opcao == "3":
        print("Finalizando...")
        break
    else:
        print("Opção inválida! Tente novamente.")
