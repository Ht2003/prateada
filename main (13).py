#o usuário deve informar os três valores
x = int(input ("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
z = int(input("Informe o valor de z: "))
#formam os intervalos dos valores inteiros que o usuário digitar 
while True:
       if  x  <  y:
          if   z  <=  y: 
                   break
   
          else:
                  z = int(input("Informe o valor de z: "))
       else: 
              x = int(input ("Informe o valor de x: "))
# os intervalos de x e y
print("\nValores inteiros entre x e y divisiveis por z:")
[print (i) for i in range(x, y + 1) if i % z == 0]
print("\nSoma dos valores pares impressos") 
#A função sum para somar os elementos!
print(sum([i for i in range(x, y + 1) if i % z == 0 and i % 2 == 0]))
