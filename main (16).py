#usuario vai digitar 
x=int (input('digite o valor de x'))
y=int(input('digite o valor de y'))
z=int(input('digite o valor de z'))
#variavel 
v=0 
# vai adicionar +1 em y pois seu numero antecessor é impar
for c in range(x, y + 1): 
   if x < y and z <= y:
       if c % z ==0:
  #vai verificar se a condicao é verdadeira 
    
          print (f' {c}\n')# o intervalo de x e y
          if c % 2 == 0: #ocorre a soma dos números pares 
             v += c
print('A soma dos pares {}'.format(v))
