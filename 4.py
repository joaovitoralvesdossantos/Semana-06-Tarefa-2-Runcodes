# V
def ano(anos):
    anos_espaciais = anos / 2
    return anos_espaciais

# Função principal
def main():

    #entrada de dados
    anos = int(input("Digite sua idade: ").strip())

    #processamento
    anos = ano(anos)
    
    #saida de dados
    print(f"Você tem {int(anos)} anos em anos espaciais.")

# Chama a função principal
if __name__ == '__main__':
    main()