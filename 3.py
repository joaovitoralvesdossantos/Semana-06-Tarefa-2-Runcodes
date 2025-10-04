# Calcula o preço final de dois produtos com quantidades diferentes
def preco(prec, prec2):
    preco_final = (prec * 3) + (prec2 * 2)
    return preco_final

# Função principal
def main():

    #entrada de dados
    prec = float(input("Digite o preço da maça: ").strip())
    prec2 = float(input("Digite o preço da banana: ").strip())

    #processamento
    prec = preco(prec, prec2)
    
    #saida de dados
    print(f"O preço final é: {prec:.2f}")

# Chama a função principal
if __name__ == '__main__':
    main()