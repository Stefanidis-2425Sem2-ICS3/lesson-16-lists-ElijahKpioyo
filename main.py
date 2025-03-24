import random
num = [random.randint(0,100) for i in range(100)]

print ("The 100 numbers are:")
print (num)

average = sum(num)/len(num)

print ("The average of your numbers is: ", average)
