# Homework-04-12.7
# Joshua Perez
#ID: 1837170
# using the function given by the exercise and adding the range for the age.
def get_age():
   age = int(input())
   #age is going to be between 18 and 75
   if 18 <= age <= 75:
       return age
   #if age is not within the range the raise function will recognize as a valid error
   raise ValueError("Invalid age.")


#using the function to determine the fat burning rate.
def fat_burning_heart_rate(age):
   return (220 - age) * 0.7


#last function that is given by the exercise
if __name__ == "__main__":
   try:
       #adding rules for the fucntion to continue
       age = get_age()
       print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
   except ValueError as no_range:
       print(no_range)
       print("Could not calculate heart rate info.\n")
