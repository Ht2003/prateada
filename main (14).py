#as alternativas das questÃµe do professor 
Q1, Q2, Q3, Q4, Q5 = "A", "B", "C", "D","E"
Q6,Q7, Q8, Q9, Q10 = "A", "B", "C", "D", "E"

x = 0
Aluno = input("Nome do aluno: ") 
print()
#As alternativas do aluno pra comparar com a do gabarito do professor teve o uso da função if !!
a=input("Q1 = ")

if a == "A":
   x = x + 15
  
b=input("Q2 = ")
if b == "B":
  x = x + 15

c=input("Q3 = ")
if c == "C":
   x = x + 15

d=input("Q4 =")
if d == "D":
   x = x + 15
  
e=input("Q5 =")
if e == "E":
  x = x + 20

f=input("Q6 =")
if f == "A":
   x = x + 20

g=input("Q6 = ")
if g == "B":
   x = x + 20

h=input("Q8 = ")
if h == "C":
  x = x + 30

i=input("Q9 = ") 
if i== "D":
 x = x + 30

j =input("Q10 = ") 
if j == "E":
 x = x + 30 
#toda vez que as alternativas forem iguais, a do professor e a do aluno,o aluno soma pontos
print()
print("A quantidade de pontos somada de {} foi {}".format(Aluno, x))