#function to check next Vertex
#bounding function
def nextVertex(arr,result,V,i,j):
	#checking if vertex already choosen
	for k in range(0,i):
		if(result[k]==j):
			return -1

	#checking if an edge is present or not
	src=result[i-1]
	if(arr[src-1][j-1]!=1):
		return -1

	if((i==V-1)and(arr[j-1][0]!=1)):
		return -1
	return 1

#function to generate hamiltonian cycle
def hamiltonian(arr,result,V,i):
	if(i==V):
		print("\nhamiltonian cycle is:")
		for k in range(0,V):
			print(result[k],end=" ")
		return 1	
	else:
		for j in range(1,V+1):
			check1=nextVertex(arr,result,V,i,j)
			if(check1==1):
				result[i]=j
				i=i+1
				hamiltonian(arr,result,V,i)
				i=i-1	
				result[i]=0		




#main function
#adjancency matrix for connected undirected graph
arr=[[0,1,1,0,1],
	 [1,0,1,1,1],
	 [1,1,0,1,0],
	 [0,1,1,0,1],
	 [1,1,0,1,0]]

V=5

result=[1,0,0,0,0]

if(hamiltonian(arr,result,V,1)==-1):
	print("No hamiltonian cycle is present in this graph")






