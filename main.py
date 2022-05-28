#gabarito do professor vai ser comparado com o gabarito do aluno
Q1, Q2, Q3, Q4, Q5,='A', 'B', 'C','D','E'
Q6, Q7, Q8, Q9, Q10='A', 'B' ,'C','D','E'

v=0 # atribuicao dos pontos, vai comecar em zero, vai somar pontos conforme o aluno for acertando  as alternativas

aluno=str(input('nome do aluno'))


print()
Qt1=input('digite alternativa da questão 1 = ')
if Qt1 == 'A':
    v= v + 15
Qt2=input('digite a alternativa da questão 2 =')
if Qt2 == 'B':
      v= v + 15
Qt3=input('digite a alternativa da questão 3 =')
if Qt3 == 'C':
    v= v + 15
Qt4=input('digite a alternativa da questão 4 =')
if Qt4 == 'D':
    v= v + 15
Qt5=input('digite a alternativa da questão 5 =')
if Qt5 == 'E':
    v = v + 20
Qt6=input('digite a alternativa da questão 6 =')
if Qt6 == 'A':
    v = v + 20
Qt7=input('digite a alternativa da questão 7 =')
if Qt7 == 'B':
    v = v + 20
Qt8=input('digite a alternativa da questão 8 =')
if Qt8 == 'C':
    v= v + 30
Qt9=input('digite a alternativa da questão 9 =')
if Qt9 == 'D':
    v= v + 30
Qt10=input('digite a alternativa da questão 10 = ')
if Qt10 == 'E':
    v= v + 30

print()
print('A quantidade de pontos de {} foi de {}'.format(aluno,v))




