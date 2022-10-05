from PyQt5 import QtWidgets, uic
import functions as f


# FUNCTIONS
def login_enter():  # func para efetuar o login
    email = login.le_email.text()
    senha = login.le_senha.text()

    if email != "":
        if senha != "":
            login.close()
            main.show()
        else:
            login.label_erro.setText("Insira a senha!")
    else:
        if senha != "":
            login.label_erro.setText("Insira o email!")
        else:
            login.label_erro.setText("Coloque seus dados!")
    login.top.show()


def registro_enter():  # func para efetuar o registro
    email = registro.le_email.text()
    senha = registro.le_senha.text()
    confirmar_senha = registro.le_senhaconfirmar.text()

    if email != "":
        if senha != "":
            if senha == confirmar_senha:
                login.show()
                registro.close()
                login.label_erro.setText("Registrado com sucesso!")
            else:
                registro.label_erro.setText("As senhas estão diferentes!")
        else:
            registro.label_erro.setText("Insira a senha!")
    else:
        if senha != "":
            registro.label_erro.setText("Insira o email!")
        else:
            registro.label_erro.setText("Coloque seus dados!")
    registro.top.show()


def to_registro():  # func para ir ao registro
    registro.show()
    registro.top.hide()
    login.close()


def to_login():  # func para ir ao login
    login.show()
    registro.close()


def to_fonemas():  # func para ir para os fonemas
    main.close()
    fonemas.show()


def to_audios():  # func para ir para os fonemas
    main.close()
    audios.show()


def to_gravacao():  # func para ir para os fonemas
    main.close()
    gravacao.show()
    gravacao.label_frase.hide()
    gravacao.imagem.hide()
    gravacao.frame_3.hide()


def audios_to_main():
    audios.close()
    main.show()


def fonemas_to_main():
    fonemas.close()
    main.show()


def gravacao_to_main():
    gravacao.close()
    main.show()


def gravacao_frases():
    frase = f.frasesrandom()
    gravacao.label_frase.setText(frase)
    gravacao.label_frase.show()
    gravacao.imagem.setStyleSheet('background-image: url(:/frases_imagens/cachorro.png);')
    gravacao.imagem.show()


app = QtWidgets.QApplication([])

# PAGINAS
login = uic.loadUi("ui/login.ui")
registro = uic.loadUi("ui/registro.ui")
main = uic.loadUi('ui/main.ui')
audios = uic.loadUi('ui/audios.ui')
fonemas = uic.loadUi('ui/fonemas.ui')
gravacao = uic.loadUi('ui/gravacao.ui')

# CALL FUNCTIONS

"""Login"""
login.bt_erro.clicked.connect(lambda: login.top.hide())
login.bt_login.clicked.connect(lambda: login_enter())
login.bt_cadastrar.clicked.connect(lambda: to_registro())

"""Registro"""
registro.bt_erro.clicked.connect(lambda: registro.top.hide())
registro.bt_cadastrar.clicked.connect(lambda: registro_enter())
registro.bt_login.clicked.connect(lambda: to_login())

'''Main'''
main.bt_fonemas.clicked.connect(lambda: to_fonemas())
main.bt_audios.clicked.connect(lambda: to_audios())
main.bt_gravacao.clicked.connect(lambda: to_gravacao())

"""Audios"""
audios.bt_toHome.clicked.connect(lambda: audios_to_main())

"""Fonemas"""
fonemas.bt_toHome.clicked.connect(lambda: fonemas_to_main())

"""Gravação"""
gravacao.bt_toHome.clicked.connect(lambda: gravacao_to_main())
gravacao.bt_gravar.clicked.connect(lambda: gravacao.frame_3.show())
gravacao.bt_gravar.clicked.connect(lambda: f.audio_save(gravacao))
gravacao.bt_escutar.clicked.connect(lambda: f.repAudio("./PACIENTES/audio.wav"))
gravacao.bt_direita.clicked.connect(lambda: gravacao_frases())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login.show()
    app.exec()
