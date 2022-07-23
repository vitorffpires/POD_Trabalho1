def valor_coringa(valor):
    texto_coringa = ''
    if valor == 100:
        texto_coringa = 'cem'
        return str(texto_coringa)
    elif 10 <= valor <= 19:
        if valor == 10 or valor % 100 == 10:
            texto_coringa = 'dez'
        elif valor == 11 or (valor % 100) == 11:
            texto_coringa = 'onze'
        elif valor == 12 or valor % 100 == 12:
            texto_coringa = 'doze'
        elif valor == 13 or valor % 100 == 13:
            texto_coringa = 'treze'
        elif valor == 14 or valor % 100 == 14:
            texto_coringa = 'quatorze'
        elif valor == 15 or valor % 100 == 15:
            texto_coringa = 'quinze'
        elif valor == 16 or valor % 100 == 16:
            texto_coringa = 'dezesseis'
        elif valor == 17 or valor % 100 == 17:
            texto_coringa = 'dezessete'
        elif valor == 18 or valor % 100 == 18:
            texto_coringa = 'dezoito'
        elif valor == 19 or valor % 100 == 19:
            texto_coringa = 'dezenove'
        return str(texto_coringa)
    else: 
        return False


def verifica_numero(valor):
    cen = ''
    dez = ''
    uni = ''
    if 100 < valor < 1000:
        cen = centena(valor)
        dez = dezena(valor)
        if dez == valor_coringa(valor):
            return str(cen + 'e ' + dez)
        else:
            uni = unidade(valor)
        return str(cen + 'e ' + dez + 'e ' + uni)
    if 10 < valor < 100:
        dez = dezena(valor)
        if dez == valor_coringa(valor):
            return str(dez)
        else:
            uni = unidade(valor)
        return str(dez + 'e ' + uni)
    else:
        uni = unidade(valor)
        return str(uni)


def centena(valor):
    cen = ''
    c = valor // 100
    if c == 1:
        cen = 'cento '
    elif c == 2:
        cen = 'duzentos '
    elif c == 3:
        cen = 'trezentos '
    elif c == 4:
        cen = 'quatrocentos '
    elif c == 5:
        cen = 'quinhentos '
    elif c == 6:
        cen = 'seiscentos '
    elif c == 7:
        cen = 'cetecentos '
    elif c == 8:
        cen = 'oitocentos '
    elif c == 9:
        cen = 'novecentos '
    return str(cen)


def dezena(valor):
    dez = ''
    d = (valor % 100) // 10
    if d == 1:
        dez = valor_coringa(valor)
    if d == 2:
        dez = 'vinte '
    elif d == 3:
        dez = 'trinta '
    elif d == 4:
        dez = 'quarenta '
    elif d == 5:
        dez = 'cinquenta '
    elif d == 6:
        dez = 'secenta '
    elif d == 7:
        dez = 'setenta '
    elif d == 8:
        dez = 'oitenta '
    elif d == 9:
        dez = 'noventa '
    return str(dez)


def unidade(valor):
    uni = ''
    u = (valor % 10) // 1
    if u == 1:
        uni = 'um '
    elif u == 2:
        uni = 'dois '
    elif u == 3:
        uni = 'três '
    elif u == 4:
        uni = 'quatro '
    elif u == 5:
        uni = 'cinco '
    elif u == 6:
        uni = 'seis '
    elif u == 7:
        uni = 'sete '
    elif u == 8:
        uni = 'oito '
    elif u == 9:
        uni = 'nove '
    return str(uni)


#main App
m = int(input('Digite um valor: '))
if valor_coringa(m) == False:
    print(verifica_numero(m))
else:
    print(valor_coringa(m))

