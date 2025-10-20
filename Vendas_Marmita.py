# [EXIGÊNCIA DE CÓDIGO 1 de 8]; [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]
print('Bem-vindo ao Restaurante Joao Pedro A.B Duarte')
print('               ---------Menu--------                       ')
print('--| Tamanho |  Bife Acebolado (BA) | Filé de Frango (FF) |')
print('--|    P    |       R$16,00        |       R$15,00       |')
print('--|    M    |       R$18,00        |       R$17,00       |')
print('--|    G    |       R$22,00        |       R$21,00       |')


total_pedido = 0  # Acumulador do valor total [EXIGÊNCIA DE CÓDIGO 5 de 8]
historico_pedido = ''  # String para acumular os pedidos
contador_pedido = 1     # Contador de itens


while True:  # Loop principal [EXIGÊNCIA DE CÓDIGO 4 de 8]
    # Validação do sabor (BA ou FF)[EXIGÊNCIA DE CÓDIGO 2 de 8]
    while True:
        sabor = input('Qual é o seu sabor favorito? Bife Acebolado (BA) ou Filé de Frango (FF)? ')
        if sabor == 'BA' or sabor == 'ba' or sabor == 'Ba' or sabor == 'bA':
            sabor_nome = 'Bife Acebolado'
            preco_base = 16
            break
        elif sabor == 'FF' or sabor == 'ff' or sabor == 'Ff' or sabor == 'fF':
            sabor_nome = 'Filé de Frango'
            preco_base = 15
            break
        else:
            print('Erro de digitação. Escolha novamente o sabor')
            continue


    # Validação do tamanho (P, M ou G) [EXIGÊNCIA DE CÓDIGO 3 de 8]
    while True:
        tamanho = input('Qual tamanho você prefere? P, M ou G? ')
        if tamanho == 'P' or tamanho == 'p':
            tamanho_nome = 'Pequeno'
            preco = preco_base
            break
        elif tamanho == 'M' or tamanho == 'm':
            tamanho_nome = 'Médio'
            preco = preco_base + 2
            break
        elif tamanho == 'G' or tamanho == 'g':
            tamanho_nome = 'Grande'
            preco = preco_base + 6
            break
        else:
            print('Erro de digitação. Escolha novamente o tamanho')
            continue


    # Atualiza o histórico - += (x =(x+1))
    historico_pedido += f'  {contador_pedido}. {sabor_nome} ({tamanho_nome}): R${preco:.2f}\n'
    contador_pedido += 1
    total_pedido += preco


    # Pergunta se deseja continuar [EXIGÊNCIA DE CÓDIGO 6 de 8]
    while True:
        continuar = input('Deseja mais alguma coisa? Sim (S) ou Não (N)? ')
        if continuar == 'N' or continuar == 'n':
            break  # Sai do loop de continuação
        elif continuar == 'S' or continuar == 's':
            break  # Volta ao início do loop principal
        else:
            print('Erro de digitação. Digite S ou N.')
            continue
   
    if continuar == 'N' or continuar == 'n':
        break  # Encerra o programa [EXIGÊNCIA DE CÓDIGO 7 de 8]


# Exibe pedidos e o total [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]
print('')
print('--- Resumo do Pedido ---')
print(historico_pedido)
print(f'Total a pagar: R${total_pedido:.2f}')
print('')
print('Obrigado e volte sempre!')
print('Restaurante Joao Pedro Alves Branco Duarte')