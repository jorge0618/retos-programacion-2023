'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def primo(int):
    b=0
    for i in range(1,x+1):
        if x%i==0:
            b=b+1
    print("es primo") if b<=2 else print("no es primo")

def fibonacci(int):
    a=0
    b=1
    for i in range(x):
        c=a+b
        b=a
        a=c
        if b==x:
            break
        
    print("es fibonaci") if x==b else print("no es fibonacci")

def par(int):
    print("es par") if x%2==0 else print("es impar")

if __name__=="__main__":
  
    x=int(input("ingrese un número :\n"))
    primo(x)
    fibonacci(x)
    par(x)
