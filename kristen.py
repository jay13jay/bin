#!/usr/bin/python

print("Welcome to My Widget Store!")
 
name = input("What is your name? ")
 
quarters = input("How many of Product A do you want to buy, at 25 cents each? ")
dimes = input("How many of Product B do you want to buy, at 10 cents each? ")
nickles = input("How many of Product C do you want to buy, at 5 cents each? ")
pennies = input("How many of Product D do you want to buy, at 1 cents each? ")
 
total = (float(quarters)*(.25))+ (float(dimes)*(.10)) + (float(nickles)*(.05)) + (float(pennies)*(.01))
 
print("Your total is: " + str(total))
 
funds = input("How many cents are you paying with? ")
change = float(funds)-float(total)
 
print("Your change is: " + str(change) + " cents, given as:")
 
change_q = (float(change)//.25)
change_d = (float(change)-(float(change_q)*(.25)))//.10
change_n = (float(change)-((float(change_q)*(.25))) + (float(change_d)*(.10)))//.05
change_p = ((float(change))-((float(change_q)*(.25)) + (float(change_d)*(.10)) + (float(change_n)*(.05))))//.01
 
print( str(change_q) + "quarters")
print( str(change_d) + "dimes")
print( str(change_n) + "nickles")
print( str(change_p) + "pennies")
 
print ("Thank you, " + str(name))
