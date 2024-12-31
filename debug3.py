def factorial(n):
   counter = 0
   total = 1
   while counter < n:
       total *= (n-counter)
       counter += 1

   return total

print(factorial(3)) #should print 6