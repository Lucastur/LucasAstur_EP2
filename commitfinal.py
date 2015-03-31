

import random
import turtle

"""Por Lucas Scarlato Astur, 1B

Jogo da forca! comece clicando em run e boa sorte!

observações:
1)o jogo diferencia letras com e sem acento, portanto, fique atento nisso!
"""

lista = open("entrada.txt", encoding = "UTF-8").readlines()

a = random.choice(lista)
a = a.lower()

letras = 0
guess=0
print (a)
b= "___  "
acertos= []

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Forca")



lucas = turtle.Pen()
lucas.speed(5)
lucas.color("black")
lucas.penup()
lucas.pensize(5)
lucas.setpos(-100,-200)
lucas.pendown()
lucas.backward(250)
lucas.forward(50)    
lucas.left(90)        
lucas.forward(400)    
lucas.right(90)
lucas.forward(75)
lucas.right(90)
lucas.forward(50)
lucas.right(270)
lucas.penup()
lucas.forward(200)
lucas.pendown()

for i in range(0,len(a)-1):
    if a[i] == " ":
        lucas.write("  ")
    else:
        lucas.penup()
        lucas.hideturtle
        lucas.setpos(-20+24*(i), 150)
        lucas.write("___ ")

    
        
def cabeca():
    lucas = turtle.Turtle()
    lucas.pensize(2)
    lucas.color("blue")
    lucas.hideturtle()
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,110)
    lucas.pendown()
    lucas.circle(20)

def tronco():
    lucas = turtle.Turtle()
    lucas.pensize(2)
    lucas.color("blue")
    lucas.hideturtle()
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,110)
    lucas.pendown()
    lucas.left(270)
    lucas.forward(90)

def bracoesq():
    lucas = turtle.Turtle()
    lucas.pensize(2)
    lucas.color("blue")
    lucas.hideturtle()
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,90)
    lucas.pendown()
    lucas.left(225)
    lucas.forward(40)
    
def bracodir():
    lucas = turtle.Turtle()
    lucas.pensize(2)
    lucas.color("blue")
    lucas.hideturtle()
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,90)
    lucas.pendown()
    lucas.left(315)
    lucas.forward(40)
    
def pernaesq():
    lucas = turtle.Turtle()        
    lucas.pensize(2)
    lucas.hideturtle()
    lucas.color("blue")
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,20)
    lucas.pendown()
    lucas.left(240)
    lucas.forward(60)
    lucas.color("black")
    
def pernadir():
    lucas = turtle.Turtle()        
    lucas.pensize(2)
    lucas.hideturtle()
    lucas.color("blue")
    lucas.speed(5)
    lucas.penup()
    lucas.setpos(-225,20)
    lucas.pendown()
    lucas.left(300)
    lucas.forward(60)
    lucas.color("black")
    

   


while guess==0:
    perguntaa = window.textinput('errou nenhum ate agora', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    else:
        if perguntaa in a:
            letras+=1
            print("parabens!")
            lista1 = []
            for i in range(len(a)):
                if a[i] == perguntaa:
                    lista1.append(i)
                    acertos.append(i)
                elif perguntaa == 'a' and (a[i] == "ã" or a[i] == "á"):
                    acertos.append(i)
                    lista1.append(i)
                elif perguntaa == 'o' and (a[i] == "ó" or a[i] == "ô"):
                    acertos.append(i)
                    lista1.append(i)
                elif perguntaa == 'i' and a[i] == "í":
                    acertos.append(i)
                    lista1.append(i)                
            print (lista1)
            for pos in lista1:
                lucas.penup()
                lucas.hideturtle()
                lucas.setpos(-20+24*(pos), 150)
                lucas.write(perguntaa, font=("arial",10))
        else:
            cabeca()
            guess +=1

while guess==1:
    perguntab = window.textinput('errou 1 ate agora', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    if perguntab in a:
        print("parabéns")
        lista2 = []
        for i in range(len(a)):
            if a[i] == perguntab:
                lista2.append(i)
                acertos.append(i)
            elif perguntab == 'a' and (a[i] == "ã" or a[i] == "á"):
                acertos.append(i)
                lista2.append(i)
            elif perguntab == 'o' and (a[i] == "ó" or a[i] == "ô"):
                acertos.append(i)
                lista2.append(i)
            elif perguntab == 'i' and a[i] == "í":
                acertos.append(i)
                lista2.append(i)
        print (lista2)
        for pos in lista2:
            lucas.penup()
            lucas.hideturtle()
            lucas.setpos(-20+24*(pos), 150)
            lucas.write(perguntab, font=("arial",10))
    else:
            tronco()
            guess+=1
            
while guess==2:
    perguntac = window.textinput('errou 2 ate agora', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    if perguntac in a:
        print("parabéns")
        lista3 = []
        for i in range(len(a)):
            if a[i] == perguntac:
                lista3.append(i)
                acertos.append(i)
            elif perguntac == 'a' and (a[i] == "ã" or a[i] == "á"):
                acertos.append(i)
                lista3.append(i)
            elif perguntac == 'o' and (a[i] == "ó" or a[i] == "ô"):
                acertos.append(i)
                lista3.append(i)
            elif perguntac == 'i' and a[i] == "í":
                acertos.append(i)
                lista3.append(i)
        print (lista3)
        for pos in lista3:
            lucas.penup()
            lucas.hideturtle()
            lucas.setpos(-20+24*(pos), 150)
            lucas.write(perguntac, font=("arial",10))
    else:
            bracoesq()
            guess+=1
            
while guess==3:
    perguntad = window.textinput('errou 3 ate agora', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    if perguntad in a:
        print("parabéns")
        lista4 = []
        for i in range(len(a)):
            if a[i] == perguntad:
                lista4.append(i)
                acertos.append(i)
            elif perguntad == 'a' and (a[i] == "ã" or a[i] == "á"):
                acertos.append(i)
                lista4.append(i)
            elif perguntad == 'o' and (a[i] == "ó" or a[i] == "ô"):
                acertos.append(i)
                lista4.append(i)
            elif perguntad == 'i' and a[i] == "í":
                acertos.append(i)
                lista4.append(i)
        print (lista4)
        for pos in lista4:
            lucas.penup()
            lucas.hideturtle()
            lucas.setpos(-20+24*(pos), 150)
            lucas.write(perguntad, font=("arial",10))
    else:
            bracodir()
            guess+=1

while guess==4:
    perguntae = window.textinput('errou 4 ate agora', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    if perguntae in a:
        print("parabéns")
        lista5 = []
        for i in range(len(a)):
            if a[i] == perguntae:
                lista5.append(i)
                acertos.append(i)           
            elif perguntae == 'a' and (a[i] == "ã" or a[i] == "á"):
                acertos.append(i)
                lista5.append(i)
            elif perguntae == 'o' and (a[i] == "ó" or a[i] == "ô"):
                acertos.append(i)
                lista5.append(i)
            elif perguntae == 'i' and a[i] == "í":
                acertos.append(i)
                lista5.append(i)
        print (lista5)
        for pos in lista5:
            lucas.penup()
            lucas.hideturtle()
            lucas.setpos(-20+24*(pos), 150)
            lucas.write(perguntae, font=("arial",10))
    else:
            pernaesq()
            guess+=1
            
        
while guess==5:
    perguntaf = window.textinput('sua ultima chance!!', 'diga seu palpite')
    if (len(acertos)+2) == len(a):
        lucas.penup()
        lucas.setpos(0,0)
        lucas.pendown()
        lucas.color("green")
        lucas.write("GANHOU FERA!", font=("Arial", 40))
        window.exitonclick()
    if perguntaf in a:
        print("parabéns")
        lista6 = []
        for i in range(len(a)):
            if a[i] == perguntaf:
                lista6.append(i)
                acertos.append(i)
            elif perguntaf == 'a' and (a[i] == "ã" or a[i] == "á"):
                acertos.append(i)
                lista6.append(i)
            elif perguntaf == 'o' and (a[i] == "ó" or a[i] == "ô"):
                acertos.append(i)
                lista6.append(i)
            elif perguntaf == 'i' and a[i] == "í":
                acertos.append(i)
                lista6.append(i)            
        print (lista6)
        for pos in lista6:
            lucas.penup()
            lucas.hideturtle()
            lucas.setpos(-20+24*(pos), 150)
            lucas.write(perguntaf, font=("arial",10))
    else:
            pernadir()
            guess+=1

if guess==6:
    lucas.penup()
    lucas.setpos(-100,0)
    lucas.hideturtle()
    lucas.pendown()
    lucas.color("red")
    lucas.write("PERDEU PLAYBOY", font=("Arial", 40))
    lucas.penup()
    lucas.speed(2)
    lucas.forward(200)
 
        
        
    
    
    

window.exitonclick()


        

        
    