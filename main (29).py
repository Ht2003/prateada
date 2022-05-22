#Q3 prova C
sequencia1=[]
sequencia2=[]
N=int(input('Digite N='))#A quantidade de vezes que vai rodar no for
for i in range (N):
     Nip=int(input('Digite os numeros inteiros positivos'))#os valores inteiros que o usuário vai digitar em ordem crescente 
     sequencia1.append(Nip)#esses valores serão adicionados nas 2 listas
     sequencia2.append(Nip)
     sequencia2.sort()# é para ordenar a sq2
if sequencia1 == sequencia2:#a comparação das listas se é diferente ou igual 
    print("esta em ordem crescente")
elif sequencia1 != sequencia2:
    print("não esta em ordem crescente")

  
  
  #obs:o replit buga as letras