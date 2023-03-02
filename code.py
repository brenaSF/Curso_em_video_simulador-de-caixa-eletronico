
#simulador de caixa 


cont = 1 
cedula = (50,20,10,1)
i=0

valor = int(input("qual valor deseja sacar?  "))


while valor != 0 :

        if  cont*cedula[i] <= valor :

            cont += 1 

        else :

            cont -= 1 

            print("{} cédulas de {} reais".format(cont,cedula[i]))

            valor = valor - (cont*cedula[i])

            i+=1

            cont = 1






