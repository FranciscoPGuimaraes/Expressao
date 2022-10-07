import functions as f


# FUNCTIONS

# Função para realizar o login
def login_enter(login, main):  # func para efetuar o login
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


# Função para realizar o cadastro
def registro_enter(registro, login):  # func para efetuar o registro
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


# Função para mudar de tela
def new_page(ui, new):
    new.show()
    ui.close()


# Função para ir ao registro
def to_registro(registro, login):
    registro.show()
    registro.top.hide()
    login.close()


# Função para ir ao registro
def to_audio(main, audio):
    audio.show()
    audio.audio_name.setText("Audio-1")
    main.close()


# Função para gravar as frases
def gravacao_frases(gravacao):
    frase = f.frasesrandom()
    gravacao.label_frase.setText(frase)
    gravacao.label_frase.show()
    gravacao.imagem.setStyleSheet('background-image: url(:/frases_imagens/cachorro.png);')
    gravacao.imagem.show()
