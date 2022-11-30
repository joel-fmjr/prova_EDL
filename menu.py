from utils import (
    print_erro,
    print_ok,
    print_verde,
    print_roxo,
    buscar_palavra,
)


def opcoes_menu():
    print('\nMenu de opções:')
    print(f" P - Vai para próxima linha")
    print(f" A - Vai para linha anterior")
    print(f' I - Insere linha depois da linha atual.')
    print(f' R - Remove linha atual.')
    print(f' T - Substitui a linha atual.')
    print(f' S - Salva as alterações e encerra o programa.')
    print(f" B - Busca uma palavra")
    print(f' V - Vai até uma linha # específica.')


def executa_menu(nome_arquivo, lista):
    executar = True
    mostrar_arquivo = True

    while executar:
        mostra_detalhes(nome_arquivo, lista, mostrar_arquivo)
        opcoes_menu()

        opcao = input('Opção do Menu? ').upper()

        if opcao == 'P':
            if lista.lista_vazia() or not lista.tem_proximo():
                print_erro('Não existe próxima linha!')
            else:
                lista.atual = lista.atual.proximo
                print_ok('Movido para a próxima linha.')
        elif opcao == 'A':
            if lista.lista_vazia() or (lista.atual == lista.primeiro):
                print_erro('Não existe linha anterior!')
            else:
                lista.atual = lista.atual.anterior
                print_ok('Movido para a linha anterior')
        elif opcao == 'I':
            item = input('Insira a linha à ser inserida após a linha atual: ')
            lista.inserir_depois(lista.atual, item + '\n')
        elif opcao == 'R':
            if lista.lista_vazia():
                print_erro("Não tem nada à ser removido!")
            else:
                item = lista.remover(lista.atual)
        elif opcao == 'T':
            if lista.lista_vazia():
                print_erro(
                    "Não tem nada à ser substituido. Adicione uma linha ao arquivo primeiro!"
                )
            else:
                item = str(input('Insira a linha substituta: '))
                newLineString = '\n' if lista.tem_proximo() else ''
                replacement = f'{item}{newLineString}'
                lista.atual.valor = replacement
        elif opcao == 'B':
            if lista.lista_vazia():
                print_erro("Não se pode achar algo em uma lista vazia!")
            else:
                word = str(input('Insira uma palavra à ser buscada: '))
                buscar_palavra(word, lista)

        elif opcao == 'V':
            if lista.lista_vazia():
                print_erro('A lista está vazia!')
            else:
                linha = int(
                    input("Insira o número da linha que você gostaria de ir.")
                )
                lista.buscar_no(linha)
        elif opcao == 'S':
            executar = False
            print_verde('Salvando suas alterações....')
            return True
        else:
            print_erro('Escolha de menu invalida!')


def mostra_detalhes(nome_arquivo, lista, mostrar_arquivo):
    print('\n===============================================================')
    print_roxo(f'Arquivo atual: {nome_arquivo}')

    if lista.lista_vazia():
        print_erro('Esse é um arquivo vazio. Escreva algo!')
    else:
        print_roxo(f'Linha atual: {lista.atual.valor}')
    if mostrar_arquivo:
        lista.imprimir(lista.primeiro)
