pecas = []


def gerar_codigo(pecas):
    tamanho_lista = len(pecas)
    if tamanho_lista > 0:
        ultima_peca = pecas[tamanho_lista - 1]
        ultimo_codigo = ultima_peca['codigo']
        return ultimo_codigo + 1

    return 1


def cadastrar_peca(pecas):
    codigo = gerar_codigo(pecas)
    print(f'\nCódigo da peça: {codigo:03d}')
    nome = input('Por favor entre com o nome da peça: ')
    fabricante = input('Por favor entre com o fabricante da peça: ')
    valor = float(input('Por favor entre com o valor da peça (R$): '))
    peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    pecas.append(peca)
    print('Peça Adicionada!\n')
    return len(pecas)


def imprimir_peca(peca):
    print(f'Código: {peca["codigo"]:03d}')
    print(f'Fabricante: {peca["fabricante"]}')
    print(f'Valor: {peca["valor"]:.2f} R$')
    return f'{peca["codigo"]:03d} {peca["fabricante"]} {peca["valor"]:.2f}'

def consultar_pecas(pecas):
    finaliza_consulta = False
    count = 0
    while not finaliza_consulta:
        print('Você selecionou a opção para consultar peças')
        print('Escolha a opção desejada:')
        print('1 - Consultar todas as pecas')
        print('2 - Consultar peças por código')
        print('3 - Consultar peças por fabricante')
        print('4 - Retornar')
        opcao_consulta = int(input('Opção: '))
        print()
        
        if opcao_consulta == 1:
            for peca in pecas:
                count += 1
                imprimir_peca(peca)
                print('-' * 15)
        elif opcao_consulta == 2:
            codigo = int(input('Digite o código da peça: '))
            for peca in pecas:
                if peca['codigo'] == codigo:
                    count += 1
                    imprimir_peca(peca)
                    print('-' * 15)
                    break
        elif opcao_consulta == 3:
            fabricante = input('Digite o fabricante da peça: ')
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    count += 1
                    imprimir_peca(peca)
                    print('-' * 15)
        elif opcao_consulta == 4:
            finaliza_consulta = True
            print()
        else:
            print('Opção inválida. Tente novamente')
            return -1
    return count


def remover_peca(pecas):
    print('Você selecionou a opção para remover uma peça')
    codigo = int(input('Código da peça a ser removida: '))
    for peca in pecas:
        if peca['codigo'] == codigo:
            pecas.remove(peca)
            break
        
    
    print('Peça removida com sucesso')
    return len(pecas)


# if __name__ == '__main__':
#     opcao = 0
#     while opcao != 4:
#         print('Escolha a opção desejada')
#         print('1 - Cadastrar Peças')
#         print('2 - Consultar Peças')
#         print('3 - Remover Peças')
#         print('4 - Sair')
#         opcao = int(input('Opção desejada: '))

#         if opcao == 1:
#             cadastrar_peca(pecas)
#         elif opcao == 2:
#             consultar_pecas(pecas)
#         elif opcao == 3:
#             remover_peca(pecas)
#         elif opcao > 4 or opcao < 1:
#             print('Opção inválida')

#     print('Obrigado por usar nossos aplicativos')