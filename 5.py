# V
def fah(fh):
    Fahrenheit = (fh * (9 / 5)) + 32
    return Fahrenheit

# Função principal
def main():

    #entrada de dados
    fh = float(input("Digite a temperatura em Celsius: ").strip())

    #processamento
    fh = fah(fh)
    
    #saida de dados
    print(f"A temperatura em Fahrenheit é: {fh:.2f}")

# Chama a função principal
if __name__ == '__main__':
    main()