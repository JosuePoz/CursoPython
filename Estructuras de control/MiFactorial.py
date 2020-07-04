#Forma 1
def Funcion_Factorial (acumn, factorial):
    if factorial > 0:
        acumn = factorial * Funcion_Factorial(acumn, factorial-1)
    return acumn

#Forma 2
def funcion_factorial2 (x):
    if x==0:   
        return 1
    else:
        return x * funcion_factorial2(x -1)

factorial= 20
acum = 1
print (Funcion_Factorial(acum, factorial))
print (funcion_factorial2(factorial))