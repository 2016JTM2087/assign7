#!bin/python

###### this is the first .py file ###########

import sys				#for command line input

m={}
g=list(sys.argv)
l=range(1,len(g)) 			# to check the range of i
for i in range(1,len(g)):		#c=count
	c=0				#initialise the variable	
	for j in range(1,len(g)):	#start the sub loop	
		if g[i]==g[j]:		#check equality condition
			c=c+1		#increment the variable
	l[i-1]=c	
	print "%s occurs %d times in the string" % (g[i], c)
	m.update({g[i]:c})		# update with the new value
 



