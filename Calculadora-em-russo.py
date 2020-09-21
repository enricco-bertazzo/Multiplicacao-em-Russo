lista_mult = [] #lista para tratamento do resultado
lista_div = [] #lista para tratamento do resultado
def dividindo_por_dois(n1):
  while True:
    lista_div.append(n1)
    n1 = n1//2
    if n1 == 1:
      break
  lista_div.append(1)
  return lista_div

def multiplicando_por_2 (n2):
  count = len(lista_div) #parametro de contagem para a multiplicação do multiplicador
  while True:
    lista_mult.append(n2)
    n2 = n2*2
    count = count - 1
    if  count == 0:
      break
  return lista_mult

def parametro(lista_div, lista_mult):
  count = len(lista_div)-1
  while True:
    if (lista_div[count]%2) == 0:
      lista_mult.pop(count)
    count = count - 1
    if  count == -1:
      break
  return lista_mult

def resultado (lista_mult):
  soma_das_notas = sum(lista_mult)
  return (soma_das_notas)

############################################################################################

import time
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
operacao = input("Digite '+' para soma e '*' para multiplicação")

if(operacao == '*'):
  t1 = time.time()
  lista_dividida = dividindo_por_dois(n1)
  lista_multiplicada = multiplicando_por_2(n2)
  lista_multiplicada_impares = parametro(lista_dividida, lista_multiplicada)
  resultado = resultado(lista_multiplicada_impares)
  print(resultado)
  tempoExec = time.time() - t1
else:
  print(n1+n2)