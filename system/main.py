from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from imports.QtDesigner.design import Ui_MainWindow
from imports.validador_de_email import emailValida
from imports.bd_SQlite3 import main
import sqlite3
import sys


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        super().setupUi(self)
        self.setWindowIcon(QIcon('icons\\login_icon.ico'))
        self.setFixedSize(573, 443)
        self.btn_cadastrar.clicked.connect(self.cadastrar)

        #Adicionando imagens
        self.img_nome.setPixmap(QPixmap('imagens\\user.png'))
        self.img_email.setPixmap(QPixmap('imagens\\email.png'))
        self.img_senha.setPixmap(QPixmap('imagens\\senha.png'))
        self.img_senha_login.setPixmap(QPixmap('imagens\\senha.png'))
        self.img_email_login.setPixmap(QPixmap('imagens\\email.png'))
        self.fundo_login.setPixmap(QPixmap('imagens\\fundo_login.jpg'))
        self.btn_sobre.setIcon(QIcon('imagens\\info.png'))
        self.img_nome.setPixmap(QPixmap('imagens\\user.png'))

        self.Senha_cadastro.setEchoMode(
            self.Senha_cadastro.PasswordEchoOnEdit)  # Deixando a senha oculta depois de uma açao
        self.btn_login.clicked.connect(self.validacao_do_login)
        self.Senha_login.setEchoMode(self.Senha_login.Password)
        self.btn_sobre.clicked.connect(self.sobre_o_dev)

    # Cadastro
    def validacao_do_cadastro(self):
        valor_nome = self.Nome_cadastro.text()
        valor_email = self.Email_cadastro.text()
        valor_senha = self.Senha_cadastro.text()

        if valor_nome == '' or valor_senha == '':
            self.Excecoes.setStyleSheet('color:red;border-radius:1px')
            self.Excecoes.setText('Preencha todos os campos.')
            return False

        if emailValida(valor_email):
            self.Excecoes.setStyleSheet('color:lime;border-radius:1px')
            self.Excecoes.setText('Cadastro bem sucedido!')
            return True
        else:
            self.Excecoes.setStyleSheet('color:red;border-radius:1px')
            self.Excecoes.setText('Email ínvalido.')
            return False

    def cadastrar(self):
        valor_nome = self.Nome_cadastro.text()
        valor_email = self.Email_cadastro.text()
        valor_senha = self.Senha_cadastro.text()
        if self.validacao_do_cadastro():
            try:
                bd = main.BancoDeDados(sqlite3.connect('imports\\bd_SQlite3\\users.db'))
                bd.inserir_cadastro(valor_nome, valor_email, valor_senha)
                # limpando os campos de cadastro após ser concluido.
                self.Nome_cadastro.setText('')
                self.Email_cadastro.setText('')
                self.Senha_cadastro.setText('')
            except:
                self.Excecoes.setStyleSheet('color:yellow;border-radius:1px')
                self.Excecoes.setText('E-mail já usado')

    # Login
    def validacao_do_login(self):
        valor_email = self.Email_login.text()
        valor_senha = self.Senha_login.text()

        bd = main.BancoDeDados(sqlite3.connect('imports\\bd_SQlite3\\users.db'))
        dicionario_contas = bd.contas_cadastradas()
        for valor in dicionario_contas:
            if valor['email'] == valor_email and valor['senha'] == valor_senha:
                from imports.QtDesigner.janela_2 import Ui_MainWindow
                self.Excecoes_login.setStyleSheet('color:lime;border-radius:1px')
                self.Excecoes_login.setText('Login efetuado')
                # abrindo segunda janela
                self.janela = QMainWindow()
                self.segunda = Ui_MainWindow()
                self.segunda.setupUi(self.janela)
                self.janela.show()
                self.hide()  # fechando a ultima janela, aq no caso é a primeira.

        self.Excecoes_login.setStyleSheet('color:red;border-radius:1px; background-color: transparent;')
        self.Excecoes_login.setText('Email ou senha incorretos')

    # sobre
    def sobre_o_dev(self):
        from imports.QtDesigner.sobre import Ui_Sobre
        self.janela = QMainWindow()
        self.janela.setWindowIcon(QIcon('icons\\info.ico'))  # adicionando icon
        self.sobre = Ui_Sobre()
        self.sobre.setupUi(self.janela)
        self.sobre.github.setPixmap(QPixmap('imagens\\github.png'))
        self.sobre.LocalImagem.setPixmap(QPixmap('imagens\\eu.jpeg'))
        self.sobre.btn_voltar.setIcon(QIcon('imagens\\voltar.png'))
        self.sobre.linkedin.setPixmap(QPixmap('imagens\\linkedin.png'))
        self.sobre.email.setPixmap(QPixmap('imagens\\gmail.png'))
        self.janela.show()


if __name__ == '__main__':
    go = QApplication(sys.argv)
    app = App()
    app.show()
    go.exec_()
