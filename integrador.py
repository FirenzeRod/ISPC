
import msvcrt

print ("¡BIENVENIDO!", "\n")

num1= int(input("Digite un numero:"))
num2= int(input("Digite un numero:"))
num3= int(input("Digite un numero:"))
num4= int(input("Digite un numero:"))
num5= int(input("Digite un numero:"))

print ("\n")
suma= num1+num2+num3+num4+num5
print ("La suma de los numeros es:",suma)
print ("\n")
prom= num1+num2+num3+num4+num5/5
print ("El promedio es:",prom)
print ("\n")
max_value = max(num1,num2,num3,num4,num5)
print('Valor Maximo:', max_value)
print ("\n")
min_value = min(num1,num2,num3,num4,num5)
print('Valor Minimo:', min_value)

print ("\n")
print ("¡Muchas gracias!, Adios", "\n" )

msvcrt.getch()
