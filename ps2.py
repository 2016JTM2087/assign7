#!bin/python

###### this is the second .py file ###########


import random,math
						       
 # importing the packages for using the function defined within them

m=input("enter the number of users in the locality \n")

# taking the no. of users from the user
c=0

for i in range(m): 

# generating the location of the users 

	(x,y)=(random.random()*2- 1, random.random()*2-1)

	d=math.sqrt(x*x+y*y)    

					
# calculating the distance of each user from origin

	if d<=1:   
	
#if distance is less than equal to unity they lie within range of tower

		c=c+1  
    						
# for incrementing  the no of users in range

k=(float(c)/float(m))*100	
	
# for calculating the %age of users in range

print k

