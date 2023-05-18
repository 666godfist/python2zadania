a=input("Podaj liczbę a: \n")
b=input("Podaj liczbę b: \n")
x=input("Podaj operację: ")

if(x=="/"):
    print("Ta operacja jest dzieleniem.\n")
    if(b==0):
        print("Dzielenie przez 0 jest niemożliwe.")
    else:
        print(eval(a+x+b))
else:
    print(eval(a+x+b))