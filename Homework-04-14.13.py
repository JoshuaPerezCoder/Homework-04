# Homework-04-14.13
# Joshua Perez
#ID:1837170
#Global variable
num_calls = 0
#setting up fucntion asked by the exercise
def partition(user_ids, i, k):
   #setting parameters for function
   pivot = user_ids[(i + k) // 2]
   #setting varibles for low and high elements
   low = i - 1
   high = k + 1
#making parameters for elements
   while True:
       low += 1
       while user_ids[low] < pivot:
           low += 1
       high -= 1
       while user_ids[high] > pivot:
           high -= 1
       if low >= high:
           return high
       #changing the position of the values
       user_ids[low], user_ids[high] = user_ids[high], user_ids[low]
def quicksort(user_ids, i, k):
   #using the global fucntion to set num call as a variable to be accepted throughout the program
   global num_calls
   #adding how many chnages are being made throughout the program
   num_calls += 1
   #in case the list is empty or singular
   if i >= k:
       return
   else:
       #continuing to sort the elements
       part = partition(user_ids, i, k)
       quicksort(user_ids, i, part)
       quicksort(user_ids, part + 1, k)
if __name__ == "__main__":
   #setting up an empty list to append all the elements
   user_ids = []
   user_id = input()
   while user_id != "-1":
       user_ids.append(user_id)
       user_id = input()
       #recalling quicksort fucntion for the sorting
   quicksort(user_ids, 0, len(user_ids) - 1)
   print(num_calls)
   for user_id in user_ids:
       print(user_id)
