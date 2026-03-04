# Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es: ", i)
    
    
resultado = 0    
for i in mi_lista: 
    resultado += i

print(f"El resultado de la suma de mi lista es:  {resultado}")

for i in range(2,9):
    print(i)

    mi_lista_2 = ["Lunes", "Martes","Miercoles","Jueves","Viernes"]

    for i in mi_lista_2:
        if i != "Lunes":
            print(f"Feliz {i}!")

#While loop
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print (i)
    if i == 4:
        break

    else:
        print("i es ahora mayor o igual 5")

#Practica 2
#Dada la lista mi_lista_2 = ["lunes,"Martes","Miercoles","jueves","Viernes"]
#Imprime cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
#Pista: Usalos dos tipos loops while y for en el mismo programa para logralo
#Resultado
#martes
#miercoles
#jueves"
#viernes
#martes
#miercoles
#jueves"
#viernes
#martes
#miercoles
#jueves"
#viernes


# ================ Practica 2 ==============
'''mi_lista_2 = ["Lunes","Martes","Miercoles","Jueves","Vieres"]
for dia in mi_lista_2:
        if dia != "Lunes":
            contador = 0 
            while contador < 3:
                print (dia)
                contador += 1
                for i in mi_lista_2:
  '''



# ================ Practica 3 ===================
# Dada la lista my_list_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#imprime cada elemento de la lista 3 veces y cuando sea lunes no la incluyas.
#Pista: usa los tipos de loops while y for en el mismo programa para lograrlo
#resultado:
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes
#Martes
#Miercoles
#Jueves
#Viernes



''''mi_lista_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

contador_general = 0
while contador_general < 3:
    for dia in mi_lista_2:
        if dia != "Lunes":
            print(dia)
    contador_general += 1'''



#============Practica 4==========
#Cree un función en python llamada calculadora, la cual debe tomar los parámetros (num_1, num_2, operacion) y debe ser capaz de realizar toda la lógica de un calculadora simple como: sumar, restar, multiplicar y dividir.
#Nota: Las entradas serán proporcionadas por el usuario.
#Pista: Este código es un ejemplo de una suma 
print("========Mi Super Calculadora==========")
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")
def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        if num_2 != 0:
            return num_1 / num_2
resultado = calculadora(num_1, num_2, operacion)
print("Resultado:", resultado)