from os import getenv
import qrcode

print('-'*20)
print('----- QR CODER -----')
print('-'*20)
print('')

useerr = getenv("USERNAME")

while True:
    link = str(input('Link: '))
    namearq = str(input('Nome do arquivo: '))
    
    ddpast = str('C:\\Users\\{}\\Downloads\\'.format(useerr))
    vapo = ddpast + namearq + '.png'

    imagem = qrcode.make(link)
    imagem.save(vapo)

    print('\n>>> Baixado com sucesso!')

    while True:
        cnt = str(input('Quer fechar? [S/N]: ')).upper().strip()[0]
        if cnt.isalpha() == True and cnt in 'SN':
            print('')
            break
        else:
            print('Digite uma opção valida!\n')

    if cnt == 'S':
        print('Programa Finalizado!')
        break
    if cnt == 'N':
        print('')
        print('<-> '*4)
