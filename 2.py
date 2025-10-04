# Calcula o valor inteiro arredondado de um número decimal
def numero_inteiro(round):
    round = int(round)
    return round

# Função principal
def main():

    #entrada de dados
    numero_inteiro = float(input("Digite uma quantidade de dinheiro: ").strip())
    
    #processamento
    resultado = round(numero_inteiro)
    
    #saida de dados
    print(f"O valor arredondado é: {resultado}")

# Chama a função principal
if __name__ == '__main__':
    main()