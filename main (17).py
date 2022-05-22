Q1, Q2, Q3, Q4, Q5 = "A", "B", "C", "D","E"
Q6,Q7, Q8, Q9, Q10 = "A", "B", "C", "D", "E"

 
s = 0 #criacao de variavel pra receber os pontos por cada alternativa certa
Aluno = input("Nome do aluno: ") 
print()
#As alternativas do aluno pra comparar com a do gabarito do professor teve o uso da funcao if !!
# obs algumas letras estão bugando
a=input("Q1 = ")
if a == "A":
   s = s + 15
  
b=input("Q2 = ")
if b == "B":
  s = s + 15

c=input("Q3 = ")
if c == "C":
   s = s + 15

d=input("Q4 =")
if d == "D":
   s = s + 15
  
e=input("Q5 =")
if e == "E":
  s = s + 20

f=input("Q6 =")
if f == "A":
   s = s + 20

g=input("Q6 = ")
if g == "B":
   s = s + 20

h=input("Q8 = ")
if h == "C":
  s = s + 30

i=input("Q9 = ") 
if i== "D":
 s = s + 30

j =input("Q10 = ") 
if j == "E":
 s = s + 30 
#toda vez que as alternativas forem iguais, a do professor e a do aluno,o aluno somarÃ¡ pontos
print()
print("A quantidade de pontos que {} obteve foi {}".format(Aluno, s))