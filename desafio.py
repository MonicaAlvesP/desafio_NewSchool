# Faça um programa que solicite ao usuário que elle digite uma senha.
# Se a senha digitada for "abcde", exiba a mensagem "Acesso concedido" senão exiba "Acesso negado"

# Definindo uma função para a verificação de senha
def main():
    senha_correta = "abcde"
    num_tentativas = 3

# Enquanto o número de tentativas for maior que zero, este bloco será repetido
    while num_tentativas > 0:
        senha_digitada = input("Digite sua senha (de 5 digitos): ")

        # Condicional para verificar se a senha esta correta
        if senha_digitada == senha_correta:
            print("Acesso concedido.")
            return # termina a função, se ela estiver correta

        # Se a senha estiver incorreta, decremente(tire 1) do número de tentativas restantes
        num_tentativas -= 1 # numero de tentativas menor igual a 1
        print(f"Senha incorreta. Tentativas restantes: {num_tentativas}")

    # Se o número de tentativas acabarem
    print("Acesso negado.")

main()