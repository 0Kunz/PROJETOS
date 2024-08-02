from tkinter import *
percent = False


def mudar(posicao):
    global text
    n2 = ''
    conta = float()
    if posicao[1] == '':
        n1 = achar(posicao, False)
    else:
        n1 = achar(posicao, False)
        n2 = achar(posicao, True)
    contastr = n1 + posicao[1] + n2
    if contastr[0] == '+':
        contastr = contastr[1::]
    n1 = float(n1)
    if n2 == '':
        pass
    else:
        n2 = float(n2)
    if posicao[1] == 'x':
        conta = n1 * n2
    elif posicao[1] == '/':
        conta = n1 / n2
    elif posicao[1] == '+':
        conta = n1 + n2
    elif posicao[1] == '-':
        conta = n1 - n2
    elif posicao[1] == '':
        conta = n1 / 100
    elif posicao[1] == '^':
        conta = n1 ** n2
    text = text.replace(contastr, str(conta))


def numero(algo):
    floats = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')
    if algo in floats:
        return True
    else:
        return False


def achar(lugar, positivo):
    ne = 1
    fbreak = True
    index_fim = index_inicio = int()
    if positivo:
        index_inicio = lugar[0] + 1
        while fbreak:
            fbreak = False
            try:
                if numero(text[lugar[0] + ne]):
                    index_fim = lugar[0] + ne + 1
                    fbreak = True
            except IndexError:
                pass
            ne += 1
    else:
        index_fim = lugar[0] if lugar[1] != '' else lugar[0]+1
        while fbreak:
            fbreak = False
            if numero(text[lugar[0] - ne]) and not positivo:
                index_inicio = lugar[0] - ne
                fbreak = True
            ne += 1
        index_inicio = 0 if index_inicio < 0 else index_inicio
    return text[index_inicio:index_fim]


def calculo():
    global text
    operacoes = list()
    for letra in text:
        if letra == '^':
            index_operador = (text.find('^'), '^')
            mudar(index_operador)
        elif letra in ('x', '/'):
            multi = text.find('x') if text.find('x') != -1 else len(text)
            divi = text.find('/') if text.find('/') != -1 else len(text)
            index_operador = (text.find('x'), 'x') if multi < divi else (text.find('/'), '/')
            if multi == len(text) and divi == len(text):
                pass
            else:
                mudar(index_operador)
        else:
            if letra in ('+', '-'):
                operacoes.append(letra)
    for operacao in operacoes:
        index_operador = (text.find(f'{operacao}'), f'{operacao}')
        mudar(index_operador)


def condicoes(num):
    global percent, text
    try:
        ultimo_c = text[-1]
    except IndexError:
        ultimo_c = ''
    try:
        if num.isnumeric():
            return num
        elif num == '=':
            calculo()
        elif num == 'C':
            text = ''
        elif num == '<-':
            text = text[:-1]
        elif num == '%' and ultimo_c.isnumeric() and not percent:
            ultimo_c = (len(text), '')
            mudar(ultimo_c)
        elif num == 'Exp' and ultimo_c.isnumeric():
            return '^'
        elif num == '.':
            n1 = achar((len(text), ''), False)
            if n1.find('.') == -1:
                return num
            else:
                return ''
        elif num in ('/', '-', 'x', '+') and ultimo_c in ('/', '-', 'x', '+') or num in ('Exp', '%'):
            return ''
        elif num in ('/', '-', 'x', '+'):
            return num
        return ''
    except IndexError or UnboundLocalError:
        return ''


def botao(texto, alt, lar, g1, g2):
    button = Button(Buttons, text=texto, height=alt, width=lar, command=lambda: pressed(texto))
    button.grid(column=g1, row=g2)
    return f'botão{text}'


def pressed(num):
    num = condicoes(num)
    global text
    text += num
    display.config(width=len(text), text=text)


janela = Tk()
text = str()
display = Label(fg='black', bg='white', font=('Arial', 40), width=9)
display.pack(anchor='w')
botao_textos = ('C', '<-', '%', '/', 1, 2, 3, 'x', 4, 5,
                6, '-', 7, 8, 9, '+', 'Exp', 0, '.', '=')
Botao = list()
Buttons = Frame(janela)
n = 0
for lin in range(1, 6):
    for c in range(0, 4):
        Botao.append(botao(f'{botao_textos[n]}', 2, 9, c, lin))
        n += 1
Buttons.pack()
janela.title('Calculadora')
icone = PhotoImage(file='pngegg.png')
janela.iconphoto(False, icone)
janela.mainloop()
