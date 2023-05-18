x = input("(1) Wpisz liczbę: ").strip()

while not x.isdigit():

   print("Musisz wprowadzić liczbę całkowitą")

   x = input("(1) Wpisz liczbę: ").strip()

y = input("(2) Wpisz liczbę: ").strip()

while not y.isdigit():

   print("Musisz wprowadzić liczbę całkowitą")

   y = input("(2) Wpisz liczbę: ").strip()

if int(x)>int(y):

   print("%s jest większy niż %s" % (x,y))

elif int(y)>int(x):

   print("%s jest większy niż %s" % (y, x))

else:

   print("Dwie liczby są takie same")