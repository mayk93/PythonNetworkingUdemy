from random import randint as RandomInteger

a = input("Input value of variable a: ")
b = input("Input value of variable b: ")
print("Creating variable c with value equal to a.")
c = a
print("Variable a: "+str(a)+" with id: "+str(id(a)))
print("Variable b: "+str(b)+" with id: "+str(id(b)))
print("Variable c:"+str(c)+" with id: "+str(id(c)))
print("Changing value of variable c.")
c = RandomInteger(RandomInteger(10,15),RandomInteger(100,150))
print("Variable c:"+str(c)+" with id: "+str(id(c)))
