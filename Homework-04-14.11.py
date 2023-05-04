# Homework-04-14.11
# Joshua Perez
#ID:1837170
# creating function needed by the exercise
def selection_sort_descend_trace(n):
   #creating rows in array and cuttinh off one row
   for i in range(len(n) - 1):
       #creating new values for next rows
       new = i
       for j in range(i + 1, len(n)):
           if n[new] < n[j]:
               new = j
       #rearraging items in string
       n[i], n[new] = n[new], n[i]
       #cutting off row and starting a new row
       for value in n:
           print(value,end=" ")
       print()
       # returning the final list
   return n


if __name__ == "__main__":
   n = []
#converting items in input of "n" into integers to make rearraging easier
   n = [int(x) for x in input("").split()]
   selection_sort_descend_trace(n)
