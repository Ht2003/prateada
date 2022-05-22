#leitura do gabarito 
Q1, Q2, Q3, Q4, Q5 = "A", "B", "C", "D","E"
Q6,Q7, Q8, Q9, Q10 = "A", "B", "C", "D", "E"

 
s = 0 #criacao de variavel pra receber os pontos por cada alternativa certa
#nome do aluno que vai utilizar o programa 
Aluno = input("Nome do aluno: ") 
print()
#Apartir daqui iniciam-se as condições aninhadas com  comparaçã utilizand o if para comparar o gabarito do aluno com o do professor, se o aluno acertar todas as questões ele acertará a prova toda e vai ganha pontos pelos acertos!!!
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

l=input("Q6 =")
if l == "A":
   s = s + 20

m=input("Q6 = ")
if m == "B":
   s = s + 20

n=input("Q8 = ")
if n == "C":
  s = s + 30

o=input("Q9 = ") 
if o== "D":
 s = s + 30

i=input("Q10 = ") 
if i == "E":
 s = s + 30 
#toda vez que as alternativas forem iguais, a do professor e a do aluno,o aluno somar pontos
print()
print("A quantidade de pontos que {} obteve foi {}".format(Aluno, s))
#obs as letras ficam bugadas quando são baixadas pra serem enviadas