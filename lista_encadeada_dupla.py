from no import No
import gc


class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.atual = self.primeiro

    def tem_proximo(self):
        return self.atual.proximo != None

    def lista_vazia(self):
        return self.primeiro == None

    def buscar_no(self, pulos):
        temp = self.primeiro
        pulos -= 1
        while pulos > 0:
            if temp:
                temp = temp.proximo
                pulos -= 1
            else:
                print('lista não tem tantos nós')
                break
        else:
            self.atual = temp

    def inserir_inicio(self, valor):

        novo_no = No(valor)

        novo_no.proximo = self.primeiro

        if not self.lista_vazia():
            self.primeiro.anterior = novo_no

        self.primeiro = novo_no
        self.atual = self.primeiro

    def inserir_depois(self, no_anterior, valor):

        if no_anterior is None:
            self.inserir_inicio(valor)
            return

        novo_no = No(valor)
        novo_no.proximo = no_anterior.proximo
        no_anterior.proximo = novo_no
        novo_no.anterior = no_anterior

        if novo_no.proximo:
            novo_no.proximo.anterior = novo_no
        self.atual = novo_no

    def inserir_final(self, valor):

        novo_no = No(valor)

        if self.primeiro is None:
            self.primeiro = novo_no
            return

        ultimo = self.primeiro
        while ultimo.proximo:
            ultimo = ultimo.proximo

        ultimo.proximo = novo_no

        novo_no.anterior = ultimo
        self.atual = novo_no

        return

    def remover(self, no_a_deletar):

        if self.primeiro is None or no_a_deletar is None:
            return

        if self.primeiro == no_a_deletar:
            self.primeiro = no_a_deletar.proximo
            if no_a_deletar == self.atual:
                self.atual = self.primeiro

        if no_a_deletar.proximo is not None:
            no_a_deletar.proximo.anterior = no_a_deletar.anterior
            if self.atual == no_a_deletar:
                self.atual = no_a_deletar.proximo

        if no_a_deletar.anterior is not None:
            no_a_deletar.anterior.proximo = no_a_deletar.proximo
            if self.atual == no_a_deletar:
                self.atual = no_a_deletar.anterior

        gc.collect()

    def imprimir(self, no):
        while no:
            print(' {}'.format(no.valor), end='')
            no = no.proximo
