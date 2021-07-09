# Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos. < >
numero1 = int(input("Ingrese número "))
a = numero1
numero2 = int(input("Ingrese número "))
b = numero2
cont = conta = 0
while(numero1 > 10):
    numero1 = numero1 // 10
    cont = cont + 1
    if (numero1 < 10): cont = cont + 1   
while (numero2 > 10):    
    numero2 = numero2 // 10
    conta = conta + 1
    if (numero2 < 10): conta = conta + 1  
if (cont > conta):
    print(f"El numero {a} tiene mayor cantidad de digitos que el numero {b}, ya que tiene {cont} digitos")
elif (cont < conta):
    print(f"El numero {b} tiene mayor cantidad de digitos que el numero {a}, ya que tiene {conta} digitos")
