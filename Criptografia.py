def shift_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # Verifica se é uma letra
            result += chr(ord(char) + shift)  # Substitui pela letra deslocada
        else:
            result += char  # Mantém caracteres que não são letras
    return result

def translate_message(message):
    # Tentando tanto o deslocamento para frente (1) quanto para trás (-1)
    shifted_forward = shift_message(message, 1)
    shifted_backward = shift_message(message, -1)
    
    print(f"Mensagem traduzida para a próxima letra: {shifted_forward}")
    print(f"Mensagem traduzida para a anterior letra: {shifted_backward}")

# Entrada do usuário
action = input("Você deseja 'decodificar' ou 'traduzir' a mensagem? ").strip().lower()

if action == "decodificar":
    message = input("Digite a mensagem codificada para decodificar: ")
    print("Escolha uma opção de decodificação:")
    print("1 - Substituir cada letra pela próxima no alfabeto")
    print("2 - Substituir cada letra pela anterior no alfabeto")
    option = input("Digite 1 ou 2: ").strip()

    if option == "1":
        transformed_message = shift_message(message, 1)
        print("Mensagem criptografada (deslocada para a próxima letra):", transformed_message)
    elif option == "2":
        transformed_message = shift_message(message, -1)
        print("Mensagem descriptografada (deslocada para a anterior letra):", transformed_message)
    else:
        print("Opção inválida. Escolha 1 ou 2.")
elif action == "traduzir":
    message = input("Digite a mensagem codificada para traduzir: ")
    translate_message(message)
else:
    print("Ação inválida. Escolha 'decodificar' ou 'traduzir'.")
