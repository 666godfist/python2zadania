a=int(input("Podaj liczbę a: \n"))
b=int(input("Podaj liczbę b: \n"))

if(a>b):
    index=a
    for index in range(a,b+1):
        print(index)
        index+1
elif(a<b):
    c=a
    b=a
    a=c
    index=a
    for index in range(a,b+1):
        print(index)
        index+1