#Q1 fazer um programa que saia em ordem crescente ou não 
lista=[] # duas listas para comparar 
L2=[]
N=int(input("N="))#N valores
for i in range(N):
    NI=int(input ("digite um número inteiro positivo"))
    lista.append(NI)
    L2.append(NI)#adicionar NI nas listas 
    L2.sort()#essa função faz com que a lista 2 sempre saia em ordem crescente 
if lista == L2: #comparação das listas
  print("está em ordem crescente" )
elif lista != L2:
  print(" não está em ordem crescente")
  
