# E. Kpioyo
# 100 Number Averager
# March 24, 2025
# This program lists 100 numbers and prints the average of them.
import random
num = [random.randint(0,100) for i in range(100)]

print ("The 100 numbers are:")
print (num)

average = sum(num)/len(num)

print ("The average of your numbers is: ", average)
