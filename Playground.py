# myArray = [1,2,3,5,5,3];
# mySum = 0;

# for eachMember in myArray:
#     mySum += eachMember
#     print(mySum)

# print("bora")

# for x in range(0,len(myArray)):
#     print(myArray[x])


# #Alttaki ikisi ayni fakat bir tanesi index ile gezerken bir tanesi direkt elemanlari geziyor

# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:
#    print ('Current fruit :', fruit)

# fruits = ['banana', 'apple',  'mango']
# for index in range(0,len(fruits)):
#    print ('Current fruit :', fruit)


# if 2 == 2:
#     print("2 2ye esit")
# if 3 == 4:
#     print("3 4e esit")
# elif(4 == 4):
#     print("4 4'e esit")
# else:
#     print("3 4ye esit degil")


# def myFunction(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)

# myFunction(15, 5) 
# myFunction(y=15, x=5)
## myFunction(yy=15, xy=5) --> doesn't work because yy or xy isn't defined in the function
#x ve y parametlerini sirayla gondermek istemezsen parametre isimleri ile gonderebiliyorsun

# def defaultParametersOfFunctions(x=0, y=0, z=0):
#     print(x + y + z)

# defaultParametersOfFunctions() #prints zero
# defaultParametersOfFunctions(2,4,5) #prints 11

# def withoutDefaultParametersOfFunctions(x, y, z):
#     print(x + y + z)


# # withoutDefaultParametersOfFunctions(1) # doesn't work, gives compiler error because some parameters weren't defined

# withoutDefaultParametersOfFunctions(1,3,4) #prints 8

'''
Mesela javascriptte boyle bir sey yazsak NaN sonucunu verecekti

function testFunction(x,y,z) {
    console.log(x+y+z);
}

testFunction(1);

'''

# myGlobalVariable = 5
# print(myGlobalVariable) #output is 5
# def myFunction():
#     global myGlobalVariable
#     myGlobalVariable += 5
#     print(myGlobalVariable) #output is 10

# myFunction()
# print(myGlobalVariable) #output is 10


# to install a module --> pip install ModuleName

# text = 'My text to write'
# myFileVariable = open('exampleFile.txt', 'w')
# myFileVariable.write(text)
# myFileVariable.close


# appendText = '\n My append text is here'
# appendFile = open('exampleFile.txt', 'a')
# appendFile.write(appendText)
# appendFile.close()


# readMe = open('exampleFile.txt', 'r').read() ## Normal okuyor, alttaki array'e atiyor her line'i
# print(readMe)

# readMe2 = open('exampleFile.txt', 'r').readlines() ## Bu her line'i arraye atiyor
# print(readMe2)

# for x in range(0, 100):
#     appendFile = open('myTest.txt', 'a')
#     xString = str(x)
#     appendFile.write(xString + '\n')


# class calculator:

#     def addition(x,y):
#         print(x+y)
    
#     def substraction(x,y):
#         print(x-y)
    
#     def mult(x,y):
#         print(x*y)

#     def division(x,y):
#         print(x/y)


# calculator.addition(3,4)


# x = input('Give an input: ')
# print(x)

# import statistics as s

# myArray = [1,2,4,5,2]
# median = s.median(myArray)
# print(median)


# from statistics import median as m

# myArray = [1,2,4,5,2]
# median = m(myArray)
# print(median)

# x = [2,3,4,1,5]
# x.append(4)
# print(x)

# x = [2,3,4,1,5]
# x.insert(2, 9)
# print(x)

# x = [2,3,4,1,5]
# x.remove(2) ## or you can use x.remove(x[2])
# print(x)



# x = [2,3,4,1,5,3,4,3,3,3,3,3,3,3,3]
# print(x[2:4]) #2. indexden 3. indexe kadar olan elemanlari yazdiracak
# print(x[-1]) #listenin son elmanini yazdiracak
# print(x[-2]) #sondan bir onceki elemani verecek

# str = 'Hello World!'

# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
# print (str[2:5])     # Prints characters starting from 3rd to 5th
# print (str[2:])      # Prints string starting from 3rd character
# print (str * 2)      # Prints string two times
# print (str + "TEST") # Prints concatenated string

# print(x.index(3)) #1'in ilk kez kacinci indexte oldugunu verecek
# print(x.count(3)) #3 sayisinin arrayde kac kere gectigini verecek

# y = ["Bora", "bora", "Ali", "ali", "Ahmet"]

# x.sort() #x'i sort ediyor
# print(x)

# y.sort() # y boyle oldu --> ['Ahmet', 'Ali', 'Bora', 'ali', 'bora']
# print(y)


# multiDimensionalArray = [[1,2,3], 
#                          [4,5,6], 
#                          [7,8,9]
#                           ]
# print(multiDimensionalArray[1][2]) #prints 6

# multiDimensionalArray = [ [[0.5, 1],2,3], [4,5,6], [7,8,9] ]
# print(multiDimensionalArray[0][0][1]) #prints 1



# import csv

# with open('data.csv') as csvFile:
#     readCSV = csv.reader(csvFile, delimiter=',')
#     companyNames = []
#     for row in readCSV:
#         companyNames.append(row[1])

# print(companyNames)


# try:
#     open('data2.csv', 'r')
# except Exception as e:
#     print(e) #prints --> Errno 2] No such file or directory: 'data2.csv'

# print('''test
# test 2. line
# test 3. line
# test 4. line
# ------------
# |          |
# |  LOADING |
# |          |
# |------------
# ''')


# dictionary1 = {'Jack': '15', 'bora': 21, 'ali': 19}
# print(dictionary1)
# print(dictionary1['Jack']) #Output is 15



# for x in range(0,100):
#     print(x)
#     if(x == 10):
#         break



# #bu assagisi 10'u bastirmayacak
# for x in range(0,12):
#     if(x == 10):
#         pass
#     else:
#         print(x)


# #bu assagisi 10'u bastirmayacak yukaridaki gibi
# for x in range(0,12):
#     if(x != 10):
#         print(x)



# import random as r
# for x in range(0,15):
#     myRandomNumber = r.random()
#     print(myRandomNumber)


# file = open('MyTestFile.txt', 'a')
# file.write('test1')
# file.close()




# def docTestFunction(test):
#     ''' docTestFunction icindeki yorumu altta cagirinca burayi verecek'''

# import Playground
# print(Playground.__doc__) ## ''' ''' arasinda yazdiklarin .__doc__ objesinde cikiyor
# print(Playground.docTestFunction.__doc__)




# import datetime

# beforeLoop = datetime.datetime.now()

# for x in range(0,1000):
#     print("hi")

# print(datetime.datetime.now() - beforeLoop)





    
try:
    print('hey')
except:
    print('hata var')
else:
    try:
        print('ikinci try')
    except:
        print('ikinci hata')
    else:
        print('sona geldik')
boras