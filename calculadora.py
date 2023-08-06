class Operaciones :
    @staticmethod
    def sumar (x, y):
    
        return x + y
    @staticmethod
    def restar (x, y):
    
        return x - y
    @staticmethod
    def multiplicar (x, y):
    
        return x * y
    @staticmethod
    def dividir (x, y):
    
        return x / y
    @staticmethod
    def potencia (x, y):
    
        return x ** y
    @staticmethod
    def raízCuadrada (x):
    
        return x ** 0.5
    @staticmethod
    def bin_to_hex (x)  :  
      decimal = int(x, 2)
      hexadecimal = hex(decimal)
      return hexadecimal
    @staticmethod
    def hex_to_bin (x)  :  
      decimal = int(x, 16)
      binario = bin(decimal)[2:]
      return binario
            
    @staticmethod
    def coseno(x):
      import math
      radianes = math.radians(x) 
      coseno = math.cos(radianes)
      return coseno

    @staticmethod
    def seno(x):
      import math
      seno = math.sin(x)
      return seno

    @staticmethod
    def tangente(x):
      import math
      radianes = math.radians(x) 
      tangente = math.tan(radianes)
      return tangente       
      
print("Que operacion quieres hacer?\n" +
      "1.  sumar\n" 
      "2.  restar\n"
      "3.  multiplicar\n"
      "4.  dividir\n"
      "5.  potencia\n"
      "6.  raíz cuadrada\n"
      "7.  binario a hexadecimal\n"      
      "8.  coseno\n"
      "9.  seno\n"
      "10. tangente\n"      
      )  
    
eleccion = int(input())
if eleccion <=6 :
    numero1 = float(input("Ingrese el número1: "))
    
if eleccion ==7 :
  print("Que operacion quieres hacer?\n" +
      "1.  bin_to_hex\n" 
      "2.  hex_to_bin\n")
  new_eleccion = int(input())
  if new_eleccion == 1:
    numero1 = input("Ingrese el número binario: ")
  elif new_eleccion == 2:
    numero1 = input("Ingrese el número hexadecimal: ")
  else :
    numero1 = input("Ingrese el número corecto (1-2): ")
    
if eleccion > 7  & eleccion <=10:  
    numero1 = float(input("Ingrese el ángulo: "))
if eleccion <= 4 :
    numero2 = float(input("Ingrese el número2: "))
if eleccion == 5 :
    numero2 = int(input("Ingrese el exponente: "))
if eleccion == 6 :
    numero2 = None
 

if eleccion == 1:
  resultado = Operaciones.sumar(numero1, numero2)
elif eleccion == 2:
  resultado = Operaciones.restar(numero1, numero2)
elif eleccion == 3:
  resultado = Operaciones.multiplicar(numero1, numero2)
elif eleccion == 4:
  resultado = Operaciones.dividir(numero1, numero2)
elif eleccion == 5:
  resultado = Operaciones.potencia(numero1, numero2)
elif eleccion == 6:
  resultado = Operaciones.raízCuadrada(numero1)
elif eleccion == 7:
  if new_eleccion == 1:
    resultado = Operaciones.bin_to_hex(numero1)  
  if new_eleccion == 2:
    resultado = Operaciones.hex_to_bin(numero1)    
elif eleccion == 8:
  resultado = Operaciones.coseno(numero1)  
elif eleccion == 9:
  resultado = Operaciones.seno(numero1)   
elif eleccion == 10:
  resultado = Operaciones.tangente(numero1) 
else :
    print("¡Ingrese un número!.")  



print("El resultado es:", resultado)
