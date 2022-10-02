""" 

url = str(input('Insira o texto: '))
imagem = qrcode.make(url)
imagem.save('vapo.png') """

from PySimpleGUI import PySimpleGUI as sg
import qrcode
from time import sleep
from os import getenv, remove

useerr = getenv("USERNAME")
ciclos = 0
txt = 'QR Code'
cc = ''
opa = 0



# layout
sg.theme('DarkBlue13')
layout = [
    [sg.Text('Link'), sg.Text('                                           ') , sg.Text('Nome do arquivo')],
    [sg.Input(key='url',size=(30,2)),sg.Input(key='nameqr', size=(30,2), default_text=('QR Code'))],
    [],
    [sg.Button('Gerar',size=(5,6)), sg.Button('Resetar',size=(5,6)), sg.Text('     '),sg.Image(
        "dino.png", key='mamage', size=(290, 290))],
    [sg.Checkbox('Salvar QR code?', key='savee')]

]

# Janela
janela = sg.Window('QR Coder', layout=layout)

# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break


    ddpast = str('C:\\Users\\{}\\Downloads\\'.format(useerr))

    if valores["nameqr"] == 'QR Code':
        if ciclos == 0:
            vapo = str(valores["nameqr"])
            vapo = ddpast + vapo + '.png'
        else:
            vapo = str(valores["nameqr"])
            cc = str(ciclos)
            cc = '(' + cc + ')'
            vapo = ddpast + vapo + '.png'
    else:
        vapo = ddpast + (str(valores["nameqr"])) + '.png'


    if eventos == 'Gerar':
        opa = 0
        ciclos += 1
        url = valores['url']
        imagem = qrcode.make(url)
        imagem.save(vapo)
        sleep(3)
        janela['mamage'].update(vapo)
        opa += 1

    if valores['savee'] == False:
        remove(vapo)
        ciclos -= 1

    if opa == 1 and eventos == 'Resetar':
        janela['mamage'].update('dino.png')
        opa = 0

    if ciclos > 1:
        cc = '(' + str(ciclos) + ')'
        txt = txt + ' ' + cc


        
        
    
        
