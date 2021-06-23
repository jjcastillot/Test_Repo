Largest=None
Smallest=None
while True:                         #Permanece en el ciclo hasta False
    sval=input("Enter a number: ")  #Recibe la entrada
    if sval == "done" :             #Sale del loop con break, cuando la entrada
        break                       #es done
    try:
        ival=int(sval)              #Convierte la entrada en float
    except:
        print("Invalid input")   #Si la entrada es inválida, vuelve al
        continue                    #inicio del loop
    if Largest==None and Smallest==None:
        Largest=ival
        Smallest=ival
    elif ival>Largest:
        Largest=ival
    elif ival<Smallest:
        Smallest=ival

print("Maximum is",Largest)
print("Minimum is",Smallest)
