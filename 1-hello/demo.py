#!/usr/bin/env python3

var = 100
if var == 100:
   print ("1 - Got a true expression value")
   print (var)
elif var == 150:
   print ("2 - Got a true expression value")
   print (var)
else:
   print ("3 - Got a false expression value")
   print (var)
   
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
   
var = 1
while var == 1 :  # This constructs an infinite loop
   num = input("Enter a number  :")
   print ("You entered: ", num)
   if( num == "5" ):
       break
   
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)
   
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])
   
print ('bye')