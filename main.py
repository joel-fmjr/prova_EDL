from lista_encadeada_dupla import ListaEncadeadaDupla
from menu import executa_menu
import os
from utils import salvar_arquivo


def recebe_nome_arquivo():
    nome_arquivo = ''
    while nome_arquivo == '':
        nome_arquivo = str(input(f'Nome do arquivo com a extensão .txt: '))
        extensao = os.path.splitext(nome_arquivo)[-1]
        if extensao != '.txt':
            print('O nome de arquivo não tem a extensão .txt')
            nome_arquivo = ''
    return nome_arquivo

def main():
    nome_arquivo = recebe_nome_arquivo()
    lista = ListaEncadeadaDupla()

    # Tenta abrir arquivo com o nome informado
    try:
        with open(nome_arquivo, 'r+') as arquivo:
            linhas = arquivo.readlines()
    # Cria arquivo com esse nome, caso não exista        
    except:
        arquivo = open(nome_arquivo, "x")
        arquivo.close()
    # Popula nos da lista com as linhas do arquivo    
    else:
        for linha in linhas:
            lista.inserir_final(linha)
        arquivo.close()
    # executa o menu de opções
    finally:
        salvar_mudancas = executa_menu(nome_arquivo, lista)
    
    if salvar_mudancas:
        salvar_arquivo(nome_arquivo, lista)
        return

if __name__ == '__main__':
    main()
