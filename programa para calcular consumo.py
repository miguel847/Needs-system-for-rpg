import sys
import time
import pyperclip

def linhas():
      print("------------------------------------------------------")



# Pede o quanto é o consumo por hora
linhas()
nessecidade = float(input("Qual é a nessecidade por hora?"))
linhas()

# Pede quantos minutos se pasarão
quantos_minutos = int(input("Quantos minutos são gastos?"))
linhas()

# Pede quanto tem de nessecidade
nessecidade_atual = float(input("Qual é a nessecidade atual?"))
linhas()

#divide o consumo por hora por 60, para saber o consumo por minuto
nessecidade_por_minuto = nessecidade/60

#Faz uns calculos aí e descobre o quanto vai ser consumido naquele tempo
consumo = nessecidade_por_minuto*quantos_minutos

#Pega a nessecidade atual e subtrae o consumo para ter o valor final
valor_final = nessecidade_atual - consumo

print("A nessecidade final ficara {:.1f}".format(valor_final))
linhas()
pyperclip.copy(valor_final)

e = input("Quer sair? [S,N]")
if e == "S":
      sys.exit()
elif e == "N":
      time.sleep(10)


