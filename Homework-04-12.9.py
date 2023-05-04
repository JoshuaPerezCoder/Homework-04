# Homework-04-12.9
# Joshua Perez
#ID:1837170
# Splitting the input into parts so that variables are identified
parts = input().split()
name = parts[0]
#The while loop will stop when the input is -1
while name != '-1':
   # Inserting blocks to catch any exceptions.
   try:
       age = int(parts[1]) + 1
       print(f"{name} {age}")
   #when the string does not register in the restrictions it passes on
   except ValueError:
       # printing name and age as 0 for the strings that do not pass
       print(f'{name} {0}')
  #starting the loop over till "-1" is typed.
   parts = input().split()
   name = parts[0]
