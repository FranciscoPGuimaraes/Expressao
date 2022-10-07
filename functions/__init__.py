import pyttsx3
from random import randint
import pyaudio
import wave
from difflib import SequenceMatcher
from array import array
import json as js
import shutil
# import Speech_Recognition as sr
import os
import webbrowser
from datetime import date


# -------------------------------------------FUNCOES---------------------------------------------------------------------
def callback():
    webbrowser.open_new(r"https://inatel.br/ehealth/")


def dataaudio():
    data_atual = date.today()
    data_em_texto = '{}-{}-{}'.format(data_atual.day, data_atual.month, data_atual.year)
    return data_em_texto


# VERIFICAR SE O PACIENTE JA ESTA CADASTRADO
def arquivoex(nome):
    try:
        a = open(f'./PACIENTES/{nome}', 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# CADASTRAR NOVO PACIENTE
def new_pacient(Nome, Email, Nascimento):
    if arquivoex(Nome) == False and arquivoex(Nome) != 'Digite seu nome':
        data = {
            "Nome": Nome,
            "Email": Email,
            "Nascimento": Nascimento
        }
        with open(f'{(Nome)}', "w") as arquivo:
            js.dump(data, arquivo)
            arquivo.close()
        shutil.move(Nome, "PACIENTES")
        os.mkdir(f'./AUDIOS/{Nome}')
        return True
    else:
        return False


# ESCOLHER FRASE ALEATORIA
def frasesrandom():
    pronome = ['cachorro','gato']
    frase = (pronome[randint(0, len(pronome) - 1)])
    return frase


# FALAR AS FRASES
def fale(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    engine.say(audio)
    engine.runAndWait()


# SALVAR AUDIO DO PACIENTE
def audio_save(ui):
    # PRE-REQUISITOS DE GRAVAÇÃO 1
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    FILE_NAME = ('audio.wav')

    # INICIAÇÃO DO PYAUDIO
    audio = pyaudio.PyAudio()

    # PRE-REQUISITOS DE GRAVAÇÃO 2
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    # COMEÇO DA GRAVAÇÃO
    frames = []

    for i in range(1, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        data_chunk = array('h', data)
        vol = max(data_chunk)
        if vol >= 1:
            frames.append(data)

    # FIM DA GRAVAÇÃO
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # SALVANDO ARQUIVO
    wavfile = wave.open(FILE_NAME, 'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))
    wavfile.close()
    ui.frame_3.hide()

    # MOVENDO ARQUIVO PARA A PASTA DE AUDIO
    shutil.move(FILE_NAME, f"./PACIENTES/")


# SIMILARIDADE DAS FRASES
def igualdade(a, b):
    def sml(x, y):
        return SequenceMatcher(None, x, y).ratio()

    x = a
    y = b

    return round(sml(x, y) * 100, 2)


# ESCUTAR AUDIO
class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.p.terminate()


def repAudio(nome):
    a = AudioFile(nome)
    a.play()
    a.close()


# RECOGNIZE GOOGLE
# def verificar(nome,pasta):
"""    r = sr.Recognizer()

    hello = sr.AudioFile(f'./AUDIOS/{pasta}/' + nome)
    with hello as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio,language="pt-BR")
        return s

    except Exception as e:
        fale("Tente novamente!" + str(e))"""


# LISTA AUDIO
def listboxBusca(nome, a):
    try:
        arr = os.listdir(f'AUDIOS/{nome}')
        n = 0
        for i in arr:
            a.insert(n, arr[n])
            n += 1
    except FileNotFoundError:
        return 0
