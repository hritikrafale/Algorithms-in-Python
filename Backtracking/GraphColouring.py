#function to check next Vertex
#bounding function
def nextVertex(arr,result,V,i,j):
	#checking if adjancent vertex is not having same colour
	#first check if there is an edge between previous vertex and current vertex
	k=i-1
	while(k>=0):
		#check if edge is there between k vertex and current vertex
		if(arr[k][i]==1):
			#now check if colour we are going to choose is already an adjancent colour or not
			if(result[k]==j):
				return -1
		k=k-1
			
	return 1

#function to generate hamiltonian cycle
def graphColouring(arr,result,V,i):
	if(i==V):
		print("\nColours of each vertex are:")
		for k in range(0,V):
			if(result[k]==1):
				print('Red',end=" ")
			elif(result[k]==2):
				print('Blue',end=" ")
			else:
				print('Green',end=" ")	
				
		return 1	
	else:
		for j in range(1,4):
			check1=nextVertex(arr,result,V,i,j)
			if(check1==1):
				result[i]=j
				i=i+1
				graphColouring(arr,result,V,i)
				i=i-1	
				result[i]=0		




#main function
#adjancency matrix for connected undirected graph
arr=[[0,1,0,0,1],
	 [1,0,1,0,1],
	 [0,1,0,1,1],
	 [0,0,1,0,1],
	 [1,1,1,1,0]]

V=5

result=[1,0,0,0,0]

graphColouring(arr,result,V,1)




