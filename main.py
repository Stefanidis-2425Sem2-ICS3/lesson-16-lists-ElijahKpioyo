# E. Kpioyo
# 100 Number Averager
# March 24, 2025
# This program lists 100 numbers and prints the average of them.
import random
list = []

#num = [random.randint(0,100) for i in range(100)]


for i in range(100):
  num = random.randint(0,100)
  list.append(num)

print ("The 100 numbers are:")
print (num)

average = sum(list)/len(list)

print ("The average of your numbers is: ", average)
