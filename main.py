from PyQt6 import QtWidgets, uic
import functions as f
import ui_functions as ui

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
login.bt_login.clicked.connect(lambda: ui.login_enter(login, main))
login.bt_cadastrar.clicked.connect(lambda: ui.to_registro(login, registro))

"""Registro"""
registro.bt_erro.clicked.connect(lambda: registro.top.hide())
registro.bt_cadastrar.clicked.connect(lambda: ui.registro_enter(registro, login))
registro.bt_login.clicked.connect(lambda: ui.new_page(registro, login))

'''Main'''
main.bt_fonemas.clicked.connect(lambda: ui.new_page(main, fonemas))
main.bt_audios.clicked.connect(lambda: ui.to_audio(main, audios))
main.bt_gravacao.clicked.connect(lambda: ui.new_page(main, gravacao))

"""Audios"""
audios.bt_toHome.clicked.connect(lambda: ui.new_page(audios, main))
audios.audio_rep.clicked.connect(lambda: f.repAudio("./PACIENTES/audio.wav"))

"""Fonemas"""
fonemas.bt_toHome.clicked.connect(lambda: ui.new_page(fonemas, main))

"""Gravação"""
gravacao.bt_toHome.clicked.connect(lambda: ui.new_page(gravacao, main))
gravacao.bt_gravar.clicked.connect(lambda: gravacao.frame_3.show())
gravacao.bt_gravar.clicked.connect(lambda: f.audio_save(gravacao))
gravacao.bt_escutar.clicked.connect(lambda: f.repAudio("./PACIENTES/audio.wav"))
gravacao.bt_direita.clicked.connect(lambda: ui.gravacao_frases(gravacao))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login.show()
    app.exec()
