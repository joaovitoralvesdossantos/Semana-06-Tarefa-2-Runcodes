# Calcula a quantidade de caracteres em uma frase
def caracteres(frase):
    frase = len(frase)
    return frase

# Função principal
def main():

    #entrada de dados
    frase = input("Digite uma frase: ").strip()
    
    #processamento
    resultado = caracteres(frase)
    
    #saida de dados
    print(f"A frase '{frase}' tem {resultado} caracteres.")

# Chama a função principal
if __name__ == '__main__':
    main()