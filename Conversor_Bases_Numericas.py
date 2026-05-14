# Função de validação, verifica se as entradas do usuário estão no escopo do sistema. 
def validacao():
    while True:
        invalido = False
        n = input(str("Informe o numero para conversao: ")).strip().upper()
        # Validação de n 
        for c in range(len(n)):
            if n[c] not in "0123456789ABCEF":
                print("\nNumero invalido. Tente novamente")
                invalido = True
                break
        if invalido == True:
            continue

        basei = int(input("Informe a base do numero acima: "))
        # Validação de basei 
        if basei > 16 or basei < 2:
            print("\nBase invalida. Tente novamente.")
            continue

        # Validação entre n e basei
        for c in range(len(n)):
            if n[c] not in "0123456789ABCDEF"[:basei]:
                print("\nBase incompativel com o numero. Tente novamente.")
                invalido = True
                break
        if invalido == True:
            continue

        basef = int(input("Informe a base para conversao: "))
        # Valicao da basef
        if basef > 16 or basef < 2:
            print("\nBase invalida. Tente novamente.")
            continue
        
        if invalido == False:
            break
    return(n, basei, basef)
n, basei, basef = validacao()

# Função central, esta converte o numero n para a base 10 de acordo com a variável "basei"
def central(n, basei):
    expoente = 0
    soma = 0

    for i in range(len(n)-1, -1, -1):
        if n[i] == "A":
            soma += 10 * (basei ** expoente)
        elif n[i] == "B":
            soma += 11 * (basei ** expoente)
        elif n[i] == "C":
            soma += 12 * (basei ** expoente)
        elif n[i] == "D":
            soma += 13 * (basei ** expoente)
        elif n[i] == "E":
            soma += 14 * (basei ** expoente)
        elif n[i] == "F":
            soma += 15 * (basei ** expoente)
        else:
            soma += int(n[i]) * (basei ** expoente)
        expoente += 1
    return(soma)
soma = central(n, basei)

# Função de saída final, onde o número "soma", que está na base 10, é convertido para a base "basef"
def saida(soma, basef):
    result = ""
    resto = 0
    quo = soma
    if soma == 0:
        result = "0"
    while True:
        resto = quo % basef
        if resto == 10:
            result = "A" + result
        elif resto == 11:
            result = "B" + result
        elif resto == 12:
            result = "C" + result
        elif resto == 13:
            result = "D" + result
        elif resto == 14:
            result = "E" + result
        elif resto == 15:
            result = "F" + result
        else:
            result = str(resto) + result
        
        quo = quo // basef
        if quo == 0:
            break
    
    return(result)
result = saida(soma, basef)
print("O numero {} de base {} convertido para a base {} e: {}".format(n, basei, basef, result))
        