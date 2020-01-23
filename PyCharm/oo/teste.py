
def cria_conta(numero, titular, saldo, limite):
    conta = {"Numero": numero, "Titular": titular, "saldo": saldo, "limte": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

