#for c in range(0, 100+1):
 #   print(c)

#for x in range(100, 0-1, -1):
  #  print(x)

n = int(input("Que termo deseja encontrar:"))
ultimo = 1
penultimo = 1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)