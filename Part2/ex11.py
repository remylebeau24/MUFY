def calculate(a,operation,b):
if operation == "+":
return a + b
elif operation == "-":
return a - b
elif operation ==
"":
return a b
elif operation == "/":
if b != 0:
return a / b
else:
return "Cannot divide by zero!"
else:
return "Unknown operation"
print(calculate(10, "+"
,10))
print(calculate (10," -"
,10))
print(calculate(10, "",10))
print (calculate (10,"/",10))
