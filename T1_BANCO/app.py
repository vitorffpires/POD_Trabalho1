import Contas as C

def opera_conta(opera):
    opera = opera.lower()
    if "sacar" in opera:
        num = int(opera[27:])
        try:
            conta3.saque(num)
        except ValueError:
            print("o valor deve ser positivo")
            erros.write(str(ValueError) + "o valor deve ser positivo \n")
    elif "depositar" in opera:
            num = int(opera[27:])
            try:
                conta1.deposito(40)
            except ValueError:
                print("o valor deve ser positivo")
                erros.write(str(ValueError) + "o valor deve ser positivo \n")
    elif "saldo" in opera:
            print(conta1.saldo)
    elif "rendimento" in opera:
            num = int(opera[28:31])
            print(conta1.consulta_rendi(num/30))

def criar_contas(criar):
    if ("corrente" in(criar.lower())):
        criar = C.ContaCorrente
        saida.write("contaCorrente \n")
        saldo = file.readline()
        saldo = int(saldo[13:])
        saida.write("valorSaldo" + str(saldo) + "\n")
        id = file.readline()
        id = id[4:]
        id = id.split()
        saida.write("id"+str(id) +"\n")
        chequeespecial = file.readline()
        saida.write("chequeEspecia"+ chequeespecial[21:] +"\n")
        chequeespecial = int(chequeespecial[21:])
        try:
            return C.ContaCorrente(id, nome, cpf, saldo, chequeespecial)
        except C.ErroQuantidade:
            print("cpf invalido")
            erros.write(str(C.ErroQuantidade) + "\n")
        except ValueError:
            print("dente digitar o valor novamente")
            erros.write(str(ValueError) + "\n")
    elif "poupanca"  in(criar.lower()):
        criar = C.ContaPoupanca
        saldo = file.readline()
        saldo = int(saldo[13:])
        saida.write("valorSaldo" + str(saldo) + "\n")
        id = file.readline()
        id = id[4:]
        id = id.split()
        saida.write("id"+str(id) +"\n")
        taxa = file.readline()
        taxa = taxa[16:]
        taxa = float(taxa)
        saida.write("taxaPoupanca"+str(taxa)+"\n")
        try:
            return C.ContaPoupanca(id, nome, cpf, saldo, taxa)
        except C.ErroQuantidade:
            print("cpf invalido")
            erros.write(str(C.ErroQuantidade + "\n"))
        except ValueError:
            print("dente digitar o valor novamente")
            erros.write(str(ValueError) + "\n")
    elif "invest"  in(criar.lower()):
        criar = C.ContaInvestimento
        saldo = file.readline()
        saldo = int(saldo[13:])
        saida.write("valorSaldo" + str(saldo) + "\n")
        id = file.readline()
        id = id[4:]
        id = id.split()
        saida.write("id"+str(id) +"\n")
        risco = file.readline()
        risco = risco[10:]
        risco = risco.lower()
        saida.write("riscoInvest"+str(risco)+"\n")
        try:
            return C.ContaInvestimento(id, nome, cpf, saldo, risco)
        except C.ErroQuantidade:
            print("cpf invalido")
            erros.write(str(C.ErroQuantidade + "\n"))
        except ValueError:
            print("dente digitar o valor novamente")
            erros.write(str(ValueError) + "\n")

for i in range (1,3):
    with open(f"Individuos/{i}.txt", "r") as file:
        erros = open(f"Individuos/{i}log.txt", "a")
        saida = open(f"Individuos/{i}saida.txt", "a")
        nome = file.readline()
        saida.write("nome"+str(nome) + "\n")
        cpf = file.readline()
        cpf = cpf[5:]
        saida.write("cpf"+str(cpf) + "\n")
        criar = file.readline()
        criar = criar[7:]
        conta1 = criar_contas(criar)
        next = file.readline
        if "criar" in next:
            conta2 = criar_contas(criar)
            next = file.readline
        if "criar" in next:
            conta3 = criar_contas(criar)
            next = file.readline
        control = True
        while (control == True):
            if "sacar" or "depositar" or "saldo" or "rendimento" in next:
                opera_conta(next)
                next = file.readline
            else:
                control = False
file.close()
erros.close()
saida.close()
