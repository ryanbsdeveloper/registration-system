import sqlite3

class BancoDeDados():
    def __init__(self, conexao):
        self._conexao = conexao
        self._cursor = self._conexao.cursor()

    def inserir_cadastro(self, nome, email, senha):
        consulta = 'INSERT INTO clientes (nome, email, senha) VALUES(?,?,?)'
        self._cursor.execute(consulta, (nome, email, senha))
        self._conexao.commit()

    def contas_cadastradas(self):
        consulta = 'SELECT * FROM clientes'
        self._cursor.execute(consulta)
        lista = list()
        contas = dict()
        for linha in self._cursor.fetchall():
            nome, email, senha, id = linha
            contas['email'] = email
            contas['senha'] = senha
            lista.append(contas.copy())
        return lista

    def fechar(self):
        self._cursor.close()
        self._conexao.close()


if __name__ == '__main__':
    bd = BancoDeDados(sqlite3.connect('users.db'))
    #bd.inserir_cadastro('RyanTeste', 't@gmail.com', '11111')
    v = bd.contas_cadastradas()
    bd.fechar()
