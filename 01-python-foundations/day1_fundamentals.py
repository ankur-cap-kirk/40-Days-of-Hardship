
## VARIABLES AND TYPES

name ="Ankur" # str(text)
age = 24 # int  
height = 6.1 # float
trying_to_learn = True # bool

print(type(name))
print(type(age))
print(type(height))
print(type(trying_to_learn))

print(f"My name is {name} and I am {age}")

## IF/ELSE STATEMENTS

if age >= 18:
    print("adult")
else:
    print("minor")

number = 15
if number % 2 == 0:
    print("even")
else:
    print("odd")
   

## LOOPS
# FOR LOOP
for i in range(5):
    print(i)

for i in range (1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

# WHILE LOOP

count = 0
while count < 5:
    print(count)
    count = count + 1

count = 10
while count >= 0:
    print(count)
    count = count - 1
print("liftoff!")    