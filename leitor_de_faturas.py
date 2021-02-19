class LeitorDeTransacoes:

    def le(self):
        lista_linhas = []
        with open("faturas/terceiro-ciclo.ftr") as fileObj:
            for i, line in enumerate(fileObj):
                lista_linhas.append(line)
            print(lista_linhas[1])
