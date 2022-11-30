def buscar_palavra(palavra, lista):
    lista.atual = lista.primeiro
    linha = 1
    linha_atual = lista.atual.valor
    encontrou = False

    while linha_atual is not None and encontrou is False:
        linha_atual = lista.atual.valor
        if palavra.lower() in linha_atual.lower():
            encontrou = True
            print("\nPalavra encontrada: ", linha_atual.replace(palavra, '\033[44;33m{}\033[m'.format(palavra)))
            print("Encontrada na linha", linha)
            return
        else:
            if lista.tem_proximo():
                lista.atual = lista.atual.proximo
                linha += 1
            else:
                linha_atual = None
    if not encontrou:
        print_erro("Palavra não encontrada")
    return
    
def salvar_arquivo(nome_arquivo, lista):
    arquivo = open(nome_arquivo, "w")
    string_do_arquivo = ""
    lista_arquivo = lista

    if not lista_arquivo.lista_vazia():
        lista_arquivo.atual = lista_arquivo.primeiro
        atual = lista_arquivo.primeiro
        while atual is not None:
            atual = lista_arquivo.atual
            linha_a_adicionar = lista_arquivo.atual.valor
            e_ultima_linha = lista_arquivo.tem_proximo()

            if "\n" not in linha_a_adicionar and e_ultima_linha:
                linha_a_adicionar += "\n"
            string_do_arquivo += (linha_a_adicionar)
            if e_ultima_linha:
                lista_arquivo.atual = lista_arquivo.atual.proximo
            else:
                atual = None

    arquivo.write(string_do_arquivo)
    arquivo.close()
    print(f"Alterações salvas no arquivo{nome_arquivo}.")

def print_erro(mensagem):
    print('\033[1;33;31m{}\033[m'.format(mensagem))
def print_ok(mensagem):
    print('\033[1;33;34m{}\033[m'.format(mensagem))
def print_roxo(mensagem):
    print('\033[1;33;35m{}\033[m'.format(mensagem))    
def print_verde(mensagem):
    print('\033[1;33;32m{}\033[m'.format(mensagem))      
