import json, pyttsx3, os
import PySimpleGUI as sg
pasta = './nvi/'
bibliaCompleta={}

# LER CADA ARQUIVO
def lerTudo(arquivo):
    with open(f'{pasta}/{arquivo}','r', encoding='utf-8') as ler:
        livro=json.loads(ler.read())
    nomeLivro=arquivo.split(".")[0].upper()
    dic_capt = {}
    for capitulos in livro:
        bibliaCapitulos = {}
        dic_vers = {}
        for capt in capitulos:
            for vrs in capitulos[capt]:
                dic_vers[vrs]=capitulos[capt][vrs]
                bibliaCapitulos[capt]=capitulos[capt][vrs]
            dic_capt[capt]=dic_vers
        bibliaCompleta[nomeLivro]=dic_capt

# LENDO A PASTA COM OS ARQUIVOS
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        lerTudo(arquivo)

#  OUVIR A LEITURA DO VERSÍCULO
def ler_biblia(livro,capitulo,versiculo):
    leitor = pyttsx3.init()
    texto = f'Livro: {livro.upper()}, Capítulo: {capitulo}, Versículo: {versiculo} é este: {bibliaCompleta[livro][capitulo][versiculo]}'
    leitor.say(texto)
    leitor.runAndWait()

lista_livros = []
for key in bibliaCompleta.keys():
    lista_livros.append(key.upper())
def name(name):
    dots = 0
    return sg.Text(name + ' ' + '•' * dots, size=(len(name)+2, 1), justification='r', pad=(0, 0), font='Courier 10')
layout=[
    [sg.Text('livro', size=(30, 1))],
    [sg.InputText('zacarias', key='livro_escolhido', size=(30, 1))],
    [sg.Text('capitulo', size=(30, 1))],
    [sg.InputText('', key='capitulo_escolhido', size=(30, 1))],
    [sg.Text('versiculo', size=(30, 1))],
    [sg.InputText('', key='versiculo_escolhido', size=(30, 1))],
    [sg.Button('Ouvir versículo', size=(30, 0), key='digitos', disabled=False)],
    [sg.Multiline('',key='texto', size=(60,5))],
    [sg.Button('Sair', size=(30, 2), key='sair')]
]
janela = sg.Window('Leitor da Bíblia').layout(layout)
while True:
    Button, values = janela.Read()
    if (Button == 'sair' or Button == sg.WINDOW_CLOSED):
        break
    else:
        if (Button == 'digitos'):
            janela['texto'].update(value=f"{bibliaCompleta[values['livro_escolhido'].upper()][values['capitulo_escolhido']][values['versiculo_escolhido']]}")
            ler_biblia(values['livro_escolhido'].upper(),values['capitulo_escolhido'],values['versiculo_escolhido'])
