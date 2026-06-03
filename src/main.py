produtos = {}

def cadastrar_produtos():
    global produtos

    print("Cadastro de Produtos (Deixe o nome vazio para encerrar)")
    
    # Enquanto o usuario nao deixar vazio, ele pode cadastrar quantos produtos ele quiser
    while True:
        nome = input("\nNome do produto: ").strip()
        
        if not nome:
            break
        # Enquanto tiver um nome de produto, ele precisa ter um preco válido
        while True:
            try:
                preco = float(input(f"Preço de '{nome}': "))
                if preco < 0:
                    print("Preço inválido. Digite um valor positivo.")
                    continue
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
        
        # Salva no dicionário global
        produtos[nome] = preco

def calcular_total(produtos):

    total = sum(produtos.values()) # Soma o total dos valores dos produtos
    print(f'Total: {total}')

def produto_mais_caro(produtos):

    mais_caro = max(produtos.values()) # Pega o produdo mais caro de toda a lista
    print(f'Mais caro: {mais_caro}')
    
def produto_mais_barato(produtos):

    mais_barato = min(produtos.values()) # Pega o produto mais barato de toda a lista
    print(f'Mais barato: {mais_barato}')

def calcular_media(produtos):
    soma =  0
    
    for preco in produtos.values(): # Olha todos os valores dos produtos da lista e soma todos eles
        soma += preco
    
    media = soma / len(produtos) # Aqui ele divide pelo tamanho da lista para pegar a media dos valores dos produtos
    print(f"Média: {media:.2f}")
    return media

def procurar_produto(produtos):
    nome_busca = input("\nDigite o nome do produto para buscar: ").strip()
    
    # Busca do tipo linear
    encontrado = False
    for nome in produtos.keys():
        if nome.lower() == nome_busca.lower():
            print(f"Produto encontrado: {nome} - Preço: {produtos[nome]}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Produto '{nome_busca}' não encontrado.")

def remover_produto(produtos):
    nome_para_remover = input("\nDigite o nome do produto para remover: ").strip()
    
    if nome_para_remover in produtos: # Verifica se o produto existe
        del produtos[nome_para_remover] # Deleta o produto
        print(f"Produto '{nome_para_remover}' removido com sucesso.")
    else:
        print(f"Produto '{nome_para_remover}' não encontrado.")

def main():
    global produtos # A variavel global definida na primeira parte do codigo

    print('Bem vindo')
    cadastrar_produtos()

    print('Relatorio final:')

    print('Produtos cadastrados:')
    for nome, preco in produtos.items():
        print(f'- {nome}: R$ {preco:.2f}')

    calcular_total(produtos)
    produto_mais_caro(produtos)
    produto_mais_barato(produtos)
    calcular_media(produtos)

    print('Agora, você pode procurar um produto ou remover ele')
    print('[1] -> procurar produto')
    print('[2] -> remover um produto')
    print('[0] -> para sair do programa')

    escolha_usuario = input()

    match escolha_usuario:
        case '1':
            procurar_produto(produtos)
        case '2':
            remover_produto(produtos)
        case 'e0':
            print('Ate logo')        

if __name__ == "__main__":
    main()
