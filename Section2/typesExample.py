from random import randint as RandomInteger
from random import uniform as RandomFloat
from random import choice as RandomChoice
from math import sin,ceil

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def RandomString(length=0):
    if length <= 0:
        length = RandomInteger(5,15)
    randomString = ""
    for index in range(0,length):
        randomString += RandomChoice(letters)
    return randomString

def RandomList(length=0):
    if length <= 0:
        length = RandomInteger(5,15)
    randomList = []
    for index in range(0,length):
        if bool((index+RandomInteger(5,10))%2) == True:
            randomList.append(RandomInteger(5,15))
        elif bool((ceil((abs(sin(index)+1)+RandomFloat(5,10))))%2) == True:
            randomList.append(RandomFloat(5,15))
        else:
            randomList.append(RandomString())
    return randomList

def RandomTuple(length=0):
    if length <= 0:
        length = RandomInteger(5,15)
    randomTuple = []
    for index in range(0,length):
        if bool((index+RandomInteger(5,10))%2) == True:
            randomTuple.append(RandomInteger(5,15))
        elif bool((ceil((abs(sin(index)+1)+RandomFloat(5,10))))%2) == True:
            randomTuple.append(RandomFloat(5,15))
        else:
            randomTuple.append(RandomString())
    return tuple(randomTuple)

def RandomDictionary(length=0):
    if length <= 0:
        length = RandomInteger(5,15)
    randomDictionary = {}
    for index in range(0,length):
        if bool((index+RandomInteger(5,10))%2) == True:
            randomDictionary.update({"Entry-"+str(index):RandomInteger(5,15)})
        elif bool((ceil((abs(sin(index)+1)+RandomFloat(5,10))))%2) == True:
            randomDictionary.update({"Entry-"+str(index):RandomFloat(5,15)})
        else:
            randomDictionary.update({"Entry-"+str(index):RandomString()})
    return randomDictionary

def Mutate(example):
    if type(example) == type(0):
        example += RandomInteger(5,15)
        print("Int example now: "+str(example))
        print("'The example now' will show the old value. This is because assignment is not binding in python.")
        return "Modification Succesful. Performed addition."
    elif type(example) == type(0.0):
        example -= RandomFloat(5,15)
        print("Float example now: "+str(example))
        print("'The example now' will show the old value. This is because assignment is not binding in python.")
        return "Modification Succesful. Performed substraction."
    elif type(example) == type([]):
        example.append(RandomList(3))
        if len(example) > 3:
            example.pop(0)
        if len(example) > 5:
            example[1],example[len(example)-1] = example[len(example)-1],example[1]
        example[0] = -999
        return "Modification Succesful. Performed insertion, removal, swaping and a change of value."
    elif type(example) == type({}):
        del example["Entry-"+str(RandomInteger(0,len(list(example.keys()))))]
        example["Entry-"+str(RandomInteger(0,len(example.keys())))] = "Modification."
        example.update({"ModificationEntry":-999})
        return "Modification Succesful. Performed update, deletion and a change of value."
    elif type(example) == type(""):
        result = ""
        try:
            example[0] = "$"
            result += "Managed to change the first letter.\n"
        except Exception as e:
            result += str(e) + "\n"
        try:
            del example[1]
            result += "Managed to delete second letter.\n"
        except Exception as e:
            result += str(e) + "\n"
        try:
            example[0],example[1] = example[1],example[0]
            result += "Managed to swap two letters.\n"
        except Exception as e:
            result += str(e)
        return result
    elif type(example) == type(()):
        result = ""
        try:
            example[0] = "$"
            result += "Managed to change the first element of the tuple.\n"
        except Exception as e:
            result += str(e) + "\n"
        try:
            del example[1]
            result += "Managed to delete second element of the tuple.\n"
        except Exception as e:
            result += str(e) + "\n"
        try:
            example[0],example[1] = example[1],example[0]
            result += "Managed to swap two elements of the tuple.\n"
        except Exception as e:
            result += str(e)
        return result
    else:
        return "This type is not recognized."



exampleInt = RandomInteger(10,150)
exampleFloat = RandomFloat(10,150)
exampleString = RandomString()
exampleList = RandomList()
exampleTuple = RandomTuple()
exampleDictionary = RandomDictionary()

dictionaryOfExamples = {'Int':exampleInt,'Float':exampleFloat,'String':exampleString,'List':exampleList,'Tuple':exampleTuple,'Dict':exampleDictionary}

print("Example Int: "+str(exampleInt))
print("The type is: "+str(type(exampleInt)))
print("---")
print("Example Float: "+str(exampleFloat))
print("The type is: "+str(type(exampleFloat)))
print("---")
print("Example String: "+str(exampleString))
print("The type is: "+str(type(exampleString)))
print("---")
print("Example List: "+str(exampleList))
print("The type is: "+str(type(exampleList)))
print("---")
print("Example Tuple: "+str(exampleTuple))
print("The type is: "+str(type(exampleTuple)))
print("---")
print("Example Dictionary: "+str(exampleDictionary))
print("The type is: "+str(type(exampleDictionary)))
print("---")

print("\nOptions: Int, Float, String, List, Tuple, Dict\n")
typeToMutate = input("Enter a type to try and modify: ")
while typeToMutate not in dictionaryOfExamples.keys():
    print("Bad option. See options above.")
    typeToMutate = input("Enter a type to try and modify: ")

print("Trying to modify "+str(typeToMutate)+".")
exampleToMutate = dictionaryOfExamples[typeToMutate]
print("Chosen example: "+str(exampleToMutate)+".")
result = Mutate(exampleToMutate)
print("Result: "+str(result))
print("The example now: "+str(exampleToMutate))
