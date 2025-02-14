print("Calculator build for calculations")   

print ()
print("Please follow the instructions")
print ()
print("press 1 for  addittion.")
print ()
print ("press 2 for subtraction.")
print ()
print ("press 3 for multiplication.")
print ()
print("press 4 for division.")
print ()
n1=float(input ("Please enter your first no:"))
print ()
n2=float(input ("please enter your second no:"))
print ()
n=int(input("Please enter your choice:"))
if(n== 1):
 print(n1+n2) 
if(n== 2):
 print(n1-n2)
if(n== 3):
 print(n1*n2)
if(n== 4):
 print(n1/n2)
elif (n>=5):
     print("invalid operation.")