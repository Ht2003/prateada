#obs comentários estão saindo bugados 
#Q1 prova C
#usuario vai digitar 
x=int (input('digite o valor de x'))
y=int(input('digite o valor de y'))
z=int(input('digite o valor de z'))
#variavel 
v=0 
# vai adicionar +1 em y pois o numero que vem antes é impar,ou seja a soma do pares daria errada!!
for c in range(x, y + 1): 
   if x < y and z <= y:
       if c % z ==0:
  #vai verificar se a condicao é verdadeira , se for serão executada
    
          print (f' {c}\n')# o intervalo de x e y
          if c % 2 == 0: 
             v += c#ocorre a soma dos pares que serão impressos 
print('A soma dos pares {}'.format(v))