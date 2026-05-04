# Este programa recebe um número, a base deste e uma base para conversão desse número, compreendendo das bases 2 à 16.

def variaveis():
    while True:
         n = str(input('\nDigite um número em qualquer base: ')).strip().upper()
         basei = int(input('\nDigite a base do número digitado: '))
         basef = int(input('\nBase para converter: '))
         carac = len(n.strip())
        
         if basei>16 or basei<2: # verificação do escopo da base inicial
            print('\nErro: Base do número inválida.\n', '='*10)
            continue
            
         if basef>16 or basef<2: # verificação do escopo da base final
            print('\nErro: Base de conversão inválida.\n', '='*10)
            continue

         if n == "":
            print("\nErro: número vazio.\n")
            continue

         invalido = False    
         for d in range(0, carac):
             if n[d] not in '0123456789ABCDEF'[:basei]:
                print('\nErro: Base incompatível com o número.\n', '='*10)
                invalido = True
                break
         if invalido == True:
             continue
         else:
             break
    return(n, basei, basef, carac)

# Cálculo para ler caracteres, atribuir valores numéricos e conversão para base 10
n, basei, basef, carac = variaveis()
def conversão_base10():
    vlr = 0 # valor das letras
    vlrnum = 0 # valor dos números
    expo = 0 # expoente
    global soma # resultado da conversão a base 10
    soma = 0

    for c in range(carac-1, -1, -1):
        if n[c] in 'ABCDEF':
            vlr = ord(n[c]) - 55
            soma += (vlr * (basei ** expo))
        elif n[c] in '0123456789':
            vlrnum = int(n[c])
            soma += (vlrnum * (basei ** expo))
        expo += 1
    return(soma)

# Passando da base 10 para a basef (base final)
soma = conversão_base10()
def conversão_basef(soma):
    resto = 0 # resto
    result = '' # resultado final

    if soma == 0:
        result = "0"
    else:
        while soma > 0:
            resto = (soma % basef)
            if resto >= 10:
                result = chr(resto + 55) + result
            else:
                result = str(resto) + result
            soma = soma // basef
    return(result)

# Saída final.
result = conversão_basef(soma)
print('O número {} de base {}, convertido para a base {}, é: {}.'.format(n, basei, basef, result))