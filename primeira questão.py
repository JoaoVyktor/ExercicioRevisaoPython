nota1 =  float(input())
nota2 =  float(input())
nota3 =  float(input())
media = (nota1+nota2+nota3)/3

if(media>=7):
    print("Aprovado")
    print("{:.1f}".format(media))

elif(media<7):
    print("Reprovado")
    print("{:.1f}".format(media))

elif(media==10):
    print("Aprovado com distinção")
    print("{:.1f}".format(media))
